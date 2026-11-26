---
{
  "module": "src/Lib/Adelic/AutomorphicForms/AutomorphicAsAlgebraic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/AutomorphicAsAlgebraic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/AutomorphicAsAlgebraic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Automorphic forms on standard definite spaces as algebraic forms

On a standard definite space (`New.Space.IsStd`: all signs `1` and point `x = 1`), this file
identifies automorphic forms with smooth algebraic forms. Let `ρ = New.conjWeylRep κ e` be the
representation of the compact group `G_∞` of weight `(κ, e)`, `d` its dimension, and
`v⁺ = New.highestVector` its highest unit vector when `l` matches the weight. An algebraic form
`φ` (`New.AlgForm`, vector valued on `G_f`) gives `φ♮ = New.ofAlgForm l s φ` with
`φ♮ (x, g) = ⟨v⁺, ρ(x⁻¹) φ(g)⟩`. The inverse map sends a form `y` to
`y♭ g = d ∫ y(x, g) ρ(x) v⁺ dx`. This file also writes integrals over `Γ \ G` as class sums over
`Γ \ G_f`.

## Main definitions and results

* `New.Space.toAlgForm`: the two maps are inverse between forms of type `New.typeKernel l` (fixed by
  `realConv k y (x, g) = ∫ k(z) y(xz, g) dz` for `k = typeKernel l 1`, which is
  `z ↦ d ⟨v⁺, ρ(z) v⁺⟩`) and smooth algebraic forms, by Schur orthogonality, when `l` matches the
  weight (`New.IsHCParam`).
* `New.Space.toAlgForm_formRep`, `New.Space.algFormEquiv`, `New.hasHeckePolynomial_toAlgForm_iff`:
  the equivalence commutes with `G_f`, so it respects levels and Hecke eigenvalues.
* `New.Space.integral_eq_classIntegral_of_isLevel`,
  `New.Space.integral_mul_eq_classIntegral_toAlgFormFun`, `New.Space.integral_mul_eq_classIntegral`:
  integrals over `Γ \ G`, in particular against `φ♮`, as class sums `New.classIntegral` over
  `Γ \ G_f`.
* `New.Space.classSum_gramForm_eq_mul_petersson`: for two algebraic forms that transform under a
  level by one character with values of finite order, the class sum of their Gram pairings is a
  multiple of the Petersson product of the associated functions.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s), for the signs s, at the infinite places and 1 at the finite places.
* `New.Space.IsAutomorphic`: a function on `G = G_∞ × G_f` that is continuous, left invariant under
  rational points and right invariant under an open subgroup of `G_f`.
* `New.algFormCoeff s L φ`: the function `(x, g) ↦ L (ρ(x⁻¹) φ(g))`; it is `New.ofAlgForm l s φ` for
  `L = ⟨v⁺, ·⟩`, where `⟨·, ·⟩ = New.gramForm`.
* `New.stdLevelIndex K`: the index `[stdLevel : K ∩ stdLevel]` in the standard level
  `stdLevel = New.stdLevel E n`; a level (`New.IsLevel K`) is an open subgroup `K ≤ stdLevel`.
* `New.classIntegral Γ K f`: the integral of `f` over `Γ \ G_f` for `vol K = 1`, as a finite sum; in
  this file `Γ = New.stdRatPoints`, the rational points of the standard space.

## Relation to the literature

Known result: algebraic modular forms as functions on the adelic group. For the source see
`Lib.Adelic.AutomorphicForms.SmoothAlgebraicForms`.


### `continuous_conjWeylMatrix`

 The matrix `conjWeylMatrix κ e x` depends continuously on the archimedean point `x`. 

 ### The maps `φ ↦ φ♮` and `y ↦ y♭` 

### `algFormCoeff_algFormRep`

 The coefficient of a translated algebraic form is the translated coefficient:
`algFormCoeff` turns `algFormRep κ e a` into right translation by `(1, a)`. 

### `isAutomorphic_algFormCoeff`

 Let V be standard and φ an algebraic form of weight (κ, e) (so its stabiliser under right
translation is open). For every linear functional L, the function g ↦ L(ρ(g_∞⁻¹) φ(g_f)) on G
(`New.algFormCoeff`) is automorphic. 

