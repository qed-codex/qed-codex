"""Select static records and run the same indexed statements as the browser."""
from source_registry import directory_proof
import csv
import hashlib
from html import escape, unescape
import re
import json
import os
import sqlite3
import subprocess
import yaml
from pathlib import Path

from agent_files import write_agent_files
from informalizations import render_informalization
from fixtures import parameters
from statement_links import unlinked_cards


def proof_index_rows(db):
    # Aggregate entries per module first. A shared module counts once for each proof that uses it.
    return [dict(row) for row in db.execute("""
        WITH entries AS (
            SELECT module, max(entry_type='source-documentation') AS documented,
                   sum(entry_type='informalization' AND license!='with-permission') AS contributed
            FROM informalizations GROUP BY module
        ), extra_role_modules AS (
            SELECT DISTINCT r.proof, r.module FROM proof_roles r
            WHERE NOT EXISTS (
                SELECT 1 FROM proof_modules m WHERE m.proof=r.proof AND m.module=r.module
            )
        )
        SELECT p.id, p.source, count(pm.module) AS modules,
               coalesce(sum(e.documented), 0) AS documented,
               coalesce(sum(e.contributed), 0) + coalesce((
                   SELECT sum(other.contributed) FROM extra_role_modules r
                   JOIN entries other ON other.module=r.module WHERE r.proof=p.id
               ), 0) AS contributed
        FROM proofs p LEFT JOIN proof_modules pm ON pm.proof=p.id
        LEFT JOIN entries e ON e.module=pm.module
        GROUP BY p.id ORDER BY p.title COLLATE NOCASE, p.id
    """)]


def registered_proofs(db, packages):
    """Use each proof's pinned metadata for its landing page, directory listing and agent guide."""
    counts = dict(db.execute("SELECT package, count(*) FROM modules GROUP BY package"))
    catalogue = []
    for package, source in packages.items():
        for file in source.get("proofFiles", []):
            details = json.loads(Path(file).read_text())
            artifacts = Path(details["artifacts"])
            material = {}
            for name, digest in details["assetHashes"].items():
                data = (artifacts / name).read_bytes()
                if hashlib.sha256(data).hexdigest() != digest:
                    raise ValueError(f"Pinned proof artifact differs: {artifacts / name}")
                material[name] = data.decode()
            modules = [dict(row) for row in db.execute("""
                SELECT m.path FROM proof_modules p JOIN modules m ON m.id=p.module
                WHERE p.proof=? ORDER BY m.path""", (details["id"],))]
            root = f"{source['url']}/blob/{source['commit']}/"
            catalogue.append(dict(details, package=details["id"], sourceKey=package,
                                  source=root + source["repositoryFolder"] + details["statement"],
                                  commit=source["commit"], rootURL=root, material=material,
                                  scopeHTML=render_informalization(material["scope.md"],
                                      root + source["repositoryFolder"] + details["scope"]),
                                  moduleCount=len(modules), modules=modules, titleHTML=escape(details["title"]),
                                  credit="OpenAI (unnamed internal model)", creditSource=root + "README.md",
                                  license=source["license"]))
        if "proofFile" not in source:
            continue
        details = json.loads(Path(source["proofFile"]).read_text())
        folder = source.get("repositoryFolder", "").rstrip("/")
        pin = f"{source['url']}/tree/{source['commit']}" + ("/" + folder if folder else "")
        item = dict(package=package, source=pin, commit=source["commit"], moduleCount=counts[package],
                    verificationRecords=details["verificationRecords"])
        if "papers" in details:
            item.update(papers=details["papers"], papersHeading=details.get("papersHeading", "Papers"))
        if "metadata" in details:
            data = Path(details["metadata"]).read_bytes()
            if hashlib.sha256(data).hexdigest() != details["metadataSha256"]:
                raise ValueError(f"Project metadata differs from its pin for {package}")
            item["metadata"] = yaml.safe_load(data)
            project = item["metadata"]["project"]
            title = project["name"]
            item.update(title=title, titleHTML=escape(title), credit=", ".join(project["authors"]),
                        license=project["license"], creditSource=source["url"] + "/blob/" +
                        source["commit"] + "/" + folder + "/" + Path(details["metadata"]).name)
        elif "readmeOpening" in details:
            data = Path(details["readmeOpening"]).read_bytes()
            if hashlib.sha256(data).hexdigest() != details["openingSHA256"]:
                raise ValueError(f"README opening differs from its pin for {package}")
            root = source["url"] + "/blob/" + source["commit"] + "/" + source["repositoryFolder"]
            excerpt = render_informalization(data.decode(), root + "README.md")
            # Enable just the literal superscript pair after the Markdown sanitizer.
            excerpt = excerpt.replace("&lt;sup&gt;", "<sup>").replace("&lt;/sup&gt;", "</sup>")
            heading = re.match(r"<h1>(.*?)</h1>", excerpt, re.S)
            if not heading:
                raise ValueError(f"Missing project title in the pinned README for {package}")
            # The list supplies its own link; keep the title's inline typography.
            title_html = re.sub(r"<(?!/?(?:sup|sub|em|strong|code)>)[^>]+>", "", heading[1])
            plain = title_html.replace("<sup>", "^(").replace("</sup>", ")")
            license_id = json.loads((Path("packages") / package / "import.json").read_text())["license"]
            item.update(title=unescape(re.sub(r"<[^>]+>", "", plain)), titleHTML=title_html,
                        markdownTitle=data.decode().splitlines()[0].removeprefix("# "),
                        credit=details["writer"], listCredit=details.get("listCredit", details["writer"]), creditSource=details["creditSource"], license=license_id,
                        openingHTML=excerpt, root=root, noticeText=details.get("noticeText"))
        else:
            title = details["title"]
            item.update(title=title, titleHTML=escape(title), credit=" and ".join(details["authors"]),
                        creditSource=details["creditSource"], license=details["license"])
        if "materials" in details:
            sections = []
            for material in details["materials"]:
                path = material["path"]
                raw = (Path(details["artifacts"]) / path).read_bytes()
                if hashlib.sha256(raw).hexdigest() != material["sha256"]:
                    raise ValueError(f"{package}: pinned {path} differs")
                address = item["root"] + path
                body = (render_informalization(raw.decode(), address) if path.endswith(".md")
                        else "<pre>" + escape(raw.decode()) + "</pre>")
                sections.append(dict(heading=material["heading"], address=address, html=body, path=path))
            item.update(sections=sections, sourceDocuments=details["sourceDocuments"],
                        otherVersions=details["otherVersions"], rootModule=details["root"], solution=details["solution"])
        if "moduleList" in source:
            item["modules"] = [dict(row) for row in db.execute("""
                SELECT m.path,
                    EXISTS(SELECT 1 FROM informalizations WHERE module=m.id AND entry_type='source-documentation') AS documented,
                    EXISTS(SELECT 1 FROM informalizations WHERE module=m.id AND entry_type='informalization') AS contributed
                FROM modules m WHERE m.package=? ORDER BY m.path""", (package,))]
        catalogue.append(item)
    return catalogue


