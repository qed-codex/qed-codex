---
{
  "module": "proof/variables/VariableBound/Params/Ineq.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Ineq.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Ineq.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Setting and parameters of Appendix D: the inequalities of the paragraph

With L = log(2Δ), the definition of n̄ says n̄·L ≤ n < 2·n̄·L (`nb_mul_le`, `lt_nb_mul`). From this
and the bound log C(t, μ) ≤ μ'·max{1, log(3t/μ')} of the paragraph, which is `binom`, proved in
proof/rates/ClauseBound/ParityChecks/Binom.lean, follow the bounds on s̄, on 3m/(n̄+1) and on β.
In the docstrings n̄ stands for any number with `IsNb n Δ n̄`; where a statement needs the r̄ or t̄
defined in the paper (`IsRb`, `IsTb`) rather than an arbitrary number, its docstring says so.
The bound r̄ ≤ 2.41·β + 1 comes from (4/3)^241 > 2^100 and the minimality of r̄. The bounds r̄ ≤ 10n
and M ≤ 14n are proved for n ≥ 29·L + 19. The bound on t̄ uses log(1+p) ≤ (3/2)·p and the minimality
of t̄. 

### `two_le_lg`

 log(2Δ) ≥ 2 for Δ ≥ 2. 

### `lg_le`

 log(2Δ) ≤ 2Δ for Δ ≥ 1. 

### `nb_mul_le`

 n̄·log(2Δ) ≤ n, for Δ ≥ 1. 

### `lt_nb_mul`

 n < 2·n̄·log(2Δ). 

### `binom`

 The bound on binomial coefficients of «Setting and parameters»: log C(t, μ) ≤ μ'·max{1,
log(3t/μ')} for integers t ≥ 0, 0 ≤ μ ≤ μ' and μ' ≥ 1. 

### `nb_pos`

 n̄ ≥ 1. 

### `m_div_lt`

 m/n̄ < 2Δ·log(2Δ), for 2 ≤ Δ and m ≤ Δ·n. 

### `three_m_lt`

 3m/(n̄+1) < 6Δ·log(2Δ), for 2 ≤ Δ and m ≤ Δ·n. 

### `six_le`

 6Δ·log(2Δ) ≤ (2Δ)³, for Δ ≥ 2. 

### `beta_le₁`

 β ≤ n + 3(n̄+1)·log(2Δ) + 2, for 2 ≤ Δ and n̄ < m ≤ Δ·n. 

### `beta_le₂`

 n + 3(n̄+1)·log(2Δ) + 2 ≤ 4n + 3·log(2Δ) + 2, for Δ ≥ 1. 

### `rb_le`

 r̄ ≤ 2.41·β + 1 for the r̄ of the text (`IsRb β r̄`), because 2.41·log(4/3) > 1. 

### `large`

 The bounds for large n: r̄ ≤ 10n and M ≤ 14n for the β, r̄ and M of the text, for 2 ≤ Δ, n̄ < m
≤ Δ·n and n ≥ 29·log(2Δ) + 19. 

### `p_rb`

 p·r̄ < 22·log(2Δ), for 2 ≤ Δ and any number r̄ ≤ 10n. 

### `lg_one_add_le`

 log(1+p) ≤ (3/2)·p for p ≥ 0. 

### `tb_le`

 t̄ ≤ log m + 33·log(2Δ) + 1 for the t̄ of the text (`IsTb m n̄ r̄ t̄`), for 2 ≤ Δ, m ≥ 1 and any
number r̄ ≤ 10n. 

### `paramIneq`

 «Setting and parameters»: the inequalities of the paragraph, each under the hypotheses listed at
its field of `ParamIneq`; the bounds r̄ ≤ 10n and M ≤ 14n under n ≥ 29·log(2Δ) + 19. 
