---
{
  "module": "src/New/Determinant/Exchange/RemovingPlanes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/RemovingPlanes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/RemovingPlanes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Change of point and sign, and descent of the exchange identity by removing hyperbolic planes

This file records how forms and theta integrals behave under passage to opposite signs and under
change of point. It also descends the exchange identity `New.Exchange.RowColExchangeIdentity`
between theta integrals from a pair of large spaces to the pair with hyperbolic planes removed. For
any number of planes there is a space with an adapted splitting over a given space `W`.

## Main definitions and results

* `New.Exchange.isForm_neg_iff_and_integral_neg`: passing to the opposite signs (`G.neg`, the
  identity on matrices) preserves forms of a given type and integrals over the quotient, if it
  matches the rational points of the two spaces.
* `New.Exchange.exists_thetaLarge_thetaSmall_eq_circle_mul`: triples of spaces with the same signs
  have the same integrals `thetaLarge` and `thetaSmall`, up to one translation and numbers of
  modulus one.
* `New.Exchange.RowColExchangeIdentity.cone`: the identity descends along one plane of adapted
  splittings, to the cone integral of the real vector, if `rk W` is even and `rk V ≥ rk W / 2`;
  `New.Exchange.RowColExchangeIdentity.dualCone` is the case `rk V < rk W / 2`, on the other side of
  Poisson's formula.
* `New.Exchange.exists_rowColExchangeIdentity_removing_planes`: the identity descends along the
  planes of an adapted splitting, if `rk W` is even and `V'` has as many more negative signs than
  `V` as planes.

Notions from other files:
* `New.Exchange.RowColExchangeIdentity W V U μ σ x y ℓ`: the real vectors `x`, `y` are Schwartz
  vectors (all their weighted norms are finite), and for every tame character `𝔠` of weight `μ` the
  theta integrals `thetaLarge` over `[U(V)]` and `thetaSmall` over `[U(U)]` are proportional on
  standard data, with a factor `c` such that `D |c| ^ 2` is
  `lValueProdInt 𝔠 (rk V - rk W / 2) * ℓ 𝔠` for a constant `D` that does not depend on `𝔠`. The
  bijection `σ : b ⊕ r ≃ n` of the index sets of `U`, `V`, `W` orders the rows of the standard data.
* `New.Space.Splitting`: a decomposition V = (lE^p ⊕ kE^p) ⊥ iV₀ over E: isotropic frames l, k with
  l*Jk = 1, an isometry i from V₀ orthogonal to both, and rk V = rk V₀ + 2p.
* `New.Exchange.realSlice A U x`: the slice at `x` of a real vector for `(W', U)` in the mixed model
  of the splitting `A` of `W'` over `W`, a real vector for `(W, U)`; at `x = 0` it is the zero term.
* `New.stdColDatum χ z`: the standard datum `y ↦ χ⁻¹(det (z y))`, supported on the integral `y` for
  which this determinant is a unit.

## Relation to the literature

See `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.


 ## Forms and theta integrals under change of point and sign 

### `neg_mem_neg_Gamma_iff`

 `G.neg` carries the rational points of `W` onto those of the opposite space `W.neg`, whose point
is a scalar multiple of that of `W`. 

### `isForm_neg_iff_and_integral_neg`

 Let `W` and `S` be Hermitian spaces with opposite signs `s`, `-s`, and let `G.neg` carry the
rational points `W.Γ` onto `S.Γ`. Let `typeKernel l s` be the product over the infinite places `w`
of the discrete series kernels with doubled parameters `l w`. Then `F` is a form of type
`typeKernel l (-s)` on `S` if and only if its pull-back along `G.neg` is a form of type
`typeKernel l s` on `W`, and integrals over the two quotients agree under this pull-back. 

### `mem_ratVectors_hom_move`

 Let the points `W.x`, `W₁.x` differ by a rational matrix `c` on the left and an adelic unitary
element `k` on the right, and likewise those of `V` and `V₁` by `c'` and `k'`. Then the rational
vectors (`ratVectors`) of the space `W.hom V` of `a × n` matrices are rational for `W₁`, `V₁` with
their points multiplied on the right by `k`, `k'` (`Space.move`). 

### `exists_circle_thetaIntegral_localDatum_eq_mul`

 Let the points of `W` and `W₁` differ by a rational matrix `c` on the left and by `k` in the
adelic unitary group on the right, and let `V`, `V₁` have the same signs. Let the semilocal field
`F` be read off from the finite adeles at the places `A` by `π` (`ReadsAt`). For any characters `α`,
`β`, consider the datum with real part `v`, the function `Φ` of the components in `F`, and the
vacuum at the other places. Its theta integral for `(W, V)` at `g` is `u` times that for `(W₁, V₁)`
at `k * g`, where `u` has modulus one and does not depend on `v`, `Φ`, `g`. 

### `exists_thetaLarge_eq_mul_thetaLarge`

 Let the points of `W` and `W₁` differ by a rational matrix `c` on the left and `k` in the adelic
unitary group on the right, and let `V`, `V₁` have the same signs. Let `𝔠` be a character of
`[U(1)]` of weight `μ` at the infinite places, tamely ramified at a finite set `𝔠.ramifiedPlaces`
of split places. For a vector `v` of the Fock space and a function `Φ` of matrices over the product
`LocProd` of the completions at these places, `thetaLarge W V 𝔠 v Φ` is the theta integral over
`[U(V)]` of the datum that is `v` at the infinite places, `Φ` at the ramified places and the vacuum
elsewhere. Its value at `g` is `u` times the value for `(W₁, V₁)` at `k * g`, where `u` has modulus
one and does not depend on `v`, `Φ`, `g`. 

### `exists_thetaLarge_thetaSmall_eq_circle_mul`

 Let `W, W₁`, `V, V₁` and `V', V'₁` be pairs of Hermitian spaces with the same signs. For a split
tame character `𝔠` there are two theta integrals on the adelic unitary group `G E s` of `W`, of data
with real part a vector of the Fock space `PairFock`, a given function at `𝔠.ramifiedPlaces` and the
vacuum at other places. There is a point `γ` of `G E s`, depending on the spaces only, such that for
every `𝔠` the integrals `thetaLarge` for `(W₁, V₁)` and `thetaSmall` for `(W₁, V'₁)` at `g` are, up
to numbers of modulus one, those for `(W, V)` and `(W, V')` at `γ * g`. 


## Descent of the exchange identity along hyperbolic planes

The identity passes from `(W ⊕ H, V ⊕ H, U)` to `(W, V, U)` by taking constant terms along the new
isotropic line. On the side of `U` only the zero vector contributes
(`integral_thetaSmall_lineRadical_eq_mul_thetaSmall`); on the side of `V ⊕ H` the constant term is a
cone integral. Throughout, `New.Exchange.realSlice A U 0` gives the zero term along `A` of real
data.


### `exists_isBaseAdapted`

 Let the signs `t` have the rank and the number of minus signs (`negCount`) of `W` plus `card p`
hyperbolic planes. Then there is a space `W'` with signs `t` and a splitting of `W'` over `W` with
frames indexed by `p` that is adapted (orthonormal at the infinite places, integral at the finite
places). 

### `realSlice_zero_congr`

 Let `A`, `B` be adapted splittings of `W'` over `W`, and suppose that (`hBA`) the isotropic
frame `B.k` consists of the columns `e` of `A.k` and the inclusions `B.i`, `A.i` of `W` are equal.
Then `A`, `B` have the same zero term (`realSlice` at `0`) on real vectors for `(W', U)`. 

### `realSlice_zero_comp`

 Let `A` split `card p` hyperbolic planes off `W'`, with complement `W`, and let `B` split
`card r` planes off `W`, with complement `V'`, both adapted. For a vector `y` of the Fock space of
`(W', U)`, the zero term along the composite splitting is the zero term along `B` of its zero term
along `A`. 

### `stdColDatum_mul_transpose_mem_schwartzBruhat`

 Let `A` split a hyperbolic plane off `W'`, with complement `W`, and let `dualI` be the matrix of
the projection to `W` in the frame of `A` read at the ramified places `𝔠.ramifiedPlaces` of `𝔠`
(`adaptedFrame`). For an integral matrix `z` at these places the function equal to
`𝔠.semilocalChar⁻¹(det (z dualI wᵀ))` at integral `w` with this determinant a unit, and zero
elsewhere, that is the standard datum of `z dualI` read on transposes, is a Schwartz–Bruhat function
supported on the matrices of full rank. 

### `homSlice_localDatum_stdColDatum`

 Let `A` split one hyperbolic plane off `W'`, with complement `W`, and let `z` be an integral
matrix at the ramified places of the tame character `𝔠`. Take the datum for `(W', U)` with real part
`y` and the standard datum of `z ∘ pr_W`, read on transposes at the conjugates of these places. Its
slice along `A` at `WeilData.scaleIdele E • x` vanishes unless the finite part of `x` is integral.
In that case it is the nonzero constant `vacuumFactor` of `A`, by which slices multiply the vacuum,
times the datum for `(W, U)` with real part the slice of `y` at `x` and the standard datum of `z`,
read in the same way. 

### `theta_zeroTerm_stdColDatum_eq_zero`

 Let `X` split a hyperbolic plane off `U`, with complement `U₀`, and let `z` be an integral
matrix at the ramified places of the tame character `𝔠`. The standard datum `stdColDatum χ z`, for
the character `χ = 𝔠.semilocalChar` at these places, sends an integral `w` with `det (z w)` a unit
to `χ⁻¹ (det (z w))` and any other `w` to zero, so it lives on matrices of full rank. Take the datum
for `(W, U)` with real part `v` and this function on transposes, read at the conjugate places
(`𝔠.readsAt.star`), and translate it by `(g, h)` in the Weil representation with characters `α`,
`β`. The theta functional of `Hom(W, U₀)` vanishes on its zero term along the isotropic line `X.k`,
the datum for `(W, U₀)` whose theta function is the mean over adelic translations along this line,
modulo rational ones. 

### `integral_thetaSmall_lineRadical_eq_mul_thetaSmall`

 One plane, the side of `U`. Let `A` split one hyperbolic plane off `W'`, with complement `W`,
and be adapted. Let `y` be a real Schwartz vector and `z` an integral matrix at the ramified places
of `𝔠`. The constant term along `A`, at the point `(1, g)` of the Levi subgroup, of the theta
integral for `(W', U)` of `y` and the standard datum of `z ∘ pr_W` is the constant `vacuumFactor`
times the theta integral for `(W, U)` of the zero term `realSlice A U 0 y` and the standard datum of
`z`. 

### `RowColExchangeIdentity.congr_second_space`

 The exchange identity `RowColExchangeIdentity W V U μ σ x y ℓ` says that `x`, `y` are Schwartz
vectors of the Fock spaces of `(W, V)`, `(W, U)` and that there is a real `D` such that, for every
tame character `𝔠` of `[U(1)]` of weight `μ`, the theta integral of `(W, V)` at `x` is `c` times
that of `(W, U)` at `y` on standard data (rows ordered by the bijection `σ`), where
`D |c| ^ 2 = L(rk V - rk W / 2) ℓ(𝔠)` and `L = lValueProdInt 𝔠` is a product of `L`-values of `𝔠`.
It depends on `V` only through its signs: the theta integrals of two spaces `V`, `V₁` with the same
signs differ by a factor of modulus one. 

### `RowColExchangeIdentity.of_planeConstantTerm_eq`

 The exchange identity `RowColExchangeIdentity W V U μ σ x y ℓ` says: for every split tame
character `𝔠` of `[U(1)]` of weight `μ`, the theta integral `thetaLarge` of `(W, V)` at the Fock
vector `x` is `c` times the theta integral of `(W, U)` at `y` on standard data, with
`D |c| ^ 2 = L(rk V - rk W / 2) ℓ(𝔠)` for a `D` independent of `𝔠` and the product of `L`-values
`L = lValueProdInt 𝔠`. The standard datum `stdRowDatum σ χ w` is `χ⁻¹ ∘ det` of the matrix with the
rows of `w` and of the argument, ordered by `σ`, where that matrix is integrally invertible over the
product `LocProd` of the completions at the ramified places, and zero elsewhere.

Let `A` and `X` be splittings `W' = W ⊕ H` and `V' = V ⊕ H`, where `H` is a hyperbolic plane, both
adapted (frames orthonormal at infinite, integral at finite places). Suppose that for every `𝔠` the
constant term along `A` of the theta integral of `(W', V')` (`planeConstantTerm`) is `γ ≠ 0` times
the theta integral of `(W, V)` at the cone integral of `x` with exponent `z > 0` on the side `β` of
Poisson's formula (the integral of `coneIntegrand` over the maximal compact subgroup for `V'` and
the torus at the infinite places: `β = true` gives `cone`, `β = false` gives `dualCone`), where
`|γ| ^ 2 L(e) = C L(e + 1)` for `e = rk V - rk W / 2`. The constant term is formed from the standard
datum of `w dualI` (`dualI` is the projection to `W`) at `(1, g)`, the other side from that of `w`
at `g`, for integral matrices `w` and adelic unitary `g`. Then the identity for `(W', V', U)` at
`x`, `y` gives the identity for `(W, V, U)`, with the same `ℓ`, at the cone integral of `x` and the
zero term `realSlice A U 0 y`, the value of `y` at `0` in the mixed model of `A`. 

### `RowColExchangeIdentity.cone`

 Removing a plane by the cone integral. Let `W` have even rank, let `A` and `X` be splittings
`W' = W ⊕ H` and `V' = V ⊕ H` with a hyperbolic plane `H`, both adapted, and let
`rk V - rk W / 2 = z` be a natural number. The identity for `(W', V', U)` at `x`, `y` gives the
identity for `(W, V, U)`, with the same `ℓ`, at the cone integral of `x` with exponent `z + 1` and
the zero term of `y`, its value at `0` in the mixed model of `A`. 

### `RowColExchangeIdentity.dualCone`

 Removing a plane by the cone integral on the other side of Poisson's formula. Let `W` have even
rank, let `A`, `X` be splittings `W' = W ⊕ H`, `V' = V ⊕ H` with a hyperbolic plane `H`, both
adapted, and let `rk V - rk W / 2 = -z - 1 < 0`. The identity for `(W', V', U)` at `x`, `y` gives
the identity for `(W, V, U)`, with the same `ℓ`, at `dualCone A X μ (z + 1) x` and the zero term
`realSlice A U 0 y` of `y`, its value at `0` in the mixed model of `A`. 

### `exists_rowColExchangeIdentity_removing_plane`

 Removing a plane. Let `W` have even rank, let `A` be a splitting `W' = W ⊕ H` with a hyperbolic
plane `H` that is adapted, let `V'` have one negative sign more than `V`, and let the bijections
`σ`, `σ'`, which order the rows of the data, say that `rk U + rk V = rk W` and
`rk U + rk V' = rk W'`. The identity for `(W', V', U)` at `x`, `y` gives the identity for
`(W, V, U)`, with the same `ℓ`, at some `x₀` and the zero term of `y`, its value at `0` in the mixed
model of `A`. 

### `exists_rowColExchangeIdentity_removing_planes`

 Removing `card p ≥ 1` planes. Let `W` have even rank, let `A` split `W'` as `W` plus `card p`
hyperbolic planes and be adapted, let `V'` have `card p` more negative signs than `V`, and let the
bijections `σ`, `σ'`, which order the rows of the data, say that `rk U + rk V = rk W` and
`rk U + rk V' = rk W'`. The identity for `(W', V', U)` at `x`, `y` gives the identity for
`(W, V, U)`, with the same `ℓ`, at some `x₀` and the zero term `realSlice A U 0 y` of `y`, its value
at `0` in the mixed model of `A`. 
