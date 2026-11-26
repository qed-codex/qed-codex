---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Projective.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Projective.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Projective.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The projective maps and frozen affine slices in Appendix A.2

These lemmas isolate the actual maps used by the character construction. A
frozen eigenvalue slice is convex; the full nonlinear fixed set is only claimed
to be closed. The last lemma is the compact finite-intersection step, not an
existence theorem for the required finite common fixed points.


### `projective`

 The normalized multiplication map from Appendix A.2. 

### `eigenSlice`

 Freeze the eigenvalue as a real constant, retaining affine equations. 

### `multiplicativeSet`

 The original nonlinear multiplicativity equations for one multiplier. 

### `projective_mem_eigenSlice`

 All other projective maps preserve every frozen equation. No cancellation
or division by a possibly zero coordinate is needed for this algebraic fact. 

### `freeze_fixedPoint`

 Once a fixed point is obtained, freezing its eigenvalue preserves that
witness and yields a compact convex slice invariant under every projective map. 

### `multiplicative_of_finite_common_points`

 The compactness step in Appendix A.2. Finite common fixed points are an
explicit obligation; this lemma does not assume or assert their existence. 
