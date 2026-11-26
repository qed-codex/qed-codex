---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Rational.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Rational.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Rational.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite rational alternatives

Fourier–Motzkin elimination proves the rational Farkas alternative directly.
The proof keeps the nonnegative combination of original rows at every
elimination step.  Consequently the obstruction has rational coefficients;
neither a real separation theorem nor a rational-density premise is assumed.


### `RationalCertificate`

 A negative constant obtained as a nonnegative rational combination of rows. 

### `rational_alternative`

 A finite rational affine system has a solution or a rational obstruction.
    The alternatives are constructed by elimination of one coordinate at a time. 

### `rational_certificate_of_infeasible`

 Infeasibility produces an actual certificate, rather than an assumed
    separation functional or a real coefficient vector. 
