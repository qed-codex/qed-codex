---
{
  "module": "proof/threesat/ThreeSatPrinted/ThmEveryDelta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatPrinted/ThmEveryDelta.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatPrinted/ThmEveryDelta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem 2 in its decision form through the printed proofs of Lemma 1, Lemma 2 and Proposition 3, and on the tree of the sparsification procedure of Appendix C

proof/networks/Eight/ViaGrouping proves Lemma 1 along its printed proof and, on top of it,
Proposition 3 and Algorithm 1 (Section 8).
It takes the sparsification through one property, `Eight.SufficesSparse δ M S`: the deciding form of
«By Lemma 4 with ε = δ/3, … it suffices …»: to decide whether a 3-CNF Φ with m ≤ Mn clauses is
satisfiable,
in time O(2^{δ'm}) plus a polynomial in n (in the property, steps are counted and nothing is added
for the polynomial; and the machine for the sparse formulas must answer for every m, not only m ≤
Mn).
Here it comes from `ThreeSatOnTree.sufficesSparse_viaC`
(proof/threesat/ThreeSatOnTree/ThmEveryDelta.lean), with M = 2·(θ 0 + θ 1 + θ 2)
and S = `ThreeSatOnTree.satC τ`, the walk of the tree of the procedure of Appendix C (thresholds θ 0 =
1, θ i = 4·τ^(2i−1), not Calabro's; its leaves are those that the Lean statement of Lemma 4 lists).
* `SATCp_polyTimeSteps`, `algPseudocode_viaC` and `algPseudocode_decides_viaC` name the machine
  `SATCp ℓ τ` (proof/threesat/ThreeSatPrinted/Defs.lean) and show that Algorithm 1 on the tree of
  Appendix C decides 3-SAT within c·2^{δn} steps.
About the tree and the networks this file proves nothing of its own: besides `satC_polyTimeSteps`
(every τ, from the general `isPolyT_satMK`), it puts together theorems of
proof/networks/Eight/ViaGrouping and proof/threesat/ThreeSatOnTree/.
Different from the paper: the walk tests at each leaf its formula ψ, not the output ψ ∪ 𝒩 of the
procedure of Appendix C (𝒩 is the set of one-literal clauses that the procedure carries along and
never reads); the list of Lemma 4 is never written, and the time clause of Lemma 4 is not used. 

### `satC_polyTimeSteps`

 The steps of `satC τ Mc` are polynomial time if those of `Mc` are, for every τ. 

### `SATCp_polyTimeSteps`

 The steps of `SATCp ℓ τ` are polynomial time. 

### `algPseudocode_viaC`

 **Algorithm 1 decides 3-SAT within c·2^{δn} steps**, with the level chosen as in the header of
Algorithm 1: for every δ > 0 there are a parameter τ ≥ 24 and δ' = min(δ/(3M), 1), M = 2·(θ 0 + θ 1 +
θ 2), such that `SATCp ℓ τ` with «ℓ the first level with K_ℓ ≥ 72/δ' and
e_ℓ ≤ δ'/12» decides 3-SAT on n variables within c·2^{δn} steps. Different from the paper: δ' =
min(δ/(3M), 1) (the paper assumes δ ≤ 1 and has δ' = δ/(3M)); M is the bound per variable on the
clauses of a leaf of the tree walked by `satC τ`, not the M(δ/3) of Lemma 4. 

### `algPseudocode_decides_viaC`

 **Theorem 2 in its decision form for step machines, with the machine named.** For every δ > 0
there are a level ℓ and a parameter τ ≥ 24 such that `SATCp ℓ τ` has polynomial-time steps and
decides 3-SAT on n variables within c·2^{δn} steps. (`algPseudocode_viaC` says which ℓ and τ.) 
