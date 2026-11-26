---
{
  "module": "ThreeSumApsp/Sec5/Corollary40/GeneralParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/GeneralParameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/GeneralParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40, "General τ": the choice of the parameters

Proof of Corollary 40: "Let 0 < τ < ε*, and fix ε with τ < ε < ε*.  By Corollary 31, with c and θ
chosen as in the proof of Theorem 24 for q := 1/2, there is, after absorbing the logarithmic
factors, a γ > 0 such that [...]".  Here this choice of c > 10 and of θ in (0, 0.9) is made for a
given τ (`exists_genParams`), together with a number γ ≤ 1 below the γ of Corollary 31, which leaves
room for the logarithmic factors.  What the three hinted problems use about the four numbers is the
structure `GenParams`.


### `GenParams`

 Numbers c, θ, ε to which Corollary 31 applies with D ≤ N^ε and whose q, the exponent of the
query time D^q in Corollary 31, is below 1/2; and a number 0 < γ ≤ 1 below the γ of Corollary 31 for
c and θ. 

### `GenParams.ε_lt_epsStar`

 ε is below ε*. 

### `exists_genParams`

 For τ < ε* there are numbers c, θ, ε, γ as in `GenParams` with τ < ε. 

### `exists_genParams_mul`

 For τ₁ < ε* τ₂ there are numbers c, θ, ε, γ as in `GenParams` with τ₁ < ε τ₂ (proof of
Corollary 40: "τ₁ ≤ ετ₂ for some ε < ε*"). 
