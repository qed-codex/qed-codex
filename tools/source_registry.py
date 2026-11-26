"""Load pinned library and result records, independently of their public addresses."""
import json
import re
import yaml
from pathlib import Path


def directory_proof(read=None):
    if read is None:
        read = lambda name: Path(name).read_bytes()
    proof = json.loads(read("proofs/rh/proof.yml"))
    proof["packages"] = {key: json.loads(read(f"packages/{key}/source.yml"))
                         for key in proof.pop("sourceKeys")}
    return proof


def distinct_spellings(names, label):
    seen = set()
    for name in names:
        key = name.casefold()
        if key in seen:
            raise ValueError(f"Duplicate or case-only {label}: {name}")
        seen.add(key)


def result_files(source):
    return ([source["proofFile"]] if "proofFile" in source else []) + source.get("proofFiles", [])


def proof_title(proof):
    if "metadata" in proof:
        return yaml.safe_load(Path(proof["metadata"]).read_bytes())["project"]["name"]
    if "readmeOpening" in proof:
        heading = Path(proof["readmeOpening"]).read_text().splitlines()[0].removeprefix("# ")
        return re.sub(r"[*_]", "", heading.replace("<sup>", "^(").replace("</sup>", ")"))
    return proof["title"]


def populate_proofs(db, packages):
    for key, source in packages.items():
        modules = dict(db.execute("SELECT path,id FROM modules WHERE package=?", (key,)))
        distinct_spellings(modules, "module path in " + key)
        records = [json.loads(Path(p).read_text()) for p in result_files(source)]
        distinct_spellings((p.get("id", key) for p in records), "proof ID in " + key)
        for proof in records:
            proof_id = proof.get("id", key)
            names = proof.get("declarations", [proof["declaration"]] if proof.get("declaration") else [])
            paths = modules
            if "members" in proof:
                paths = Path(proof["members"]).read_text().splitlines()
                config = json.loads((Path(proof["artifacts"]) / "config.json").read_text())
                challenge = config["challenge_module"].removeprefix("ComparatorChallenges.")
                if (config["challenge_module"] != "ComparatorChallenges." + challenge
                        or proof["statement"] != config["challenge_module"].replace(".", "/") + ".lean"
                        or proof["solution"] != config["solution_module"].replace(".", "/") + ".lean"
                        or not challenge.isidentifier() or proof_id != key + "/" + challenge
                        or proof["root"] not in paths or names != config["theorem_names"] or not names):
                    raise ValueError(f"Invalid proof membership or challenge ID: {proof_id}")
            if comparator := proof.get("comparator"):
                config = json.loads(Path(comparator["file"]).read_bytes())
                for role, field in (("statement", "challenge_module"), ("solution", "solution_module")):
                    expected = comparator["sourceDirs"][role] + config[field].replace(".", "/") + ".lean"
                    if proof[role] != expected:
                        raise ValueError(f"{proof_id}: invalid {role} path {proof[role]}, expected {expected}")
                if names != config["theorem_names"]:
                    raise ValueError(f"{proof_id}: comparator theorem names differ")
            root, statement, solution = (modules[proof[k]] if k in proof else None
                                         for k in ("root", "statement", "solution"))
            db.execute("INSERT INTO proofs VALUES(?,?,?,?,?,?,?)",
                       (proof_id,key,next(iter(names), None),root,statement,solution,proof_title(proof)))
            aliases = {}
            for name in names:
                for alias in (name.lower(), name.rsplit(".", 1)[-1].lower()):
                    aliases.setdefault(alias, name)
            db.executemany("INSERT INTO proof_names(lookup,proof,name) VALUES(?,?,?)",
                           ((alias,proof_id,name) for alias,name in sorted(aliases.items())))
            for role in ("statement", "solution"):
                role_paths = ([proof[role]] if role in proof else []) + proof.get("additionalRoles", {}).get(role, [])
                db.executemany("INSERT INTO proof_roles VALUES(?,?,?)",
                               ((modules[path], proof_id, role) for path in role_paths))
            db.executemany("INSERT INTO proof_modules VALUES(?,?)", ((proof_id,modules[path]) for path in paths))
