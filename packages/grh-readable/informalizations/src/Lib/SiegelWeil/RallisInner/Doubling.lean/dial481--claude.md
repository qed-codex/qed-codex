---
{
  "module": "src/Lib/SiegelWeil/RallisInner/Doubling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/RallisInner/Doubling.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/RallisInner/Doubling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Doubling: clean data, the doubling identity and the inner product formula

This file defines the doubled datum `New.SiegelWeil.doubleDatum` on `Hom(S ⊕ S⁻, T)`, clean data
(`New.SiegelWeil.IsClean`) and sharp data (`New.SiegelWeil.IsSharp`), for hermitian spaces `S`,
`T` of ranks `n`, `m`. It applies Siegel–Weil to `S ⊕ S⁻` to prove the doubling identity for
`2 n < m`. It then integrates that identity to the inner product formula before the choice of a
sharp datum. It also computes the coefficient of a vacuum at points supported above a set of
places (`New.SiegelWeil.weilMatrixCoeff_mul`) and constructs an integral isotropic frame.
Conventions: `New.G E s` is the adelic unitary group, a pair of an archimedean and a finite part;
`New.pairWeil S T a b` is the twisted Weil representation of `U(S) × U(T)` on the data
`𝒮 (S.hom T)`, with inner product `New.Space.dataInner`; `New.localLevel n A` consists of the
finite points that are integral at the places of `A`, and `New.stdLevel E n` of those integral at
all places, the stabiliser of `Ô ^ n`.

## Main definitions and results

* `New.SiegelWeil.integral_conj_theta_mul_theta`: the doubling identity for `2 n < m`:
  apply Siegel–Weil (`New.SiegelWeil.siegel_weil`) to `S ⊕ S⁻`; for a clean datum
  (`New.SiegelWeil.IsClean`) only the Lagrangians that are graphs of isometries contribute
  (`New.SiegelWeil.exists_graph_eq_of_zeroTerm_ne_zero`, `New.SiegelWeil.zeroTerm_graphSplitting`).
* `New.SiegelWeil.inner_product_formula`: Rallis' inner product formula, obtained by integrating
  the doubling identity against two functions on `[U(S)]`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by signs s, a matrix J over E and x in GL_n(𝔸)
  with xᴴJx equal to diag(s) at the infinite places and 1 at the finite places.
* `New.SiegelWeil.Lagrangian.zeroTerm`: the term of a Lagrangian L in the Siegel–Weil formula, the
  value at 0 in the Schrödinger model of a complete splitting along L.
* `New.Space.projOn`: the mean of the finite Heisenberg operators of the integral vectors above a
  set A of places and its conjugate; the data that it fixes are the vacua above A.

## Relation to the literature

Rallis inner product formula by doubling. Here only Weil's range is treated, with forms that are
rapidly decreasing rather than cuspidal. The boundary orbits are removed by the test datum. Source:
S. Rallis, L-functions and the oscillator representation, LNM 1245 (1987); J.-S. Li, Crelle 428
(1992); the unitary unfolding is written out in Y. Liu (2011) Prop 2.3 and
Eischen–Harris–Li–Skinner 4.1.4.


### `negSourceFactor`

 A chosen number `c` of modulus one with `θ (c • conj f) = conj (θ f)` for all data `f` on
`Hom(S, T)`, where `conj f = negSource.map f` is the transport of `f` to `Hom(S⁻, T)`; see
`norm_negSourceFactor` and `theta_negSourceFactor_smul`. 

### `theta_negSourceFactor_smul`

 The theta functional of `S⁻, T` at the transport of `f`, multiplied by `negSourceFactor S T`,
is the complex conjugate of the theta functional of `S, T` at `f`. 

### `doubleDatum`

 The doubling map sending `(f', f)` to the datum `f ⊠ c • conj f'` on `Hom(S ⊕ S⁻, T)`,
conjugate-linear in `f'` and linear in `f`. Here `conj f' = negSource.map f'` is the transport of
`f'` to `Hom(S⁻, T)`, and `c = negSourceFactor S T`, so that `θ (c • conj f') = conj (θ f')`. 

### `graphSplitting`

 For a rational isometry `δ` of `S`, the splitting of `S ⊕ S⁻` into hyperbolic planes whose
Lagrangian is the graph `{(δ y, -y)}`; the dual frame spans `{(δ y, y)}`. Here `k` is the isotropic
frame, `l` the dual frame (`lᴴ J k = 1`), and the anisotropic part `i` is empty. 

### `cosetTerm`

 The term `ρ(g) ⟨y', g y⟩` of a coset `γ` of the finite points integral at `A`. Here
`g = cosetRep γ` is the representative of `γ` supported above `A` and its conjugate,
`ρ = vacuumCoeff M b`, and `y'`, `y` are forms of type `e` on `S`, on which `g` acts by right
translation. 

### `weilMatrixCoeff`

 The matrix coefficient `g ↦ ⟨f', ω(g, 1) f⟩` of the twisted Weil representation
`ω = pairWeil S T 1 b`. The argument `f'` defaults to `f`: `weilMatrixCoeff b f` is the function
`g ↦ weilMatrixCoeff b f f g`. 

### `IsClean`

 The datum `F` is clean: (a) all signs of `S` agree, or (b) `F` is a datum
`Ψ ⊗ f = (S.hom T).schrodingerOp A Ψ f`, where `A` is a set of places disjoint from its conjugate,
`Ψ` is Schwartz–Bruhat above `A`, and at some place `w` every matrix `y` with `Ψ y ≠ 0` has a left
inverse. In both cases the only Lagrangians with a nonzero term are graphs
(`New.SiegelWeil.exists_graph_eq_of_zeroTerm_ne_zero`). 

### `IsSharp`

 The datum `F` of the finite part is sharp for the level `J` off `S₀`. With `K₀ = stdLevel E n`
the stabiliser of `Ô ^ n`, at the finite points `g` integral off `S₀` the coefficient `⟨F, ω(g) F⟩`
equals `⟨F, F⟩` if `g ∈ J ∩ K₀` and is zero otherwise, and the quotient of `⟨F, F⟩` by the index
`[K₀ : J ∩ K₀]` is the constant `c`. Also `⟨F, F⟩ ≠ 0`, and for each vector `v` of the Fock model
the datum `v ⊗ F = integrated (S.hom T) v F` is clean and a vacuum off `S₀`. The datum `Ψ ⊗ vac` of
a sharp function `Ψ` modulo `𝔪` has these properties if `𝔪 ≠ (1)` or all signs of `S` agree
(`New.SiegelWeil.IsSharpFn.isSharp`). 

### `IsSharp.self_ne_zero`

 The inner product `⟨F, F⟩` is not zero. 

### `IsSharp.mem_finitePart`

 The datum `F` lies in the finite part, the span of the finite translates of the vacuum. 

### `IsSharp.vacuum_off`

 For every `v`, the datum `v ⊗ F` is a vacuum above any set `A` of places disjoint from
  `S₀`. 

### `IsSharp.weilMatrixCoeff_eq`

 At the finite points `g` integral off `S₀`, the coefficient `⟨F, ω(g) F⟩` is `⟨F, F⟩` on
  `J ∩ stdLevel E n` and zero elsewhere. 

### `IsSharp.mass_eq`

 The quotient of `⟨F, F⟩` by the index `stdLevelIndex J = [K₀ : J ∩ K₀]` is `c`. 

### `IsSharp.clean`

 For every `v`, the datum `v ⊗ F` is clean (`IsClean`). 

### `theta_doubleDatum`

 The theta functional of `S ⊕ S⁻, T` at the doubled datum is `conj (θ f') * θ f`. 

### `rho_fromCols_boxProd`

 The Heisenberg operator of a map on `S ⊕ S⁻` with blocks `X`, `Y` moves the first factor of
`f ⊠ f'` by `X` and the second by `Y`. 

### `doubleDatum_apply_fromCols`

 The value of the doubled datum `doubleDatum f' f` at a map on `S ⊕ S⁻` with blocks `X`, `Y` is
the value of `f` at `X` times the conjugate value of `f'` at `u⁻¹ Y`. Here `u = normNegOneIdele E`
is the idele by which the point of `S⁻` differs from the point of `S`. 

### `rho_fromCols_zero_doubleDatum`

 The Heisenberg operator of a map on `S ⊕ S⁻` that vanishes on `S⁻` moves only the factor `f` of
`doubleDatum f' f`. 

### `zeroTerm_graphSplitting`

 For a rational isometry `δ` of `S`, the zero term of the Siegel–Weil formula along the graph of
`δ`, taken at the doubled datum `doubleDatum f' f`, is the matrix coefficient `⟨f', ω(δ⁻¹, 1) f⟩`
of the Weil representation `ω = pairWeil S T 1 b` twisted by the character `b`. 

### `zeroTerm_doubleDatum_rho`

 Let the isotropic frame of a complete splitting `D` of `S ⊕ S⁻` have blocks `K` (in `S`) and
`K'` (in `S⁻`), and let `K' c = 0`, so that the columns of `K c` are vectors of `S` in the
Lagrangian of `D`. Then the zero term at `doubleDatum f' f` does not change when `f` is moved by the
Heisenberg operator of `X⁻¹ Z Yᴴ ε`, where `Z` is any adelic matrix, `X` is the dual frame of `T`,
`Y` holds the adelic coordinates of `K c` and `ε` is the standard form. 

### `pairWeil_rho_shiftMatrix`

 Moving the Heisenberg operator of `shiftMatrix s X Y *ᵥ z = X z Yᴴ ε` (`ε` the standard form)
through the Weil operator `pairWeil S T a b (g, 1)` turns the adelic coordinates
`Y = S.coordMatrix g c` of a rational matrix `c` at `g` into its coordinates at `1`. 

### `mul_eq_zero_of_zeroTerm_ne_zero`

 Let `f` be a clean datum (`IsClean`), and let the isotropic frame of a complete splitting `D` of
`S ⊕ S⁻` have blocks `K` (in `S`) and `K'` (in `S⁻`). If the zero term along the Lagrangian of `D`
is not zero at the doubled datum of `f'` and `ω(g, 1) f`, where `ω = pairWeil S T a b`, then the
Lagrangian contains no nonzero vector of `S`: `K' c = 0` forces `K c = 0`. 

### `exists_graph_eq_of_zeroTerm_ne_zero`

 Let `f` be a clean datum (`IsClean`) and `L` a Lagrangian of `S ⊕ S⁻`. If the term of `L` in the
Siegel–Weil formula is not zero at the doubled datum of `f'` and `ω(g, 1) f`, where
`ω = pairWeil S T a b`, then `L` is the graph of a rational isometry of `S`. 

### `graphSplitting_lagrangian_injective`

 Distinct isometries `δ` of `S` have distinct graphs, so `δ ↦ (graphSplitting S δ⁻¹).lagrangian`
is injective. 

### `theta_splitWeil_doubleDatum`

 For spaces `S`, `T` with data `f`, `f'`, the conjugate theta kernel of `f'` at
`(g', x)` times the theta kernel of `f` at `(g, x)` is the theta kernel of the pair `S ⊕ S⁻, T` at
`x`, acting by `splitWeil`, and the doubled datum `doubleDatum` of `ω(g', 1) f'` and `ω(g, 1) f`.
Here `θ` is the theta functional and `ω` is `pairWeil` with characters `a`, `b`; at a point `(g, 1)`
the character `a` does not matter and is taken to be `1`. 

### `zeroTerm_graphSplitting_doubleDatum`

 For a rational isometry `δ` of `S`, the zero term of the Lagrangian `{(δ⁻¹ y, -y)}` of
`S ⊕ S⁻`, at the doubled datum of `ω(g', 1) f'` and `ω(g, 1) f`, is the matrix coefficient
`⟨f', ω(g'⁻¹ δ g, 1) f⟩`. 

### `integral_conj_theta_mul_theta`

 Doubling. Let `T` have rank `m`, `S` rank `n`, with `2 n < m`, and let the datum `f` be clean
(`IsClean`: only graphs of isometries have nonzero terms). The integral over `[U(T)]` of the theta
kernel of `f` at `g` times the conjugate kernel of any datum `f'` at `g'` is the volume of `[U(T)]`
times the sum over the rational points `γ` of `U(S)` of `⟨f', ω(g'⁻¹ γ g) f⟩`. 

### `exists_doubling_bound`

 Let the rank of `T` exceed twice that of `S`. There is a finite constant `C` such that, with
absolute values inside, both sides of the doubling identity (the integral of the product of two
theta kernels over `[U(T)]` and the sum of matrix coefficients over the rational points of `U(S)`)
are at most `C ‖ω(g') f'‖ ‖ω(g) f‖`. 

### `exists_doubling_le_height`

 Let the rank of `T` exceed twice that of `S`. For any data `f`, `f'`, both sides of the doubling
identity, with absolute values inside (the integral over `[U(T)]` and the sum over the rational
points of `U(S)`), are at most a finite constant times a common power of the heights `S.height`
of `g` and `g'`. 

### `measurePreserving_quotMeasure_unfold`

 Unfolding: `((g', g), γ) ↦ (g', g'⁻¹ * (γ * g))` carries the measure of
`[U(S)] × [U(S)] × Γ` (counting measure on the rational points `Γ`) to that of
`[U(S)] × U(S)(𝔸)`. 

### `enorm_mul_height_pow_le`

 If `‖y g‖ * height g ^ l ≤ B` and `‖y' g‖ * height g ^ l ≤ B'` for all `g`, then a constant `C`
times the two powers of the heights, weighted by `‖y' g'‖ * ‖y g‖`, is at most `C B' B`. 

### `inner_product_formula`

 The inner product formula before the choice of a sharp datum. Let `2 n < m` for the ranks of
`S`, `T`, let `f` be clean (`IsClean`) and `f'` any datum (by default `f`); `a`, `b` are the
characters that twist the Weil representation `ω`. For automorphic `y`, `y'` of rapid decay
(`rapidFunctions`), the Petersson product of the theta lifts `⟨Θ_{f'} y', Θ_f y⟩` (`lift`,
`petersson`) is the volume of `[U(T)]` times `∫ ⟨f', ω(g) f⟩ ⟨y', R(g) y⟩ dg` over the adelic
points of `U(S)`, with `⟨f', ω(g) f⟩ = weilMatrixCoeff b f f' g` and `R` the right translation,
and this integral converges absolutely. 

 ### The coefficient of the vacuum 

### `weilMatrixCoeff_mul`

 Let `f` be a vacuum above `A` (fixed by `projOn` at `A`), let the finite point `γ` be supported
on `A` and its conjugate, and let `g` be integral at `A`. Then `⟨f, ω(γ g, 1) f⟩` is
`⟨f, ω(g, 1) f⟩` times the vacuum coefficient `vacuumCoeff (card m) b γ`, the inverse of the product
of `b (det γ)` and the `card m`-th power of the multiplier of `γ`. 

 ### An integral isotropic frame 

### `exists_integral_isotropic_frame`

 If `2 n ≤ m` for the cardinalities of `n` and `m`, there is an `m × n` matrix `x` over the
integral adeles `Ô E` with `xᴴ x = 0` (an integral isotropic frame), some `n` of whose rows form the
identity matrix. 
