---
{
  "module": "src/Lib/SiegelWeil/Tower/FiniteTateIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/FiniteTateIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/FiniteTateIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of `L`-values and Tate's integral at the finite places

This file defines the product `L_*` of partial Hecke `L`-values of a split tame character and the
factor `L♯`, a single value `|L^S(z, ν)|` times powers of the `q_w`. It proves the recursions for
`L_*`, in which `L♯ ^ 2` is the factor. It defines the finite factor `New.Exchange.lineFinFactor` of
the datum along the line. For `x > 1` it computes Tate's integral over the finite ideles as a
partial `L`-value. It also proves a lemma that unfolds a sum over `Eˣ` against the integral over the
idele classes, in the variable `a` or `ā⁻¹` of either side of Poisson's formula.

## Main definitions and results

* `New.Exchange.lValueProd_succ`: The recursion `L_*(z + 1) = L♯(z + 1) ^ 2 * L_*(z)` for natural
  `z`.
* `New.Exchange.integral_finTateIntegrand`: For `x > 1` and a Haar measure `ρ`, Tate's integrand
  `finTateIntegrand 𝔠 x` over the finite ideles is integrable. It is the finite factor times the
  base change of `ν = 𝔠.character` times the `x`-th power of the module. Its integral is the partial
  `L`-value `L^S(x, ν)`, for `S = 𝔠.ramifiedPlaces`, times the `ρ`-volume of the unit ideles
  `idelesUnitOff ∅`.

Notions from other files:
* `𝔠 : SplitTameChar E μ` is a character `𝔠.character` of `[U(1)]` of positive weight `μ`, tamely
  ramified exactly on a finite set `𝔠.ramifiedPlaces` of places disjoint from its conjugate;
  `𝔠.semilocalChar` is `t ↦ ν(t / t̄)` on the product `LocProd 𝔠.ramifiedPlaces` of the completions
  at `𝔠.ramifiedPlaces`.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` for sources.


 ### Products of `L`-values 

### `lValueProd`

 For a set `S` of finite places of `E`, with residue cardinalities `q_w`, and a character `ν` of
`[U(1)]`, the product `L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ z ≤ e} |L^S(z, ν)| ^ 2`, where
`L^S(z, ν) = ν.L S z` is the Euler product of the base change of `ν` outside `S ∪ S̄`. 

### `lValueProdInt`

 `L_*(e)` for the character `𝔠.character` and its set `𝔠.ramifiedPlaces` of ramified places,
extended to every integer `e` by `L_*(-e) = L_*(e)⁻¹`. 

### `lSharp`

 `L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`. It is used only for `z ≥ 1`, as `𝔠.character.L` is an Euler product and not
its analytic continuation. 

### `SplitTameChar.L_ne_zero`

 The partial `L`-function of a split tame character has no zero on `[1, ∞)`, because the weight
of the character is not zero. 

### `lValueProd_succ`

 The recursion `L_*(z + 1) = L♯(z + 1) ^ 2 * L_*(z)` for natural `z`. 

### `lValueProdInt_succ`

 For a split tame character `𝔠` of `[U(1)]` over the CM field `E`, with character
`ν = 𝔠.character` and ramified set `S = 𝔠.ramifiedPlaces`, this gives a recursion for every natural
`z`. The value `lValueProdInt 𝔠 (z + 1)`, written `L_*(z + 1)`, equals `L♯(z + 1)² · L_*(z)`. Here
`L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` is `lSharp 𝔠 z`, and `L_*` is extended to all
integers by `L_*(-e) = L_*(e)⁻¹`. 

### `lValueProdInt_neg`

 For natural `z`, `L_*(-z) = L♯(z + 1) ^ 2 * L_*(-z - 1)`, which computes `L_*` at the
nonpositive integers by downward recursion. Here `L_*` (`lValueProdInt`) is the value for the
character `𝔠.character` and its set `𝔠.ramifiedPlaces` of ramified places, extended to all integers
by `L_*(-e) = L_*(e)⁻¹`. Also `L♯(z) = |L^S(z, ν)| ∏_{w ∈ S} q_w ^ (z - 1/2)` (`lSharp`). 

 ### Tate's integral at the finite places 

### `lineFinFactor`

 The finite factor of the datum along the line, shifted by `p`. Let `S = 𝔠.ramifiedPlaces` and
let `χ = 𝔠.semilocalChar` be the tame character on the completions at `S`. At a finite adele `a`
that is integral off `S ∪ S̄` the value is `χ⁻¹(a) χ(ā p)`, read as `0` unless `a` and `ā p` are
units at `S` (the quotient by `0` is `0`). At other adeles it is `0`. 

### `exists_lineFinFactor_uniformizer_eq`

 There is a finite idele `c` of module `∏_{w ∈ S} q_w⁻¹`, `S = 𝔠.ramifiedPlaces`, such that the
finite factor shifted by the uniformisers `ϖ` at `S` is the translate by `c` of the unshifted
one. 

### `valuation_of_lineFinFactor_ne_zero`

 On the support of the finite factor an adele is integral off `S ∪ S̄` and a unit at `S ∪ S̄`,
where `S = 𝔠.ramifiedPlaces`. 

### `lineFinFactor_mul_finPart`

 On the finite ideles that are units at all places, the finite factor is the inverse of the
finite part of the base change `x ↦ ν(x / x̄)` of `ν = 𝔠.character`. 

### `lineFinFactor_congr`

 On integral adeles the finite factor depends only on the components at `S ∪ S̄`,
`S = 𝔠.ramifiedPlaces`. 

### `finTateIntegrand`

 The integrand of Tate's integral over the finite ideles: the finite factor times the base change
of `𝔠.character` times the `x`-th power of the module. 

### `integral_finTateIntegrand`

 For `x > 1` and a Haar measure `ρ`, Tate's integrand `finTateIntegrand 𝔠 x` over the finite
ideles is integrable. It is the finite factor times the base change of `ν = 𝔠.character` times the
`x`-th power of the module. Its integral is the partial `L`-value `L^S(x, ν)`, for
`S = 𝔠.ramifiedPlaces`, times the `ρ`-volume of the unit ideles `idelesUnitOff ∅`. 

### `continuousOn_L`

 The partial `L`-function of a split tame character is continuous on `[1, ∞)`, as a character of
nonzero weight is not trivial. 

 ### Unfolding over the idele classes 

### `poissonVariable`

 The variable of Tate's integral on the two sides of Poisson's formula: `a` itself for
`β = true`, and `ā⁻¹` for `β = false`. 

### `baseChange_poissonVariable`

 The base change `x ↦ ν(x / x̄)` of a character `ν` of `[U(1)]` has the same value at `a` and at
the Poisson variable `poissonVariable E β a`, which is `a` or `ā⁻¹`. 

### `ideleParts`

 The isomorphism that splits an idele into its archimedean and its finite part. 

### `exists_haar_ideleParts`

 Haar measure on the ideles, read in the variable `a` or `ā⁻¹` of either side of Poisson's
formula and split by `ideleParts` into the archimedean and the finite part, is the product of the
Haar measure `haar` on the archimedean ideles and a Haar measure `ρ` on the finite ideles. 

### `principalAdeleUnit`

 The principal idele of a unit of `E`. 

### `exists_equiv_principalAdeleUnits`

 The principal ideles can be listed by a bijection `J` from `Eˣ` so that the Poisson variable
(`a` or `ā⁻¹`) at the idele `J ξ` is the principal idele of `ξ`. 

### `measurePreserving_prod_parameters`

 A measure-preserving map `φ : X₁ × X₂ → Z₁ × Z₂` stays measure preserving when two parameters
`y₁` and `y₂` are carried along. 

### `integral_ideleClass_tsum`

 Unfolding a sum over `Eˣ` against the integral over the idele classes (computed by the
measure `quotMeasure` on the ideles), with parameters in two further measure spaces `Y₁` and `Y₂`.
Suppose that Haar measure on the ideles, read in the variable `poissonVariable E β a` (`a` or `ā⁻¹`)
and split by `ideleParts` into the archimedean and the finite part, is the product of Haar measure
and `ρ`. If the term at `ξ` of `Θ` is a product `Z * ζ` of integrable functions of the two parts of
`ξ * poissonVariable E β a * c`, then `Θ` is integrable and its integral is the product of the
integrals of `Z` and `ζ`. 
