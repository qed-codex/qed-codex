---
{
  "module": "src/Lib/Shimura/Transfer/MarkedPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/MarkedPairs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/MarkedPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eigenline reflections of a separable matrix, and the term of the count at a marked triple

Invariance properties of the terms of the point count `New.Variety.countTerm`, a function on
GL_n(E)-orbits of triples (coset xK, rational matrix y, index μ of a root), the type
`MarkedTriple (levelGU n 𝔑) n`.

* `New.Variety.isReflection_markedReflection` and
  `New.Variety.exists_eq_markedReflection_iff_of_ratConj_eq` (bundled as
  `New.Variety.isReflection_markedReflection_and_exists_eq_iff`): for y with separable
  characteristic polynomial, the matrices `New.Variety.markedReflection y i` are reflections, and
  each reflection that commutes with y equals exactly one of them.
* `New.Variety.countTerm_mk`: the term of an orbit may be computed at any representative.
* `New.Variety.finsum_countTerm_eq_sum`: the weighted count as a finite sum over the support of the
  count of weight 1.

`New.Variety.IsReflection J` says J = u wᵀ - 1 with w · u = 2. `New.Variety.ratConj z` conjugates by
Φ_{v₀}(z), the image of z in GL_n(ℂ) under the fixed embedding Φ v₀ : E → ℂ used throughout.
`New.Variety.IsSignedFrame x J` says that x is a frame for a rational form whose signature is given
by J.

Notions from other files:
* `New.Variety.heckeAlgebra`: the Hecke algebra of level K(𝔑): the subalgebra of elements ∑ a_g [g]
  of ℂ[GL_n(𝔸_f)] that are supported on `GUPlus E n` and whose function ∑ a_g 1_{gK} is left
  K(𝔑)-invariant.
* `New.Variety.levelGU`: the principal level K(𝔑), the similitudes in `GL_n(Ô E)` that are congruent
  to `1` modulo `𝔑`.
* `New.Variety.toFinGL`: The diagonal embedding of GL_n(E) in GL_n of the finite adeles of E.
* `New.Variety.heckeCosetFn f`: for f = ∑ a_g [g] in the Hecke algebra, the function ∑ a_g 1_{gK} on
  the cosets of the level `K`.
* `New.Variety.eigenReflection ε y μ`: if `ε` holds, the matrix `New.Variety.markedReflection y μ`,
  a polynomial in Φ_{v₀}(y) that is `1` on the eigenline of the `μ`-th listed root of the
  characteristic polynomial and `-1` on the other eigenlines; if `ε` fails, the identity.

## Relation to the literature

Known; see `Lib.Shimura.Transfer.WeightOccurs` and `Lib.Shimura.TraceFormula.MarkedDefiniteSums` for
sources.


### `ratConj_eigenReflection`

 For y, z in GL_n(E), conjugating the eigenline reflection `New.Variety.eigenReflection` of y by
Φ_{v₀}(z) gives the eigenline reflection of zyz⁻¹. 

### `isSignedFrame_mul_iff`

 The signature condition is unchanged when `x` is multiplied by a similitude `g` (an element of
`GU E n`) on the right, or by a rational `z` on the left with `ℓ` conjugated by `z`. 

### `finsum_countTerm_eq_sum`

 If the unweighted count `countTerm ε f 1` has finite support, the count with weight `w` is a
finite sum over that support. For the chosen representative `(xK, y, μ)` of an orbit, the weight is
read at the characteristic polynomial of `y` and at the mark `μ`. 

### `exists_conj_diagonal_markedReflection`

 For `y` with separable characteristic polynomial, some `k` conjugates the diagonal matrix of
the listed roots `numberedRoots (Φ v₀) _` of that polynomial to Φ_{v₀}(y), and the diagonal matrix
with `1` at `i` and `-1` elsewhere to `markedReflection y i`, for every `i`. 

### `isReflection_markedReflection`

 For `y` with separable characteristic polynomial, `markedReflection y i` is a reflection (a
matrix `u wᵀ - 1` with `w ⬝ᵥ u = 2`). It is the polynomial in Φ_{v₀}(y) that is `1` on the
eigenline of the `i`-th listed root `numberedRoots (Φ v₀) _ i` of the characteristic polynomial and
`-1` on the other eigenlines. 

### `exists_eq_markedReflection_iff_of_ratConj_eq`

 Let `y` have separable characteristic polynomial, and let `J` be a reflection fixed by
conjugation with Φ_{v₀}(y). Then `J` equals `markedReflection y i` for exactly one `i`, and
Φ_{v₀}(y) acts on the image of `J + 1` by the `i`-th listed root `numberedRoots (Φ v₀) _ i` of its
characteristic polynomial. 

### `isReflection_markedReflection_and_exists_eq_iff`

 For `y` with separable characteristic polynomial, each `markedReflection y i` is a reflection
(`isReflection_markedReflection`), and a reflection `J` fixed by conjugation with Φ_{v₀}(y) equals
`markedReflection y i` for exactly one `i`, whose eigenline contains the image of `J + 1`
(`exists_eq_markedReflection_iff_of_ratConj_eq`). 

### `_root_.Representation.coeff_ofMulAction_smul`

 Under the permutation representation of a group `G` on `k[H]`, the coefficient of `g • v` at
`g • q` is the coefficient of `v` at `q`. 

### `heckeAlgebra.heckeCosetFn_conj`

 For `x` in the level `K = levelGU n 𝔑`, the function `heckeCosetFn f` of an element `f` of the
Hecke algebra takes the same value at the cosets of `x⁻¹ g x` and of `g`. 

### `heckeAlgebra.mem_GUPlus_of_ne_zero`

 If the function `heckeCosetFn f` of an element `f` of the Hecke algebra does not vanish at the
coset of `g`, then `g` lies in `GUPlus E n`, the similitudes whose inverse has integral
entries. 

### `countTerm_mk`

 The term `countTerm ε f w` of the orbit of the triple `(xK, y, μ)` may be computed at this
triple: if `x` is a signed frame for `eigenReflection ε y μ`, it is
`heckeCosetFn f (invAutInFrame y x) * w (charpoly y) μ` with `invAutInFrame y x = x⁻¹ y⁻¹ x`, and
otherwise it is `0`. (`countTerm` itself reads a chosen representative.) 
