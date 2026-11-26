---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkMotifOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkMotifOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkMotifOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical order of shrinking terms

A CD occurrence is stored in the row of its assigned port, at the
lane-relative rank used to split the AB bundle. The product of the two
ordinals indexes the dense demand, term and score arrays.


### `number`

 Bundle ordinal followed by the CD rank inside that bundle. 

### `stateNumber`

 The dense order uses the same base, tag and lane numerals as the
shrinking graph scans. 

### `entries`

 The cardinal-length form can be used directly by history readers. 
