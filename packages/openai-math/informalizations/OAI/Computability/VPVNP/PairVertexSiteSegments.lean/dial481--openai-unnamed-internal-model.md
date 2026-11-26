---
{
  "module": "OAI/Computability/VPVNP/PairVertexSiteSegments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexSiteSegments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexSiteSegments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing the actual ordinal guard and persistent return in the vertex image 

### `BootstrapLabel`

 The entry guard, exit tests, and site bootstrap labels installed before the geometry
segment. 

### `BootstrapLabel.stage`

 Interpret a local bootstrap instruction label as its stage in the terminal site program. 

### `bootstrapPC`

 Map a terminal site stage into the bootstrap's program counters, using the supplied
fallback for stages outside this block. 

### `bootstrapReg`

 Resolve bootstrap registers from the DFS, saved-operand, and local working banks. 

### `bootLabels`

 Number the finite set of bootstrap labels to place the site-entry instructions in a
segment. 

### `bootstrapSegment`

 Install the terminal site guard and bootstrap instructions with three local working
registers before entering geometry. 

### `finishSegment`

 The four return rows reload the genuine persistent ordinal, increment
it and return the resulting word. 

### `segments`

 Assign concrete segments to all named vertex parts, including the fixed bootstrap and
finishing blocks. 

### `sitePC`

 Host program counter of a terminal site-bootstrap label in the assembled vertex. 

### `finishPC`

 Host program counter of a local finishing instruction in the assembled vertex. 

### `siteBank`

 The bootstrap and return fragments use their own temporaries, alongside
the same DFS and stable register banks. 

### `bootBank`

 Register assignment for site-bootstrap instructions using the bootstrap segment's three
work registers. 

### `finishBank`

 Register assignment for final site-return instructions using the finishing segment's three
work registers. 

### `returnPC`

 Resolve the terminal site's increment, unit, add, and return stages to the installed
finishing code. 
