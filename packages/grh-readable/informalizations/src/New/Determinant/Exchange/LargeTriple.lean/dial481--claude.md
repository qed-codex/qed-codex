---
{
  "module": "src/New/Determinant/Exchange/LargeTriple.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/LargeTriple.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/LargeTriple.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parabolic theta terms, equal ranks, and the exchange identity for the large triple

The theta kernel of the dual pair (U(X), U(V)) is unfolded along a splitting of X over W₁ with an
isotropic frame. It becomes a sum of terms `New.Space.Splitting.thetaTerm` indexed by rational
matrices. Take a standard datum v ⊗ Φ, with v real and Φ an explicit function at the finite places
A. Its terms are computed at points n(c, z) m(q, g) of the parabolic subgroup. They are expressed
through the theta functional `New.Exchange.thetaOnRealData` of the smaller pair (W₁, V). For
V = V' ⊕ W₁ this functional factors as a product. Let `𝔠` be a tamely ramified character,
`V = V' ⊕ W₁`, and `X` equal to `W₁` plus a hyperbolic space. Then the identity between the theta
integrals `New.Exchange.thetaLarge` and `New.Exchange.thetaSmall` for standard data follows from an
identity of periods over `[U W₁]`, under conditions on the rank of `W₁`, the signs and the data,
when `W₁` splits off a hyperbolic plane.

## Main definitions and results

* `New.Exchange.thetaTerm_eq_and_centreCoeff_eq_zero`: the terms are integrable
  (`hasIntegrableTerms_localDatum_of_eq_stdDatum`), each is an explicit factor times a value of
  `New.Exchange.thetaOnRealData` (`thetaTerm_localDatum_of_eq_stdDatum`), and the Fourier
  coefficient of the theta integral at `j • T` (`j` the purely imaginary element of the Weil data)
  vanishes if some signs represent the Gram matrices of all points with non-zero real slice but do
  not represent the matrix T (`centreCoeff_thetaIntegral_localDatum_eq_zero`).
* `New.Exchange.thetaOnRealData_boxProd_eq_mul`: on a product of real data, the functional of the
  datum built from a vector for (W₁, V') and a vector for (W₁, W₁) is the one for (W₁, V') times the
  theta kernel `New.pairTheta` of the pair (W₁, W₁).
* `New.Exchange.thetaLarge_eq_apply_one_of_even_rank`: if `W₁` has even rank and splits off a
  hyperbolic plane, the theta integral of `(W₁, W₁)` on the datum `χ⁻¹ ∘ det` is constant.
* `New.Exchange.RowColExchangeIdentity`: the two theta integrals are proportional on the standard
  data `New.stdRowDatum` and `New.stdColDatum`, with a condition on the size of the factor.
* `New.Exchange.IsPeriodIdentity`: the identity of periods over `[U W₁]` between real slices.
* `New.Exchange.exists_thetaLarge_eq_smul_of_isPeriodIdentity`,
  `New.Exchange.rowColExchangeIdentity_of_periods`: the identity for `V = V' ⊕ W₁`, where `X` is
  `W₁` plus a hyperbolic space, follows from an identity of periods over `[U W₁]`, for one character
  and for all characters, when `W₁` splits off a hyperbolic plane.

Notions from other files:
* `New.Space.integrated`: the bounded bilinear map (v, f) ↦ v ⊗ f = ∫ v(y) ϱ(y)f dy, for v in the
  Fock space, f in 𝒮(V), y over real vectors in Fock coordinates.
* `New.Exchange.IntegralFrame.stdDatum`: for a frame with blocks K, I, L and a function G, the
  function y ↦ G(y (K|I)) on integral y, and 0 elsewhere.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work.



## Terms of a standard datum at a point of the parabolic subgroup

`New.Exchange.namedVector` is the vector given by a function at the places A, read through π
(`New.Exchange.ReadsAt`), and the vacuum elsewhere. `New.Exchange.realSlice` is the slice of a real
datum for (X, V) at a point of Hom(isotropic frame, V), a real datum for (W₁, V).


### `thetaOnRealData`

 The functional v ↦ θ(ϱ(x) ω_{α,γ}(p) (v ⊗ F)) on real data v of the pair (W₁, V): the value of
the theta distribution θ at the Schwartz vector with real part v and
finite part given by a vector F, moved first by the Weil representation ω_{α,γ} = `pairWeil` with
characters α, γ at a point p of U(W₁) × U(V) and then by the Heisenberg translation ϱ by an adelic
matrix x. 

### `RepresentedBy.of_conjTranspose_mul_mul`

 If at every infinite place `qᴴ T q` has the form `yᴴ diag(t') y` for some matrix `y`
(`RepresentedBy`), with `q` invertible, then so has `T`. 

### `SlicesVanishOutside`

 The real slice of `v` along `D` vanishes at every adelic matrix `x` whose Gram matrix for the
standard form with signs `t` is not represented by the signs `t'` at the infinite places. 

### `coordMatrix_mul_fromBlocks_eq_fromCols`

 Let the splitting `D` write `X` as `W₁` plus the spans of two dual isotropic frames; `D.k` is
one of the frames and `D.i` the embedding of `W₁`, as matrices over `E`, and `D.kAdelic`,
`D.iAdelic` are the same in the standard coordinates over the adeles. The point
`p = n(c, z) m(q, g)` of the parabolic subgroup of `D` maps the span of `(k | i)` to itself: the
coordinates `p⁻¹ X.x⁻¹ (k | i)` at `p`, times a block triangular matrix, give
`(D.kAdelic | D.iAdelic)`. Here `X.x` and `W₁.x` carry the forms of `X` and `W₁` to the standard
forms. 

### `hasIntegrableTerms_localDatum_of_eq_stdDatum`

 Let D split X as W₁ plus a hyperbolic space with isotropic frame of size b. Let π map the finite
adeles onto the product `LocProd P` of the fields at a finite set P of places, reading the
components at the places A (`ReadsAt`), with O its subring of integral elements, and let (K I L) be
the image of the frame of D. Let v be a real Schwartz vector and
Φ(y) = ε 1_O(y) χ⁻¹(det (y (K|I) N)), for a number ε, a character χ and a fixed matrix N, be
Schwartz–Bruhat with support in a set Ω; here χ⁻¹ is `invOnUnits χ`, zero off the units of O. Then,
for any characters β, γ of the norm-one ideles in the Weil representation, the terms of the theta
kernel of v ⊗ Φ (vacuum at the other finite places) at n(c, z) m(q, g) are integrable over
[U(V)]. 

### `thetaTerm_localDatum_of_eq_stdDatum`

 Let π read the components at the places A, with O the integral elements of its target, let (K I
L) be the local frame adapted to D, and let Φ(y) = ε 1_O(y) χ⁻¹(det (y (K|I) N)), for a number ε, a
character χ and a fixed matrix N, be Schwartz–Bruhat with support in a set Ω; here χ⁻¹ is
`invOnUnits χ`, zero off the units of O. Let x' be the standard coordinates of a rational matrix x,
and x' q = `scaleIdele E` • Y, with `scaleIdele E` the normalising idele of the Weil data. Let υ be
the splitting Hecke character of the Weil data and `upsilonU1` its restriction to the norm-one
ideles, and put β' = β `upsilonU1`^b, where b is the size of the isotropic frame. At the point
(`D.radicalElement c z * D.levi (q, g)`, k), the term of x in the theta kernel of v ⊗ Φ with
characters β' and γ is the product of ψ(½ tr(z xᴴJx)) χ_V(det q)⁻¹ |det q|^(a/2), where J = `V.J` is
the form of V, a is the rank of V and χ_V = `γ.spaceChar a` is the Hecke character u ↦ γ(u/ū)
υ(u)^(-a);
* `vacuumFactor`, the non-zero constant in the formula for the slices of the vacuum, if y, the
finite part of k⁻¹Y, is integral, and 0 otherwise;
* `thetaOnRealData`, the theta functional θ(ϱ(translation) ω_{β,γ}(g, k) (· ⊗ finite vector)) of the
pair (W₁, V), at the translation x' cᴴ J_s (J_s the standard form of W₁), for the finite vector that
is the slice of Φ at y at the places A and the vacuum elsewhere (`namedVector`), evaluated at the
real slice of v at k⁻¹Y (`realSlice`: v restricted to the maps sending the isotropic frame `D.k` to
k⁻¹Y). 

### `centreCoeff_thetaIntegral_localDatum_eq_zero`

 Let `π` read the components at the places `A` (`ReadsAt`), with O the integral elements of its
target, let (K I L) be the local frame `adaptedFrame hπ D`, let `v` be a Schwartz vector, and let
`Φ(y) = ε 1_O(y) χ⁻¹(det (y (K|I) N))`, for a number `ε`, a character `χ` and a fixed matrix `N`, be
Schwartz–Bruhat with support in a set `Ω`. Suppose that the signs `t'` represent, at the real
places, the Gram matrix of every `x` with non-zero real slice of `v`, but do not represent `T`. Then
the Fourier coefficient at `j • T` of the theta integral of `v ⊗ Φ` vanishes at
`D.radicalElement c z * D.levi (q, g)`. Here `j` is the purely imaginary element of the Weil data,
and `centreCoeff T F p` is the mean of ψ(tr TM) F(z(M) p) over adelic matrices M modulo rational
ones, with z(M) in the centre of the unipotent radical. 

### `thetaTerm_eq_and_centreCoeff_eq_zero`

 Let D be an adapted splitting of X (signs r, indices m) over W₁ with isotropic frame of size b,
and V a space with signs t and rank a; `G E r`, `G E t` are their adelic unitary groups and
`PairFock E r t` the space of real data of the pair. Let π : 𝔸_f → `LocProd P` read the components
at the places A, with O the integral elements, let (K I L) be the local frame of D and χ a
multiplicative character of `LocProd P`. Let v be a Schwartz vector and let
Φ(y) = ε 1_O(y) χ⁻¹(det (y (K|I) N)), with a number ε and a fixed matrix N, be Schwartz–Bruhat with
support in a set Ω; here χ⁻¹ is `invOnUnits χ`, zero off the units of O. Put β' = β υ^b
(υ = `upsilonU1`), f = v ⊗ Φ and p = `D.radicalElement c z * D.levi (q, g)`; β', γ are the two
characters of the Weil representation of (X, V), and β, γ those left for (W₁, V).
(a) The terms of the theta kernel of f at p are integrable over [U(V)]; (b) with x' the standard
coordinates of x and x' q = `scaleIdele E` • Y, the term of x at k is ψ(½ tr(z xᴴJx)) χ_V(det q)⁻¹
|det q|^(a/2), χ_V = `γ.spaceChar a`, times `vacuumFactor` or 0 (as y, the finite part of k⁻¹Y, is
or is not integral), times the theta functional `thetaOnRealData` of (W₁, V) for the slice of Φ at y
with vacuum elsewhere (`namedVector`), evaluated at the real slice of v at k⁻¹Y; (c) if all x with
non-zero real slice have Gram matrix represented by the signs t' at the real places
(`SlicesVanishOutside`), and T is not, then the Fourier coefficient at `j • T` of the theta integral
of f vanishes at p (`j` is the purely imaginary element of the Weil data). 


## A product formula for the theta functional on real data


### `thetaOnRealData_boxProd_eq_mul`

 Take the pair (W₁, V' ⊕ W₁), the datum built from a vector f for (W₁, V') and a vector F for
(W₁, W₁), the translation (c; 0), the point (g, u ⊕ l) and a product φ ⊗ v of real data. Here
`New.Exchange.thetaOnRealData` sends a real datum to θ(ϱ(translation) ω(point) (real datum ⊗ finite
vector)), with θ the theta distribution, ϱ the Heisenberg translation and ω the Weil representation
with the two given characters. With characters α, αβ it is a product of two factors. The first is
`New.Exchange.thetaOnRealData` for (W₁, V') with characters α, β at f, c, (g, u), φ. The second is
the theta kernel `New.pairTheta` of (W₁, W₁) with characters α, α at (g, l), for the datum v ⊗ F. 


## Equal ranks, and the exchange identity for the large triple from an identity of periods

`[U W]` is the quotient of the adelic unitary group of `W` by its rational points. Integrals over it
are taken against the measure `W.quotMeasure`.


### `thetaLarge_eq_apply_one_of_even_rank`

 Equal ranks: let `W₁` have even rank and let the adapted splitting `D₁` split a hyperbolic plane
off `W₁`. For a tame character `𝔠`, the theta integral `thetaLarge` with both spaces equal to `W₁`,
on a real Schwartz vector `v` and the datum `χ⁻¹ ∘ det` at the ramified places
(`stdColDatum 𝔠.semilocalChar 1`), is constant on `U(W₁)`. 

### `equalRankThetaRatio`

 The squared absolute value at `1` of the theta integral `thetaLarge` of the pair `(X, X)`, for
the real vector `v` and the datum `χ⁻¹ ∘ det` on integral invertible matrices, divided by `L_*(e)`
with `e` half the rank of `X`, rounded down. Here `L_*(e) = lValueProdInt 𝔠 e` is
`∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2` for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`. 

### `RowColExchangeIdentity`

 The exchange identity for standard data. The real vectors `v` and `y` are Schwartz vectors (all
weighted norms finite), and there is a real `C` such that for every tame character `𝔠` of weight `μ`
some `c : ℂ` satisfies (a) `C * ‖c‖ ^ 2 = L_*(rk V - rk X / 2) * ℓ 𝔠`, with the half rounded down,
and (b) for all integral `z`, the theta integral of `(X, V)` on `v` and the row datum of `z` is `c`
times the theta integral of `(X, V')` on `y` and the column datum of `z`. Here
`L_*(e) = lValueProdInt 𝔠 e` is `∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2` for `e ≥ 0`,
`ν = 𝔠.character`, `S = 𝔠.ramifiedPlaces`, and `L_*(-e) = L_*(e)⁻¹`. The row datum sends `x` to
`χ⁻¹ ∘ det` of the matrix with the rows of `z` and `x`, ordered by `σ`; the column datum sends `x`
to `χ⁻¹ (det (z x))`; both vanish unless `x` is integral and the determinant is a unit. No sign is
asked of `C`; by (a) it is positive as soon as `ℓ 𝔠 > 0` for one `𝔠`. 

### `mem_map_sum_iff_fixes_cols`

 The image in `U(V' ⊕ W₁)` of the group `W₁.Γ` of rational points of the second summand consists
of the rational points of the sum that fix the first block of columns `(1; 0)`. 

### `map_snd_adeleMatrix_inv_mul`

 The finite part of `k⁻¹ Y` is the inverse of the finite component of `k` times the finite part
of `Y`. 

### `exists_blockSumOne_mul_mem_stdLevel`

 Let `Y k` be unitary at the finite places, with `k` in `GL_b(Ô E)`. Suppose that the finite part
of the inverse of `(y ⊕ y') (h, u)` maps the columns `(Y, 0)` to integral ones. Then some block
diagonal translate of `u` lies in `stdLevel`, the stabiliser of the standard lattice. 

### `namedVector_det_fromCols_eq_boxProd`

 Let `x` in `GL_b(𝔸_f)` have integral entries. The vector of `𝒮(Hom(W₁, V' ⊕ W₁))` given at the
places `𝔠.ramifiedPlaces` by `y ↦ ε χ⁻¹(det ((x; 0) | y))` on integral `y` is `ε χ⁻¹(det x)` times
the product of the vacuum of `(W₁, V')` with the vector of the datum `χ⁻¹ ∘ det` of `(W₁, W₁)`. Here
`χ⁻¹` is `invOnUnits 𝔠.semilocalChar`, which vanishes off the units of `O`. 

### `namedVector_det_star_eq_vacElem`

 For `x` in `GL_b(𝔸f E)`, the vector named at the conjugates of the places `𝔠.ramifiedPlaces` by
the constant `χ⁻¹ (det x̄)` on integral matrices is that constant times the vacuum of `Hom(W₁, V')`.
This is the finite slice of the datum of the small side. 

### `det_mem_idelesUnitOff_of_mul_mem`

 If `x` is integral and `x * k` is unitary for some `k` in `GL_b(Ô E)`, then `det x` is a unit at
every finite place. 

### `stdColDatum_transpose_eq_stdDatum`

 Let `𝔠` be a tame character, `χ` its component `semilocalChar` on the product `LocProd` of the
fields at its ramified places, read by `readsAt` there and by `readsAt.star`, through conjugation,
at the conjugate places. Let `D` be an adapted splitting; `adaptedFrame` is the image of its frames
(K I L) at these places, with `dualL` the L-block of the dual frame. Then the transpose of
`y ↦ χ⁻¹ (det (dualL y))` on integral `y` equals the datum `stdDatum` of the conjugate frame:
integral `y ↦ χ⁻¹ ∘ det` of the first block of columns of `y (K|I)`. 

### `gram_sum_fromRows_one_zero`

 The first block of columns of `V' ⊕ W₁` has Gram matrix the form of `V'`. 

### `thetaTerm_stdRowDatum_mul_of_mem_stdLevel`

 Let `𝔠` be a tame character, `χ` its component `semilocalChar` at the places `𝔠.ramifiedPlaces`,
read through `𝔠.readsAt`. Let the splitting `D` split `X` as `W₁` plus a hyperbolic space, and let
`σ` order the rows of a square matrix made of `b` and `a` rows. Unfolded along `D`, the theta kernel
of `(X, V)` has one term `thetaTerm` for each rational matrix `x`, a function of `P` in `G E r` and
`k` in `G E t`. Take the characters `rankTwist 𝔠.character⁻¹ m = ν⁻¹ υ ^ ⌊rk X / 2⌋`
(`ν = 𝔠.character`, `υ` the splitting character of the Weil data) and any `γ`, and the datum
(`localDatum`) with real part `v` in the Fock space `PairFock`, the row datum `stdRowDatum` of an
integral matrix `z₀` at the ramified places, and the vacuum elsewhere. Then the term does not change
when `k` is multiplied on the right by a finite point `u` in `stdLevel`, the stabiliser of the
standard lattice. 

### `thetaTerm_stdRowDatum_eq`

 The term at the rational matrix `(1; 0)` of the theta kernel of `(X, V' ⊕ W₁)` for the row
datum, assumed to be `ε` times the standard datum of the frame adapted to `D`. Let
`q = scaleIdele • V'.x * Y` and `γ = ν⁻¹ υ ^ ⌊rk X / 2⌋` (`rankTwist`, with `ν = 𝔠.character` and
`υ` the splitting character of the Weil data), and let `a` be the rank `card (b ⊕ n)` of `V' ⊕ W₁`.
At `(radicalElement c z * levi (q, g), k)`, whose first entry is the point n(c, z) m(q, g) of the
parabolic subgroup, the term is the product of
* `ψ(½ tr(z V'.J)) (γ.spaceChar a)(det q)⁻¹ |det q| ^ (a / 2)`;
* `vacuumFactor` if the finite part `y` of `k⁻¹ (Y; 0)` is integral at all finite places, and `0`
  otherwise;
* `thetaOnRealData`, the theta functional of `(W₁, V' ⊕ W₁)` for the finite slice of the datum at
  `y` with vacuum elsewhere (`namedVector`), moved by `(g, k)` and the translation by
  `(V'.x⁻¹; 0) cᴴ J_s`, evaluated at the real slice of `v` at `k⁻¹ (Y; 0)`. 

### `thetaTerm_stdColDatum_eq`

 The term at `1` of the small theta kernel, that of `(X, V')`. Its datum is the standard column
datum of the frame adapted to `D`, transposed, as `V'` indexes rows here, and read at the conjugates
of the ramified places through conjugation (`readsAt.star`). Let `q = scaleIdele E • V'.x * Y`, with
`scaleIdele E` the normalising idele of the Weil data. Let `υ` be the splitting Hecke character of
the Weil data and `upsilonU1` its restriction to the norm-one ideles, so that
`rankTwist ν m = ν upsilonU1 ^ ⌊card m / 2⌋`, and put `γ = upsilonU1 ^ b` with `b` the rank of `V'`.
The term at `(radicalElement c z * levi (q, g), k)` is the product of
* `ψ(½ tr(z V'.J)) χ_{V'}(det q)⁻¹ |det q| ^ (b / 2)`, where `χ_{V'} = γ.spaceChar b` is the Hecke
  character `u ↦ γ(u / ū) υ(u) ^ (-b)`;
* `vacuumFactor`, the non-zero constant in the formula for the slices of the vacuum, or `0`, as the
  finite part `y` of `k⁻¹ Y` is integral or not; `thetaOnRealData`, the theta functional of
  `(W₁, V')` moved by `(g, k)` and by the translation `V'.x⁻¹ cᴴ J_s`, for the finite slice of the
  datum at `y` with vacuum elsewhere (`namedVector`; on the slice variable `y₂` it is constant where
  `y₂` is integral), evaluated at the real slice of `v'` at `k⁻¹ Y`. 

### `infiniteDet`

 The determinant of `B` read at the infinite places. 

### `infiniteDet_apply`

 The component of `infiniteDet B` at `w` is the determinant of the component of `B` at `w`. 

### `det_eq_realIdele_mul_finIdeleIncl`

 The determinant of an adelic matrix `B` is the product of its part at the infinite places and
the determinant of the finite part `x` of `B`. 

### `IsPeriodIdentity`

 The identity of periods over `[U W₁]` for a tame character `𝔠` of weight `μ` (an integer for
each infinite place) and real data `v` of `(X, V' ⊕ W₁)` and `v'` of `(X, V')`, with weight function
`ρ` and period `I₀`. For each real point `h` there is `p` in `U V' × U W₁` with the following
property for all invertible `B`, characters `β`, vectors `f`, matrices `x` and points `g`, `y`. Take
the slice of `v` at `(p h)⁻¹ (B, 0)`, where `p` is read at the infinite places, and move it by `p h`
in the real Weil representation `realPairWeil`, in which `p h` acts by its Fock operator times
`∏_w det ^ (⌊n / 2⌋ - μ w)`. Integrate over `u ∈ [U W₁]` its theta functional for the vector
`f ⊠ (χ⁻¹ ∘ det)` at `(x, 0)` and `(g, y ⊕ u)`, with characters `γ` and `γ β`. The result is
`ρ h * I₀ / (ν(z / z̄) |z|^(n/2))` times the theta functional for `f` at `x` and `(g, y)`, with
characters `γ` and `β`, of the slice of `v'` at `B`. Here `z` is the idele equal to `det B` at the
infinite places and to `1` at the finite places, `ν` is `𝔠.character`, `n` is the rank of `W₁`, and
`γ = rankTwist ν⁻¹ n` is `ν⁻¹ υ ^ ⌊n / 2⌋` with `υ` the splitting character of the Weil data. 

### `thetaOnRealData_smul`

 `thetaOnRealData` is homogeneous in the vector `F`. 

### `thetaOnRealData_mul_real`

 Let `𝔠` be a tame character of weight `μ`, `ν = 𝔠.character` and `υ` the splitting character of
the Weil data; write `n` also for the rank of `W₁`. The functional `thetaOnRealData` sends a real
datum `φ` in the Fock space `PairFock` of `(W₁, V)` to `θ(ϱ(x) ω(g, k) (φ ⊗ F))`. Here `θ` is the
theta distribution, `ϱ` the Heisenberg translation by `x`, and `ω` the Weil representation of the
pair with characters `rankTwist 𝔠.character⁻¹ n = ν⁻¹ υ ^ ⌊n / 2⌋` and `γ`. For `w ∈ GInf`, a point
of the unitary group at the infinite places, let `(w, 1)` be the point of `G E t` equal to `w` at
the infinite places and to `1` at the finite places. Multiplying `k` on the right by `(w, 1)` has
the same effect as moving `φ` by `w` in the real Weil representation `realPairWeil`. There `w` acts
by its Fock operator times `∏_τ det (w τ) ^ (⌊n / 2⌋ - μ τ)`. 

### `adeleMatrix_inv_sum_mul_mul_fromRows`

 The inverse of `(y ⊕ y') k` maps the columns `(Y, 0)` to `k⁻¹ (y⁻¹ Y, 0)`. 

### `exists_integral_thetaTerm_eq_of_periods`

 Let `D` split `X` as `W₁`, of even rank `n`, plus a hyperbolic space, let `lFrame` be the
L-block of the dual frame at the ramified places of `𝔠`, and let
`p = radicalElement c z * levi (q, g)` with `q = scaleIdele • V'.x * Y`, where the finite part of
`Y` times some `k ∈ GL_b(Ô E)` (`intGL`) is in the unitary group `U 1` of the form `1`. Let
`IsPeriodIdentity` hold: at every real point, the integral over `[U W₁]` (for `quotMeasure`) of the
theta functional of the moved slice of `v` is the weight `ρ` times the period `I₀`, divided by
`ν(ζ / ζ̄) |ζ| ^ (n / 2)` for the infinite part `ζ` of a determinant, times that of the slice of
`v'`; here `ν = 𝔠.character`. Let the row datum of `lFrame` be `ε` times the standard datum of the
frame. For a point `(gInf, u)` of `U (V' ⊕ W₁)` there is `k'` in `U V' × U W₁` such that the term at
`(1; 0)` of the large theta kernel at `p`, integrated over the translates of `k' (gInf, u)` by
`U V' × [U W₁]`, equals `ρ gInf * (κ₀ ε ν(d₀ / d̄₀) I₀)` times the integral over `U V'` of the term
at `1` of the small theta kernel; it is zero if no block diagonal translate `blockSumOne u₀ * u`
lies in `stdLevel`. The constants `d₀` and `κ₀` depend only on the spaces and `D`. 

### `hasIntegrableTerms_and_centreCoeff_thetaLarge_eq_zero`

 Let `D` split `X` as `W₁` plus a hyperbolic space, let `𝔠` be a tame character, let `v` be a
Schwartz vector in the real (Fock) data `PairFock` of `(X, V' ⊕ W₁)`, and take the row datum
`stdRowDatum` of the L-block of the dual frame of `D` at the ramified places of `𝔠`. At the point
`radicalElement c z * levi (q, g)` of the parabolic subgroup, (a) the terms of the large theta
kernel, that of `(X, V' ⊕ W₁)`, are integrable, and (b) the Fourier coefficient of `thetaLarge` at
`j • T`, with `j` the purely imaginary element of the Weil data, vanishes under two conditions: `T`
is not of the form `yᴴ diag(t') y` at some infinite place (`¬RepresentedBy`), while the Gram matrix
of every `x` at which the real slice of `v` is non-zero has this form at all infinite places. 

### `hasIntegrableTerms_and_centreCoeff_thetaSmall_eq_zero`

 Let `D` split `X` as `W₁` plus a hyperbolic space, `V'` have rank `b` and signs `t'`, and `𝔠` be
a tame character. Let `v'` be a Schwartz vector in the real (Fock) data `PairFock` of `(X, V')` and
take the column datum `stdColDatum` for the L-block `l` of the dual frame of `D`, used at the
conjugates of the ramified places. At the point `radicalElement c z * levi (q, g)`, (a) the terms of
the small theta kernel, that of `(X, V')`, are integrable, and (b) the Fourier coefficient of
`thetaSmall` at `j • T`, with `j` the purely imaginary element of the Weil data, vanishes if the
signs `t'` do not represent `T` at the infinite places. 

### `exists_centreCoeff_eq_mul_of_isPeriodIdentity`

 Let the adapted splitting `D` split `X` as `W₁`, of even rank, plus a hyperbolic space, and let
`σ' : b ⊕ b ⊕ n ≃ m` order the rows of a row datum. Let `v`, `v'` be Schwartz vectors in the real
(Fock) data `PairFock` of `(X, V' ⊕ W₁)`, `(X, V')` and let `ρ ≥ 0` be nonzero near `1`. The real
class of `V'` consists of the matrices of the form `yᴴ diag(t') y` at every infinite place
(`RepresentedBy t'`). Suppose that the real slices of `v` vanish at the points with Gram matrix
outside this class, or that `t' = -1` and the signs `s` contain a `1` with at most half of them
(`negCount`) equal to `-1`. Then there is `K > 0` such that, for every tame character `𝔠` of weight
`μ` (`SplitTameChar`), if `IsPeriodIdentity` holds with weight `ρ` and period `I₀`, there is a
number `C` with `‖C‖ = K * ‖I₀‖` and the following property. At the point
`radicalElement c z * levi (q, g)` the Fourier coefficient at `j • T` of `thetaLarge`, the theta
integral of `(X, V' ⊕ W₁)` on `v` and the row datum `stdRowDatum σ'` of the frame
`(adaptedFrame 𝔠.readsAt D).dualL`, is `C` times that of `thetaSmall`, the one of `(X, V')` on `v'`
and the column datum `stdColDatum` of that frame, if `(T, q)` is a test pair for `V'`: (a) `T` is
the form of `V'` and `q` is `scaleIdele E` times a basis of a lattice that is self-dual for `T`, or
(b) `T` is invertible and outside the real class of `V'`. 

### `exists_thetaLarge_eq_smul_of_isPeriodIdentity`

 Let `D` split `X` as `W₁` plus a hyperbolic space, where `W₁` has even rank, and let `D₁` split
`W₁` as `W` plus a hyperbolic plane. Let both splittings be adapted. Let `v`, `v'` be Schwartz
vectors in the real (Fock) data `PairFock` of `(X, V' ⊕ W₁)`, `(X, V')` and let `ρ ≥ 0` be nonzero
near `1`. Suppose that the real slices of `v` vanish at the points whose Gram matrix is not
represented by the signs `t'` of `V'`, or that `t' = -1` and the signs `s` of `W₁` contain a `1`
with at most half of them equal to `-1`. Then there is `K > 0` such that for every tame character
`𝔠` of weight `μ`, if `IsPeriodIdentity` holds with weight `ρ` and period `I₀`, then there is a
number `C` with `‖C‖ = K * ‖I₀‖` such that for every integral `z` at the ramified places the theta
integral `thetaLarge` of `(X, V' ⊕ W₁)` on `v` and the row datum `stdRowDatum σ' χ z` (`χ⁻¹ ∘ det`
of the rows of `z` and the variable, ordered by `σ'`, where `χ = 𝔠.semilocalChar`) is `C` times the
theta integral `thetaSmall` of `(X, V')` on `v'` and the column datum `x ↦ χ⁻¹ (det (z x))`. 

### `rowColExchangeIdentity_of_periods`

 Let the adapted splittings `D` and `D₁` split `X` as `W₁` plus a hyperbolic space and `W₁`, of
even rank, as `W` plus a hyperbolic plane. Let `V = V' ⊕ W₁`, let `v`, `v'` be Schwartz vectors in
the real (Fock) data `PairFock` of `(X, V)`, `(X, V')`, and let `ρ ≥ 0` be nonzero near `1`. Suppose
(a): for every tame character `𝔠` of weight `μ`, `IsPeriodIdentity` holds with weight `ρ` and period
`period 𝔠`. Suppose (b): either the real slices of `v` vanish at the points whose Gram matrix is not
represented by the signs `t'` of `V'`, or `t' = -1` and the signs `s` of `W₁` contain a `1` with at
most half of them equal to `-1`. Then `RowColExchangeIdentity` holds with
`ℓ 𝔠 = ‖period 𝔠‖ ^ 2 / L_*(n / 2)`: there is a real `C` such that for every `𝔠` some `c : ℂ` has
`C * ‖c‖ ^ 2 = L_*(rk V - rk X / 2) * ℓ 𝔠` and, for all integral `z`, the theta integral
`thetaLarge` of `(X, V)` on `v` and the row datum of `z` is `c` times the theta integral
`thetaSmall` of `(X, V')` on `v'` and the column datum `x ↦ χ⁻¹ (det (z x))`. Here `n` is the rank
of `W₁` and `L_*(e) = lValueProdInt 𝔠 e` is `∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2`
for `ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`. 
