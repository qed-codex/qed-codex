---
{
  "module": "OAI/Computability/VPVNP/CompressorSurvivingReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a surviving width from its admitted term

The selected layout chooses one of two groups of four payload cells. The width
of its role is that cell plus one selector field per repetition, computed from
the repetition header of the same dense motif row.


### `selected_width_readback`

 Reading the repetition and payload as naturals gives the selected role's
width, including all selector bits. 

### `selected_width_word`

 The machine's word multiply and add agree with the exact selected width
whenever that output fits in a word. 
