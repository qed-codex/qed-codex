---
{
  "module": "Nc/Rate/Truncate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Rate/Truncate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Rate/Truncate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Truncation of the constants of an approximate circuit

An approximate circuit has constants in the field of Laurent series in ε. If every constant is cut off at a high power
of ε, the output changes only by terms with positive powers of ε. So the constants may be taken to be Laurent
polynomials. This is the first half of the proof of the lemma of the paper that reduces to the algebraic closure of the
prime field; the second half is in Nc/Rate/Transfer.lean.


### `isStep_update`

 A circuit with t gates is extended by one gate g, which is a variable, a constant, or the sum or product of two of
the t gates. 

### `exists_lift_steps`

 A circuit over R all of whose constants are images of elements of A under a homomorphism φ is the image under φ,
gate by gate, of a circuit over A. 

### `laurentToSeries`

 A Laurent polynomial in ε, read as a Laurent series in ε. 

### `coeff_laurentToSeries`

 The series of a Laurent polynomial has the same coefficients. 

### `exists_laurentPolynomial_coeff`

 Every Laurent series agrees below any given power ε ^ n with a Laurent polynomial. 

### `OrdGe`

 All coefficients of the polynomial u are Laurent series without terms below ε ^ n. 

### `coeff_mul_eq_zero`

 The product of a series without terms below ε ^ m and one without terms below ε ^ n has none below ε ^ (m + n). 

### `exists_ordGe`

 The poles of the coefficients of finitely many polynomials over the Laurent series have bounded order. 

### `exists_truncated_steps`

 If every constant of a circuit over the Laurent series is cut off
at a sufficiently high power of ε, every gate changes only by terms from ε ^ n on: for every circuit over the Laurent
series and every n there is a circuit of the same shape over the Laurent polynomials whose gates differ from the given
ones by polynomials all of whose coefficients have no terms below ε ^ n. 

### `Approximates.exists_laurentPolynomial`

 A polynomial f that is approximated by a circuit with s gates is approximated
by one whose constants are Laurent polynomials in ε: this circuit computes a polynomial p over the Laurent polynomials
in which no negative power of ε occurs and in which the terms without ε are those of f. 

### `Approximates.of_laurentPolynomial`

 Conversely, a circuit over the Laurent polynomials in ε is a circuit over the Laurent series. 
