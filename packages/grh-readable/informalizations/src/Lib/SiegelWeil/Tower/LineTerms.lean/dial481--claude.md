---
{
  "module": "src/Lib/SiegelWeil/Tower/LineTerms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LineTerms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LineTerms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinates on a line parabolic and Poisson's formula for terms along lines

This file concerns the stabiliser of an isotropic line in a hermitian space `V'`, split by
`D : V'.Splitting V Unit` into a hyperbolic plane and `V`. It gives coordinates on the unipotent
radical and on the Levi factor of this stabiliser.

## Main definitions and results

* `New.Exchange.lineTerm`: two families, indexed by an adele, of operators from `Hom(W', V')` data
  to those of `Hom(W, V)`: a rank-one translation, then both zero terms.
* `New.Exchange.lineTerm_pairWeil_levi`: if the line of `W'` is fixed or `W` and `V` have equal
  rank, they intertwine the Weil representations `New.pairWeil` on Levi elements, up to a scalar and
  a rescaling of the adele.
* `New.Exchange.tsum_lineTerm`: the theta sums over `E` of the two families agree, since they are
  the two mixed models of one hyperbolic plane.
* `New.Exchange.lineTermSplitting`, `New.Exchange.frameAt_lineTermSplitting`: the splittings behind
  the two models, and their frames.

Notions from other files:
* `New.Space`: a hermitian space over `E` with Gram matrix `J` and an adelic frame `x` that
  diagonalises `J` at every place; `𝒮 V` is its data space and `θ V` the theta functional on it.
* `New.Space.Splitting`: for `D : V.Splitting V₀ p`, dual isotropic frames `k`, `l` indexed by `p`
  and an isometric embedding `i` of `V₀` orthogonal to both, which together fill `V`.
* `New.Space.Splitting.zeroTerm`: the map `𝒮 V → 𝒮 V₀` that averages over the adelic span of `k`
  modulo its rational points; `D.slice x` is translation by `l x` followed by it.
* `New.Space.Splitting.levi`: the homomorphism sending `(m, g₀)` to the element that acts by `m` on
  the frame `k`, by `g₀` on `V₀` and by `m*⁻¹` on the frame `l`.
* `New.pairWeil W V a b`: the Weil representation of the two unitary groups on `𝒮 (W.hom V)`,
  twisted by the automorphic characters `a` and `b` of the determinants.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` for sources.



## Coordinates on the radical and Levi factor of a line stabiliser

For a splitting `D : V'.Splitting V Unit` of `V'` into a hyperbolic plane and `V`, coordinates on
the stabiliser of the isotropic line: `New.Exchange.lineRadical` on the unipotent radical and
`New.Exchange.lineLevi` on the Levi factor.


### `lineRadical`

 The element `D.radicalElement c b` of the unipotent radical with `c = V.x⁻¹ * q.1` and
`b = 2 q.2`. 

### `lineLevi`

 The homomorphism that sends an idele `a` and an element `g` of the group of `V` to the Levi
element `D.levi (a⁻¹, g)`, which acts by `a⁻¹` on the isotropic line. 


## Terms along a line in two models and Poisson's formula

Let `A` split `W'` as a hyperbolic plane plus `W`, and `X` split `V'` as a hyperbolic plane plus `V`
(`New.Space.Splitting`: isotropic dual frames `k`, `l` and an isometry `i`; `kAdelic`, `lAdelic`,
`iAdelic` are these in adelic coordinates, `kCoord`, `lCoord`, `iCoord` the forms that give the
three coordinates of a vector).


### `lineTerm`

 The term at the adele `a`, from `𝒮 (W'.hom V')` to `𝒮 (W.hom V)`, in the model `β`. For
`β = true` it is translation by the map `a • X.kAdelic * A.kCoord`, followed by the zero term along
the line of `A` and then the one along the line of `X`. For `β = false` it is translation by
`a • X.lAdelic * A.lCoord`, followed by the zero term along the line of `X` and then that of `A`. 

### `iCoord_levi_iAdelic`

 The block on `W` of the Levi element of `A` attached to an invertible `m` and a unitary `g`
is `g`. 

### `lineLevi_inv_mul_kAdelic_mul_levi`

 The Levi element of `A` acting by the scalar `u` on its line, on the right, and the inverse of
`lineLevi X (c, h)`, on the left, scale the rank-one map `X.kAdelic * A.kCoord` by `c * u`. 

### `lineLevi_inv_mul_lAdelic_mul_levi`

 The Levi element of `A` acting by the scalar `u` on its line, on the right, and the inverse of
`lineLevi X (c, h)`, on the left, scale the rank-one map `X.lAdelic * A.lCoord` by the conjugate of
`(c * u)⁻¹`. 

### `lineTerm_pairWeil_levi`

 Equivariance of `lineTerm` under Levi elements. `lineTerm A X β ξ` is the term at the adele `ξ`
from data on `Hom(W', V')` to data on `Hom(W, V)`, in one of two models chosen by `β`. Let the idele
`u` act on the line of `A` in `W'` and `c⁻¹` on that of `X` in `V'`, and assume that `u = 1` or that
`W` and `V` have equal rank. Apply these Levi elements (with `g`, `h` on `W`, `V`) in the
representation twisted by `a * upsilonU1`, with `upsilonU1` the fixed splitting character on
norm-one ideles. The result is the following, with `x = c * u`: replace `ξ` by `ξ x` if `β` holds
and by `ξ (star x)⁻¹` otherwise, apply `(g, h)` in the representation twisted by `a`, and multiply
by `√|u|^(2 card r + 2) / (a.spaceChar (card n) x * √|x|^(card n + 2))`, where the `+ 2` in the last
exponent is present only when `β` is false. Here `a.spaceChar k` is the idele character attached to
`a` in rank `k`, and `|·|` is the idele norm `ideleAbs`. 

### `LineIndex`

 The index set of the isotropic frames that split `W'.hom V'` over `W.hom V`. The right summand
indexes one line of the hyperbolic plane `Hom(A, B) ⊕ Hom(A*, B*)`, where `A`, `A*` are the lines
spanned by `A.k`, `A.l` and `B`, `B*` those spanned by `X.k`, `X.l`. 

### `instance : DecidableEq (LineIndex n r)`

 A shortcut: the search for this instance inside larger index sets exceeds the default size. 

### `planeSplitting`

 The splitting of `Hom(W', V')` along `Hom(W ⊕ A*, B) ⊕ Hom(A*, V)`, over the plane
`Hom(A, B) ⊕ Hom(A*, B*)` plus `Hom(W, V)`. Here `hyperbolicSum p T` is the orthogonal sum of
`card p` hyperbolic planes and `T`, and `A`, `A*`, `B`, `B*` are the lines as in `LineIndex`. 

### `planeModel`

 The two splittings over `Hom(W, V)` of the plane `Hom(A, B) ⊕ Hom(A*, B*)` plus `Hom(W, V)`.
For `β = true` the first line is the frame `l` of the translation and the second the frame `k` of
the zero term; for `β = false` the two lines are exchanged. 

### `planeSplitting_iAdelic_mul_planeModel_lAdelic`

 In each model, the adelic frame `l` of the plane, embedded in `Hom(W', V')` by `planeSplitting`,
is the Kronecker product of the frames of the two lines that translate in `lineTerm`. 

### `lineTerm_eq_comp_zeroTerm`

 Each line term is the zero term for `planeSplitting` followed by the mixed term `slice`
(translation by `l`, then the zero term) of `planeModel W V β`, the model `β` of the hyperbolic
plane, at the vector with single coordinate `a`. 

### `tsum_lineTerm`

 Poisson's formula along the line: the values of the theta functional `θ` at the line terms,
summed over the rational points `ξ : E`, have the same sum in the model `β` as in `true`. 

### `lineTermSplitting`

 The splitting of `Hom(W', V')` over `Hom(W, V)` behind the model `β`. 

### `lineTermBasis`

 The block-diagonal change of basis, built from `star W.x` and `adaptedHomBasis Unit V`, in which
the frame of `lineTermSplitting` is adapted (`isAdapted_lineTermSplitting`). 

### `lineTerm_eq_slice`

 Each line term is the mixed term `slice` (translation by `l`, then the zero term) of
`lineTermSplitting`, the composite of `planeSplitting` and the model `β`, at the vector with last
coordinate `a` and all others `0`, transformed by the conjugate transpose of the inverse of the
basis `lineTermBasis` (`matrixToVec` reads a matrix as a vector). 

### `frameAt_lineTermSplitting`

 The frame of `lineTermSplitting` in the basis `lineTermBasis` at the group element `1`
(`frameAt`: the columns of `l`, `k` and `i` in adelic coordinates), as a block matrix of Kronecker
products of the frames of `X` and `A`; `stdForm` is the diagonal matrix of the signs. The two models
differ by the exchange of two columns. 

### `isAdapted_lineTermSplitting`

 If the frames of `A` and `X` are orthonormal at the infinite places and integral at the finite
ones, so is the frame of `lineTermSplitting` in the basis `lineTermBasis`. 
