---
{
  "module": "proof/rates/GeneralPieces/Ring/Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Pieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2: the steps of the proof that are statements about the ring

`GeneralPieces.pieceFacts` derives `AppHalfPieces.PieceFacts`, field by field along the sentences of
the proof of the theorem on the pieces (Appendix B), from the lemma on the operators Q_s and the
lemma on the dual
families: a^μ is a combination of monomials of weight at most h; Σ_s A_s = h!·[x = v]·[y = u]; the
displays (54) and (55), by expanding a^⟨i⟩[s−h+i]t^{μ(y)} ∈ V_{s+i} (after the factors have been
exchanged) and b[h−s−i]t^{μ(y)} ∈ V_{2h−s−i} in monomials; all factors are integers by (O1); both
numbers of terms are at least 1.
The two lemmas (`GeneralPieces.lemmaQ`, `GeneralPieces.Dual.lemmaDual`), the facts on a[r] that come
with display (47) (`GeneralPieces.opFacts`), the property (O1) (`GeneralPieces.o1`) and the fact
that h!/z_μ is an integer
(`GeneralPieces.Dual.zDvd`) are hypotheses; `proof/rates/GeneralPieces/Main.lean` feeds them in.
Claim (b) of the lemma on the Q_s, which the paper quotes
for the sum, is not needed there: the index set {−2h, …, 2h} is exactly the range |s| ≤ E + h of
claim (c) for E = h. 

 ### Combinations of monomials of weight at most h 

### `Le`

 Every monomial of a has weight at most h. 

### `le_y`

 Every monomial of y_n has weight at most n. 

### `le_aFam`

 "Here a^μ is a combination of monomials of weight at most h." 

 ### Polynomials with integer coefficients 

### `isInt_bFam`

 b^ν has integer coefficients, because h!/z_ν is an integer. 

 ### Expanding in monomials 

### `coef_comp_gen`

 "Expanding these polynomials in monomials t^σ": if f ∈ V_E, then b[r']f ∈ V_{E+r'} by (O1), and
the coefficient of t^π in a[r]b[r']f is the sum over |σ| = E + r' of the coefficient of t^π in
a[r]t^σ times the coefficient of t^σ in b[r']f. 

### `pieceFacts`

 The steps of the proof of the theorem on the pieces with ρ = 1/√2 that are statements about the
ring, from the two lemmas and the other hypotheses named at the head. 
