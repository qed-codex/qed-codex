---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermPhases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPhases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPhases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The consecutive demand-gather and term-selection segments

The first segment reads the balanced AB table and old CD table. Its final
memory is the initial memory of the second segment. The second segment
admits precisely the paper's term choices. Its final memory contains
both the selected term rows and the original widths and starts needed
by the shrinking kernel.


### `bundles`

 Number of directed packed bundles, counting each base vertex, packing tag, residual lane
and outgoing port. 

### `ranks`

 Number of motif ranks or balanced pieces in one shrinking bundle at input degree exponent
`a`. 

### `oldRows`

 Readback of the thick and CD width rows and AB pieces in their physical per-bundle orders. 