def render(database, stage, base_url=None, preview_probe=False, *, database_source_docs=True):
    proof = directory_proof()
    settings = json.loads(Path("site-settings.json").read_text())
    proof["repository"] = settings["repository"]
    for package, spec in proof["packages"].items():
        terms = stage / "LICENSES" / package
        spec["sourceTerms"] = {name: f"/LICENSES/{package}/{name}.txt"
                               for name in ("LICENSE", "NOTICE") if (terms / (name + ".txt")).is_file()}

        if (terms / "ATTRIBUTION.md").is_file():
            spec["sourceTerms"]["ATTRIBUTION.md"] = f"/LICENSES/{package}/ATTRIBUTION.md"

    samples = json.loads((stage / "samples.json").read_text())
    queries = json.loads((stage / "queries.json").read_text())
    records = {}
    extra = {}
    with sqlite3.connect(f"{database.resolve().as_uri()}?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        counts = dict(db.execute("SELECT metric,value FROM summary"))
        offset = counts["fts_declaration_offset"]
        def record(kind, value, package=None):
            groups = [kind, "trail", "siblings"] if kind == "declaration" else [kind]
            result = {}
            for group in groups:
                args = parameters(group, value, offset, package, proof["packages"][package]["sourceRoot"] if package else None)
                for key, sql in queries[group].items():
                    result[key] = [dict(r) for r in db.execute(sql, args)]
            return result

        for sample in samples:
            data = record(sample["type"], sample["value"], sample["package"])
            if not data.get("facts", data.get("declarations")):
                raise ValueError(f"Missing sample {sample['value']}")
            records[sample["id"]] = data
        module_pages = {(s["package"], s["value"]): f"/sample/{s['package']}/{s['id']}/"
                        for s in samples if s["type"] == "module"}
        source_only = set()
        if database_source_docs:
            source_only = set(tuple(row) for row in db.execute("""
                SELECT m.package, m.path FROM modules m JOIN informalizations i ON i.module=m.id
                GROUP BY m.id HAVING COUNT(*) = SUM(i.entry_type='source-documentation')"""))
        paths = db.execute("""SELECT package,path FROM modules WHERE id IN
            (SELECT module FROM informalizations UNION SELECT module FROM links UNION
             SELECT id FROM modules WHERE spine_rank IS NOT NULL) ORDER BY path""")
        for package,path in paths:
            if (package,path) in module_pages or (package,path) in source_only:
                continue
            key = package + "/" + hashlib.sha256(path.encode()).hexdigest()[:16]
            if key in extra:
                raise ValueError(f"Duplicate static module key for {path}")
            extra[key] = record("module", path, package)
            module_pages[package, path] = f"/m/records/{key}/"
        unmatched = unlinked_cards(url for (url,) in db.execute("SELECT DISTINCT url FROM links"))
        if len(unmatched) != counts["unmatched_statements"]:
            raise ValueError("Unmatched statement page differs from the compiled summary")
        catalogue = registered_proofs(db, proof["packages"])
        proof_rows = proof_index_rows(db)
        board = record("wanted", 1)["modules"]
        write_agent_files(db, stage, proof, settings, samples, module_pages, base_url, catalogue)
    with Path("imports.tsv").open(encoding="utf-8", newline="") as ledger:
        imports = list(csv.DictReader(ledger, delimiter="\t"))
    config = {"proof": proof, "samples": samples,
              "staticModules": sorted(extra), "wantedCount": counts["most_wanted"]}
    (stage / "directory.json").write_text(json.dumps(config, ensure_ascii=False, separators=(",", ":"))+"\n")
    # System Node may need SQLite extensions omitted from the pinned compiler runtime.
    env = os.environ.copy()
    runtimes = Path("inputs/sqlite").resolve()
    env["LD_LIBRARY_PATH"] = os.pathsep.join(
        part for part in env.get("LD_LIBRARY_PATH", "").split(os.pathsep)
        if part and not Path(part).resolve().is_relative_to(runtimes)
    )
    subprocess.run(["node", "tools/prerender.mjs", str(stage)], check=True, text=True, env=env,
                   input=json.dumps({**config, "catalogue": catalogue, "proofRows": proof_rows, "settings": settings, "baseURL": base_url, "previewProbe": preview_probe, "imports": imports, "records": records, "extra": extra, "board": board, "unmatched": unmatched}, ensure_ascii=False))
