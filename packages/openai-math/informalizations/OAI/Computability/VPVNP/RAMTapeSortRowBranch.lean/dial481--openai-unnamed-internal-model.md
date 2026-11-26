---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatching and closing a comparison row

The public local-stride bit selects the corresponding row pass. The
private partner cursor is emptied when that pass returns.


### `rowCost_le`

 One row visits at most two records of its block, verifies at most one
outgoing field, and selects one of its two operands. 
