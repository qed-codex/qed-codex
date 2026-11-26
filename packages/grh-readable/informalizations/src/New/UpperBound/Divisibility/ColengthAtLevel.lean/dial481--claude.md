---
{
  "module": "src/New/UpperBound/Divisibility/ColengthAtLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ColengthAtLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ColengthAtLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The colength of source forms at p = N

This file compares three modules of source forms, `𝒜_ι`, `𝒜^L` and `𝒜^∨`, with values integral
for the standard lattice, for `L_0` and for `L_0^∨` at `Σ_N`. These are
`integralFormsAt D.SourceForm d` for `d = 1`, `diagPointN 0` and `dualPointN 0`. The comparison
shows that `𝒜' ∩ 𝒜_ι` has colength at most `m f b D_X` in `𝒜_ι`, where `D_X` is the dimension of
the space of source forms. It bounds a colength by a mean degree. The case of monomials, which is
not used later, comes first as a model.

## Main definitions and results

* `New.Data.exists_colengthDvd_upIntegralForms_pow`: `𝒜'` has colength at most `m f b D_X`.

Notions from other files:
* `New.Data.nonInducedPlaces`: the set `Σ_N` of the conjugates of the places above `N` that `ιₚ`
  induces.
* `New.Data.diagPointN`: the point `δ_j`, which takes the standard lattice at `Σ_N` to `L_j`.
* `New.Data.upIntegralForms`: the module `𝒜'`, the preimage of `𝒜^L` under `Up ^ (m / 2)`.


### `colengthDvd_span_pow_monomials`

 The model case of the bound on colengths. In the free module on the monomials `z ^ α` of degree
`a` in `k` variables, the span of the vectors `N ^ α_i • z ^ α` has index dividing
`N ^ ∑_α α_i`, in the sense of `New.ColengthDvd`. 

### `mul_sum_monomials_apply`

 The mean degree in one of `k` variables of the monomials of degree `a` is `a / k`, by symmetry
in the variables. 

### `sumDegreeOf`

 The degree in the variable `a`, summed over all pairs of a class and a basis vector of the
values of source forms. A basis vector is a family of tableaux (`WeylIndex`), one for each infinite
place `τ : D.Φ` of `E`; its degree in `a` is the number of entries equal to `a` (`tableauWeight`),
summed over `τ`. 

### `sumDegreeOf_eq`

 The summed degree `D.sumDegreeOf a`, the degree in the variable `a` summed over all pairs of a
class and a basis vector of the values of source forms, is the same for all variables `a` of
`X_0`. 

### `mul_sumDegreeOf_le`

 The number `D.sumDegreeOf u` counts the entries equal to `u` in a family of tableaux, a basis
vector of the Weyl module in which source forms take values, summed over all pairs of a double coset
for the level `D.levelX 0` and such a basis vector. There are `D_X = finrank ℂ D.SourceForm` pairs,
and the mean is at most `D.f * D.a / D.k`. 

### `integralFormsAt_one_le`

 `𝒜_ι ⊆ 𝒜^∨`, with `𝒜_ι` and `𝒜^∨` the source forms integral at `1` and at `D.dualPointN 0`. A
source form `φ` is integral at `d` if the coordinates of `(g * d)⁻¹ φ g` are `N`-integral for all
`g`. 

### `exists_mul_dualPointN_mem_integralAbove`

 For every finite adelic point `c` there is a rational point `γ` such that `γ c δ_0^∨` is
integral above `N` and `γ c δ_0` is `diag (1, …, 1, N)` at `Σ_N` times an element integral above
`N`. Here `δ_0 = D.diagPointN 0` and `δ_0^∨ = D.dualPointN 0`. 

### `colengthDvd_integralFormsAt_diagPointN`

 Let `𝒜^L` and `𝒜^∨` be the modules of source forms `φ` integral at `δ_0 = D.diagPointN 0` and at
`δ_0^∨ = D.dualPointN 0`. The colength (`ColengthDvd`) of `𝒜^L` in `𝒜^∨` divides `N ^ l`, with
`l = D.sumDegreeOf (.inr ())` the sum of the degrees in the last variable. 

### `upOperator_mem_integralFormsAt`

 The operator `Up = upOperator (D.formRepAtN 0)`, a sum of right translates with roots of unity
as coefficients (see `upOperator_mem_sourceForm`), maps `𝒜^L`, the source forms integral at
`D.diagPointN 0`, to `𝒜^∨`, those integral at `D.dualPointN 0`. 

### `colengthDvd_comap_upOperator_pow`

 Let `𝒜_ι` and `𝒜^L` be the modules of source forms (`D.SourceForm`) that are integral at the
points `1` and `δ_0 = D.diagPointN 0`. Let `Up = upOperator (D.formRepAtN 0)` be the sum of right
translates described at `upOperator_mem_sourceForm`. Let `l = D.sumDegreeOf (.inr ())` be the summed
degree in the last variable of `X_0`. Then the index (`ColengthDvd`) in `𝒜_ι` of the preimage of
`𝒜^L` under `Up ^ i` divides `N ^ (l (i + 1))`. 

### `exists_colengthDvd_upIntegralForms_pow`

 **The prime `N`, colength.** Let `𝒜_ι` be the module of source forms with `N`-integral values
for the standard lattice, and `𝒜' = D.upIntegralForms` the module of forms `φ` on `X_0` such that
`Up ^ (m / 2) φ` is a source form integral at `D.diagPointN 0`, with
`Up = upOperator (D.formRepAtN 0)`. There is `e ≤ m f b D_X` such that every finite family in `𝒜_ι`
is carried into `𝒜'` by a square matrix whose determinant divides `N ^ e`. Here `m = D.m` is the
number of theta lifts from `X_0` to `X_m`, `f = D.f` the number of infinite places of `E`, `b = D.b`
the value of `D.weight` on the set `D.bPlaces` of infinite places, and `D_X` the dimension of the
space of source forms. 
