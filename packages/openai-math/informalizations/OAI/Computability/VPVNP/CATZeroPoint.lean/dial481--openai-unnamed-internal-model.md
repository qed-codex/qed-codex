---
{
  "module": "OAI/Computability/VPVNP/CATZeroPoint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CATZeroPoint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CATZeroPoint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Fractional points of CAT(0) segments

The squared-distance comparison of (4.2) determines the point at each
fraction of a segment. These points have constant speed and interpolation
on a subsegment agrees with interpolation on the full segment.


### `catPoint`

 The point at fraction `t` on the segment from `a` to `b`. 

### `dist_left_catPoint`

 Distance to the initial endpoint. 

### `dist_right_catPoint`

 Distance to the final endpoint. 

### `catPoint_unique`

 Endpoint distances characterize a fractional point uniquely. 

### `dist_catPoint_catPoint`

 Constant speed along a CAT(0) segment. 

### `catFraction`

 Fraction obtained by taking a fraction `u` of the way from `s` to `t`. 

### `catPoint_subsegment`

 A segment between two fractional points follows the original segment, including when
the two fractions are in decreasing order. 
