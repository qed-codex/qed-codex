---
{
  "module": "Zeta23/LinAlg/RankTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/RankTrace.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/LinAlg/RankTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The linear algebra of §3 of the paper (Hermitian positive/negative parts, inertia, the positive index,
von Neumann's trace inequality, the rank–trace inequality, Weyl's perturbation bound). These seven files
were produced first, as a self-contained development (namespace `RHLinalg`) accompanying §3 of the paper —
like all Lean code in this repository, written by Claude, under the direction of the paper's authors — and are
incorporated here unchanged; they have no upstream outside this project (see README § Provenance and attribution).
-/
```


# The rank–trace inequality (paper §3, `lem:ranktrace`)

Let `P, Q` be Hermitian `d × d` matrices with `P ⪰ 0`, `rank P ≤ r`, and
`n₊(Q) ≤ b`. Then for every `c > 0`,

  `‖P+Q‖_F² ≥ c · tr P − (c²/4) · r + 2c · tr Q − c² · b`.

## Proof structure (the paper's proof of [lem:ranktrace], §3)

Decompose `Q = Q₊ − Q₋` (spectral positive/negative parts). Expand
`‖P+Q‖_F² = ‖P‖_F² + 2 tr(PQ₊) − 2 tr(PQ₋) + ‖Q₊‖_F² + ‖Q₋‖_F²` (using
`Q₊Q₋ = 0`). Drop `tr(PQ₊) ≥ 0`. By von Neumann,
`‖P‖_F² − 2 tr(PQ₋) + ‖Q₋‖_F² ≥ ∑(pᵢ−nᵢ)²`. The two elementary estimates
`sum_sq_diff_lower` and `sum_sq_lower_of_card_pos_le` bound the remaining
pieces, and `linarith` assembles.


 ### Elementary real-sequence estimates 

### `sq_ge_linear`

 Elementary scalar inequality `x² ≥ c·x − c²/4`, i.e. `(x − c/2)² ≥ 0`. 

### `sq_ge_linear'`

 Elementary scalar inequality `x² ≥ 2c·x − c²`, i.e. `(x − c)² ≥ 0`. 

### `sum_sq_diff_lower`

 **Sum estimate A** (first elementary estimate in the proof of [lem:ranktrace]). For `p, m ≥ 0` with at most `r`
indices where `p` is nonzero, and `c ≥ 0`:
`∑(pᵢ − mᵢ)² ≥ c·∑pᵢ − (c²/4)·r − 2c·∑mᵢ`. 

### `sum_sq_lower_of_card_pos_le`

 **Sum estimate B** (second elementary estimate in the proof of [lem:ranktrace]). For `q ≥ 0` with at most `b`
indices where `q` is nonzero: `∑qᵢ² ≥ 2c·∑qᵢ − c²·b`. 

 ### Trace and Frobenius-norm identities 

### `trace_mul_nonneg_of_posSemidef`

 `tr(AB) ≥ 0` when `A, B ⪰ 0`. Proof: diagonalise `A = U D Uᴴ`; then
`tr(AB) = tr((UᴴBU)D) = ∑ᵢ λᵢ · (UᴴBU)ᵢᵢ`, where each `λᵢ ≥ 0` (PSD
eigenvalues) and each `(UᴴBU)ᵢᵢ ≥ 0` (diagonal of a PSD matrix). 

### `re_trace_mul_comm`

 For Hermitian `A, B`: `Re tr(BA) = Re tr(AB)`. (In fact `tr(BA) = tr(AB)`.) 

### `frobSq_add_hermitian`

 Frobenius-norm expansion for a sum of two Hermitian matrices. 

 ### The main theorem 

### `rank_trace_ineq`

 **Rank–trace inequality** (paper `lem:ranktrace`, eq. `eq:ranktrace`).

Hypotheses: `P ⪰ 0` with `rank P ≤ r`; `Q` Hermitian with `n₊(Q) ≤ b`; `c > 0`.
Conclusion:
  `c · tr P − (c²/4) · r + 2c · tr Q − c² · b ≤ ‖P + Q‖_F²`.


### `rank_trace_ineq_two`

 **Rank–trace inequality, `c = 2` form** (paper `lem:ranktrace`,
"in particular"). Rearranged: `r ≥ 2 tr P + 4 tr Q − 4b − ‖P+Q‖_F²`. 
