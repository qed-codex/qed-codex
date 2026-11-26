"""Extract reachable branch history for local, redacted secret scans and human review."""
import argparse
import collections
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def git(*args):
    return subprocess.check_output(["git", *args])


def audit(destination, ocr):
    refs = git("for-each-ref", "--format=%(refname) %(objectname)", "refs/heads", "refs/remotes").decode().splitlines()
    refs = dict(r.split(" ", 1) for r in refs if "/HEAD " not in r)
    commits = git("rev-list", *sorted(set(refs.values()))).decode().splitlines()
    dump = destination / "objects"
    dump.mkdir(parents=True)
    evidence = collections.defaultdict(set)
    paths = collections.defaultdict(set)
    pngs = []
    binary = []
    for commit in commits:
        (dump / (commit + ".commit")).write_bytes(git("cat-file", "commit", commit))
        for entry in git("ls-tree", "-rz", commit).split(b"\0"):
            if entry:
                meta, name = entry.split(b"\t", 1)
                mode, kind, oid = meta.decode().split()
                if kind != "blob" or mode not in ("100644", "100755"):
                    raise ValueError("Review non-regular Git entry")
                paths[oid].add(name.decode())
    for oid in paths:
        data = git("cat-file", "blob", oid)
        if data.startswith(b"\x89PNG\r\n\x1a\n"):
            path = dump / (oid + ".png")
            path.write_bytes(data)
            pngs.append(path)
        else:
            try:
                data.decode("utf-8")
            except UnicodeDecodeError:
                binary.append(oid)
            (dump / oid).write_bytes(data)
    (dump / "historical-paths.txt").write_text("\n".join(sorted({p for names in paths.values() for p in names})))
    def read_image(image):
        text = subprocess.check_output([ocr, str(image), "stdout"], stderr=subprocess.DEVNULL)
        image.with_suffix(".ocr").write_bytes(text)
    if ocr:
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(read_image, pngs))
    # Candidate lists stay local. Include names in metadata, visible image text and filenames.
    patterns = {
        "machine-path": r"(?:/(?:home|Users|private|tmp|workspace|mnt)/[^\s`\x22'<>]+|[A-Za-z]:\\(?:Users|Documents)\\[^\s]+)",
        "private-file": r"(?im)^[^\n]*(?:/(?:\.env|credentials|private-notes|sharing\.md|prompts?\.md)(?:$|/)|^(?:\.env|credentials|private-notes|sharing\.md)$)[^\n]*",
        "private-language": r"(?i)\b(?:private (?:notes?|drafts?)|internal use only|do not (?:publish|share)|system prompt|outreach pitch|personal access token)\b",
        "email": r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
        "name-candidates": r"\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ’'-]+(?: [A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ’'-]+){1,3}\b",
    }
    for f in dump.iterdir():
        if f.suffix == ".png" or f.name in binary:
            continue
        body = f.read_text()
        for key, pattern in patterns.items():
            evidence[key].update(re.findall(pattern,body))
    (destination / "candidates.json").write_text(json.dumps({k:sorted(v) for k,v in evidence.items()}, indent=2))
    return {"branches":refs,"commits":len(commits),"uniqueBlobs":len(paths),"pngs":len(pngs),
            "pngsReadWithOCR":len(pngs) if ocr else 0,"otherBinary":binary,
            "candidateCounts":{k:len(v) for k,v in sorted(evidence.items())}}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("out", type=Path, help="Fresh ignored directory")
    cli.add_argument("--ocr", help="Tesseract executable")
    args = cli.parse_args()
    print(json.dumps(audit(args.out,args.ocr), indent=2))
