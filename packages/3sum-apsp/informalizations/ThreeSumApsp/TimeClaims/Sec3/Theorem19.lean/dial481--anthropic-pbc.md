---
{
  "module": "ThreeSumApsp/TimeClaims/Sec3/Theorem19.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Theorem19.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Theorem19.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 19 from Theorem 17 and Corollaries 15 and 16

Theorem 17 reduces Exact Triangle to `4 n g` calls of Lop-AE-SparseTri plus some extra time.  The
proof of Theorem 19 puts in the cost of one call (Corollary 15 or Corollary 16) and the parameters
`D` and `g`, and adds up.  Both routes have the same three steps:

1. the parameters satisfy the hypotheses of Theorem 17 and of the corollary (`Theorem19.choice_*`);
2. one call, with the reading of its answers, costs `O(I)` (`call_cost_corollary_15` and
   `call_cost_corollary_16`);
3. the sum of all terms is `O(κ P)` (`Theorem19.total_*`, the calculation of the proof of
   Theorem 19).

`time_le_of_calls` puts the three steps together.  The result keeps the dependence on `κ`
(`Claim.Theorem_19_explicit`).  From it follow the two bounds as printed, for every constant `κ`
(`Claim.Theorem_19_explicit.eventually_le`), and a bound for all sizes and all bounds on the
weights, which is what Theorem 21 is applied to (`exactTriangleUniform_of_explicit`): small sizes by
brute force (`dominated_bruteForce`), large sizes by the explicit bound with
`κ = max 1 (log u / log s)` (`dominated_explicit`).


### `time_le_of_calls`

 **How both routes of Theorem 19 end.**  Theorem 17 bounds the time by
`calls · call + C · extra`.  If one call costs at most `c I`, and if the calculation of the proof of
Theorem 19 bounds `calls · c I + C · extra` by `B`, then the time is at most `B`. 

### `call_cost_corollary_16`

 One call on the route through Corollary 16, with the reading of its answers, costs
`O(n²/D^{0.063})`: an instance has `|W| ≤ n²/√D` query pairs, so `|W| D^{0.437} ≤ n²/D^{0.063}`. 

### `call_cost_corollary_15`

 One call on the route through Corollary 15, with the reading of its answers, costs
`O(n² log² D / D^{1/18})`. 

### `Theorem19.explicit_of_theorem_17_corollary_15`

 The deduction "By Theorem 5" in the proof of Theorem 19: from Theorem 17 (with
Strassen's algorithm) and the first case of Corollary 15, with `D` the largest power of four at most
`n^{1/18}` and `g = ⌈D^{1/36}⌉`. 

### `Theorem19.explicit_of_theorem_17_corollary_16`

 The deduction "By Corollary 26" in the proof of Theorem 19: from Theorem 17 (with
Strassen's algorithm) and Corollary 16, with `D = ⌊n^{1/18}⌋` and `g = ⌈D^{0.0315}⌉`. 

 ## The bounds as printed 

### `Claim.Theorem_19_explicit.eventually_le`

 The explicit form along `u = n^κ`: for every `κ` and all large `n` the time is at most
`K max(κ, 1) n^{3-δ} (log n)^e`. 

### `Theorem19.first_of_explicit`

 The first bound of Theorem 19 in the printed form, for every constant `κ ≥ 1`, from
the explicit form. 

### `Theorem19.second_of_explicit`

 The second bound of Theorem 19 in the printed form, with
"O(n^{3-ε'} log n) ≤ O(n^{3-ε_T})", from the explicit form. 

### `exactTriangleIn_of_explicit`

 The first deterministic line of Theorem 2, "Exact Triangle on n-vertex graphs in
O(n^{2.9983}) time", for the tripartite form of the problem, from the explicit form of Theorem 19
(`3 - ε_T = 2.9983`). 

 ## A bound for all sizes and all bounds on the weights 

### `SizeBound`

 The number `s` of vertices per part and the bound `u` on the weights. 

### `SizeBound.s`

 The number of vertices per part. 

### `SizeBound.u`

 The bound on the absolute values of the weights. 

### `uniformShape`

 The time `uniformTime` without its constant: `s^{3-δ} (log s + 1)^e (1 + log u)²`. 

### `one_le_uniformShape`

 Each of the three factors of `uniformShape` is at least 1. 

### `dominated_bruteForce`

 "Smaller instances are solved by brute force": below a fixed size `n₀`, the time
`s³ (1 + log u)` is `O(s^{3-δ} (log s + 1)^e (1 + log u)²)`, because `s^δ ≤ n₀^δ`. 

### `le_rpow_max_log_div`

 Weights up to `u` are weights up to `s^κ` for `κ = max 1 (log u / log s)`. 

### `max_log_div_le`

 The exponent `max 1 (log u / log s)` is at most `1 + log u`. 

### `dominated_explicit`

 From the size `16^18` on: the explicit bound of Theorem 19 with `κ = max 1 (log u / log s)`. 

### `exactTriangleUniform_of_explicit`

 From the explicit form of Theorem 19, brute force for small instances
("smaller instances are solved by brute force") and two closure properties: Exact Triangle in time
`K s^{3-δ} (log s + 1)^e (1 + log u)²` for all `s` and `u`.

NOTE.  This step is not in the paper; see `Claim.ExactTriangleUniform` for why our rendering of
"Plug Theorem 19 into Theorem 21" needs it. 
