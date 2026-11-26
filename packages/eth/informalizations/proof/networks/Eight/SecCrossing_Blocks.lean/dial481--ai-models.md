---
{
  "module": "proof/networks/Eight/SecCrossing_Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The functions R and C of four blocks

This file proves, for the functions R and C of four blocks of Section 4 of the paper, the closed
forms R = [x ⊕ y = v ⊕ u]σ(x,y)σ(v,u) and C = [x ⊕ u = v ⊕ y]σ(x,u)σ(v,y), the identity R + C = 2[x =
v][y = u] along the paragraph that begins with «Indeed»,
that R has values in {−1, 0, 1}, and the bounds |R|, |C|, |ψ_k| ≤ 1. The sign rule σ(p,q)σ(p',q') +
σ(p,q')σ(p',q) = 0 (`Eight.Signs`) is a hypothesis `hS` wherever the paper uses it; it is proved in
`SecCrossing_Identity.lean`. 

 ## Signs and ⊕ 

### `sigma_eq_or`

 σ(p,q) is 1 or −1. 

### `sigma_mul_self`

 σ(p,q)² = 1. 

### `sigma_mul_eq_or`

 A product of two signs is 1 or −1. 

### `bxor_eq_iff_zero`

 «Both brackets say x ⊕ y ⊕ u ⊕ v = 000»: x ⊕ y = v ⊕ u says this. 

### `bxor_eq_iff_zero'`

 «Both brackets say x ⊕ y ⊕ u ⊕ v = 000»: x ⊕ u = v ⊕ y says this too. 

### `bxor_eq_swap`

 The two brackets say the same. 

### `bxor_right_cancel`

 «If it holds and y = u, then x = v»: x ⊕ y = v ⊕ y only if x = v. 

 ## R and C in closed form 

### `sum_psi_mul`

 Σ_k ψ_k(p,q)·ψ_k(p',q') = [p ⊕ q = p' ⊕ q']·σ(p,q)·σ(p',q'): only k = p ⊕ q contributes. 

### `Rb_eq`

 «Indeed, R = [x ⊕ y = v ⊕ u]σ(x,y)σ(v,u)». 

### `Cb_eq`

 «and C = [x ⊕ u = v ⊕ y]σ(x,u)σ(v,y)». 

### `Cb_eq_Rb`

 C is R with y and u exchanged; this holds by the definitions. The paper uses it in the words
«column-wise the roles of R and C are exchanged». 

 ## The three cases of the paragraph «Indeed» 

### `Rb_of_ne`

 «If this fails, all three functions are 0»: R. 

### `Cb_of_ne`

 «If this fails, all three functions are 0»: C. 

### `not_cross_of_ne`

 «If this fails, all three functions are 0»: [x = v][y = u]. 

### `Rb_diag`

 «If it holds and y = u, then x = v and R = C = σ(x,y)² = 1»: here with x = v and y = u put in. 

### `Cb_diag`

 «R = C = σ(x,y)² = 1»: C. 

### `Rb_of_eq`

 If x ⊕ y = v ⊕ u, then R is 1 or −1. 

### `Rb_add_Cb_of_ne`

 «If it holds and y ≠ u, then R + C = 0 by the sign rule with (p,q,p',q') = (x,y,v,u)». 

### `Rb_add_Cb`

 **R + C = 2[x = v][y = u]**, by the three cases of the paragraph «Indeed» of the paper. 

 ## The values of R and C 

### `Rb_val`

 «Both have values in {−1, 0, 1}»: R. This does not need the sign rule. 

### `abs_Rb_le`

 |R| ≤ 1. 

### `abs_Cb_le`

 |C| ≤ 1. 

 ## The bound on ψ 

### `abs_psi_le`

 |ψ_k(p,q)| ≤ 1. 
