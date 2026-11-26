"""Exercise the installed PR checker locally using temporary Git objects and the real SQLite file."""
from source_registry import directory_proof

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from check_informalization_pr import PUBLIC_MAX_BYTES, PUBLIC_MAX_DECLARATIONS

import yaml


ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "tools/check_informalization_pr.py"
AUTHOR = "fixture-reader"
MODULE = "src/Main.lean"
PATH = f"packages/riemann-hypothesis/informalizations/{MODULE}/{AUTHOR}--fixture.md"
OTHER = PATH.replace(AUTHOR, "another-reader")
OWNED = f"packages/riemann-hypothesis/informalizations/src/BuildAid/D1.lean/{AUTHOR}--fixture.md"
PIN = yaml.safe_load((ROOT / "proofs/rh/proof.yml").read_text())["source_commit"]


def note(**overrides):
    data = dict(module=MODULE, author=AUTHOR, declarations=["riemannHypothesis"],
                source_commit=PIN, writer="Fixture", origin="wrote", license="CC-BY-4.0")
    data.update(overrides)
    return "---\n" + yaml.safe_dump(data) + "---\n\nLocal fixture.\n"


def exercise(database):
    results = []
    with tempfile.TemporaryDirectory() as folder:
        repo = Path(folder)
        env = dict(os.environ, GIT_AUTHOR_NAME="dial481", GIT_COMMITTER_NAME="dial481",
                   GIT_AUTHOR_EMAIL="248182468+dial481@users.noreply.github.com",
                   GIT_COMMITTER_EMAIL="248182468+dial481@users.noreply.github.com",
                   GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)

        def git(*args):
            return subprocess.check_output(["git", "-C", repo, *args], env=env, text=True).strip()

        def put(path, body):
            path = repo / path
            path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(body, Path):
                path.symlink_to(body)
            elif body is None:
                path.unlink()
            else:
                path.write_text(body)

        def commit():
            git("add", "--all")
            git("commit", "--quiet", "-m", "Construct a local validation fixture")
            return git("rev-parse", "HEAD")

        git("init", "--quiet")
        put("site-settings.json", (ROOT / "site-settings.json").read_text())
        for source in ROOT.glob("packages/*/source.yml"):
            put(str(source.relative_to(ROOT)), source.read_text())
        put("proofs/rh/proof.yml", (ROOT / "proofs/rh/proof.yml").read_text())
        put(OTHER, note(author="another-reader"))
        published = dict(origin="other-author",source="https://example.org/work",
                         license_source="https://example.org/LICENSE",copyright="Copyright Example",
                         changes="none",notice="An upstream notice.\nSecond line.")
        put(OWNED, note(module="src/BuildAid/D1.lean", declarations=[], license="Apache-2.0", **published))
        common = commit()
        put("README.md", "A base branch change after the contribution branch was created.\n")
        peer = note(author="another-reader") + "A peer revision on the base branch.\n"
        put(OTHER, peer)
        base = commit()
        module = "Challenge.lean"
        challenge_path = f"packages/zeta23/informalizations/{module}/{AUTHOR}--fixture.md"
        spec = directory_proof()["packages"]["zeta23"]
        challenge = note(module=module, declarations=[], source_commit=spec["commit"]) + "A valid formula $a+b$.\n\n"
        bad_math = {
            "unclosed matrix": (r"\begin{pmatrix} a & b", "$$", "MissingEndError"),
            "unmatched right delimiter": (r"\right)", "$", "ExtraLeftOrMissingRightError"),
            "246 nested fractions": (r"\frac{1}{" * 246 + "1" + "}" * 246, "$", "RecursionError"),
        }
        cases = [
            ("unindexed source accepts empty declarations", {challenge_path: challenge}, 0),
            ("unindexed source refuses named declarations", {challenge_path: note(module=module, declarations=["Example"], source_commit=spec["commit"])}, 1),
            *((label, {challenge_path: challenge + delimiter + tex + delimiter}, 1)
              for label, (tex, delimiter, _) in bad_math.items()),
            ("recoverable unbalanced brace", {challenge_path: challenge + "$x^{2$"}, 0),
            ("expanded math exceeds HTML limit", {challenge_path: challenge + "$x^2$ " * 30_000}, 1),
            ("valid informalization on diverged branches", {PATH: note()}, 0),
            ("own informalization edit", {OWNED: note(module="src/BuildAid/D1.lean", declarations=[]) + "Edit.\n"}, 0),
            ("own informalization deletion", {OWNED: None}, 0),
            ("public move across modules", {OWNED: None, PATH: note()}, 1),
            ("two packages with the same module path", {PATH:note(), PATH.replace("riemann-hypothesis","mathlib"):note()}, 1),
            ("agreement at the target revision", {PATH: note(agrees_with={"another-reader--fixture":hashlib.sha256(peer.encode()).hexdigest()})}, 0),
            ("stale agreement", {PATH: note(agrees_with={"another-reader--fixture":"0" * 64})}, 1),
            ("symlink in informalization path", {PATH: Path("unresolved-fixture")}, 1),
            ("file-level informalization", {PATH: note(declarations=[])}, 0),
            ("AI informalization with model", {PATH: note(origin="generated")}, 0),
            ("valid Mathlib package and pin", {PATH.replace("riemann-hypothesis","mathlib").replace(MODULE,"Archive.lean"):note(module="Archive.lean", declarations=[], source_commit=yaml.safe_load((ROOT/"proofs/rh/proof.yml").read_text())["mathlib_commit"])}, 0),
            ("wrong package for module", {PATH.replace("riemann-hypothesis","mathlib"):note(source_commit=yaml.safe_load((ROOT/"proofs/rh/proof.yml").read_text())["mathlib_commit"])}, 1),
            ("unknown module", {PATH.replace("Main.lean", "Unknown.lean"): note(module="src/Unknown.lean")}, 1),
            ("declaration in another module", {PATH: note(declarations=["GlobalTheory.Mem.Top.Bl.anyGeometry"])}, 1),
            ("public entry at byte limit", {PATH: note().ljust(PUBLIC_MAX_BYTES)}, 0),
            ("public entry above byte limit", {PATH: note().ljust(PUBLIC_MAX_BYTES + 1)}, 1),
            ("public declaration list at limit", {PATH: note(declarations=["riemannHypothesis"] * PUBLIC_MAX_DECLARATIONS)}, 0),
            ("public declaration list above limit", {PATH: note(declarations=["riemannHypothesis"] * (PUBLIC_MAX_DECLARATIONS + 1))}, 1),
            ("nested YAML fails cleanly", {PATH: "---\nvalue: " + "[" * 1024 + "]" * 1024 + "\n---\nBody"}, 1),
            ("invalid YAML scalar fails cleanly", {PATH: "---\nvalue: 2000-02-31\n---\nBody"}, 1),
            ("missing license", {PATH: note().replace("license: CC-BY-4.0\n", "")}, 1),
            ("wrong license", {PATH: note(license="MIT")}, 1),
            ("wrong source revision", {PATH: note(source_commit="0" * 40)}, 1),
            ("missing writer", {PATH: note().replace("writer: Fixture\n","")}, 1),
            ("writer filename mismatch", {PATH: note(writer="Other writer")}, 1),
            ("legacy tool", {PATH: note(tool="fixture")}, 1),
            ("two writers for one submitter", {PATH: note(), PATH.replace("--fixture","--other"): note(writer="Other")}, 0),
            ("agreement with another writer under the same handle", {
                PATH: note(agrees_with={AUTHOR+"--other":hashlib.sha256(note(writer="Other").encode()).hexdigest()}),
                PATH.replace("--fixture","--other"): note(writer="Other")}, 0),
            ("reviewed AI", {PATH: note(origin="generated",kind="ai-reviewed-by-human")}, 0),
            ("public CC0 rejected", {PATH: note(license="CC0-1.0")}, 1),
            ("public alternate license", {PATH: note(license="CC-BY-SA-4.0")}, 1),
            ("own published Apache edit", {OWNED: note(module="src/BuildAid/D1.lean",declarations=[],
                 license="Apache-2.0",**published) + "Attribution edit.\n"}, 0),
            *((f"published {licence}", {PATH:note(license=licence,**published)}, 0)
              for licence in ("Apache-2.0","MIT","CC0-1.0")),
            ("published CC BY with changes", {PATH:note(**{**published,"changes":"Excerpted."})}, 0),
            ("published Apache without a source copyright line", {PATH:note(license="Apache-2.0",
                **{**published,"copyright":"none in the source","notice":""})}, 0),
            ("own Apache refused", {PATH:note(license="Apache-2.0")}, 1),
            *((f"missing {key}", {PATH:note(license="Apache-2.0",**{k:v for k,v in published.items() if k!=key})}, 1)
              for key in ("license_source","copyright","notice","changes")),
            ("published unsupported licence", {PATH:note(license="CC-BY-SA-4.0",**published)}, 1),
            ("public source-documentation", {PATH:note(entry_type="source-documentation",**published)}, 1),
            ("other-author missing source", {PATH: note(origin="other-author")}, 1),
            ("unsafe source", {PATH: note(origin="other-author",source="file:///work")}, 1),
            ("public permission claim", {PATH: note(origin="other-author",source="https://example.org/work",license="with-permission")}, 1),
            ("kind conflicts with origin", {PATH: note(origin="wrote",kind="ai")}, 1),
            ("unknown origin", {PATH: note(origin="unknown")}, 1),
            ("self agreement", {PATH: note(agrees_with={AUTHOR+"--fixture":"a"*64})}, 1),
            ("invalid kind", {PATH: note(kind="unclassified")}, 1),
            ("incorrect declarations type", {PATH: note(declarations="riemannHypothesis")}, 1),
            ("unknown field", {PATH: note(extra=True)}, 1),
            ("duplicate metadata key", {PATH: note().replace("---\n\n", "author: fixture-reader\n---\n\n")}, 1),
            ("wrong author in metadata", {PATH: note(author="another-reader")}, 1),
            ("other author's edit", {OTHER: note(author="another-reader") + "Edit.\n"}, 1),
            ("other author's deletion", {OTHER: None}, 1),
            ("other author's rename", {OTHER: None, PATH: note()}, 1),
            ("mixed code and informalization", {PATH: note(), "README.md": "A mixed change.\n"}, 1),
            ("code-only change", {"a.txt": "A code change.\n"}, 0),
        ]
        for label, changes, expected in cases:
            git("checkout", "--quiet", "--detach", common)
            for path, body in changes.items():
                put(path, body)
            head = commit()
            args = [sys.executable, str(CHECK), "--repo", str(repo), "--database", str(database),
                    "--author", AUTHOR, "--base", base, "--head", head]
            run = subprocess.run(args, capture_output=True, text=True, env=env)
            message = (run.stdout or run.stderr).strip()
            assert run.returncode == expected and "Traceback" not in message, (label, run.returncode, message)
            expected_message = {
                "unindexed source refuses named declarations": "zeta23 has no declaration index; leave declarations empty",
                "public move across modules": "one package and one module",
                "two packages with the same module path": "one package and one module",
                "public entry above byte limit": "256,000 bytes",
                "public declaration list above limit": "64 declarations",
                "nested YAML fails cleanly": "nested too deeply",
                "invalid YAML scalar fails cleanly": "invalid YAML front matter",
            }.get(label)
            if label in bad_math:
                tex, _, reason = bad_math[label]
                assert f"{challenge_path}: cannot render formula `{tex}`" in message and reason in message, label
            if label == "expanded math exceeds HTML limit":
                assert challenge_path in message and "limit 1,000,000 bytes" in message, message
            if expected_message:
                assert expected_message in message, (label, message)
            results.append({"fixture": label, "exit": run.returncode, "message": message})
    return results


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    args = cli.parse_args()
    print(json.dumps(exercise(args.database.resolve()), indent=2) + "\n", end="")
