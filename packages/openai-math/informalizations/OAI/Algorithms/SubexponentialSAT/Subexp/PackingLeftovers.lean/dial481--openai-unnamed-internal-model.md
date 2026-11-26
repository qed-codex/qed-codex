---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingLeftovers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingLeftovers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingLeftovers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual leftover packing pass

The immutable covered table is searched for every original vertex. A found
vertex is skipped. A missing vertex is appended to reversed storage and both
lookup tables, with actual unary rank/address increments.


### `command_eval`

 Complete scan of actual original-vertex records. The saved covered table
is unchanged, and all work ports are cleared. 

### `fold_advance_eq`

 Filtering is a specification of the proved scan; the machine itself
performs the selector call for every vertex. 

### `traceCost_le`

 Polynomial bound in serialized covered-table size, vertex count, largest
unary vertex, and the initial unary counters. 
