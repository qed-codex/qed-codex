---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Passing the sorted shrinking graph to the next compressor state

The graph used by `State.shrinkNext` uses the same current base index, binary
tag index, subdivisions and common layout as the native slot builder. Its
base-arc numbers are exactly the ordinary port numbers in the shared
incidence directory. A scatter of the forward base table constructs the
inverse at the same numerical indices.


### `levelShape`

 Slot directory dimensions for this shrink, using the current base vertices and residual
lanes and the subdivisions chosen for the outgoing degree. 

### `selectedLayout`

 The layout with lower group energy for the selected term's widths, choosing the false
layout on a tie. 

### `BaseForward`

 Base columns shared by the following level in the canonical port order. 

### `next_baseMatching`

 The kernel's actual branch and the native builder have identical topology. 

### `next_run`

 Native slot construction directly on the same selected state as the
compression kernel, using the canonical next-level port addresses. 

### `scatterBaseIn`

 Inverting the canonical base-mate permutation needs one two-probe
scatter per base port. Forward and shift columns survive in separate arrays. 
