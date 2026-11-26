---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowCompare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowCompare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowCompare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing a comparator at a local or cross-site sorting row

The selected source determines which physical stream supplies the right
record. Verification consumes the outgoing copy. Selection prepends the
chosen record in reverse bit order to the next block, and both operations
push their validity bit.


### `CompareReady`

 The comparator starts with w unary width markers and empty width scratch, saved operand
buffers and selection staging. 

### `compareResult`

 The caller retains the unread part of both operands. 

### `verify_runs`

 Verify a cross-site send against the local slot, retaining its unread tail. 

### `select_runs`

 Execute a known comparator orientation on two prepared operand streams. 

### `oriented_runs`

 Reading the public orientation takes one instruction before selection. 
