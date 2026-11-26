---
{
  "module": "Paper/Cuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Cuts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Cuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Cutting computations"

Programs, instances, plain instances and sums are those of NS1.Machine and NS1.Accel: an instance is a tree whose
first part is a program and whose second part is its argument. The generators of the ring are a table θ.


### `Generates`

 The table θ lists finitely many generators of A: every element is a fixed sum of products of them. 

### `def_cut`

 **Paper: Definition def:cut.** "A program G cuts (τ,s) into (τ′,s′) with P pieces in t steps if for every instance
z with |z| ≤ s: all runs of G on z halt, and the accepting ones take at most t steps, have empty bills and output lists
of at most P instances of size at most s′; and if z is τ-plain, then all these instances are τ′-plain and
sum(z) = ∑ weight · ∏ sum(y)." 

### `thm_onecut_evaluator`

 **Paper: Theorem thm:onecut, the evaluator.** "The sum of the evaluator on a script is the value of the piece", all
its runs halt, within (#blocks · T + #bits of units + #instructions · v^O(1))(lg v)^O(1) steps: GROUP and κ are the
evaluator and its step cost, GroupOK says halting, value and cost, GrpTimeOK bounds the cost by the bits of the piece. 

### `thm_onecut`

 **Paper: Theorem thm:onecut.** "There are constants a₀, C, v₀ such that for all v ≥ v₀, all τ ≥ v^a₀ with
4 lg τ ≤ (lg v)², all s ≤ τ and 2 ≤ k ≤ v^64, with Λ = (lg v)^C, a program of size at most v^a₀ cuts (τ,s) into
(τΛ/k, (s/k + τ/v^256)Λ) with at most kΛ pieces, in (s + τk/v^256)Λ steps." The laws and the generators θ are the
standing hypothesis "Fix the ring A and the laws". The proof takes the automaton from Proposition prop:universal and
the formula and the bounds of the pieces from Proposition prop:pieces, and puts the evaluator and the program G on
them. 

### `thm_cut`

 **Paper: Theorem thm:cut.** "There are a multiple H ≥ 272 of 16 and constants C₀, v₀ such that the following holds
whenever v ≥ v₀ and (lg v)^(C₀α) ≤ v. For v^H ≤ τ ≤ v^(Hα) and sv^48 ≤ τ some program of size at most v^H cuts (τ,s)
into (v^H, v^(H−32)) with at most τv²/v^H pieces in at most τ/v^24 steps." The proof composes the cuts of Theorem
thm:onecut. 

### `cutHyp_of_laws`

 What the next section starts from, in the form NS1.CutHyp: the conclusion of Theorem thm:cut multiplied out. 

### `exists_setting`

 "We keep A, H and C₀ of the theorem on cuts at all scales": what the next section starts from. 
