---
{
  "module": "src/Lib/DiscreteSeries/Rigidity/KernelFixes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Rigidity/KernelFixes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Rigidity/KernelFixes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The idempotent e_λ, the operator π(e_λ), and rigidity of highest vectors of type Λ

The file studies the function `e_λ = New.HCParam.dsKernel l = deg_λ · conj c_λ` on `U(diag ε)`,
where `l = 2λ`, and the operator `π(f) = New.integratedRep π f = ∫ f(g) π(g) dg`. In the main
results `λ` has gap `500 n³ + A` (`New.HCParam.HasLargeGap`), `π` has growth `‖g‖ ^ A` and an
invariant positive definite sesquilinear form `B` on `X` (`New.IsUnitaryRep`), and the `gl n`-module
`ρ` on a complex space `M` is its derivative along a linear map `ι : M → X` (`New.IsDerivedAction`).

* `New.coeff_eq_dsCoeff_of_isKHighest` (rigidity): a `K`-highest vector `x` of weight
  `Λ = New.HCParam.lowestKType l` with Casimir value at least
  `κ_λ = New.HCParam.casimirValue l = |λ|² − |ρ|²` (ρ here the half-sum of positive roots) has the
  matrix coefficient `B x (π g x) = B x x c_λ(g)`.
* `New.integratedRep_fix_of_isKHighest`: if `‖g‖ ^ A f` is integrable and `f * e_λ = e_λ`, then
  `π(f)` fixes such a vector.
* `New.exists_integration_by_parts`, `New.integratedRep_dsKernel_casimir`: integration by parts, and
  `π(e_λ) Ω = κ_λ π(e_λ)`.
* `New.re_integratedRep_dsKernel_pos`, `New.integratedRep_eq_zero_of_notMem_rootCone`: a condition
  under which `π(e_λ)` does not kill a vector, and one under which it does.
* `New.HCParam.HasLargeGap.isIdempotentKernel_dsKernel`,
  `New.HCParam.HasLargeGap.exists_bump_conv_dsKernel`: `e_λ` is a minimal idempotent, reproduced by
  a bump function.

`ρ.casimirK 1` is the Casimir operator `Ω = ∑ E_ab E_ba` of all of `gl n` (all signs equal).

Notions from other files:
* `New.HCParam.IsKHighest`: `x` is a `K`-highest vector of weight `ν`: each `E a a` acts on it by
  `ν a`, and it is killed by the compact raising operators, the `E a b` with `ε a = ε b` and
  `l b < l a`.
* `New.HCParam.lowestKType`: the integer vector Λ = λ+ρ−2ρ_c for a parameter l = 2λ, the highest
  weight of the lowest K-type.
* `New.HCParam.dsCoeff`, `New.HCParam.DsModule`: The function c_λ, and the module U(𝔤)c_λ it
  generates under right derivatives (action `New.HCParam.dsAction`, generator
  `New.HCParam.dsGenerator`).
* `New.weightMinors`, `New.HCParam.kTypeNormSq`: The coefficient m_ν of a highest vector of weight ν
  (a product of principal minors), and ∫_K |m_ν|².
* `New.HCParam.rootCone`: The cone of the positive roots for the order given by l.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Rigidity.HighestVectorsAndFiltration`,
`Lib.DiscreteSeries.Theta.LocalCorrespondence` and `Lib.DiscreteSeries.FlenstedJensen.PsiKTypes` for
sources.


### `conj_dsKernel_neg`

 For `l = 2λ` a parameter of some gap `h` (`New.HCParam.HasGap`),
`conj ((-l).dsKernel x) = l.dsKernel x` for every `x` in `U(diag ε)`. That is, `conj(e_{−λ}) = e_λ`
for the kernel `e_λ = deg_λ · conj(c_λ)` given by `dsKernel`. 

 ### The operator `π(f)` 

### `integratedRep`

 For a representation π of U(diag ε) by bounded operators and a function f, the operator π(f)
with π(f)x = ∫ f(g)π(g)x dg, when such a bounded operator exists. 

### `re_integral_pos`

 If `f` is integrable for a nonzero measure and its real part is positive everywhere, then the
real part of its integral is positive. 

### `HCParam.IsKHighest.integral_conj_weightMinors_mul`

 Let l be a parameter of any gap, π a representation as in `New.IsUnitaryRep` with derivative ρ
along ι, and v in M a K-highest vector of weight ν, with ν K-dominant for the order −l (ν b ≤ ν a
whenever ε a = ε b and l b < l a). Then for every continuous linear functional φ on X, ∫_K
conj(m_ν(k)) φ(π(k)ιv) dk = (∫_K |m_ν|²) φ(ιv), with m_ν = `weightMinors ν` and ∫_K
|m_ν|² = `ν.kTypeNormSq`. 

### `integrable_smul_rep`

 If `π` is a representation as in `New.IsUnitaryRep` of growth exponent `A` and
`g ↦ f g * ‖g‖ ^ A` is integrable on `U(diag ε)`, then so is each `g ↦ f g • π g x`. 

### `map_integratedRep`

 If `g ↦ f g * ‖g‖ ^ A` is integrable and `π` is as in `New.IsUnitaryRep` with exponent `A`, then
a continuous linear map `T` takes `π(f) x` to the integral of `g ↦ f g • T (π g x)`. 

 ### The kernel `e_λ`, its bump function, and the operator `π(e_λ)` 

### `HCParam.HasLargeGap.isIdempotentKernel_dsKernel`

 For n ≥ 1 (`Nonempty n`) and a doubled parameter l = 2λ for the signs ε with gap 500n³+A
(`HasLargeGap`), the function `l.dsKernel` on U(diag ε), e_λ(g) = deg_λ·conj(c_λ(g)), is an
idempotent kernel in the sense of `New.IsIdempotentKernel`. That is, it is continuous and
integrable, e(g⁻¹) = conj e(g), e(1) ≠ 0, and ∫ e(z) e(x⁻¹z⁻¹y) dz = e(x⁻¹) e(y)/e(1). 

### `HCParam.HasLargeGap.exists_bump_conv_dsKernel`

 For `n ≥ 1` and `λ = l / 2` with gap `500 n³ + A`, let `e_λ = l.dsKernel`. Then there is a
smooth compactly supported `α` on `U(diag ε)` with `∫ α(x⁻¹) e_λ(x⁻¹ g) dx = e_λ(g)` for all `g`. So
`β * e_λ = e_λ` for the function `β(x) = α(x⁻¹)`; the inverse comes from the convention of
`New.DiscreteSeries.smear`. 

### `exists_integration_by_parts`

 Integration by parts. Let `λ = l / 2` have gap `500 n³ + A`, and let `π` be as in
`New.IsUnitaryRep` with derivative `ρ` along `ι`. Let `(-l).DsModule` be the space U(𝔤)c_{−λ}
generated by c_{−λ} under right derivatives, with gl_n-action `dsAction`. Then there is a linear map
`P` from this space to bounded operators on `X` such that (a) `P(c_{−λ})` is `π(e_λ)`, the
integrated operator `x ↦ ∫ e_λ(g) π(g) x dg` of `e_λ = l.dsKernel` = deg_λ · conj(c_λ); (b)
`P f (ι (ρ Y v)) = −P (Y·f) (ι v)` for all `Y` in gl_n(ℂ), `f` and `v`. 

### `integratedRep_dsKernel_casimir`

 Let `l = 2λ` have gap `500 n³ + A`, let `e_λ = l.dsKernel`, and let `π` be a representation of
`U(diag ε)` on `X` with `IsUnitaryRep A π B` (strongly continuous, `‖π g‖ ≤ C‖g‖^A`, `B` hermitian,
positive definite and invariant) whose derivative along `ι` is the `gl n`-module `ρ`. Then
`π(e_λ) ι(Ω v) = κ_λ π(e_λ) ι(v)` for every `v`. Here `π(e_λ) = integratedRep π l.dsKernel`,
`Ω = ρ.casimirK 1` is the Casimir operator of `gl n`, and `κ_λ = New.HCParam.casimirValue l`. 

### `HCParam.IsKHighest.isKDominant_of_isUnitaryRep`

 For `π` as in `New.IsUnitaryRep` with derivative `ρ` along `ι`, the weight `ν` of a `K`-highest
vector `v` with `ι v ≠ 0` is `K`-dominant for the order `-l`: if `ε a = ε b` and `l b < l a`, then
`ν b ≤ ν a`. 

### `integratedRep_eq_zero_of_notMem_rootCone`

 Let `λ = l / 2` have gap `500 n³ + A`, let `π` be as in `New.IsUnitaryRep` with derivative `ρ`
along `ι`, and let `v` be `K`-highest of weight `ν`. Suppose `ν - New.HCParam.lowestKType l` lies
outside `New.HCParam.rootCone l`, the cone of integer vectors `β` with `o ⬝ᵥ β ≤ 0` for every
integer `o` strictly reversing the order of `l`; this cone contains all sums of the roots
`e_a − e_b` with `l b < l a`. Then `π(e_λ)` kills every translate `π y (ι v)`, where
`e_λ = New.HCParam.dsKernel l` is `g ↦ deg_λ · conj(c_λ(g))` and `π(e_λ) x = ∫ e_λ(g) π(g) x dg`. 

### `re_integratedRep_dsKernel_pos`

 Let `λ = l / 2` have gap `500 n³ + A`, let `π` be a representation of `U(diag ε)` with invariant
positive form `B` and growth exponent `A` (`New.IsUnitaryRep`), and let `ρ` be its derivative along
`ι`. Let `v` be `K`-highest of weight `Λ = New.HCParam.lowestKType l` and `x = ι v`. If
`B x (π z x) > 0` for every positive definite `z` in `U(diag ε)`, then `Re B x (π(e_λ) x) > 0`,
where `e_λ = New.HCParam.dsKernel l` is the function `g ↦ deg_λ · conj(c_λ(g))` and
`π(e_λ) x = ∫ e_λ(g) π(g) x dg`. 

 ### Rigidity of highest vectors 

### `IsUnitaryCasimirGe.exists_prodL2`

 Let two `gl n`-modules on inner product spaces have inner products invariant under `𝔲(ε)` and
Casimir operator at least `New.HCParam.casimirValue l` (`New.IsUnitaryCasimirGe`). Then the
componentwise action on their orthogonal direct sum is a `gl n`-module with the same property. 

### `exists_isUnitaryCasimirGe_generatedModule`

 Let `π` be a representation of `U(diag ε)` on the normed space `X` with `IsUnitaryRep A π B`: it
is strongly continuous with `‖π g‖ ≤ C‖g‖^A`, and `B` is a hermitian, positive definite,
`π`-invariant bounded form. Let `ρ` be the `gl n`-module on `M` that is the derivative of `π` along
`ι`, let `j` carry `B` to the inner product of `H`, and let `ι (Ω v) = c • ι v` with
`Ω = ρ.casimirK 1` and `c ≥ κ_λ = New.HCParam.casimirValue l = |λ|² − |ρ|²`, where `l = 2λ` and this
`ρ` is the half-sum of positive roots, not the module. Then `ρ` descends to a `gl n`-module `σ` on
the range of `j ∘ ι`, compatible with `ρ`, and the submodule generated by `j (ι v)` is as in
`New.IsUnitaryCasimirGe`: its inner product is invariant under `𝔲(ε)` and its Casimir operator is at
least `κ_λ`. 

### `coeff_eq_dsCoeff_of_isKHighest`

 Rigidity. Let `λ` have gap `500 n³ + A`, let `π` be a representation of `U(diag ε)` with
invariant positive form `B` and growth exponent `A` (`New.IsUnitaryRep`), and `ρ` its derivative
along `ι`. Let `v` be `K`-highest of weight `New.HCParam.lowestKType l` with `ι (Ω v) = c • ι v` for
the Casimir operator `Ω` of `gl n`, where `c ≥ New.HCParam.casimirValue l`. Then
`B (ι v) (π g (ι v)) = B (ι v) (ι v) c_λ(g)` for all `g`, where `c_λ = New.HCParam.dsCoeff l`.

A variant of Parthasarathy's criterion recognizing a discrete series by its lowest `K`-type `μ`: for
a large gap, with a Casimir bound in place of the absence of the types `μ - α`, as an equality of
matrix coefficients. 

### `integratedRep_fix_of_isKHighest`

 Let `λ = l / 2` have gap `500 n³ + A`, let `π`, `B` be as in `New.IsUnitaryRep` with
exponent `A`, `ρ` the derivative of `π` along `ι`, and `‖g‖ ^ A • f g` integrable. Suppose (a)
`f * e_λ = e_λ` for `e_λ = New.HCParam.dsKernel l`; (b) `v` is `K`-highest of weight
`New.HCParam.lowestKType l`; (c) `ι (Ω v) = c • ι v` for the Casimir operator `Ω = ρ.casimirK 1`,
with `c ≥ New.HCParam.casimirValue l`. Then `π(f) = ∫ f(g) π(g) dg` fixes `ι v`. 
