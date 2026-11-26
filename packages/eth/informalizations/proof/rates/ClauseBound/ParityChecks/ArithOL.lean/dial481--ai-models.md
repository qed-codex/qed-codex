---
{
  "module": "proof/rates/ClauseBound/ParityChecks/ArithOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ArithOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ArithOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of the pad is O_k(e·n·(s+1))

`stArithO : StArithO`. The plan is that of proof/rates/ClauseBound/TopN/Arith.lean and ArithR.lean,
whose lemmas are used. Notation: K = K_l the number of nodes at the level picked for n, so that
K^17 ≤ n < K^(17·C₀); Y the number of binary digits of K; s the precision, β = `betaN k s`, b = β +
3, D = 2^β = Δ; W = b²·D·Y (`Wof`), which is at most A₁·K·e_l (`master`).
* The bound on the shared bits of a network is 354·k·n·(β+1) + 54·K^16: it is LINEAR in β. This
  gives the main term e_l·354·k·n·(β+1) = O_k(e_l·n·(s+1)).
* Every other part X of the exponent, except the term n/2^s (which is at most n·e, since 1/2^s ≤ e),
  satisfies K·X ≤ c·W·n in natural numbers (`lowerO`), so that X ≤ c·A₁·e_l·n.
* Of the five tests of the plan, the fourth (Δ ≤ (⌊log₂ n⌋ + 1)^c) never fails for c = `cO`
  (`D_le_log`). If another one fails, the exponent is n, and n ≤ A·n·e_l: if s < s0K k then e_l ≥
  2^(−s0K k);
  if 2^β > n + 1 or 2·(β+1) > n then n ≤ W ≤ A₁·K·e_l ≤ A₁·n·e_l; if n < n₀ then 1/e_l ≤ (log₂ K)^C₀
  ≤ n₀^C₀. 

 ### Natural numbers 

### `two_le_D`

 2 ≤ 2^β. 

### `GO`

 The constant in g·P ≤ G·W·n. 

### `UbO_le`

 Ub ≤ 354·k·n·(β+1) + 54·K^16. 

### `gPO_le`

 g·P ≤ 1330·(2n)·D·(β+1)·(β + 2 + size n). 

### `gPO_le_W`

 g·P ≤ G·W·n. 

### `argO_le`

 The argument of the logarithm in the bound of the solver: K·(λ + B) ≤ 2^(5·17·C₀·Y + 16). 

### `lowerO`

 The parts of lower order of the exponent, each multiplied by K. 

 ### Real numbers 

### `lowerOR`

 The inequalities of `lowerO` between real numbers. 

### `real_coreM`

 The estimate of the exponent, between real numbers: the parts T1, T2, T3, R1, Rx of lower order
and the exponent nd of the solver; M is the main part of the bound on the shared bits. 

### `real_finalO`

 The main term and the rest, in terms of n·e·(s+1). 

### `ccO`

 The sum of the constants of the parts of lower order. 

### `needO_le_sum`

 The exponent as a sum of its parts. 

### `needO_le`

 The exponent `needO` is at most (354k·c_k + cc·A₁ + 1)·n·e·(s+1). 

 ### The plan 

### `planAtO_getD_le`

 The exponent of a plan, or else n, is at most n; and at most `needO` if the five tests are
passed. 

 ### The tests of the plan 

### `cO`

 The exponent c of the fourth test. 

### `D_le_log`

 The fourth test never fails: Δ = 2^β ≤ (⌊log₂ n⌋ + 1)^c. 

### `le_of_W`

 If n ≤ W, then n ≤ A₁·(n·e), by the master inequality. 

### `le_of_lt_n0`

 If n < n₀, then n ≤ n₀^C₀·(n·e), because 1/e ≤ (log₂ K)^C₀ and K ≤ n. 

### `combineO`

 The cases together. 

### `planAtO_le`

 The statement at one level: K the number of nodes, K^17 ≤ n < K^(17·C₀). 

 ### The statement 

### `stArithO`

 For c = `cO k C C₀` and every n₀: with l the level picked for n and s = s(l), the exponent of
the pad is at most A·n·e_l·(s+1). 
