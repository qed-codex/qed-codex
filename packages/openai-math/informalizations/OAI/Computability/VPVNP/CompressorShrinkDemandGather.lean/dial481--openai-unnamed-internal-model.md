---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkDemandGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkDemandGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering the two rectangular shrink demands in motif order

The AB and CD rectangles may use different strides. Each visit reads one
cell of each rectangle and writes both values into the next dense demand
row. The output is disjoint from both sources. Source padding is never read.


### `Layout`

 The two source rectangles need room for their strides and the destination
needs two cells per motif. Either rectangle can precede or follow the output. 

### `source_range`

 Each physical read address belongs to its live input rectangle. 

### `Gathered`

 Exact execution, dense row contents, frame, and costs of one shrink gather pass. 

### `gather`

 The scan reads the original source cell at every bundle and rank, even
when earlier rows have already been written to dense memory. 
