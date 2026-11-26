---
{
  "module": "src/Lib/General/LinearAlgebra/TensorChains.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/TensorChains.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/TensorChains.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chains of linear maps, tensor products of their data, and separation by forms

The file composes initial segments of a chain of linear maps and computes the index of the
stabiliser of a nonzero vector in a finite general linear group. It extends a chain of bilinear
steps from pure data to arbitrary tensors of the data.

## Main definitions and results

* `New.index_stabilizer_GL_vector`: over a finite field `F`, the stabiliser in `GL n F` of a nonzero
  vector has index `|F| ^ |n| - 1`, by orbit-stabiliser.
* `New.TensorChain`: the tensor product `S (j-1) ⊗ (⋯ ⊗ (S 0 ⊗ ℂ))`, which is `ℂ` for `j = 0`.
* `New.TensorChain.lift`, `New.TensorChain.lift_pure`: for `x` in `M 0`, the linear map to `M j`
  that sends a pure tensor to the composite (`New.compUpTo`) of the maps `b i (f i)`, `i < j`,
  applied to `x`.
* `New.TensorChain.ofPairs`, `New.TensorChain.lift_ofPairs`: data of double steps regrouped into
  single factors.
* `New.tensor_eq_zero_of_separating`: over a principal ideal domain, if the forms `f i` on `U` have
  no common zero but `0` and `V` is torsion-free, then the maps `U ⊗ V → V`,
  `u ⊗ v ↦ f i u • v`, have no common zero but `0`.



## Composites of chains and the stabiliser of a vector in a finite GL

* `New.exists_GL_smul_single`: a vector with a unit entry is a column of an invertible matrix.


### `New.compUpTo`

 For linear maps `L i : M i → M (i + 1)`, the composite `L (j-1) ∘ ⋯ ∘ L 0 : M 0 → M j`; the
identity for `j = 0`. 

### `New.exists_GL_smul_single`

 Over a commutative ring, a vector with a unit entry is, for any `i`, the `i`-th column
`g • Pi.single i 1` of an invertible matrix `g`. 

### `New.index_stabilizer_GL_vector`

 Over a finite field `F`, the stabiliser in `GL n F` of a nonzero vector has index
`|F| ^ |n| - 1`, the number of nonzero vectors. 


## Iterated tensor products of data and the multilinear chain of maps

A chain of bilinear steps `b j : S j → M j → M (j + 1)` is multilinear in its data, so it factors
through the tensor product of the spaces `S j`, and so extends from pure data to arbitrary tensors.


### `New.TensorChain`

 The complex tensor product `S (j-1) ⊗ (⋯ ⊗ (S 0 ⊗ ℂ))`, equal to `ℂ` for `j = 0`. Below it is
written `S (j-1) ⊗ ⋯ ⊗ S 0`, the last factor `ℂ` (and `1` in pure tensors) being left out. 

### `pure`

 For a family of vectors `f i` in `S i`, the pure tensor `f (j-1) ⊗ ⋯ ⊗ f 0` in
`S (j-1) ⊗ ⋯ ⊗ S 0`; it is `1 : ℂ` for `j = 0`. 

### `liftInPairs`

 Two steps at once: the linear map from `S (2 * i) ⊗ S (2 * i + 1)` to
`Hom (M (2 * i), M (2 * i + 2))` sending `s ⊗ s'` to `b (2 * i + 1) s' ∘ b (2 * i) s`. 

### `lift`

 For bilinear maps `b i : S i → M i → M (i + 1)` and `x` in `M 0`, the linear map from
`S (j-1) ⊗ ⋯ ⊗ S 0` to `M j` that sends `f (j-1) ⊗ ⋯ ⊗ f 0` to
`(b (j-1) (f (j-1)) ∘ ⋯ ∘ b 0 (f 0)) x`. 

### `lift_succ_tmul`

 On `s ⊗ z`, the lift of length `j + 1` applies the step `b j s` to the lift of `z`. 

### `lift_pure`

 On the pure tensor `f (j-1) ⊗ ⋯ ⊗ f 0`, the map `lift b x j` takes the value
`(b (j-1) (f (j-1)) ∘ ⋯ ∘ b 0 (f 0)) x`, the composite `compUpTo` of the steps applied to `x`. 

### `lift_sub`

 The lift is additive in the starting vector: at `x - y` it is the difference of the lifts at `x`
and at `y`. 

### `map`

 For endomorphisms `t i` of `S i`, the endomorphism `t (j-1) ⊗ ⋯ ⊗ t 0` of
`S (j-1) ⊗ ⋯ ⊗ S 0`; the identity of `ℂ` for `j = 0`. 

### `map_pure`

 The map `t (j-1) ⊗ ⋯ ⊗ t 0` sends the pure tensor `f (j-1) ⊗ ⋯ ⊗ f 0` to the pure tensor
with factors `t i (f i)`. 

### `pure_smul`

 Scaling the factor `f j` by `c j` for each `j < m` scales the pure tensor
`f (m-1) ⊗ ⋯ ⊗ f 0` by the product of the `c j`. 

### `pure_congr`

 The pure tensor `g (m-1) ⊗ ⋯ ⊗ g 0` depends only on the factors of index less than `m`. 

### `pure_sum`

 Multilinearity: the pure tensor of the finite sums `∑ a, g j a`, `j < n`, is the sum over the
tuples of indices `y` of the pure tensors of the terms `g j (y j)`. Here `F y` is any family with
`F y j = g j (y j)` for `j < n`. 

### `liftInPairs_tmul`

 The double step with datum `s ⊗ s'` is the step `b (2 * i) s` followed by
`b (2 * i + 1) s'`. 

### `compUpTo_liftInPairs_tmul`

 Let `b j : S j →ₗ M j →ₗ M (j + 1)` be bilinear steps and `f j : S j`. Composing the double
steps `liftInPairs b i (f (2 * i) ⊗ₜ f (2 * i + 1))` for `i < p` gives the same value at `x` as
composing the single steps `b j (f j)` for `j < 2 * p`. 

### `ofPairs`

 For data `τ i` in `S (2 * i) ⊗ S (2 * i + 1)` of `p` double steps, the tensor
`τ (p-1) ⊗ ⋯ ⊗ τ 0` regrouped into `2 * p` single factors. 

### `lift_ofPairs`

 The chain of `2 * p` steps with the regrouped tensor `ofPairs τ p` as data is the composite of
the `p` double steps with data `τ i`. 

### `map_ofPairs`

 Acting by `t j` on each factor of the regrouped tensor `ofPairs τ p` is acting by
`t (2 * i) ⊗ t (2 * i + 1)` on each `τ i`. 

 ## Linear forms separating the points of a tensor product 

### `New.tensor_eq_zero_of_separating`

 Let `R` be a principal ideal domain, `V` a torsion-free `R`-module and `f i` linear forms on
`U` whose only common zero is `0`. An element of `U ⊗ V` killed by all the maps
`u ⊗ v ↦ f i u • v` is `0`. 
