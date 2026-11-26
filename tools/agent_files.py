"""Write the static reading guide and ledger index alongside the pre-rendered pages."""

import hashlib
import json
import os
import subprocess
from pathlib import Path
from urllib.parse import quote, urlsplit

from check_informalization_pr import note_key


def write_agent_files(db, stage, proof, settings, samples, module_pages, base_url, catalogue):
    repository = settings["repository"].rstrip("/")
    ledger = Path("packages")
    # A change to a template or report does not change the raw Markdown addresses.
    revision = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", ledger], text=True
    ).strip()
    status = subprocess.check_output([
        "git", "status", "--porcelain=v1", "-z", "--no-renames", "--untracked-files=all",
        "--", ledger,
    ])
    drafts = {os.fsdecode(record[3:]) for record in status.split(b"\0") if record}
    raw_root = "https://raw.githubusercontent.com" + urlsplit(repository).path
    site_root = (base_url or settings["base_url"]).rstrip("/")
    entries = []
    for row in db.execute("""
        SELECT m.package, m.path AS module, i.writer, i.kind, i.origin, i.author,
               i.license, i.copyright, i.license_source, i.notice, i.changes, i.source_commit, i.declarations_json
        FROM informalizations AS i JOIN modules AS m ON i.module = m.id
        WHERE i.entry_type='informalization'
        ORDER BY m.package, m.path, i.submitted_order, i.author, i.writer
    """):
        entry = dict(row)
        package, module = entry["package"], entry["module"]
        key = note_key(entry["author"], entry["writer"])
        file = ledger / package / "informalizations" / module / (key + ".md")
        entry["declarations"] = json.loads(entry.pop("declarations_json"))
        entry["page"] = site_root + module_pages[package, module] + "#informalization-" + quote(key)
        # An uncommitted local draft has a prospective main address until it lands.
        ref = "refs/heads/main" if file.as_posix() in drafts else revision
        entry["markdown"] = f"{raw_root}/{ref}/{quote(file.as_posix())}"
        entry["sha256"] = hashlib.sha256(file.read_bytes()).hexdigest()
        entries.append(entry)
    (stage / "informalizations.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    sample_links = "\n".join(
        f"- [{s['value'].rsplit('/', 1)[-1]}](/sample/{s['package']}/{s['id']}/) ({s['type']})"
        for s in samples
    )
    proof_links = "\n".join(
        f"- [{item.get('markdownTitle', item['title'])}]({item['source']}) — {item.get('listCredit', item['credit'])}. "
        f"Commit `{item['commit']}`. Licence: {item['license'] or 'none stated in the pinned source'}."
        for item in catalogue
    )
    guide = Path("tools/templates/llms.txt").read_text(encoding="utf-8")
    (stage / "llms.txt").write_text(
        guide.format(**proof, ledger_revision=revision, contact=settings["contact_email"], sample_links=sample_links, proof_links=proof_links),
        encoding="utf-8",
    )
