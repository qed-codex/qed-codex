---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSelectedExponentBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSelectedExponentBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSelectedExponentBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Histogram headroom at a selected shrinking level

The tag determines the scheduled shrinking pass. Its resident map witnesses
give the exponents of the selected reader, and the branch width bound controls
the number of copies in each resident map.


### `level_exponent_le_square`

 Each coordinate of the exponent vector contributed by one shrinking
vertex fits the quadratic histogram allowance. 

### `selected_exponent_le_square`

 At every shrinking vertex on the chosen execution, the input width
estimate of the branch suffices for the per-coordinate histogram bound. 
