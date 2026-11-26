---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Interval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Interval.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Interval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reconstruction of one rational variable

The compatibility conditions produced by eliminating one variable from a finite
system of affine inequalities suffice to reconstruct that variable over `ℚ`.


### `exists_nonneg_affine_of_pairwise`

 The one-variable reconstruction step of Fourier--Motzkin elimination.
Zero coefficients require a nonnegative constant, and each positive/negative
pair requires a nonnegative elimination combination. These conditions suffice
for a rational solution to every original inequality. 
