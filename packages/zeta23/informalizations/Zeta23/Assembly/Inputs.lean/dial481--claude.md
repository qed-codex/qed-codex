---
{
  "module": "Zeta23/Assembly/Inputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/Inputs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/Inputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
  Part of the Zeta23 formalization of the paper
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
  Bracketed labels ([prop:cross], [eq:Msplit], …) and section numbers (§5.4, …) refer to that paper.
-/
```


# Interfaces consumed by `Zeta23/Assembly.lean` from `ZeroSide.lean` (prop:block) and `Tail.lean` (prop:tail)
This small file exists so that `ZeroSide.lean` / `Tail.lean` can *prove*
`∀ᶠ T, BlockInputs Z P T` / `TailInputs Z P T (θ₀ T)` without importing all of `Assembly.lean`, and
`Main.lean`  can plug those proofs into `Assembly.thmA_abstract`.
Every field is a statement announced by the producing file; docstrings quote the paper labels.


### `NII`

 `N(I′∖I) := N(T−D₀,T) + N(2T,2T+D₀)` (the paper prop:zeroside), as a natural number. 

### `BlockInputs`

 **Inputs from prop:block + [eq:Ncount] at height `T`** (the paper `prop:block`:
"(i) `n₊(Ã) ≤ s₁+s₂+p` and `rank(Ã) ≤ s₁+s₂+2p = #𝒵(I′)`.
 (ii) `Â = P+Q` with `P,Q` real symmetric, `P ⪰ 0`, `rank P ≤ s₁+s₂`, `tr P ≤ N_on(I′)`, and `n₊(Q) ≤ p`";
[eq:Ncount]: "`N(I′) ≥ s₁+2s₂+2p`" and "`N(I′) ≥ N_on(I′)+2p`"), produced by `ZeroSide.lean`.
Units: `Ã = P.tilde T (Z.Az P T)` [eq:AE], `Â = P.hat T (Z.Az P T)` [eq:hatunits].
`p` (number of off-line pairs in `𝒵(I′)`) is existentially quantified since only the displayed
inequalities involving it are consumed downstream. 

### `BlockInputs.hat`

 prop:block(ii) in hat units + "`N_on(I′) + 2p ≤ N(I′)`" 

### `BlockInputs.tilde`

 prop:block(i) in tilde units + "`N(I′) ≥ s₁ + 2s₂ + 2p`" [eq:Ncount] 

### `TailInputs`

 **Inputs from prop:tail at height `T`** (the paper `prop:tail`: "`‖Ẽ‖ ≤ θ₀ := 4A₀C₁²X^{1/2}
log(4T)/D₀²` … Moreover the trace norm satisfies `‖Ê‖₁ ≤ θ₀/(aL) ≤ 2θ₀/L`"), produced by
`Tail.lean` with `B = traceNorm Ê`.  Units: `Ẽ = P.tilde T (Z.Ez P T)`, `Ê = P.hat T (Z.Ez P T)`. 

### `TailInputs.tilde`

 lem:weyl's hypothesis: every eigenvalue of `Ẽ` is at most `θ₀` in absolute value
  (this is `‖Ẽ‖ ≤ θ₀` for the operator norm of a Hermitian matrix) 

### `TailInputs.hat`

 `|tr Ê| ≤ ‖Ê‖₁`, `‖Ê‖_F ≤ ‖Ê‖₁`, `‖Ê‖₁ ≤ θ₀/(aL)` 
