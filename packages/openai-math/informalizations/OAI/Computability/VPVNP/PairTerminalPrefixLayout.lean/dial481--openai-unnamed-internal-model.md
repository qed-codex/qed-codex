---
{
  "module": "OAI/Computability/VPVNP/PairTerminalPrefixLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal width scan in the actual descriptor workspace

The last reserved level's packed width column precedes its prefix table.
The high header contains the total and role offset, above every live table.
The terminal bootstrap supplies the scan's operands and zero accumulator
while preserving the actual incidence columns.


### `header_val`

 The master link and the terminal bootstrap compute the same high header. 

### `packed_layout`

 The prefix table and high accumulator obey both the scalar scan's range
conditions and the terminal worker's header separation conditions. 

### `run_after_bootstrap`

 Run the terminal bootstrap followed by the complete prefix worker stage on
the same selected final state. The role offset and bit width are the actual
traversal storage size and total width of that state. 
