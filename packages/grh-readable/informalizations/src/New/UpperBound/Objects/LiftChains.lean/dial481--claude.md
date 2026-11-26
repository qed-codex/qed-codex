---
{
  "module": "src/New/UpperBound/Objects/LiftChains.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chains of theta lifts, jointly invariant combinations, and free levels

This file treats chains of theta lifts and their jointly invariant combinations for a general
tower of finite adelic unitary groups joined by theta kernels. It shows that, in bounded rank, the
levels that reduce to `1` at the chosen places are free, that is, that they have trivial
stabilisers `New.classAut`. The chosen places of `E = D.E` are the prime divisors of
`New.Data.piM`; `D.f` is the number of infinite places of `E`. For every integral level in bounded
rank, the orders of the stabilisers divide `New.Data.chosenGroupOrder`.

## Main definitions and results

* `New.chain`: the composite of the first `j` lifts. It is equivariant (`New.chain_equivariant`),
  and its values are linear in the pure tensor of the data
  (`New.exists_linearMap_chain_eq_apply_pure`).
* `New.IsJointlyInvariant.sum_chain_mem_nsmul`: at free levels, a jointly invariant combination of
  chains is a sum with one term for each tuple of double cosets, with no denominators.
* `New.Data.principalLevel_le_chosenLevel`, `New.Data.classAut_eq_bot_of_le_chosenLevel`: in bounded
  rank, levels that reduce to `1` at the chosen places are free.
* `New.Data.card_classAut_dvd_chosenGroupOrder`: in rank at most `2 * D.n D.m` and for every
  integral level the stabilisers have order dividing `chosenGroupOrder`.

Notions from other files:
* `New.TensorChain`: The complex tensor product S_{j−1} ⊗ ⋯ ⊗ S_0, equal to ℂ for j = 0.
* `New.classAut`: `classAut Γ K g` is Γ ∩ gKg⁻¹, the stabiliser in Γ of the coset gK; here
  Γ = `stdRatPoints` is the rational unitary group of the standard definite space `New.stdSpace`,
  inside the finite adelic group.
* `New.Data.n`: The rank 𝗇_j = k + j(t + 1) of X_j.



## Chains of theta lifts and jointly invariant combinations

A tower of finite adelic unitary groups `Gf E (n j)` is joined by theta kernels `k j`
(`New.Kernel`). Each kernel lifts forms on `Gf E (n j)` to forms on `Gf E (n (j + 1))`
(`New.Kernel.lift`). The forms of stage `j` take values in the Weyl module
`WeylIndex (n j) κ → ℂ` of weight `(κ, e j)`. The kernel `k j` has a space of data `S j`, an action
`ω` of the pair of groups on `S j`, and a map `jetMap` that sends a datum to a linear map from the
Weyl module of stage `j` to that of stage `j + 1`.

For a set `A`, `n • A` is the set of sums of `n` elements of `A`.


### `chain`

 The chain of j theta lifts with data Φ_0, …, Φ_{j−1}. It is the composite linear map from
algebraic forms of stage 0 to algebraic forms of stage j. The forms `AlgForm (n j) κ (e j)` of
stage j are the smooth functions on `Gf E (n j)` that transform under the rational points by the
weight with `κ τ h` columns of height `h` and the power `e j τ` of the determinant at `τ`. 

### `TensorChain.lift_kernelLift_map_omega`

 Equivariance of the chain of lifts. For each `j`, `k j` is a theta kernel with data `S j` from
algebraic forms on `Gf E (n j)` of weight `(κ, e j)` to forms on `Gf E (n (j + 1))` of weight
`(κ, e (j + 1))`. Its lift `(k j).lift` sends a datum and a form to the lifted form. Its action
`(k j).ω` is an action of `Gf E (n j) × Gf E (n (j + 1))` on `S j`. The chain `lift` applies the
first `m` lifts in turn to a form `φ`, using the factors of a tensor `t` of data. Let `a j` lie in
`Gf E (n j)` for every `j`, and move each factor `j` of `t` by `(k j).ω (a j, a (j + 1))`. The chain
with the moved data, applied to the right translate of `φ` by `a 0`, is the right translate by `a m`
of the chain with the data `t` applied to `φ`. 

### `TensorChain.lift_algFormRep_of_map_eq`

 Moving an element to the source of a chain of lifts. Let `z i` lie in the group of stage `i`,
with `ω(z i, z (i + 1)) = 1` for every lift, let `t` be any tensor of the data of the first `m`
lifts, and let `j < m`. If `ω(1, z (j + 1))`, acting alone on the factor of the lift from stage
`j` to stage `j + 1`, fixes `t`, then the chain with data `t` has the same value at `φ` and at
the right translate of `φ` by `z 0`. 

### `chain_equivariant`

 Let `φ` be fixed by the level `K 0`, and let each `a j` lie in `K j`. Acting on each datum `Φ i`
by `(a i, a (i + 1))` and applying the chain to `φ` gives the right translate by `a j` of the chain
applied to `φ`. 

### `doubleLiftChain`

 The chain of p pairs of theta lifts, the i-th pair with datum Φ_i in S_{2i} ⊗ S_{2i+1}: a
linear map from forms of stage 0 to forms of stage 2p. 

### `twoKernelAction`

 For a_j in `Gf E (n j)`, the operator ω(a_{2i}, a_{2i+1}) ⊗ ω(a_{2i+1}, a_{2i+2}) on the space
S_{2i} ⊗ S_{2i+1}. 

### `exists_linearMap_chain_eq_apply_pure`

 Fix `φ` and `g`. The value at `g` of the chain applied to `φ` is a linear function
`β : TensorChain S j →ₗ[ℂ] (WeylIndex (n j) κ → ℂ)` of the pure tensor `Φ (j - 1) ⊗ ⋯ ⊗ Φ 0` of the
data. 

### `IsJointlyInvariant`

 Joint invariance: the tensor ∑_{x∈s} L_x ⊗ Φ_{x,m−1} ⊗ ⋯ ⊗ Φ_{x,0} is unchanged by the joint
action of every tuple a with a_j ∈ K_j and a_j = 1 for j ≥ m, as tested against all linear maps β
from S_{m−1} ⊗ ⋯ ⊗ S_0 to the Weyl module `WeylIndex (n m) κ → ℂ` of stage m. Here a acts on Φ_{x,j}
by ω(a_j, a_{j+1}), and the coefficients L_x are linear maps from that Weyl module to `M`. 

### `classPoints`

 Representatives of the classes `c j` for `j < m`, followed by the points `g j` for `m ≤ j`. 

### `kernelProduct`

 The product of the first `m` kernels, applied to the value of `φ` at `g 0`. Factor `j` is the
linear map `jetMap` between the Weyl modules of stages `j` and `j + 1` that belongs to the datum
`Φ j` moved by the action `ω` of the pair of points `(g j, g (j + 1))`. 

### `kernelProduct_succ`

 The product of `m + 1` kernels is the last kernel applied to the product of the first `m`. 

### `sum_classPoints_succ`

 A sum over tuples of `m + 1` double cosets, sorted by the last one. For a tuple `c` of classes
`c j` in `StdClasses (K j)`, the family `classPoints c g` lists their chosen representatives and
continues with the points `g j`. The sum of `F` over the tuples of length `m + 1` is the sum, over
the last class `r`, of the sums over the tuples of length `m`, where the point `g m` is replaced by
the representative `r.out`. 

### `IsJointlyInvariant.sum_chain_eq_sum_kernelProduct`

 **A chain of lifts is a plain sum.** Let `k j` be theta kernels from stage `j` to stage `j + 1`,
and let `φ : AlgForm (n 0) κ (e 0)` be an algebraic form of stage `0` fixed by the level `K 0`. Let
`∑ x ∈ s, L x ⊗ Φ x` be jointly invariant: it is unchanged when elements `a j ∈ K j`, `j < m`, move
each datum `Φ x j` by `ω(a j, a (j + 1))`, with `a m = 1`. Let the levels `K j`, `j < m`, have
trivial stabilisers `classAut`. Then ∑_x L_x(value at `g m` of the chain with data `Φ x` applied to
`φ`) is the sum, over tuples `c` of double cosets `StdClasses (K j)`, `j < m`, of ∑_x
L_x(`kernelProduct`). 

### `kernelProduct_induction`

 Let `P j g v` be a property of a point `g` of the group of stage `j` and a vector `v` of the
Weyl module of stage `j`. If `P` holds for the values of the form `φ`, and each of the first `m`
kernels `k j` with datum `Φ j` takes vectors with `P` at stage `j` to vectors with `P` at stage
`j + 1`, then `P` holds for the product `kernelProduct` of these kernels at any tuple of points. 

### `apply_kernelProduct_le_prod_mul`

 Let `size j g v` be a size of a vector `v` of the Weyl module of stage `j` at a point `g`, and
let `r j ≥ 0` for every `j`. If the kernel `k j` with datum `Φ j` multiplies the size by at most
`r j` for `j < m`, and the values of the form `φ` have size at most `B`, then the product
`kernelProduct` of the first `m` kernels has size at most `(∏ j < m, r j) * B`. 

### `IsJointlyInvariant.sum_chain_mem_nsmul`

 Let `φ : AlgForm (n 0) κ (e 0)` be an algebraic form of stage `0` fixed by the level `K 0`. Let
`∑ x ∈ s, L x ⊗ Φ x` be jointly invariant for the theta kernels `k j`: it is unchanged when
`a j ∈ K j`, `j < m`, move each datum `Φ x j` by `ω(a j, a (j + 1))`, with `a m = 1`. Let the levels
`K j`, `j < m`, have trivial stabilisers `classAut`. Let the property `P` hold for the values of
`φ`, and let each kernel preserve `P`. Let `p` be a point of the group of stage `m`, and let
`∑ x ∈ s, L x (v x)` lie in `A` whenever the vectors `v x` have `P` at `p` and are the images of the
pure tensors of the data `Φ x` under one linear map. Then the value at `p` of the combination of the
chains applied to `φ` is a sum of elements of `A`, one for each tuple of double cosets in
`StdClasses (K j)`, `j < m`. 


## Chosen places, the chosen group order and free levels

These are facts on the places of `E` that the data single out: the places above the level prime
`D.N`, and the chosen places, with `D.ChosenPlace i` the chosen places above the prime
p_i = `D.levelPrime i`. The map `D.chosenPlace` sends a pair `(i, w)` to the place `w`.

* `New.Data.chosenGroupOrder`: the order of the product of the groups `GL (r t)` over the residue
  fields at the chosen places.
* `New.Data.card_pi_GL_chosenPlace`, `New.Data.log_chosenGroupOrder_le`: the order of such a product
  in terms of the primes p_i, and the bound `log chosenGroupOrder ≤ D.x ^ 32`.


 ### Places above the level and chosen places 

### `nonempty_infinitePlace_equiv_chosenPlace`

 The infinite places `D.Φ` of E are in bijection with the chosen places above the prime
p_i = `D.levelPrime i`. 

### `chosenEquiv`

 A chosen bijection from the infinite places of E to the chosen places above p_i. 

### `v_N_eq_exp_neg_one`

 The level prime N is a uniformiser at each finite place w of E above it: its valuation in the
completion at w is exp(−1). 

### `piN_mul_star_eq_N_mul_one`

 The equation π π̄ = N for π = `D.piN`, with the cofactor `1` written out, as the lemmas on
primes `≡ 1` modulo `P.q₁ D.towerExp * P.d` take it. 

### `intValuation_piN`

 The factor π = `D.piN` of the level N = π π̄ is a uniformiser at each finite place `w` that
divides it: if `D.piN ∈ w`, then `w.intValuation D.piN = exp (-1)`. 

### `intValuation_piM`

 The integer `D.piM`, whose prime divisors are the chosen places, is a uniformiser at each place
that divides it. 

### `chosenGroupOrder`

 The product, over the chosen places above `D.levelPrime 0` and `D.levelPrime 1`, of the orders
of the groups `GL (r t)` over the residue fields, for the rank r = `D.r` and t = `D.t` = 5 r. It is
a common multiple of the orders of the stabilisers in
`New.Data.card_classAut_dvd_chosenGroupOrder`. 

### `prod_q_chosenPlace`

 The norms `w.q` of the chosen places `w` above p₀ and p₁ have product M^f, where
M = `D.M` = p₀ p₁ and f = `D.f` is the number of infinite places of E. 

### `card_GL_resField_eq_card_GL_zmod`

 At a chosen place `w` above the prime p_i = `D.levelPrime i`, the group GL_l over the residue
field at `w` has the same order as GL_l over the field with p_i elements. 

### `card_pi_GL_chosenPlace`

 The product of the groups GL_l(𝔽_w) over the chosen places w above p₀ and p₁ has order
∏_i |GL_l(𝔽_{p_i})|^f, where p_i = `D.levelPrime i` and f is the number of infinite places of E:
there are f chosen places above each p_i. 

 ### The principal level and the orders of stabilisers 

### `chosenLevel`

 The elements of the finite adelic unitary group on the index set `n` that are integral and
reduce to `1` at every chosen place, that is, at every prime divisor of `D.piM`. 

### `isChosen_star_iff`

 Of a place `w` above the prime `D.levelPrime i` and its conjugate, exactly one is chosen. 

### `card_GL_dvd_chosenGroupOrder`

 For a finite index type `n` with at most `D.r * D.t` elements, the order of the product of the
groups `GL n (ResField w)`, over the chosen places w above `D.levelPrime 0` and `D.levelPrime 1`,
divides `D.chosenGroupOrder`. 

### `isConjApart_chosenPlace`

 The chosen places, indexed by the pairs (i, w) with w a chosen place above p_i, are pairwise
distinct, and none is the conjugate of one of them. 

### `range_chosenPlace`

 The places `D.chosenPlace x`, for x = (i, w) with w a chosen place above p_i, are exactly the
chosen places. 

### `principalLevel_le_chosenLevel`

 If `D.piM`, whose prime divisors are the chosen places, divides the integer `a` of E, the
principal congruence subgroup of level `a` is contained in `New.Data.chosenLevel`. 

### `classAut_eq_bot_of_le_levelOf_chosenPlace`

 Let K be a subgroup of the integral points of the finite adelic unitary group on `n` whose
elements reduce to `1` at the chosen places above the prime `D.levelPrime i`. If `n` has at most
`4 * D.n D.m` elements, four times the rank of the last stage, the stabiliser of each coset gK in
the rational unitary group is trivial. 

### `classAut_eq_bot_of_le_chosenLevel`

 If n has at most `2 * D.n D.m` elements, every subgroup K of `New.Data.chosenLevel` is
sufficiently small: the stabiliser of each point gK in the rational unitary group is trivial. 

### `card_classAut_dvd_chosenGroupOrder`

 For the standard definite hermitian space on an index set `n` with at most `2 * D.n D.m`
elements, a subgroup K of the stabiliser of the standard lattice and any finite adelic g, the
stabiliser of gK in the rational unitary group has order dividing `New.Data.chosenGroupOrder`.

A consequence of a unitary variant of Minkowski's lemma on integral matrices of finite order. 

 ### The residue characters, and size bounds 

### `chiMLocal_zpow_ne_one_iff_isChosen`

 The character `D.chiMLocal w` of the residue field at `w` is trivial unless `w` is chosen, and
then it has order `P.q₂ D.towerExp = (P.q₀ * P.d) ^ (D.towerExp + 6)`, which exceeds `8 * D.m`. For
an integer `n` with `n ≠ 0` and `|n| ≤ 8 * D.m`, where `D.m` is the number of lifts, its `n`-th
power is nontrivial exactly when `w` is chosen. 

### `instance : D.HasLogUpper (P.q₂ D.towerExp) (D.logB / 9)`

 The number `q₂ = (q₀ d) ^ (s + 6)` with `s = D.towerExp`, which is the order of the residue
characters `D.chiMLocal w` at the chosen places, is at most `exp (log b / 9)`, where
`log b = D.logB`. 

### `log_chosenGroupOrder_le`

 The logarithm of `D.chosenGroupOrder` is at most `D.x ^ 32`, where `D.x = exp D.logX` is a scale
of the data `D`. 

### `instance : D.HasLogUpper (log D.chosenGroupOrder) (32 * D.logX)`

 The bound `log chosenGroupOrder ≤ D.x ^ 32 = exp (32 * D.logX)`, as a logarithmic upper
bound. 
