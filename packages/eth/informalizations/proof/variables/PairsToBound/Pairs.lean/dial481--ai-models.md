---
{
  "module": "proof/variables/PairsToBound/Pairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Pairs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Pairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (b) from Theorem D (a): the pairs of Appendix A

Sentences (1) to (4) of Step 6 of Appendix D, in the numbering of
proof/variables/PairsToBound/Defs.lean.

* `seq_of_rate`: the sequence of levels of the recursion of Appendix A, built as in
  `GeneralPieces.seq_of_pick`, but with the constant chosen first. There the constant C₀ is said to
  exist after the pieces; its proof takes the constant C of part (b) of Theorem A, which depends on
  c alone (`GeneralPieces.StRate2`), and puts C₀ = C + 10. Here that
  order is in the statement: for every c there is a C₀ that serves all programs with parameters (ρ,
  c) and P.m = 1, all ρ with 1/2 ≤ ρ < 1 and all x₀ ≥ 18 with 2^x₀ ≥ c + 5.
* `theRecursionHasLevels`: the same for pieces as Appendix A defines them
  (`AppRunningTime.IsPieces`), with the solver polynomial-time, K at the ℓ-th index equal to K_ℓ,
  and the level picked by the program of `pick_spec`.
* `thePairsSatisfyTheHypothesis`: the case ρ = 1/√2, x₀ = `GeneralPieces.x₀Of c`, with the fraction
  between e_ℓ and 2e_ℓ (`GeneralPieces.Between.between_half`, `GeneralPieces.Asymptotic.between`)
  and the precision ℓ + 1.
* `thetaOfThePairs`: the four inequalities are part (a) of Theorem A and two steps of its proof;
  with (1/√2)^ℓ = 1/√(2^ℓ) they give the two-sided bound. 

 ### The sequence of levels, with a constant that depends on c alone 

### `seq_of_rate`

 Parts (a) and (b) of Theorem A as a sequence of levels, with the constant before the pieces,
from the statements `StChain2`, `StRate2`, `StSolveG2` and `StNeedG` taken as hypotheses. For every
c there is a C₀ such that for all programs P with parameters (ρ, c) and P.m = 1, 1/2 ≤ ρ < 1, every
x₀ ≥ 18 with 2^x₀ ≥ c + 5 and every program `pick` that finds the level, the solver made of P has a
sequence of levels for the numbers e_ℓ of display (40) with the
constant C₀, whose ℓ-th index is the schedule of display (40) and whose level is picked by `pick`.
The proof is that of `GeneralPieces.seq_of_pick`; C₀ = C + 10 for the C of part (b). 

### `theRecursionHasLevels`

 «That its pairs satisfy the hypothesis of Theorem D (a) is checked in the proof of Theorem A
(c)» (Step 6 of Appendix D), for every ρ and x₀ of Theorem A, with a constant that depends on c
alone. 

 ### ρ = 1/√2 

### `half_le_inv_sqrt_two`

 1/2 ≤ 1/√2 < 1. 

### `precision_succ`

 For 1/2 ≤ ρ < 1 and x₀ ≥ 18, ℓ ↦ ℓ + 1 is a precision for the numbers e_ℓ of display (40), by
part (a) of Theorem A. 

### `thePairsSatisfyTheHypothesis`

 «The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy this hypothesis» (Theorem D
(b)), with constants that depend on c alone. 

 ### e_ℓ = Θ((log K_ℓ)^(−1/2)) 

### `inv_between_sqrt`

 For a > 0 and t > 0 with t² = p: if a·p ≤ L ≤ b·p, then √a/√L ≤ 1/t ≤ √b/√L. 

### `thetaOfThePairs`

 «By Theorem A (a) and its proof, ½ρ^ℓ ≤ e_ℓ ≤ 0.85ρ^ℓ and x₀2^ℓ ≤ log K_ℓ ≤ (3x₀+6)2^ℓ, so e_ℓ =
Θ((log K_ℓ)^(−1/2))» (Step 6 of Appendix D). 
