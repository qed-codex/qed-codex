---
{
  "module": "src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Valuations of lifts at non-split primes

This file concerns a non-split prime `p`, for a p-adic place of ℂ. Fix a marked set `Λ` of primes
of `D.E` above `p` (`New.Data.IsMarked`), and write 𝔯 = `D.ceilLogLifts p`. For a weak chain datum
`Ψ` for a twist `ϑ` of level prime to `p`, this file moves Hecke operators at `Λ` from the source
onto the data of the lifts, where each term is a lift evaluated at a neighbor. It then bounds the
gauge of the restricted chain on the image of powers of the scaled Hecke operators.

## Main definitions and results

* `New.Data.IsMarked.ω_ofSplitPlaces_mem_raises`: the bound for one lift evaluated at a neighbor.
* `New.Data.IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_smul`: at a prime of `Λ` of norm
  `q = z ^ 2`, with t = `D.t`, the operator `z ^ ((t + 1) i) * q ^ i.choose 2 • T_i` passes through
  one lift as an integral combination of the Hecke operators `T_{i'}` with i' ≤ i.
* `New.Data.IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_pow_smul`: so for i ≤ 𝔯 the same holds
  with the factor `p ^ (f 𝔯 t)`, where f = `D.f`.
* `New.Data.IsWeakChainDatum.exists_sum_heckeSplit_chain_eq_pow_smul`: the iteration of this over
  the lifts of the chain.
* `New.Data.IsWeakChainDatum.exists_lift_eq_chain_scaledHeckeOperator`: the operators
  `New.Data.IsMarked.scaledHeckeOperator` are moved onto the data of the lifts, with a bound on the
  changed data that involves `New.Data.liftLoss`.
* `New.Data.IsWeakChainDatum.gaugeLe_scaledHeckeOperator_pow`: the bound on the gauge of
  `New.Data.restrictedChain` on the image of the `m`-th power of the product of the operators
  `New.Data.IsMarked.scaledHeckeOperator`.

Notions from other files:
* `New.Data.N`: The level: a chosen prime N ≡ 1 mod q₂² with log N ∈ [λ, λ + √(log b)], where
  λ = `New.Data.logLevelTarget`.
* `New.Data.liftKernel`: The theta kernel of the lift from forms on X_j (`New.Data.FormX`) to forms
  on X_{j+1}. The finite unitary groups of X_j and X_{j+1} act on its data by ω.
* `New.chain`, `New.doubleLiftChain`, `New.TensorChain.lift`: The chain of theta lifts with data
  Φ_0, Φ_1, …, the same chain taken in pairs with data in S_{2i} ⊗ S_{2i+1}, and the chain with a
  tensor of data.
* `New.Data.IsMarked`: Λ is disjoint from its conjugate, each prime of Λ is induced by an a-place,
  and p is an exceptional non-split prime below the bound x₁.

## Relation to the literature

See `New.UpperBound.Divisibility.ValuationAtLevel` for related work.


 ## One lift, evaluated at a neighbor 

### `liftLoss`

 The loss of the lift from `X_j` to `X_{j+1}` evaluated at a neighbor: `𝔯 = D.ceilLogLifts p` for
each low column (height below `n_{j+1}` and different from one) at a place of `placesInducing Λ`,
less the divisibility bound for the set `placesInducing Λ`. 

### `mem_raises_neg_divisibilityBound`

 At a non-split prime `p` (`χ_K(p) ≠ 1`), a standard datum `φ` of level one for the kernel
`D.liftKernel ϑ j` of the lift from `X_j` to `X_{j+1}` multiplies `p`-adic gauges by at most
`p ^ (-D.divisibilityBound p j ∅)`. That is, it raises valuations by the divisibility bound for the
empty set of places. 

### `markedIndices`

 Sets `J l` of row indices at the primes of `Λ`, read at the infinite places: `τ` gets the set
of its induced prime if that lies in `Λ`, and the set of the conjugate prime otherwise. 

### `neighborExponent`

 The exponent of `p` by which a box with index `b` at `τ` is divided when the lift is evaluated
at the neighbor given by `J`: it is `1` on the marked indices at the places inducing a prime of `Λ`,
`-1` on those at the places inducing its conjugate, and `0` elsewhere. 

### `neighborCharge`

 The charge of a box with index `b` in a column of height `h` at `τ`. It is `1` at a place
inducing a prime of `Λ` if `h = 1` and `b` is not marked, and at a place inducing the conjugate of a
prime of `Λ`, for any `h`, if `b` is marked; otherwise it is `0`. 

### `neighborDiagonal`

 The diagonal matrix over the completion at `l` with entry `p` at the indices in `J l` and `1` at
the others. 

### `sum_card_boxes_le`

 Let `T` be a filling by indices in `X_{j+1}` of the Young diagrams with `D.columnCount τ h`
columns of height `h` at each infinite place `τ` of `E`; `(T τ).1 h c b` is the index in box `b` of
column `c` of height `h`. Let `I` be a set of at most `r` indices. Count the boxes at `τ` whose
index lies in `I`, and those in columns of height one whose index does not. There are at most
`D.a + r * D.lowColumns j τ` of them if `τ ∈ D.aPlaces` (the places with `D.a` columns of height
one), and `r * D.lowColumns j τ` elsewhere. 

### `IsMarked.neighborCharge_ne_zero_or_partner`

 Let `J l` be a set of indices for each prime `l`, and let `τ' = -p ^ e τ` be the partner of the
infinite place `τ` for an exponent `e` in `partnerExponents P.d p`. Suppose that the prime induced
by `τ` lies in `Λ`, or that `h = 1` and the prime induced by `τ'` lies in `Λ`. Then the index `b` is
charged in a column of height one at `τ` or in a column of height `h` at `τ'`. 

### `IsMarked.exists_eq_mul_neighborDiagonal_mul`

 Suppose that each component `g l` lies in the double coset `basicDoubleCoset ι l i` of
`diag(ϖ 1_i, 1)` under the group `localIntGL` of integral invertible matrices, for some `i ≤ 𝔯`.
Then `g` is, up to integral invertible factors on both sides, the diagonal `neighborDiagonal p Λ J`
for some sets `J l` of at most `𝔯` indices. 

### `IsMarked.map_ofSplitPlaces_neighborDiagonal`

 Let `Λ` be a marked set of primes of `E = D.E` above `p`. The element
`ofSplitPlaces _ (neighborDiagonal p Λ J)` of the finite adelic unitary group is diagonal with `p`
on `J l` at each `l ∈ Λ`, `p⁻¹` on `J l` at the conjugate of `l`, and `1` elsewhere. For an infinite
place `τ`, read it in `ℂ_[p]` through the extension `adeleExtension` to the finite adeles of the
embedding `weightEmbedding ιₚ τ : x ↦ ιₚ (τ x̄)`, which takes the component at the conjugate of the
prime induced by `τ`. The result is diagonal with entries `p ^ (-neighborExponent Λ J τ b)`. 

### `IsMarked.sum_neighborExponent_mul_lastEntry_eq_zero`

 Let `Λ` be a marked set of primes (`D.IsMarked Λ`). For any `J` and `j`, the sum over places `τ`
of `∑ b, neighborExponent Λ J τ b` times `D.lastEntry (j + 1) τ` is `0`: the weights on `X_{j+1}`
balance a prime of `Λ` against its conjugate. 

### `IsMarked.sum_neighborExponent_add_neighborCharge_le`

 Let `Λ` be a marked set of primes, let `J l` be sets of at most `r` indices in `X_{j+1}` at the
primes `l` of `Λ`, and let `T` be a filling of the diagrams `D.columnCount`. Summed over the boxes
of `T`, the exponents `neighborExponent` plus the charges `neighborCharge` are at most
`∑ l ∈ Λ, heckeScalingExponent l` plus `r` times the number of low columns at the places inducing a
prime of `Λ`. 

### `IsMarked.ω_ofSplitPlaces_mem_raises`

 **One lift, evaluated at a neighbor.** Let `Λ` be a marked set of primes of the CM field
`E = D.E` above `p`, and let `ϑ` be a twist. The finite adelic unitary groups of the definite spaces
`X_j` and `X_{j+1}` act by the twisted Weil action `ω` on the data of the theta lift
`D.liftKernel ϑ j` from forms on `X_j` to forms on `X_{j+1}`. Let `φ` be a standard datum of level
one: a `p`-integral combination of translates of the integral vacuum by points integral above `p`.
Let the component of `g` at each `l ∈ Λ` lie in the double coset `basicDoubleCoset` of
`diag(ϖ 1_i, 1)` for some `i ≤ 𝔯`, with `𝔯 = D.ceilLogLifts p`, the least exponent with `m ≤ p ^ 𝔯`
for `m = D.m` the number of lifts. Then the kernel of the datum `ω (1, g) φ` multiplies `p`-adic
gauges of weight vectors by at most `p ^ (∑ l ∈ Λ, heckeScalingExponent l + liftLoss Λ j)`
(`Kernel.raises`). Here `heckeScalingExponent l` is `D.a` times the number of places in `D.aPlaces`
that induce `l`, and `liftLoss Λ j` is `𝔯` times the number of columns of height below `n_{j+1}` and
different from one at the places inducing a prime of `Λ`, less `D.divisibilityBound`. 

 ## Hecke transfer along the chain of lifts 

### `IsMarked.notMem_asIdeal`

 Let `p` be coprime to the level `ϑ.normQ` of the twist. A prime of a marked set `Λ` above
`p` contains none of this level, the element `D.piMBar` of norm `D.M`, its conjugate `D.piM`
and the prime `D.N`: it contains `p`, which is prime to `ϑ.normQ` and to `D.M * D.N`. 

### `IsMarked.charUnramifiedAt_rankTwist`

 Let `Λ` be a marked set of primes above a prime `p` coprime to the level of `ϑ`. At `l ∈ Λ` the
base change `x ↦ ν(x/x̄)` of the twist `ν = rankTwist` of the character of each lift of the chain,
by a power of the splitting character fixed by the rank, is unramified. 

### `IsWeakChainDatum.projOn_translateDatum_eq_self`

 Let `Ψ` be a weak chain datum for `ϑ`, let `Λ` be a marked set of primes above `p`, a prime
coprime to the norm of `ϑ.Q`, and let `x` be in the support of `Ψ`. At a prime `l` of `Λ` the data
`D.translateDatum x j` of the lifts are the vacuum: the projection to the vacuum at `l` fixes
them. 

### `IsMarked.norm_baseChange_atUniformizer`

 Let `Λ` be a marked set of primes of `E = D.E` above `p`, for the `p`-adic place `ιₚ : ℂ → ℂ_p`,
and let `l ∈ Λ`. For a character `ϑ` of `U(1)(𝔸)` of weight `0` with given tame part, let
`ν = D.chainChar ϑ e` be the character of lift `e` of the chain, the product of
`D.untwistedLiftChar e` and `ϑ ^ e`. The value of the base change `x ↦ ν(x/x̄)` at a uniformizer at
`l` is a `p`-adic unit, as the weights `D.liftWeight e τ` have the same sum over the places `τ` that
induce `l` and over those that induce `star l`. 

### `IsMarked.exists_q_eq_sq`

 A marked prime has norm `p ^ (2 h)` with `2 h ≤ f`, for `f = D.f` the number of infinite places
of `D.E`: the exponent is the order of `D.placeOfInt (-p)`, which is even. 

### `IsWeakChainDatum.exists_heckePolyOp_lift`

 Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on tuples `x = (x_j)`
of finite adelic matrices, of a jointly invariant sum of the tensors `⊗_j D.translateDatum x j`. Let
`p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be a marked set of primes of `E = D.E`
above `p`. Let `l ∈ Λ` have norm `q = z ^ 2`. Write `T(U) = ∑ i, (-U) ^ i q ^ (i choose 2) T_i` for
the Hecke polynomial `heckePolyOp`. Let `Θ` be the theta lift from forms on `X_e` to forms on
`X_{e+1}` with datum `D.translateDatum x e`, for `x` in the support of `Ψ`. There is a polynomial
`R`, independent of `x`, with `R(0) = 1` and coefficients `p`-integral (in `embValRing`, the complex
numbers integral at the `p`-adic place), such that `Θ` takes each form `φ` spherical at `l` to a
form spherical at `l`, and `T(U) (Θ φ) = R(U) • Θ (T(z ^ (t + 1) U) φ)` for all complex `U`. 

### `heckePolyOp_mul_apply`

 The Hecke polynomial at the split place `l` (`l` differs from `star l`), applied at `s * U` to a
form `φ` on `X_e`, equals `∑ i ≤ D.n e, U ^ i • ((-s) ^ i * l.q ^ (i choose 2)) • T_{l,i} φ`. Here
`T_{l,i}` is `heckeSplit`, and this is the expansion in powers of `U`. 

### `IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_smul`

 **One lift.** Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on tuples
`x = (x_j)` of finite adelic matrices, of a jointly invariant sum of the tensors
`⊗_j D.translateDatum x j`, where `D.translateDatum x j` is the integral vacuum of
`Hom(X_j, X_{j+1})` translated by `x_j`. Let `p` be a prime coprime to the norm of `ϑ.Q`, and let
`Λ` be a marked set of primes of `E = D.E` above `p`. Let `l ∈ Λ` have norm `q = z ^ 2`. Forms on
the definite hermitian space `X_e` of rank `n_e` are algebraic forms of the weight given by
`D.columnCount` and `D.lastEntry e`, with the finite adelic unitary group acting by right
translation (`algFormRep`); spherical at `l` means fixed by the maximal compact group at `l`. Let
`Θ` be the theta lift from forms on `X_e` to forms on `X_{e+1}` with datum `D.translateDatum x e`,
for `x` in the support of `Ψ`; `T_i = heckeSplit … i` is the Hecke operator of the double coset of
`diag(ϖ 1_i, 1)` at the split prime `l`. On forms spherical at `l`, the values of `Θ` are spherical,
and for `i ≤ n_e` the number `z ^ ((t + 1) i) * q ^ i.choose 2`, with `t = D.t`, times `Θ T_i` is a
combination of the `T_{i'} Θ` with `i' ≤ i` and coefficients that are independent of `x` and
`p`-integral. 

### `pow_mul_pow_choose_two_dvd`

 Let `p` be a natural number, `f = D.f` the number of infinite places of `D.E`, and `t = D.t`,
where the rank grows by `t + 1` at each lift. Put `z = p ^ h` and `q = z ^ 2` with `2 h ≤ f`. For
`i ≤ r ≤ t` the number `z ^ ((t + 1) i) * q ^ i.choose 2 = p ^ (h i (t + i))` divides
`p ^ (f r t)`. 

### `IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_pow_smul`

 **The cost of one lift.** Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the
coefficients, on tuples `x = (x_j)` of finite adelic matrices, of a jointly invariant sum of the
tensors `⊗_j D.translateDatum x j`. Let `p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be
a marked set of primes of `E = D.E` above `p`. Let `l ∈ Λ` and `𝔯 = D.ceilLogLifts p`, the least
exponent with `m ≤ p ^ 𝔯` for `m = D.m` the number of lifts; `f = D.f` is the number of infinite
places of `E` and the rank grows by `t + 1` at each lift, `t = D.t`. Let `Θ` be the theta lift from
forms on `X_e` to forms on `X_{e+1}` with datum `D.translateDatum x e`, for `x` in the support of
`Ψ`; `T_i = heckeSplit … i` is the Hecke operator of the double coset of `diag(ϖ 1_i, 1)` at the
split prime `l`. On forms spherical at `l`, the values of `Θ` are spherical, and for `i ≤ 𝔯` the
operator `p ^ (f 𝔯 t) Θ T_i` is a combination of the `T_{i'} Θ` with `i' ≤ i` and coefficients that
are independent of `x` and `p`-integral. 

### `IsWeakChainDatum.exists_sum_heckeSplit_chain_eq_pow_smul`

 **Iteration over the lifts.** Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the
coefficients, on tuples `x = (x_j)` of finite adelic matrices, of a jointly invariant sum of the
tensors `⊗_j D.translateDatum x j`. Let `p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be
a marked set of primes of `E = D.E` above `p`. Let `l ∈ Λ` and `𝔯 = D.ceilLogLifts p`, the least
exponent with `m ≤ p ^ 𝔯` for `m = D.m` the number of lifts; `f = D.f` is the number of infinite
places of `E` and the rank grows by `t + 1` at each lift, `t = D.t`. Let `F` be the composite
`chain` of the first `e` theta lifts with data `D.translateDatum x j`, for `x` in the support of
`Ψ`; `T_i = heckeSplit … i` is the Hecke operator of the double coset of `diag(ϖ 1_i, 1)` at the
split prime `l`. On forms spherical at `l`, the values of `F` are spherical, and
`p ^ (e f 𝔯 t) F T_𝔯` is a combination of the `T_i F` with `i ≤ 𝔯` and coefficients that are
independent of `x` and `p`-integral. 

### `mul_le_transferExponent`

 With `𝔯 = D.ceilLogLifts p`, the exponent `j f 𝔯 t` of the power of `p` needed for `j ≤ m` lifts
is at most `D.transferExponent p = 𝔯 f (n_m + 𝔯)`, as `m t ≤ n_m`. 

### `IsWeakChainDatum.liftKernel_omega_translateDatum_of_mem_maxCompactAt`

 Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on tuples `x = (x_j)`
of finite adelic matrices, of a jointly invariant sum of the tensors `⊗_j D.translateDatum x j`. Let
`p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be a marked set of primes of `E = D.E`
above `p`. Let `l ∈ Λ` and let `x` be in the support of `Ψ`. The datum `D.translateDatum x j` of the
theta lift `D.liftKernel ϑ j` from `X_j` to `X_{j+1}` is spherical at `l` for the finite adelic
unitary group `Gf` of `X_{j+1}`: under the twisted Weil action, `ω (1, b)` fixes it for every `b` in
the maximal compact group at `l`. 

### `IsWeakChainDatum.exists_hecke_transfer`

 **Hecke transfer.** Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on
tuples `x = (x_j)` of finite adelic matrices, of a jointly invariant sum of the tensors
`⊗_j D.translateDatum x j`. Let `p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be a marked
set of primes of `E = D.E` above `p`. Let `l ∈ Λ` and `𝔯 = D.ceilLogLifts p`, the least exponent
with `m ≤ p ^ 𝔯` for `m = D.m` the number of lifts. Further, `T_i = heckeSplit … i` is the Hecke
operator of the double coset of `diag(ϖ 1_i, 1)` at the split prime `l`.
* For every `x` in the support of `Ψ`, the datum `D.translateDatum x j` of the theta lift from `X_j`
  to `X_{j+1}` is fixed by the maximal compact group at `l` of `X_{j+1}`, under the twisted Weil
  action `ω`.
* There are numbers `c i`, independent of `x` and `p`-integral if `j < m`, such that on forms
  spherical at `l` the operator `∑ i ≤ 𝔯, c i • T_i` after the composite `chain` of the first
  `j + 1` lifts is `p ^ D.transferExponent p` times the chain after `T_𝔯`. 

 ## The valuation on the image of the scaled Hecke operators 

### `liftTargetRep`

 The action `b ↦ ω (1, b)` of the finite unitary group of `X_{j+1}` on the data of the lift from
`X_j` to `X_{j+1}`. 

### `liftKernel_omega_heckeSplit`

 Let `ω` be the twisted Weil action of the theta lift `D.liftKernel ϑ j`, `a` an element of
the finite adelic unitary group of `X_j`, and `ψ` a datum fixed, under `b ↦ ω (1, b)`, by
`maxCompactAt _ l`, the elements of the maximal compact group
`stdLevel` that are `1` away from the split prime `l` and its conjugate. For `b` in `stdLevel`, the
operator `ω (a, b)` commutes at `ψ` with the Hecke operator of index `i` at `l`. 

### `liftKernel_lift_heckeSplit`

 The lift takes the Hecke operators of the target group on the data to the Hecke operators on
the lifted forms. 

### `IsMarked.ω_heckeSplit_mem_raises`

 Let `Λ` be a marked set of primes of `E = D.E` above `p`, and let `l ∈ Λ`. A tuple `g` of
components at the primes of `Λ` gives an element `ofSplitPlaces _ g` of the group of `X_{j+1}`.
Suppose that for every `u` in the double coset of `diag(ϖ 1_i, 1)` at `l` the action of
`g * Pi.mulSingle l u` sends `ψ` to a datum whose kernel multiplies `p`-adic gauges by at most `c`
(`Kernel.raises`). Then the action of `g` does so with the image of `ψ` under the Hecke operator
`heckeSplit` of this double coset. 

### `IsWeakChainDatum.exists_lift_eq_chain_scaledHeckeOperator`

 Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on tuples `x = (x_j)`
of finite adelic matrices, of a jointly invariant sum of the tensors `⊗_j D.translateDatum x j`. Let
`p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be a marked set of primes of `E = D.E`
above `p`. Let `L` be a list of distinct primes of `Λ`, and let `𝔯 = D.ceilLogLifts p`, the least
exponent with `m ≤ p ^ 𝔯` for `m = D.m` the number of lifts. The finite adelic unitary groups of the
definite spaces `X_j` and `X_{j+1}` act by the twisted Weil action `ω` on the data of the theta lift
`D.liftKernel ϑ j` from forms on `X_j` to forms on `X_{j+1}`; below this kernel is `k`, and `C e` is
the composite of the first `e` lifts with data `D.translateDatum x`. There is a linear map `t` on
the data with three properties for every `x` in the support of `Ψ`, where
`newDatum = t (D.translateDatum x j)`.
* At `D.translateDatum x j`, `t` commutes with `ω (a, b)` for `b` in the maximal compact group
  `stdLevel`.
* For a source form `y`, the lift by `newDatum` of `C j y` is `C (j + 1)` of the image of `y` under
  the product over `l ∈ L` of `IsMarked.scaledHeckeOperator`, which is `p ^ heckeScalingExponent l`
  times the Hecke operator of index `𝔯` at `l`.
* If `j < m` and `g` is trivial at the primes of `L` and in the double coset of some
  `diag(ϖ 1_i, 1)`, `i ≤ 𝔯`, at the other primes of `Λ`, then the kernel of `ω (1, g) newDatum`
  multiplies `p`-adic gauges by at most `p ^ β` (`Kernel.raises`), where `β` is the sum of `∑ l ∈ L,
  (D.transferExponent p - heckeScalingExponent l)`, `∑ l ∈ Λ, heckeScalingExponent l` and
  `liftLoss Λ j`. 

### `IsWeakChainDatum.gaugeLe_scaledHeckeOperator_pow`

 Let `ϑ` be a twist and `Ψ` a weak chain datum for `ϑ`: the coefficients, on tuples `x = (x_j)`
of finite adelic matrices, of a jointly invariant sum of the tensors `⊗_j D.translateDatum x j`. Let
`p` be a prime coprime to the norm of `ϑ.Q`, and let `Λ` be a marked set of primes of `E = D.E`
above `p`. Let `Y` be the product over `l ∈ Λ` of `IsMarked.scaledHeckeOperator`, which is
`p ^ heckeScalingExponent l` times the Hecke operator of index `𝔯 = D.ceilLogLifts p` at `l`, and
let `v` be an integral source form. Apply to `Y ^ m v` the combination `Ψ` of the chains of
`m = D.m` theta lifts with data `D.translateDatum x`, and restrict to the space indexed by `D.Y m`.
Its gauge at the base point `1` is everywhere at most `p ^ c` (`GaugeLe`), where `c` is the sum over
`j < m` of `#Λ * D.transferExponent p + liftLoss Λ j`. 
