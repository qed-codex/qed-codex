---
{
  "module": "OAI/Computability/VPVNP/Compression.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Compression.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Compression.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterating the wire energy estimate

Equation (7.4) of *VP and VNP differ over every field* follows from the
energy estimate for one block and the geometric decrease in the number of
positions. The bound below gives the constant multiplying the initial
position count explicitly.


### `widthSum_le_sqrtEnergy`

 With positive wire masses of total one, the energy controls total width. 

### `scaledEnergy_le`

 Multiplication by `4^i` makes the one-block estimates telescope. The term
from block `i` then has ratio `4/κ²` to the corresponding term from block
`i-1`. Only the estimates before the specified horizon are needed. 

### `sqrtEnergy_le`

 Equation (7.4), with an error coefficient independent of the number
of blocks. Here `P / κ^i` is the position count at the start of block `i`. 
