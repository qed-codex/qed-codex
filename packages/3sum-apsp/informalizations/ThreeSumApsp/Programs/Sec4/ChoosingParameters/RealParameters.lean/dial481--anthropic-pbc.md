---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/RealParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/RealParameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/RealParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 31 and 32: the parameters of the program, and where its costs are bounded

For real c > 10, 0 < θ < 0.9 and ε < R_c(γ) there are parameters G for the program text (rational c'
and θ', a threshold m₀) and a constant C such that on every instance with 1 ≤ D ≤ N^ε and with m ≥
m₀ the costs of Theorem 30 at these parameters are at most C times

    Tp = N² (log D + 1)²/D^γ     and     Tq = D^q (log D + 1),

γ and q being those of c and θ (`exists_ratParams`).

The rational parameters come from `exists_rat_params` and the costs at them from
`Corollary31.costs`. What is left is to compare the bounds: γ(c', θ') ≥ γ(c, θ) and q(θ') ≤ q(θ)
make the bounds at the rational parameters smaller (`le_preBound31`, `le_queryBound31`), and both
bounds are at least 1 (`one_le_preBound31`, `one_le_queryBound31`), so that additive constants can
be absorbed.


### `preBound31`

 The bound on the preprocessing, N² (log D + 1)²/D^γ. 

### `queryBound31`

 The bound on a query, D^q (log D + 1); the summand 1 makes it at least 1 at D = 1. 

### `eps_mul_gamma_le`

 ε γ ≤ 1 for ε < R_c(γ). 

### `le_of_le_rpow`

 D ≤ N^ε with ε ≤ 1 gives D ≤ N. 

### `rpow_le_sq`

 D ≤ N^ε with ε γ ≤ 1 gives D^γ ≤ N². 

### `one_le_preBound31`

 The bound on the preprocessing is at least 1 if D^γ ≤ N². 

### `one_le_queryBound31`

 The bound on a query is at least 1. 

### `le_preBound31`

 A larger exponent of D in the denominator, and log D in place of log D + 1, make the bound on
the preprocessing smaller. 

### `le_queryBound31`

 A smaller exponent of D, and log D in place of log D + 1, make the bound on a query smaller. 

### `exists_ratParams`

 **The parameters of the program.** On every instance with 1 ≤ D ≤ N^ε the two bounds are at
least 1, and from the threshold on the hypotheses of Theorem 30 hold and its costs are within a
constant times the two bounds. 
