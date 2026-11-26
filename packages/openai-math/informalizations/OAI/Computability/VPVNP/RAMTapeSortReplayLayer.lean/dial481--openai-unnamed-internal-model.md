---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortReplayLayer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayLayer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayLayer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # One materialized sorting layer agrees with the checked RAM replay

The machine compares arbitrary fixed-width record fields. Its initially
canonical local block supplies the left operand at every row. If every
new row flag passes, the next block is canonical and parses to the checked
replay's next block. The acceptance test also covers malformed incident fields.


### `State`

 The current block of raw five-word rows and the accumulated Boolean validity flags of the
physical replay. 

### `update`

 Replay one bitonic stage using its incident send and receive fields, replacing the local
block by the selected rows and accumulating their checks. 

### `decoded`

 Parse every raw five-word row in a physical block to the ordered slot used in the checked
sorting replay. 

### `CanonicalBlock`

 Each raw row of this block is exactly the canonical encoding of its parsed slot. 

### `update_retains`

 Existing failure flags are retained even when this layer sees arbitrary bits. 
