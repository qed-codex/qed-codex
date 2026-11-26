---
{
  "module": "proof/variables/VariableBound/Net/SizeU.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeU.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeU.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The total»: display (68)

The total U of the network of an admissible profile is twice the sum, over the pairs {a, b} of nodes
and the two kinds κ, of ⌈log C(t_(a,b,κ), μ_(a,b,κ))⌉. The file follows the text sentence by
sentence: a product of binomial
coefficients is at most the binomial coefficient of the sums (`sum_lg_choose_le`); the numbers T₀
and T₁ of tests (`tests_le`); the cost of kind 0 (`kind_zero_le`) and of kind 1 (`kind_one_le`),
both by display (59); two
roundings per pair (`sum_cw_le`, `two_mul_pairs_le`). The result is display (68) with M in place of
14n and k − 1 in place of k in its first term (`stU`), and as printed if M ≤ 14n (`stUPrinted`). The
constants 6, 28, 96 and 2g² are those of the text.
That U is twice the sum over the pairs, and the count of the tests of an object, come from
`VariableBound.Net.Tests`. Of «Setting and parameters», the bounds s̄ < 32Δ·log(2Δ) and 3m/(n̄ + 1)
< 6Δ·log(2Δ) ≤ (2Δ)³ are read from the hypothesis
`ParamIneq`; display (59), log(2Δ) ≥ 2, n̄ ≥ 1 and n̄·log(2Δ) ≤ n are taken from
`VariableBound.Params.Ineq`. 

 ### Admissible profiles 

### `totP_eq`

 μ_κ as a sum over the pairs a < b < g. 

### `adm_spec`

 What an admissible profile satisfies: Σ_a μ_(a,0) ≤ n̄ + 1, Σ_a μ_(a,1) ≤ M, and for both kinds
μ_κ ≤ (k − 1 + κ)·Σ_a μ_(a,κ) and μ_(a,b,κ) ≤ t_(a,b,κ) for a < b < g. 

 ### The sentences of «The total» 

### `lg_le_lg`

 log x ≤ log z for 0 ≤ x ≤ z and z ≥ 1; x = 0 is allowed because Lean's log 0 is 0. 

### `sum_lg_choose_le`

 Step 3, «The total»: «A product of binomial coefficients is at most the binomial coefficient of
the sums, so Σ_({a,b}) log C(t_(a,b), μ_(a,b)) ≤ log C(T, μ)», where T and μ are the sums of the
t_(a,b) and of the
μ_(a,b) over the pairs a < b < g. Needs μ_(a,b) ≤ t_(a,b) for these pairs. 

### `nb_mul_sum_le`

 I ≤ r·s̄: if n̄·|Λ_j| ≤ c for every check, then n̄·I ≤ r·c. 

### `tests_le`

 Step 3, «The total»: «T₀ ≤ (k − 1)m and T₁ ≤ kr·s̄», the second as T₁ ≤ kI and n̄·I ≤ r·16m,
that is I ≤ r·s̄ with s̄ = 16m/n̄. Here T_κ is the sum of the t_(a,b,κ) over the pairs a < b < g and
I the number of incidences.
Needs k ≥ 1, ψ and the checks well formed, and n̄·|Λ_j| ≤ 16m for every check. 

### `one_le_k`

 A formula with a clause, all of whose clauses have 1 to k literals, has k ≥ 1. 

### `kind_zero_le`

 Step 3, «The total»: by display (59) with μ' = (k − 1)(n̄ + 1), kind 0 costs at most (k − 1)(n̄ + 1)·3·log(2Δ)
≤ 3(k − 1)(n + log(2Δ)) bits. Needs 2 ≤ Δ, m ≤ Δn, the n̄ of the text, T₀ ≤ (k − 1)m and μ₀ ≤ (k − 1)(n̄ + 1),
and the inequalities of «Setting and parameters». For k = 1, where μ' = 0 and display (59) does not
apply, T₀ = μ₀ = 0 and the cost is 0. 

### `kind_one_le`

 Step 3, «The total»: «With μ' = kM and 3T₁/μ' ≤ 3s̄ (as r ≤ M), kind 1 costs at most kM·log(3s̄)
bits», where s̄ = 16m/n̄; this is at most kM·log(96Δ·log(2Δ)), as 3s̄ < 96Δ·log(2Δ). Needs 2 ≤ Δ, n̄
< m ≤ Δn, the n̄ of the text, k ≥ 1, r ≤ M, M ≥ 1,
I ≤ r·s̄ (as n̄·I ≤ r·16m), T₁ ≤ kI and μ₁ ≤ kM, and the inequalities of «Setting and parameters». 

### `sum_cw_le`

 Step 3, «The total», «Adding two roundings per pair»: for each kind one rounding per pair,
Σ_({a,b}) ⌈log C(t_(a,b), μ_(a,b))⌉ ≤ log C(T, μ) + Σ_(b<g) b, and Σ_(b<g) b is the number of pairs;
T and μ are the sums of the t_(a,b) and of the μ_(a,b). Needs μ_(a,b) ≤ t_(a,b) for the pairs a < b
< g. 

### `two_mul_pairs_le`

 There are Σ_(b<g) b = g(g − 1)/2 pairs {a, b}: twice their number is at most g². 

 ### Display (68) 

### `stU`

 Step 3, «The total», display (68) before display (61) is used: in the setting of Step 3 for m >
n̄, with g ≥ 1 nodes, the network of an admissible profile has U ≤ 6(k − 1)(n + log(2Δ)) +
2kM·log(96Δ·log(2Δ)) + 2g². Needs the
inequalities of «Setting and parameters» (the hypothesis `ParamIneq`, proved as
`VariableBound.paramIneq`). 

### `stUPrinted`

 Step 3, «The total», display (68) as printed: in the setting of Step 3 for m > n̄, with g ≥ 1
nodes and M ≤ 14n from display (61), the network of an admissible profile has
U ≤ 6k(n + log(2Δ)) + 28kn·log(96Δ·log(2Δ)) + 2g². Follows from display (68) with M. 
