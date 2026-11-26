---
{
  "module": "src/New/Appendix/DiscreteSeries/SteepParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/SteepParameters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/SteepParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Steep parameters and the setting of Laplace's method

This file begins the localization near the compact subgroups. It concerns a group `S` that maps to
`U(ε) × U(η)`, for two vectors of signs `ε` and `η`, together with the parameters of two discrete
series. Let `μ` and `μ'` be the diagonal matrices of the weights of their lowest `K`-types. Among
other properties, the function `φ s = tr (μ (g - 1)) - tr (μ' (g' - 1))` of the image `(g, g')` of
`s`, the difference of the two phases, is additive and purely imaginary.
The file defines the phase difference `New.HCParam.phase`, steep parameters, the properties
`New.DiscreteSeries.IsLaplaceDatum` and the integrand `New.HCParam.laplaceIntegrand`. It also
proves the polar decomposition of an invertible matrix.

## Main definitions and results

* `New.DiscreteSeries.IsLaplaceDatum`: the properties of `j : S →* U(ε) × U(η)` and `φ` that
  Laplace's method uses; `New.HCParam.laplaceIntegrand` is the function that is integrated.
* `New.DiscreteSeries.IsSteep`: the parameter `l` for the signs `ε` is steep with respect to `B`
  and the splitting `e : X ⊕ Fin M ≃ n` of the coordinates.

Notions from other files:
* `New.USign ε`: the unitary group `U(ε)` of the diagonal matrix `signMatrix ε` of the signs `ε`.
* `New.HCParam.lowestKType l`: the highest weight of the lowest `K`-type of the parameter `l`.
* `New.HCParam.dsCoeff l`: the matrix coefficient of that `K`-type, as a function of a matrix.

## Relation to the literature

See `New.Appendix.DiscreteSeries.Localization` for related work.


### `exists_unitary_mul_posSemidef`

 Polar decomposition: an invertible matrix is a unitary matrix times a positive semidefinite
matrix. 

 ### The setting of Laplace's method 

### `_root_.New.HCParam.phase`

 The difference `tr (μ Y) - tr (μ' Y')` of the two phases at `x = (Y, Y')`, where `μ` and `μ'`
are the weights of the lowest `K`-types of `l` and `k`, as diagonal matrices. 

### `IsSteep`

 The parameter `l` for the signs `ε` is steep with respect to `B` and the splitting
`e : X ⊕ Fin M ≃ n` of the coordinates: on `X` the sign is `+1` and the weight of the lowest
`K`-type is `0`; on the other `M` coordinates the signs are `+, -, +, …` and the weight decreases
strictly in `[-3 B, -B]`. 

### `IsSteep.sign_inl`

 The sign `ε` is `+1` on `X`. 

### `IsSteep.sign_inr`

 On the other `M` indices the signs alternate, starting with `+1`. 

### `IsSteep.weight_eq_zero`

 The weight `l.lowestKType` of the lowest `K`-type is `0` on `X`. 

### `IsSteep.weight_strictAnti`

 On the other `M` indices the weight is strictly decreasing. 

### `IsSteep.weight_mem`

 On the other `M` indices the weight lies between `-3 B` and `-B`. 

### `subOnePair`

 The pair `(g - 1, g' - 1)` for the two components `g`, `g'` of `j s`. 

### `_root_.New.HCParam.laplaceIntegrand`

 The function to which Laplace's method applies: the coefficient of `l` at the first
component of `j s`, times the conjugate of the coefficient of `k` at the second, times
`exp (-φ s)`, for a function `φ` on `S` (under `IsLaplaceDatum`, the difference of the two phases).


### `IsLaplaceDatum`

 The properties of `j : S →* U(ε) × U(η)` and `φ` that Laplace's method uses: `l` is steep, the
difference of the two phases is an additive and imaginary function `φ`, the two traces agree, the
weights of `k` are nonnegative, at most `3 B` if `η` takes both signs, and zero on the image of
`τ`, where the signs are `+1`, and the image of `j` contains a diagonal copy of `U(X)`. 

### `IsLaplaceDatum.phase_eq`

 `φ s` is the difference of the two phases at `j s - 1`. 

### `IsLaplaceDatum.trace_eq`

 The two components of `j s`, minus `1`, have the same trace. 

### `IsLaplaceDatum.phase_mul`

 The function `φ` is additive. 

### `IsLaplaceDatum.re_phase_eq_zero`

 The function `φ` is purely imaginary. 

### `IsLaplaceDatum.sign_weight_right`

 In the second factor the sign is `+1` and the weight `k.lowestKType` is `0` on the image
  of `τ`. 

### `IsLaplaceDatum.weight_nonneg_and_le`

 The weight `k.lowestKType` is nonnegative, and at most `3 B` at each index whose sign
  differs from that of some other index; if `η` takes both signs, this is every index. 

### `IsLaplaceDatum.exists_diagonal`

 The image of `j` contains a diagonal copy of `U(X)`, placed by `e` in the first factor and by
  `τ` in the second: `inclMatrix ℂ σ` is the matrix of the map `σ` of indices, whose column `x`
  is the standard basis vector at `σ x`. 
