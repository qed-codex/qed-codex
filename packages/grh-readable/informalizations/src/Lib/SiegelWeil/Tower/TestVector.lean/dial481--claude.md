---
{
  "module": "src/Lib/SiegelWeil/Tower/TestVector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/TestVector.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/TestVector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The test vector of the zeta integral

Let `H` be a hyperbolic plane over the CM field `E`. At each infinite place the Fock space
`New.PairFock` of `Hom(H, H)` has two positive coordinates, the diagonal ones. The test vector is
the Fock vector of the product of their `m w`-th powers. Its cone integrand for the pair `(H, H)`
over `(0, 0)` is the vacuum times the integrand of a zeta integral: the test function
`∏ conj (a w) ^ (2 m w) exp (-|a w|²)` times a character and a power of `|a|`.

* `New.Exchange.tateVector`: the test vector.
* `New.Exchange.realPairWeil_tateVector`: the maximal compact subgroup of the target group fixes it.
* `New.Exchange.coneIntegrand_tateVector`: its cone integrand, in either model, is an explicit
  positive function times the vacuum.

Notions from other files:
* `New.Fock.polyVector`: the Fock vector x ↦ P(ζ(x))·exp(−|x|²/2) of a polynomial P, where ζ(x)_i is
  x̄_i at positive and x_i at negative coordinates.
* `New.Fock.MixedModel`: a decomposition y = La + Iw + Kb of the large space, with a map `slice a`
  from the large Fock space to the small one.
* `Splitting.IsAdapted 1 b`: the adelic frame `D.frameAt 1 b = (l b*⁻¹, k b, ι)` of a splitting
  `D` has orthonormal columns at the infinite places and integral entries at the finite ones.
* `New.Exchange.coneIntegrand`: the integrand of the cone integral, `lineTermReal A X β a` applied
  to the translate of a vector by the compact part, times a character and a power of `|a|`.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.

Part of a known result: analytic continuation and functional equation of Hecke `L`-functions. See
`Lib.SiegelWeil.Tower.FunctionalEquation`. Up to a scaling of the variable the test function is that
of J. Tate, Fourier analysis in number fields and Hecke's zeta-functions (thesis, 1950), §2.5.


### `frameAt_real_mul_conjTranspose`

 Let `D` split `W` as `W'` plus hyperbolic planes indexed by `r`, and let it be adapted at `1`
to `b`: at each infinite place `w` the frame `D.frameAt 1 b` of `W` has orthonormal columns (and it
is integral at the finite places). This frame is square, so its rows are orthonormal as well. 

### `signMatrix_mul_frameAt_real`

 Let `D` split `W` as `W'` plus hyperbolic planes indexed by `r`, with an adapted frame
`F = D.frameAt 1 b`. At an infinite place `w`, with `S` the diagonal matrix of the signs `s` of
`W`, we have `S F = F T`, where `T` is the block diagonal matrix of the exchange of the two lines of
each plane and of the signs `s'` of `W'`. 

### `posProj_eq`

 The projection `posProj s` on the coordinates of sign `1` is `(1 + signMatrix s) / 2`, where
`signMatrix s` is the diagonal matrix of the signs. 

### `framePoint`

 The vector `L a + I z + K c` with coordinates `a`, `z`, `c` in the directions `L`, `I`, `K` of
the real mixed model of a splitting `D` adapted at `1` to `b`. 

### `framePoint_eq_mulVec`

 Let `D.frameAt 1 b` be an adapted frame. The point `framePoint h a z c`, which is
`L a + I z + K c`, is the image under the infinite components `realMatrix` of this frame of its
three blocks of coordinates, put side by side at each place in the order `a`, `c`, `z`. 

### `framePoint_apply`

 At the infinite place `w`, the point `framePoint h a z c`, which is `L a + I z + K c`, is the
image under the component at `w` of the adapted frame `D.frameAt 1 b` of the three blocks of
coordinates at `w`. 

### `posProj_mulVec_framePoint`

 The projection `posProj` on the positive coordinates sends the point `L a + I z + K c`
(`framePoint h a z c`) to the point with `a` and `c` replaced by their midpoint and `z` by its
positive projection, because the matrix of signs exchanges `L` and `K`. 

### `signMatrix_mulVec_framePoint`

 The matrix of signs exchanges `L` and `K`, so on a point `L a + I z + K a`
(`framePoint h a z a`) it acts through the middle coordinate `z` only. 

### `framePoint_sub`

 The difference of two points `L a + I z + K c` (`framePoint h a z c`) is the point of the
differences of their coordinates. 

### `star_framePoint_dotProduct`

 The columns of `L`, `K` and `I` of an adapted splitting are orthonormal, so the inner product of
the points `L a + I u + K a` and `L c + I z + K c` (both `framePoint`) is `2 ⟨a, c⟩ + ⟨u, z⟩`. 

### `exists_framePoint_eq_of_posProj_eq`

 A vector `y` in the positive coordinates (fixed by `posProj`) is a point `L c + I z + K c`
(`framePoint`) whose middle coordinate `z` is positive. 

### `slice_realHeisenbergOp_vacElem_apply`

 Let `y` be a vector in the positive coordinates, and translate the vacuum (the Gaussian) by it
with the Heisenberg operator `realHeisenbergOp y`. The value at `u` of the slice at `a` of this
translate, in the mixed model of the adapted splitting, is the value of the translate at the point
`framePoint h (-a) u (-a)`, that is `-L a + I u - K a`. 

### `realBoxProd_realHeisenbergOp_vacVector`

 Let `e` split the coordinates `ι`, with signs `ε`, into `ι₁` and `ι₂`. The external product
`realBoxProd` of the translate of the vacuum by `y` with the vacuum is the translate of the vacuum
by the vector `(y, 0)`. 

### `slice_polyVector_apply`

 Let `P` be a polynomial in the positive coordinates and `polyVector` its Fock vector
`P(ζ) exp(-|·|² / 2)`. In the mixed model of an adapted splitting, the value at `u` of the slice at
`a` of this vector is its value at the point `framePoint h (-a) u (-a)`, that is
`-L a + I u - K a`. 

### `tateVector`

 The test vector on `Hom(W, W)`, for a space `W` with signs `s` (the signs on `Hom(W, W)` are
`homSigns s s`, and the diagonal coordinates are positive for them): the Fock vector of the product,
over the infinite places `w`, of the `m w`-th powers of the diagonal variables at `w`. 

### `isSchwartzVector_tateVector`

 All weighted norms of the test vector are finite (`IsSchwartzVector`). 

### `realPairWeil_tateVector`

 Let the signs `s` take each of the values `1` and `-1` once. Let the components of `g`, a point
of the archimedean unitary group `GInf E s`, preserve the lines of each sign (`blockDiagAlg s` is
the algebra of matrices commuting with the signs). Then `(1, g)`, acting in the real Weil
representation `realPairWeil` of the pair with weight `0` on the source and
`targetWeight n m = 1 - m` on the target, fixes the test vector, which is the Fock vector of
`∏ w, ∏ i, X (w, i, i) ^ m w`. 

### `framePoint_lineTermSplitting_diag`

 Let `A` be a base-adapted splitting (`IsBaseAdapted A`, which makes each
`lineTermSplitting A A β` adapted at `1`) of `W'` along a line over a space `W` of rank zero, and
take the frame of `lineTermSplitting A A β`, the splitting of `Hom(W', W')` over `Hom(W, W)` for the
model `β` (one of the two sides of Poisson's formula on the line). Let `x` be `a` on the line (the
right summand of the index set `LineIndex`) and `0` elsewhere. The diagonal entries at the infinite
place `w` of the point `framePoint h (-x) u (-x)`, for the adapted frame `h` of this splitting, are
`-a w`. 

### `lineTermReal_tateVector`

 Let `W` have rank zero (`n` is empty), let `W'` have rank two (`hn`), and let `A` be a
base-adapted splitting of `W'` over `W` along one line (`IsBaseAdapted A`, so that
`lineTermSplitting A A β` is adapted at `1`). For either of the two models `β` of Poisson's formula
on the line, the real line term `lineTermReal A A β a` is the slice, in the real mixed model of
`Hom(W', W')` over `Hom(W, W)`, at the point with coordinates `a` on the line and `0` elsewhere. It
sends the test vector `tateVector s' m` to `exp (-∑ |a w|²) ∏ conj (a w) ^ (2 m w)` times the
vacuum, where `tateVector s' m` is the Fock vector of the product over the infinite places `w` of
the `m w`-th powers of the diagonal variables at `w`. 

### `coneIntegrand_tateVector`

 Let `A` be a base-adapted splitting (`IsBaseAdapted A`, so each `lineTermSplitting A A β` is
adapted at `1`) of `W'` along a line over a space of rank zero, and let the signs `s'` of `W'` take
each of the values `1` and `-1` once. The cone integrand `coneIntegrand` at `p = (κ, a)` is the
phase `∏ (a w / |a w|) ^ (2 m w)` times `|a| ^ z` times the line term at `a` of the translate by
`κ`; here `κ` is in the maximal compact group and `|a|` is the module of the idele with components
`a w` at infinity and `1` at the finite places. For the test vector `tateVector s' m`, the Fock
vector of `∏ X (w, i, i) ^ m w`, in either of the two models `β` of Poisson's formula on the line
and for every real exponent `z`, it is the vacuum times the number
`exp (-∑ |a w|²) |a| ^ z ∏ |a w| ^ (2 m w)`. 
