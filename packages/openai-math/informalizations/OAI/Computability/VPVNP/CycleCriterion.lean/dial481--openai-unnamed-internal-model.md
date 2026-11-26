---
{
  "module": "OAI/Computability/VPVNP/CycleCriterion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleCriterion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleCriterion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recognizing a spanning cycle by its first return

A walk from one root can check a Boolean adjacency matrix one row at a time.
If it first returns to the root after exactly as many steps as there are vertices,
the visited rows comprise the whole matrix.


### `RowValid`

 The scanned successor is the only true entry of the row. 

### `mem_spanningCycleEdges_iff_firstReturn`

 A row-by-row walk accepts exactly the adjacency matrices of spanning cycles.
It rejects a missing or ambiguous outgoing edge on any visited row, as well as
a return to the root before the final step. 
