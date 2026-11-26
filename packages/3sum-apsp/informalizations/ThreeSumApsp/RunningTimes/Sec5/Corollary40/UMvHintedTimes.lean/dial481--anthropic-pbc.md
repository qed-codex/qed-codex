---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40/UMvHintedTimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/UMvHintedTimes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/UMvHintedTimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40, Conjecture 5.12: the running times of uMv-hinted uMv

Proof of Corollary 40: "Cut the n rows of U into n/t₂ blocks of t₂ rows, and preprocess each of the
n/t₂ products of a block with Y [...].  So Phase 3 costs (n/t₂) · O(t₂²/D^0.063) =
O(n^{1+τ₂−0.063τ₁}) time.  In Phase 4, [...] t₂ queries [...] take O(t₂ D^0.437) = O(n^{τ₂+0.437τ₁})
time.  Phase 2 only stores I."

The argument is made for a data structure with given rates at the sizes N = t₂ = ⌊n^{τ₂}⌋ and
D = t₁ = ⌊n^{τ₁}⌋ (`achievesUMvHinted_of_rates`).  Phase 3 takes the time of ⌈n/t₂⌉ preprocessings
and O(t₁ t₂ + n) steps more, Phase 4 the time of t₂ queries and O(t₂) steps more.  With the rates of
Corollary 26 this gives the statement for τ₁ < τ₂/18 (`achievesUMvHinted_of_lt_eighteenth`).

Two things differ from the paper's text.  The input of a phase is written into the memory when the
phase starts, so Phase 2 has nothing to store and returns at once.  The blocks are counted from the
last row upwards, and if t₂ does not divide n, the block that starts at row 0 overlaps the next
one.  The structure of the block with the first row s lies s A t₂² cells after a common base; so
the memory has room for n such distances, and one choice of the limits serves all places
(`uMvLim_of_rates`).

"General τ" (proof of Corollary 40): "For Conjecture 5.12, we use the same blocks, which requires
n^{τ₁} ≤ n^{ετ₂}, that is, τ₁ ≤ ετ₂ for some ε < ε*."  This is `achievesUMvHinted_of_rates` with the
rates of Corollary 31 (`achievesUMvHinted_of_genParams`, `achievesUMvHinted_of_lt_epsStar`).  After
the rounding the condition t₁ ≤ t₂^ε can fail for small t₁; `exists_hint_threshold` gives a constant
such that it holds as soon as t₁ exceeds it.  The data structure needs the condition only above its
threshold, below which it answers queries by inner products; so the threshold is chosen at least as
large as that constant (`kitRates_corollary31`).


### `uMvProcsAt`

 A procedure that does nothing and serves as Phase 1 and as Phase 2, Phases 3 and 4, and their
three routines, as procedures o to o + 5.  A is the numeral in the program text that fixes the
distance of the structures. 

### `uMvTop_le`

 The inputs, the output, Y, the table and n distances of A t₂² cells are polynomially many cells.


### `uMvFr_add_le`

 The structure of the block with the first row s lies within the cells that are used. 

### `uMvLim_of_rates`

 **One choice of the limits serves the structures of all blocks**: the limits for a memory that
ends after the last structure. 

### `uMvProcsAt_lookup`

 The numbers of the six procedures after a program of o procedures. 

### `tPhase3_le_of_rates`

 **The time of Phase 3**: c = ⌈n/t₂⌉ preprocessings, c C tp ≤ C E X, and
19 t₁ t₂ + 29 t₁ + 13 c t₂ + 50 c + 89 steps, where t₁ ≤ t₁ t₂ ≤ X and c ≤ c t₂ ≤ 2 n ≤ 2 X. 

### `tPhase4_le_of_rates`

 **The time of Phase 4**: t₂ queries, t₂ C tq ≤ C E X, and 40 t₂ + 114 steps, where t₂ ≤ X. 

### `BlockRates`

 **Rates for the blocks of uMv-hinted uMv**: what the running times use about the data structure
with the parameters G at the sizes N = t₂ = ⌊n^{τ₂}⌋ and D = t₁ = ⌊n^{τ₁}⌋. 

### `BlockRates.kit`

 The preprocessing takes at most C tp n steps and a query at most C tq n. 

### `BlockRates.pre_le`

 The preprocessing of the ⌈n/t₂⌉ blocks is O(n^a₃). 

### `BlockRates.copy_le`

 Writing Y = N_{I,J} is O(n^a₃). 

### `BlockRates.query_le`

 t₂ queries are O(n^a₄). 

### `achievesUMvHinted_of_rates`

 **uMv-hinted uMv over a data structure with given rates.**  Let 0 ≤ τ₁ ≤ τ₂ ≤ 1, 1 ≤ a₃ and
τ₂ ≤ a₄.  With rates as in `BlockRates`, Phase 2 takes O(n^{τ₁}), Phase 3 takes O(n^a₃) and Phase 4
takes O(n^a₄) time on the word RAM. 

### `achievesUMvHinted_of_lt_eighteenth`

 **Corollary 40, Conjecture 5.12, 0 < τ₁ < τ₂/18, τ₂ < 1**: uMv-hinted uMv is solved on the word
RAM with Phase 2 in O(n^{τ₁}), Phase 3 in O(n^{1+τ₂−0.063τ₁}) and Phase 4 in O(n^{τ₂+0.437τ₁}) time.


### `achievesUMvHinted_of_genParams`

 **Corollary 40, Conjecture 5.12, general τ**: for parameters c, θ, ε, γ as in `GenParams`,
0 < τ₁ < ε τ₂ and 0 < τ₂ < 1, uMv-hinted uMv is solved on the word RAM with Phase 2 in O(n^{τ₁}),
Phase 3 in O(n^{1+τ₂−γτ₁}) and Phase 4 in O(n^{τ₂+τ₁/2}) time. 

### `achievesUMvHinted_of_lt_epsStar`

 **The uMv part of Corollary 40, "General τ"**: for 0 < τ₁ < ε* τ₂ and τ₂ < 1 there is a saving
γ > 0. 
