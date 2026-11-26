"""Pack nearby frozen trace nodes together with the ancestors needed to read each trail."""
import json
from pathlib import Path

# A shard contains its own ancestors, so a trail needs one request at any depth.
NODES_PER_PIECE = 512


def write_trails(db, folder: Path, store):
    folder.mkdir()
    nodes = dict((row[0],row[1:]) for row in db.execute("""
        SELECT t.id,t.parent,m.package,m.path,t.line,t.use_line,d.id IS NOT NULL,
               coalesce(d.name,t.source_name)
        FROM trace t JOIN modules m ON m.id=t.module
        LEFT JOIN declarations d ON d.id=t.declaration ORDER BY t.id"""))
    if not nodes:
        return
    for base in range(0,max(nodes)+1,NODES_PER_PIECE):
        rows = {}
        for target in range(base,base+NODES_PER_PIECE):
            if target not in nodes or not nodes[target][5]:
                continue
            node = target
            while node is not None and node not in rows:
                rows[node] = nodes[node]
                node = nodes[node][0]
        if rows:
            store(folder / str(base // NODES_PER_PIECE),
                  json.dumps(rows,ensure_ascii=False,separators=(",", ":")).encode())
