"""Keep the order in which informalizations entered this ledger, including renamed files."""
import hashlib
import json
import subprocess
from pathlib import Path


INITIAL_ORDER = "tools/initial-ledger-order.json"


def restore_initial_order(orders, snapshot):
    """Apply the published order to the sorted ledger paths of the root commit."""
    paths = sorted(path for path in orders if path.endswith(".md") and "/informalizations/" in path)
    digest = hashlib.sha256("".join(path + "\n" for path in paths).encode()).hexdigest()
    if digest != snapshot["pathListSha256"]:
        raise ValueError("Initial ledger inventory does not match its submission-order snapshot")
    end = 0
    for count, position in snapshot["runs"]:
        if count < 1 or position < 1 or end + count > len(paths):
            raise ValueError("Invalid initial submission-order range")
        for path in paths[end:end + count]:
            orders[path] = position
        end += count
    if end != len(paths):
        raise ValueError("Incomplete initial submission-order snapshot")
    return max(orders.values())


def submission_order(directory, repo=Path("."), previous=()):
    def git(*args):
        return subprocess.check_output(["git", "-C", repo, *args])

    if git("rev-parse", "--is-shallow-repository").strip() == b"true":
        raise ValueError("Submission order requires complete ledger history (git fetch --unshallow)")
    folder = directory.as_posix()
    roots = [folder, *(p.as_posix() for p in previous)]
    commits = git("rev-list", "--first-parent", "--reverse", "--full-history", "HEAD", "--", *roots).splitlines()
    orders = {}
    position = 0
    for commit in commits:
        position += 1
        parents = git("show", "-s", "--format=%P", commit).split()
        revisions = (parents[0], commit) if parents else ("--root", commit)
        fields = iter(git("diff-tree", "-r", "-M", "--no-commit-id", "--name-status", "-z",
                          *revisions, "--", *roots).decode().split("\0")[:-1])
        for status in fields:
            path = next(fields)
            if status.startswith("R"):
                orders[next(fields)] = orders.pop(path, position)
            elif status == "D":
                orders.pop(path, None)
            elif status == "A":
                orders[path] = position
        if not parents and folder == "packages" and git("ls-tree", "--name-only", commit, "--", INITIAL_ORDER):
            snapshot = json.loads(git("show", commit.decode() + ":" + INITIAL_ORDER))
            position = restore_initial_order(orders, snapshot)
    # A local draft previews after every committed contribution.
    for path in (repo / directory).rglob("*.md"):
        orders.setdefault(path.relative_to(repo).as_posix(), position + 1)
    return orders