### `toAlgFormFun`

 The function `y♭` on `G_f` attached to a function `y` on the definite group:
`y♭ g = d ∫ y (x, g) • x v` over `G_∞`, where `d` is the dimension of the Weyl module, `x` acts by
`conjWeylRep` and `v` is the highest vector. 

### `toAlgFormFun_mem_algForm`

 If `y` is automorphic on the standard space, then `y♭ = toAlgFormFun κ e l y` is an algebraic
form: its stabiliser is open and it is equivariant under rational points. 

### `realConv_typeKernel`

 Let `l` be twice the Harish-Chandra parameter of the weight `(κ, e)`. The convolution over
`G_∞` of a continuous `y` with `typeKernel l 1` is `(x, g) ↦ ⟨v, x⁻¹ y♭(g)⟩`, where `v` is the
highest vector and `y♭ = toAlgFormFun κ e l y`. 

### `toAlgFormFun_ofAlgForm`

 Let `l` be twice the Harish-Chandra parameter of `(κ, e)` and `ψ` an algebraic form of weight
`(κ, e)`. Then `(ψ♮)♭ = ψ`. Here `ψ♮ = ofAlgForm l 1 ψ` is the function `g ↦ ⟨v⁺, ρ(g_∞⁻¹) ψ(g_f)⟩`
on the group of the standard space, with `v⁺` the highest vector for `l`. For a function `y` on that
group, `y♭ = toAlgFormFun κ e l y` is `g ↦ d ∫_{G_∞} y(x, g) ρ(x) v⁺ dx`, with `d` the dimension of
the Weyl module and `ρ = conjWeylRep`. 

### `isForm_ofAlgForm`

 Let `V` be standard (all its signs `s` are +1 and its point is the identity matrix) and `l`
twice the Harish-Chandra parameter of `(κ, e)`. For every algebraic form `ψ`, the function
`ofAlgForm l s ψ`, g ↦ ⟨v⁺, ρ(g_∞⁻¹) ψ(g_f)⟩, is a form of type `typeKernel l s`. That kernel is the
product over the infinite places of the formal degree times the conjugate discrete series
coefficient. That is, this function is automorphic, bounded and fixed by convolution with that
kernel over `G_∞`. 

 ### The equivalence and its equivariance 

### `toAlgForm`

 On a standard space, for `l` twice the Harish-Chandra parameter of `(κ, e)`, the forms of type
`typeKernel l s` are the smooth algebraic forms of weight `(κ, e)`. This is the inverse `y ↦ y♭` of
`φ ↦ φ♮ = ofAlgForm l s φ`, which is injective as `(φ♮)♭ = φ`, and surjective as `y = (y♭)♮`. 

### `ofAlgForm_toAlgForm`

 Let `V` be a standard space and `l` twice the Harish-Chandra parameter of `(κ, e)`. Let `y` be a
form of type `typeKernel l s` on `V`, and let `φ = V.toAlgForm h y` be its algebraic form of weight
`(κ, e)`. Then `ofAlgForm l s φ` gives `y` back: `y(g) = ⟨v⁺, ρ(g_∞⁻¹) φ(g_f)⟩`, with `v⁺` the
highest vector for `l`. 

### `toAlgForm_eq_toAlgFormFun`

 Let `l` be twice the Harish-Chandra parameter of `(κ, e)` and `y` a form of type
`typeKernel l 1` on the standard space. The algebraic form `toAlgForm h y` corresponds to `y` under
the inverse of `φ ↦ ofAlgForm l 1 φ`. Its underlying function is `y♭ = toAlgFormFun κ e l y`, i.e.
`g ↦ d ∫_{G_∞} y(x, g) ρ(x) v⁺ dx`, with `d` the dimension of the Weyl module, `ρ = conjWeylRep` and
`v⁺` the highest vector for `l`. 

### `toAlgForm_formRep`

 For `l` twice the Harish-Chandra parameter of `(κ, e)`, the isomorphism `New.Space.toAlgForm`
from forms of type `typeKernel l s` on a standard space to smooth algebraic forms of weight
`(κ, e)` commutes with right translation by `G_f`. 

