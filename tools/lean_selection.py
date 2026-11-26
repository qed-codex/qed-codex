"""Materialize a deterministic source archive from the pinned Git tree and Lean imports."""
import hashlib
import io
import re
import subprocess
import tarfile



def select_archive(cfg, repo, archive, source_surface):
    prefix = cfg["folder"] + "/"
    pin = cfg["commit"]
    tree = subprocess.check_output(["git", "-C", repo, "ls-tree", "-rz", pin, "--", prefix])
    extra_files = set(cfg.get("extraFiles", []))
    objects = {}
    for entry in tree.split(b"\0"):
        if entry:
            info, name = entry.split(b"\t", 1)
            path = name.decode().removeprefix(prefix)
            if path.endswith(".lean") or path in extra_files:
                objects[path] = info.split()[2].decode()
    selected = {}

    def read(path):
        if path not in selected:
            working = repo / prefix / path
            oid = objects[path]
            data = working.read_bytes() if working.is_file() else subprocess.check_output(
                ["git", "-C", repo, "cat-file", "blob", oid])
            if hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest() != oid:
                raise ValueError(f"Git blob differs from {pin} for {path}")
            selected[path] = data
        return selected[path]

    groups = {}
    for root in cfg["roots"]:
        reached = set()
        pending = [root]
        while pending:
            path = pending.pop()
            if path in reached:
                continue
            reached.add(path)
            code = source_surface(read(path).decode())[1]
            for line in re.findall(r"^[ \t]*(?:(?:public|private|meta)\s+)*import[ \t]+([^\n]+)", code, re.M):
                for name in line.split():
                    dependency = cfg.get("modulePrefix", "") + name.replace(".", "/") + ".lean"
                    if dependency in objects:
                        pending.append(dependency)
        groups[root] = reached
    for path in [*cfg["extraModules"], *sorted(extra_files)]:
        read(path)
    with tarfile.open(archive, "w") as tar:
        for path, data in sorted(selected.items()):
            entry = tarfile.TarInfo(pin + "/" + prefix + path)
            entry.size = len(data)
            tar.addfile(entry, io.BytesIO(data))
    return groups
