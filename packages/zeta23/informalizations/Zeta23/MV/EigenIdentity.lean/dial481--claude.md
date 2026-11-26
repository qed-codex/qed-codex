---
{
  "module": "Zeta23/MV/EigenIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/EigenIdentity.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/EigenIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The Preissmann–Lévêque eigen-identity (arXiv:2203.14950 Lemma 2.1)

For real `c_r > 0`, injective real `freq`, complex `u` and real `μ` with the eigen-relation
`Σ_{n≠m} c_m c_n u_n/(freq m − freq n) = iμ u_m` for every `m`, we prove, for every `m`,

  `μ² |u_m|² = Σ_{n≠m} c_m² c_n² |u_n|²/(freq m − freq n)²
               + 2 Σ_{n≠m} c_m³ c_n Re(u_m ū_n)/(freq m − freq n)²`.

Proof (pure finite algebra): expand `|iμ u_m|²` as a double sum over `(n,p)`; the diagonal
`p = n` is the first term; off the diagonal use the partial fraction
`1/((λm−λn)(λm−λp)) = 1/((λm−λn)(λn−λp)) − 1/((λm−λp)(λn−λp))` to write the summand as
`G(n,p) + G(p,n)`, so the off-diagonal part is `2 Σ_n Σ_{p≠n,m} G(n,p)`; the inner sum is
`Re(u_n · W_n)` with `W_n = Σ_{p≠n,m} c_p ū_p/(λn−λp)`, and the conjugate eigen-relation at `n`
gives `W_n = −iμ ū_n/c_n − c_m ū_m/(λn−λm)`; the `−iμ|u_n|²/c_n` piece is purely imaginary and
dies under `Re` — the Montgomery–Vaughan cancellation — leaving the second term.


### `norm_sq_eq_re_mul_conj`

 `‖z‖² = Re(z z̄)`. 

### `re_mul_conj_comm`

 `Re(u_n ū_p)` is symmetric in `(n,p)`. 

### `eigen_identity'`

 **Preissmann–Lévêque eigen-identity** (arXiv:2203.14950 Lemma 2.1). 
