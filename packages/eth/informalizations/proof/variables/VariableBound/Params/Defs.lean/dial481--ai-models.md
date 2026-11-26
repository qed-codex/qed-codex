---
{
  "module": "proof/variables/VariableBound/Params/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Setting and parameters of Appendix D: definitions and interface statements

`AppVariablesStatement.lean` characterises the parameters n̄, r̄, t̄ as the text does (`IsNb`,
`IsRb`, `IsTb`). Here they are computed, so that the program can use them, and the inequalities of
the paragraph «Setting and
parameters» are stated, with the real number log(2Δ) as in the text. The text assumes n ≥ n₀ for a
number n₀ that depends only on C₀; for display (61) Lean has the explicit condition n ≥ 29·log(2Δ) + 19.
This file has definitions only. The statements are propositions;
proof/variables/VariableBound/Params proves them. 

### `lg`

 log₂. 

### `nbD`

 n̄: the largest power of two 2^a ≤ n with (2Δ)^(2^a) ≤ 2^n; 1 if there is none. 

### `rbD`

 r̄: the least j with 3^j·2^β < 4^j, searched below 3β + 2. 

### `tbD`

 t̄: the least c with m·(15n̄+16)^r̄ ≤ 2^c·(15n̄)^r̄, searched below (number of binary digits of
m) + r̄ + 1. 

### `StParamSpec`

 The computed parameters are those of the text: n̄ for Δ ≥ 1 and 2Δ ≤ 2^n, and n̄ ≥ 2 for Δ ≥ 1
and (2Δ)² ≤ 2^n; r̄ for every β; t̄ for n̄ ≥ 2. 

### `ParamIneq`

 The inequalities of the paragraph «Setting and parameters». Each field names its hypotheses; n̄
is any number with `IsNb n Δ n̄` (n̄ ≥ 2 is not assumed). 

### `ParamIneq.sb_lt`

 for 2 ≤ Δ and m ≤ Δ·n: m/n̄ < 2Δ·log(2Δ), so s̄ = 16m/n̄ < 32Δ·log(2Δ) 

### `ParamIneq.three_m`

 for 2 ≤ Δ and m ≤ Δ·n: 3m/(n̄+1) < 6Δ·log(2Δ) ≤ (2Δ)³ 

### `ParamIneq.beta_le`

 for 2 ≤ Δ and n̄ < m ≤ Δ·n: β ≤ n + 3(n̄+1)·log(2Δ) + 2 ≤ 4n + 3·log(2Δ) + 2 

### `ParamIneq.rb_le`

 for any β and the r̄ of the text (`IsRb β r̄`): r̄ ≤ 2.41·β + 1 

### `ParamIneq.large`

 display (61), for 2 ≤ Δ, n̄ < m ≤ Δ·n, the r̄ of the text and n ≥ 29·log(2Δ) + 19 (in place of
  the text's n ≥ n₀): r̄ ≤ 10n and M ≤ 14n 

### `ParamIneq.p_rb`

 for 2 ≤ Δ and any number r̄ ≤ 10n (as display (61) gives): p·r̄ < 22·log(2Δ) 

### `ParamIneq.tb_le`

 for 2 ≤ Δ, m ≥ 1, any number r̄ ≤ 10n (as display (61) gives) and the t̄ of the text for this
  r̄ (`IsTb m n̄ r̄ t̄`): t̄ ≤ log m + 33·log(2Δ) + 1 

### `StCertParam`

 n̄, β, r̄, t̄ can be written in unary in polynomial time, when n, Δ, m, β, n̄, r̄ are given in
unary (β and r̄ are separate inputs). 
