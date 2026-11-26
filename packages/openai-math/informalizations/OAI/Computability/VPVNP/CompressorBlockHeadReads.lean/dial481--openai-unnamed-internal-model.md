---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockHeadReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeadReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeadReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read footprints of the shrinking and refresh head formulas

The online recipe can read its pitch and the graph data suffix. The four
level scalars and six table pointers lie in that suffix, as does the
selected shrinking layout bit. Arithmetic on these operands makes no
additional external reads.


### `level`

 Level arithmetic reads the physical pitch cell allowed by the calendar. 

### `resident_operands_of`

 The same operand proof applies to a smaller region preserved by the
preceding calls. Only the pitch, four scalars, six table heads and the chosen
layout bit need to be available in that region. 

### `resident_operands`

 All seven inputs shared by the hidden and map resident windows. 

### `publish_supported`

 All operands of the two-word one-shot publisher use the same allowed region. 
