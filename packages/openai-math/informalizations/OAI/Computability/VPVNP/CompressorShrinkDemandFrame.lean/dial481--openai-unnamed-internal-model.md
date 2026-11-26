---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkDemandFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Retaining the sorted width and field-start rectangles

The dense demand array and term records can be allocated beyond the old
width tables. Any scan that preserves the preceding addresses then keeps
the six width and field-start columns required by the interval kernels.


### `Before`

 The two old rectangles have their own strides. The balanced AB rectangle
has one live entry per CD rank. All six columns precede the scratch arena. 

### `retain`

 The six source columns still represent the same old widths and starts
after the dense demand and term phases. 
