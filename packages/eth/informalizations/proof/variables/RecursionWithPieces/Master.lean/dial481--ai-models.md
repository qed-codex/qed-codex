---
{
  "module": "proof/variables/RecursionWithPieces/Master.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Master.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Master.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 6 for the recursion of Appendix A: from its sequence of levels to the two rates, for a conclusion that may name the solver and the choice of the level

`VariableBound.StEndS R` says: for every solver for cliques with a sequence of levels, a precision
and two rates that satisfy a list of inequalities, the conclusion R holds of the solver, the
function `pick` of the sequence,
the precision and the rates. This file meets the list for the recursion of Appendix A, as follows.
* The sequence of levels is that of proof/rates/GeneralPieces/Rec/Seq.lean
  (`GeneralPieces.seq_of_pick`): every x₀ ≥ 18 with 2^x₀ ≥ c + 5, each step of the schedule of
  display (40) in order by the hypotheses of case (ii) of the lemma on groupings with explicit cost
  (`GeneralPieces.Chain.stChain2`, `GeneralPieces.solveG2`), the exponent of the pad by
  `GeneralPieces.stRate2`.
* `pick` is the named program `ClauseBound.Gen.Pick.pick P x₀`, and the conclusion says so.
* The inequalities between e_ℓ and the rates (e_ℓ·(ℓ + 2) against log log n/(log n)^α' for the
  largest ℓ with K_ℓ ≤ n^(1/17), e_ℓ against 1/(log m)^α' for the largest ℓ with K_ℓ ≤ m^(1/9),
  2^(−ℓ−1) ≤ e_ℓ, 2^(ℓ+1) ≤ (2/e_ℓ)^C) are drawn from part (a) of the
  theorem on the general recursion as proved in proof/rates/GeneralPieces/Num/PartA.lean, for every
  x₀ ≥ 18: `GeneralPieces.PartAUse.e_mul_le`, `e_le_rPow`, `inv_two_pow_le_e`, `two_pow_le_div`, as
  proof/rates/GeneralPieces/ThmRunningTime.lean uses them for part (c).
Of the two rates alone it is shown that they are not too small, not negative, and that the rate in n
allows the fall-back to exhaustive counting. 

### `master_of_par`

 Programs P with parameters (ρ, c), 1/2 ≤ ρ < 1, whose numbers of bits are at most 2λ (`P.m = 1`)
and which are polynomial-time (`P.Keeps`), and an x₀ ≥ 18 with 2^x₀ ≥ c + 5, give the conclusion R
for the solver made of P, the choice of the
level by the program `Pick.pick P x₀`, the precision s(ℓ) = ℓ + 1, and the rates in n and in m with
the exponent log₂(1/ρ) of the logarithms. The statement `StEndS R` is a hypothesis. 

### `master_of_isPieces`

 Pieces (P₀, A, val) with parameters (ρ, c) as Appendix A defines them give the conclusion R for
the recursion on `recOf P₀ val c`, the choice of the level by `Pick.pick` with the least x₀ of the
theorem on the general recursion, the
precision s(ℓ) = ℓ + 1, and the rates with the exponent α' = log₂(1/ρ). The statement `StEndS R` is
a hypothesis. 

### `master_of_isPiecesB`

 The pieces of Appendix B, with the constant c, give the conclusion R for `solverAB`, `pickAB`,
`prec` and the rates log₂ log₂(n+4)/√(log₂(n+4)) and 1/√(log₂(m+2)). The statement `StEndS R` is a
hypothesis. 
