---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Integer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Integer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Integer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer finite obstruction

Integer-coefficient affine inequalities inherit a nonnegative integer
infeasibility certificate from rational Fourier–Motzkin elimination.  Paired
rows encode additive relations and normalization without quotienting a real
vector space or assuming a closed-cone theorem.


### `integer_certificate_of_no_real_solution`

 Farkas certificate with integer weights for a real-infeasible integer system. 

### `integer_cone_certificate_of_no_state`

 The finite integer cone certificate used in Appendix A.1.

Failure of a normalized real functional that kills the additive relations and
is nonnegative on the inequality vectors yields a strictly positive integer
multiple of the negative unit, with nonnegative integer cone coefficients and
unrestricted integer relation coefficients.

