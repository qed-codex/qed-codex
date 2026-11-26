---
{
  "module": "OAI/Computability/VPVNP/SliceGeometryPinning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryPinning.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryPinning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite slices from coordinate projections

For a coordinate image that is cofinite in the algebraic closure, pin that
coordinate to a base-field value in the image. Finite coordinate images only
shrink during later cuts. If each exceptional set has at most `B` elements and
`B < #K`, at most one pin per variable produces a nonempty slice with at most
`B^t` geometric points.


### `pinnedPoints`

 Geometric points satisfying the original equations and a set of base-field
coordinate pins. 

### `coordinateImage`

 The possible values of coordinate `i` on a geometric set. 

### `boundedOrCobounded`

 A coordinate image has at most `B` points, or its complement has at most
`B` points. The finite-set hypotheses distinguish these alternatives even when
`Set.ncard` would vanish on an infinite set. 

### `exists_finite_pinned_slice`

 At most `t` distinct coordinate equations suffice when every projection of
a partially pinned system has a bounded exceptional set. 
