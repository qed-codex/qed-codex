---
{
  "module": "src/Lib/SiegelWeil/Tower/LargeSideConstantTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LargeSideConstantTerm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/LargeSideConstantTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Removing a plane: the constant term on the side of the large space

Let `W' = W ⊕ H` and `V' = V ⊕ H` be hermitian spaces over the CM field `E`, with `H` a hyperbolic
plane and `W` of even rank. On standard data, the constant term of the theta integral of `(W', V')`
along the new isotropic line of `W'` unfolds to Tate's integral `𝒵(e + 1)`, `e = rk V - rk W / 2`,
for the base change of the character.

Neither side of Poisson's formula on the line has a term at `0`, so `𝒵` is analytic on the real
line. For `x ≥ 1` its value is, up to an explicit factor, `L(x)` times the theta integral of
`(W, V)` at a cone integral (`New.Exchange.exists_zetaIntegral`). This gives the constant term for
`e ≥ 0` (`New.Exchange.exists_planeConstantTerm_eq_thetaLarge_cone`) and, through the other side of
Poisson's formula, for `e < 0` (`New.Exchange.exists_planeConstantTerm_eq_thetaLarge_dualCone`).

## Main definitions and results

* `New.Exchange.exists_planeConstantTerm_eq_thetaLarge_cone`: for `z = rk V - rk W / 2 ≥ 0`, with
  `rk W = card n` even, a Schwartz vector `v'` and integral `y`, the constant term along `A` of the
  theta integral of `(W', V')` is `γ` times the theta integral of `(W, V)` on
  `cone A X μ (z + 1) v'` and `stdRowDatum σ 𝔠.semilocalChar y`.
* `New.Exchange.exists_planeConstantTerm_eq_thetaLarge_dualCone`: the same for
  `rk V - rk W / 2 = -z - 1 < 0`, at `u = 1`, with `dualCone A X μ (z + 1) v'` in place of the cone.

Notions from other files:
* `𝔠 : SplitTameChar E μ` is a character `𝔠.character` of `[U(1)]` of positive weight `μ`, tamely
  ramified exactly on a finite set `𝔠.ramifiedPlaces` of places disjoint from its conjugate;
  `𝔠.semilocalChar` is `t ↦ ν(t / t̄)`, for `ν = 𝔠.character`, on the product
  `LocProd 𝔠.ramifiedPlaces` of the completions at `𝔠.ramifiedPlaces`.
* `A : W'.Splitting W Unit` is a decomposition `W' = W ⊕ H`; it is `IsBaseAdapted` if its frames are
  orthonormal at the infinite places and integral at the finite places.
* `localDatum W V v Φ 𝔠.readsAt` is the datum on `Hom(W, V)` with real part `v`, the function `Φ` at
  the places of `𝔠.ramifiedPlaces` and the vacuum elsewhere; `thetaLarge W V 𝔠 v Φ` is its theta
  integral over `[U(V)]`.
* `stdRowDatum σ χ y` sends `x` to `χ⁻¹` of the determinant of the matrix with the rows of `y` and
  `x` if that matrix is integral with integral inverse, and to `0` otherwise.
* `New.Exchange.lSharp` (from `Lib.SiegelWeil.Tower.FiniteTateIntegral`) is
  `L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` for `ν = 𝔠.character`, `S = 𝔠.ramifiedPlaces`.

## Relation to the literature

Known result: the tower property for the constant term of a theta lift along an isotropic line. In
the literature the lifted form is cuspidal, whereas here it is a character, the data are ramified,
and the isotropic orbit survives as a Tate integral. The constant term is therefore the smaller lift
times a factor whose size is given by a Hecke L-value. Source: S. Rallis, On the Howe duality
conjecture, Compositio Math. 51 (1984), Thm I.1.1; for the unitary case, C. Wu, Irreducibility of
theta lifting for unitary groups, J. Number Theory 133 (2013), Prop. 3.1.


 ### The standard data of a pair with one more plane 

### `rankTwist_eq_mul_of_splitting`

 Adding `card b` hyperbolic planes to `W` multiplies the twisted character
`rankTwist ν n = ν * upsilonU1 ^ (card n / 2)` by `upsilonU1 ^ card b`. 

### `smul_localDatum`

 The datum on `Hom(W, V)` with real part the Fock vector `v` and with the function `Φ` at the
ramified places of the split tame character `𝔠` is homogeneous in `Φ`. 

### `pairWeil_stdRowDatum_eq_self`

 Let `f` be the datum of the pair `(W, V)` with real part `v` and, at the ramified places of the
split tame character `𝔠`, the standard function `stdRowDatum σ 𝔠.semilocalChar z` of a matrix `z`
with entries in the ring `O` of local integers. Then `f` is fixed by the integral finite points `k`
of `U(V)` in the Weil representation twisted by `rankTwist 𝔠.character⁻¹ n` and any character
`c`. 

### `planeDatum`

 The datum of the pair `(W', V')` with `v` at the real places and, at the places
`𝔠.ramifiedPlaces`, the standard datum of `y` composed with the projection to `W`. 

### `planeConstantTerm`

 The constant term along `A`, at the point `(u, g)` of the Levi subgroup, of the theta integral
of `(W', V')` on `planeDatum 𝔠 A σ' v y`. 

### `homSlice_zero_planeDatum`

 For every matrix `y` the datum `planeDatum 𝔠 A σ' v y` (`v` at the real places, the standard
datum of `y` composed with the projection to `W` at the places `𝔠.ramifiedPlaces`) has zero source
term at `0` along the splitting `A` of the plane of `W'`. 

### `local instance : LocallyCompactSpace (maxCompact E t)`

 A shortcut for instance search, for the Haar measures on `maxCompact E t` below. 

### `integrable_theta_cone`

 Let `A` and `X` be base-adapted splittings of a plane off `W'` and `V'`, let `v` be a Schwartz
vector (all Fock moments finite), let `y` be a matrix over the completions at the places
`𝔠.ramifiedPlaces`, and let `g ∈ U(W)` and `σ : b ⊕ r ≃ n`. Then for every character `ψ`, every side
`β` and every `x > 0`, the map that sends `(h, k, a)` to the theta kernel `pairTheta W V ψ ψ` at
`(g, h)` of the datum with real part `coneIntegrand A X μ β x v (k, a)` (the real line term of side
`β` at `a` of `k v`, times `|a| ^ x` and `∏_w (a_w / |a_w|) ^ (2 μ w)`), part
`stdRowDatum σ 𝔠.semilocalChar y` at `𝔠.ramifiedPlaces` and the vacuum elsewhere is integrable. The
measure is the quotient measure on `[U(V)]` times Haar measure on the cone (the maximal compact
subgroup of `U(V')` times the real ideles). 

 ### Tate's integral on the line 

### `lineValue`

 The function on the line in Tate's integral: for an adele `α` and a point `k` of the maximal
compact subgroup of `U(V')`, the theta kernel of `(W, V)` at `(g, h)` on `lineTerm A X β α (k f)`,
the datum of `(W, V)` read off `k f` at the point `α` of the line, all characters being `ν⁻¹`
twisted as in `rankTwist`. For `β = false` it is the function on the other side of Poisson's
formula. 

### `theta_lineTerm_levi`

 Let `rk W = card n` be even, and `u = 1` or `rk V = card n`. The Levi points `(u, g)` of `U(W')`
and `(a, h)` of `U(V')` move the line by `a u`. Move `f` by these points and `k`, take its line term
at `ξ` (`lineTerm A X β ξ`, a datum of `(W, V)`) and multiply the theta value of this term by the
module `|a| ^ (rk V + 1)` of the parabolic subgroup. The result is `ν̃(a u) |a u| ^ (e + 1)` times
`lineValue` at `ξ * poissonVariable β (a u)`, where `lineValue` is the theta kernel at `(g, h)` of
the line term of `k f`. Here `e = rk V - card n / 2` and `ν̃` is the base change of `ν`. The Poisson
variable is `a u`, or its conjugate inverse on the other side of Poisson's formula (`β = false`),
where the exponent is `e`. 

### `tsum_lineValue_poisson`

 Poisson's formula on the line. Let `E` be a CM field with Weil data, let `A` and `X` split a
hyperbolic plane off `W'` and `V'`, and let `rk W = card n` be even. Let
`lineValue ν A X f g β α h k` be the theta kernel of `(W, V)` at `(g, h)` on the line term at `α` of
`k f`, with characters `ν⁻¹` twisted as in `rankTwist`, in the model `β`. If `lineValue` vanishes at
`0` for both `β`, then for every idele `a` the sum over `ξ ∈ Eˣ` of the `β = true` value at `ξ a`,
times `|a|`, equals the sum over `ξ ∈ Eˣ` of the `β = false` value at `ξ ā⁻¹`. 

### `zetaIntegrand`

 The integrand of Tate's integral `𝒵(x)` at `p = ((a, h), k)`, for an idele `a`, a point `h` of
`U(V)` and a point `k` of the maximal compact subgroup of `U(V')`: it is `ν̃(a u) |a u| ^ x` times
the sum of `lineValue` at `(h, k)` over `Eˣ a u`. 

### `zetaIntegrand_eq_tsum`

 Let `rk W` be even and suppose that `lineValue` vanishes at `0` on both sides. Then Tate's
integrand at `x` (for `β = true`) or `1 - x` (for `β = false`) is the sum over `ξ : Eˣ` of
`ν̃(z) |z| ^ x` times `lineValue` on the side `β` at `z`, where `z` is `ξ` times the value at
`a u` of `poissonVariable E β`. 

### `stdKernelForm`

 The theta kernel of `(W, V)` at `(g, h)` on the standard datum of `y`, as a linear form in the
real vector. 

### `integral_stdKernelForm`

 The integral over `[U(V)]` of the kernel `stdKernelForm` on a real vector `v` is the theta
integral of `(W, V)` on `v` and the standard datum of `y`. 

### `exists_lineValue_eq`

 The datum factors. For integral `y`, the function of Tate's integral of `planeDatum 𝔠 A σ' v y`
at `α α₀`, where `α₀ = scaleIdele E`, is `l β * γ` times the finite factor `lineFinFactor` shifted
by the uniformiser `ϖ` times the kernel of `(W, V)` on the real line term at `α∞` of `k v`. Here `l`
does not depend on the character, and `|γ| ^ 2 = (∏ q_w)⁻¹`. 

### `coneKernel`

 The theta kernel of `(W, V)` at `(g, h)` on the cone integrand with exponent `x` at `(k, a)`,
for `p = (h, k, a)`. 

### `zetaMeasure`

 The measure of the unfolded integral: idele classes, `[U(V)]` and the maximal compact subgroup
of `U(V')`. 

### `LineValueFactors`

 For every side `β` of Poisson's formula on the line, the function of Tate's integral for `f` at
`α α₀`, where `α₀ = scaleIdele E`, is a constant `κ β` times the finite factor of `𝔠` shifted by
the uniformiser `ϖ` times the theta kernel of `(W, V)` on the standard datum of `y` and the real
line term `lineTermReal` at `α∞` of `k v` (the Weil action of the real component of `k` on `v`). 

### `shiftIdele`

 The idele `c⁻¹ α₀`, `α₀ = scaleIdele E`, by which Tate's integral is translated; in use `c` is a
finite idele with `lineFinFactor 𝔠 ϖ a = lineFinFactor 𝔠 1 (a * c)`
(`exists_lineFinFactor_uniformizer_eq`). 

 ### The cone kernel and the unfolded integral 

### `coneKernel_eq`

 The cone kernel at a triple `p = (h, k, a)` (so `h = p.1`, `k = p.2.1`, `a = p.2.2`) is
`ν̃(a) |a| ^ x` times the kernel on the real line term at `a` of `k v`, where `ν̃` is the base
change of `ν = 𝔠.character`. Only the real component `k.val.1` of `k` acts on `v`. 

### `integrable_coneKernel`

 For a Schwartz vector `v` and an exponent `x > 0` the cone kernel is integrable over `[U(V)]`
and the cone. 

### `integral_coneKernel`

 For a Schwartz vector and `x > 0` the integral of the cone kernel is the theta integral of
`(W, V)` at the cone integral, the integral of the cone integrand. 

### `continuousOn_integral_coneKernel`

 For a Schwartz vector the integral of the cone kernel is continuous in the exponent `x` on every
interval `[1, x₁]`. 

### `lineValue_zero_of_factor`

 If the datum `f` factors along the line (`LineValueFactors`) for the split tame character `𝔠`,
neither side of Poisson's formula on the line has a term at `0`. 

### `baseChange_mul_lineValue_eq_coneKernel_mul`

 Let the datum `f` factor along the line (`LineValueFactors`) for the split tame character `𝔠`,
and let the translation by `c` remove the uniformiser from the finite factor. Then one term of
Tate's integrand at the idele `α K`, with `K = c⁻¹ α₀` and `α₀ = scaleIdele E`, is the cone kernel
at the real part of `α` times a function of its finite part. 

### `integral_zetaIntegrand_of_one_lt`

 Let `𝔠 : SplitTameChar E μ` be a split tame character and `v` a real datum. Let the datum `f`
factor along the line with constants `κ` (`LineValueFactors`), let the translation by `c` remove the
uniformiser from the finite factor, let `rk W` be even, let all Fock moments of `v` be finite and
let `ρ` be a Haar measure on the finite ideles such that Haar measure on the ideles, read in
`poissonVariable E β` (`a` or `ā⁻¹`) and split by `ideleParts`, is `haar.prod ρ`. Then for `x > 1`
Tate's integral at `x` (for `β = true`) or at `1 - x` (for `β = false`) converges, and it is the
integral of the cone kernel times `L^S(x, ν)` and explicit factors, for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`. 

### `integral_zetaIntegrand_of_one_le`

 The formula of `integral_zetaIntegrand_of_one_lt` for Tate's integral of the split tame
character `𝔠 : SplitTameChar E μ` in terms of the cone kernel holds for all `x ≥ 1`, under the same
hypotheses, if Tate's integral is continuous in its exponent: both sides are then continuous up to
`1`. 

 ### Analytic continuation and the constant term 

### `analyticOnNhd_integral_zetaIntegrand`

 Let `A` and `X` split a hyperbolic plane off `W'` and `V'`, let `f` be a datum on `Hom(W', V')`,
`g` a point of `U(W)`, `u` an idele and `ν` a character of `[U(1)]`. Tate's integral `𝒵(x)` is the
integral of `zetaIntegrand ν A X f g u x` over the idele classes, `[U(V)]` and the maximal compact
subgroup of `U(V')` (the measure `zetaMeasure V t'`). If it converges absolutely at `x` and at
`1 - x` for every `x > 1`, then it converges absolutely at every real `x`, and `𝒵` is analytic on
the real line. 

### `exists_planeConstantTerm_eq_integral`

 Unfolding. Let the adapted splittings `A` and `X` split a hyperbolic plane off `W'` and `V'`,
let `rk W = card n` be even and `e = rk V - rk W / 2`. There is a constant `c ≠ 0`, independent of
the character, with the following property. Let `𝔠` be a split tame character, `v` a real vector
with finite Fock moments, `y` a matrix at the places `𝔠.ramifiedPlaces` and `(u, g)` a Levi point
with `u = 1` or `rk V = rk W`. If Tate's integral `𝒵(e + 1)` of `planeDatum 𝔠 A σ' v y`, the
integral of `Θ`, converges absolutely, then the constant term along `A` at `(u, g)` of the theta
integral of `(W', V')` on this datum is `c 𝒵(e + 1)`. 

### `exists_zetaIntegral`

 Let `E` be a CM field, let `W`, `V`, `W'`, `V'` be hermitian spaces with frames indexed by `n`,
`r`, `n'`, `r'` and signs `s`, `t`, `s'`, `t'`, let `A` and `X` split a plane off `W'` and `V'`, and
let `σ : b ⊕ r ≃ n` and `σ' : b ⊕ r' ≃ n'` list the rows of the standard data. For a split tame
character `𝔠 : SplitTameChar E μ` write `ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`. Let
`rk W = card n` be even and `e = rk V - rk W / 2`. For a Schwartz vector `v` (all Fock moments are
finite), an integral `b × n` matrix `y` over the completions at `S`, and a Levi point `(u, g)` with
`u = 1` or `rk V = rk W`, there is a function `𝒵`, analytic on the real line (in the proof a
multiple of Tate's integral), such that the constant term along `A` at `(u, g)` of the theta
integral of `(W', V')` on the plane datum of `v`, `y` is `𝒵(e + 1)`. Moreover, for `x ≥ 1`,
`𝒵(x) = ε |α₀| ^ x ∏_{w ∈ S} q_w ^ (x - 1/2) L^S(x, ν) I`, where `I` is the theta integral of
`(W, V)` at `g` of the datum with real part the cone integral of `v` (the integral of
`coneIntegrand` with exponent `x`) and with `stdRowDatum σ 𝔠.semilocalChar y` at `S`. The value
`𝒵(1 - x)` has the same form, with the cone integral on the other side of Poisson's formula
(`β = false`). Here `O` is the ring of integers of the product of the completions at `S`,
`α₀ = scaleIdele E`, and the modulus `C β` of the constant `ε β` of the side `β` does not depend on
the character. 

### `exists_planeConstantTerm_eq_thetaLarge`

 Let `rk W = card n` be even, `e = rk V - rk W / 2`, and let `e + 1` be `z + 1` (for `β = true`)
or `1 - (z + 1)` (for `β = false`). There are `C > 0`, independent of `𝔠`, and `γ` with
`|γ| = C L♯(z + 1)`, where `L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` (`lSharp`) for
`ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`. Then for a Schwartz vector `v'`, integral `y`, and
`u = 1` or `rk V = rk W`, the constant term along `A` at `(u, g)` of the theta integral of
`(W', V')` on `planeDatum` is `γ` times the theta integral of `(W, V)` on the datum with
`stdRowDatum σ 𝔠.semilocalChar y` at `S` and real part the cone integral of side `β` of `v'`, which
integrates `coneIntegrand` with exponent `z + 1` over `k` in the maximal compact subgroup of `U(V')`
and the archimedean ideles. 

### `exists_planeConstantTerm_eq_thetaLarge_cone`

 One plane: let `z = rk V - rk W / 2 ≥ 0`, with `rk W = card n` even. For a Schwartz vector `v'`
and integral `y`, the constant term along `A` of the theta integral of `(W', V')` is `γ` times the
theta integral of `(W, V)` on `cone A X μ (z + 1) v'` and `stdRowDatum σ 𝔠.semilocalChar y`. The
cone is the real Tate integral of `v'` with exponent `z + 1` over the vectors `k⁻¹ x a`, with `x`
spanning the isotropic line `X.k`. Here `|γ| = C L♯(z + 1)` with
`L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` (`lSharp`) for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`, and `C > 0` does not depend on the character. This holds at the points
`(1, g)` of the Levi subgroup, and at all its points `(u, g)` if `rk V = rk W`. 

### `exists_planeConstantTerm_eq_thetaLarge_dualCone`

 One plane for `rk V - rk W / 2 = -z - 1 < 0`, with `rk W = card n` even: for a Schwartz vector
`v'` and integral `y`, at `u = 1` (the case `rk V = rk W` cannot occur here), the constant term
along `A` of the theta integral of `(W', V')` is `γ` times the theta integral of `(W, V)` on
`dualCone A X μ (z + 1) v'` and `stdRowDatum σ 𝔠.semilocalChar y`. The cone integral is a real Tate
integral over the isotropic cone of `V'`, and `dualCone` is this integral on the other side of
Poisson's formula. Here `|γ| = C L♯(z + 1)` with `L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)`
(`lSharp`) for `ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`, and `C > 0` does not depend on `𝔠`. As
Poisson's formula is applied before the integral is evaluated, only values of `L` at points `≥ 1`
occur, and the functional equation of `L` is not needed. 
