---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotWidthState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidthState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidthState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The selected shrinking state's canonical width column

The graph and slot order read by the width writer are those used in the
selected compression branch. The old-arc-indexed split words are mapped to
the outgoing ports of the next state in its stored base order.


### `branchWidth`

 Width of the specified motif role edge in the selected term and layout before division into
surviving slots. 

### `next_counts`

 The shared port lengths agree with the branch's own base and lane cardinals. 

### `portIndex_next`

 Re-association of base, tag and remaining lane in the two mixed-radix
implementations produces the same canonical port number. 

### `width_run`

 Actual native width scan in state coordinates. Its input split rows can
be the simultaneously established rows of `ShrinkSliceSweep.graph_run`. 
