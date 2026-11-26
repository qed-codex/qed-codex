---
{
  "module": "OAI/Computability/VPVNP/PairRefreshResidentMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentMap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the selected resident refresh map

The selected interpreter receives descriptor words computed from the level
arrays and resident bits from the two node buffers. Its raw operand, selector,
and histogram ranges are supplied by the concrete packed workspace.


### `map_native`

 The actual selected map exits at the caller's continuation or at a rejecting
opcode. Its histogram additions are the multiplicities of its emitted labels.
Words preceding the scratch directory and outside the histogram are preserved. 