### `algFormEquiv`

 For V standard and l twice the Harish-Chandra parameter of (κ, e), the isomorphism
φ ↦ `ofAlgForm l s φ` from K-fixed algebraic forms to K-fixed forms of type `typeKernel l s`. No
hypothesis is put on K. 

### `_root_.New.hasHeckePolynomial_toAlgForm_iff`

 For V standard and l twice the Harish-Chandra parameter of (κ, e), a form y of type
`typeKernel l s` has Hecke polynomial p at the place w (with `star w ≠ w`) if and only if its
algebraic form, as a function on G_f, does. (`HasHeckePolynomial`: fixed by the standard group at w
and an eigenvector of the Hecke operators there, as prescribed by p; `WeilData E`: the auxiliary
element, idele and splitting character fixed on E.) 

 ### Integrals over the quotient as class sums 

### `integral_eq_classIntegral_of_isLevel`

 On a standard definite space `V` let `F` be automorphic and `K` a level (an open subgroup of the
standard level `stdLevel`). The integral of `F` over `Γ \ G` is `[stdLevel : K]⁻¹` times the class
integral at level `K` (normalised by `vol K = 1`) of `g ↦ ∫ F(x, g) dx` over `x ∈ G_∞`. 

### `integral_mul_eq_classIntegral_toAlgFormFun`

 Let `K` be a level. Let `y`, `y'` be automorphic functions on the group `G` of the standard
space: continuous, left `Γ`-invariant, and right invariant under an open subgroup of `G_f`. Suppose
`y'(x, g) = L g (ρ(x) v⁺)` for linear functionals `L g`, where `ρ = conjWeylRep` and `v⁺` is the
highest vector for `l`. Then `d ∫_{Γ\G} y' y` (for `quotMeasure`, with `d` the dimension of the Weyl
module) equals `(stdLevelIndex K)⁻¹ = [stdLevel : K]⁻¹` times the `classIntegral` at `K` of
`g ↦ L g (y♭ g)`, i.e. the integral over `Γ \ G_f` for `vol K = 1`, where
`y♭ g = d ∫_{G_∞} y(x, g) ρ(x) v⁺ dx` is `toAlgFormFun κ e l y`. 

### `integral_mul_eq_classIntegral`

 Let `V` be standard, `l` twice the Harish-Chandra parameter of `(κ, e)`, `φ` an algebraic form,
`K` a level and `Φ` automorphic. If `Φ (x, g) = L g (ρ(x) v⁺)` with each `L g` linear,
`ρ = conjWeylRep κ e`, `v⁺ = highestVector κ l`, then the integral of `Φ` times `ofAlgForm l s φ`
over `Γ \ G` is `(dim ρ * stdLevelIndex K)⁻¹` times the integral of `g ↦ L g (φ g)` over `Γ \ G_f`,
normalised by `vol K = 1`. 

### `star_ofAlgForm`

 When all signs are `1`, the conjugate of `ofAlgForm l s φ (x, g) = ⟨v⁺, ρ(x⁻¹) φ(g)⟩` is
`⟨φ(g), ρ(x) v⁺⟩`, where `⟨·, ·⟩ = gramForm`, `ρ = conjWeylRep κ e` and
`v⁺ = highestVector κ l`. 

### `classSum_gramForm_eq_mul_petersson`

 Let `V` be standard (all signs `+1`, point the identity), `l` twice the Harish-Chandra parameter
of `(κ, e)`, `K` a level and `χ` a character of `K` whose values have finite order. For algebraic
forms `φ`, `φ'` on which `K` acts by `χ`, the class sum at `K` (over `Γ\G_f/K`, the term at `g`
weighted by `1/#(Γ ∩ gKg⁻¹)`) of the Gram pairings `⟨φ(g), φ'(g)⟩` is the index
`stdLevelIndex K = [stdLevel : K]`, times the dimension of the weight, times the Petersson product
`∫_{Γ\G} conj(F_φ) F_φ'`, where `F_φ = ofAlgForm l s φ` is the function
`F_φ(g) = ⟨v⁺, ρ(g_∞⁻¹) φ(g_f)⟩` on the group. 
