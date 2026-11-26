---
{
  "module": "src/New/Spanning/MainTerm/SieveSystem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sieve systems over places: products, positivity and lower semicontinuity

An abstract sieve. A system `New.SieveSystem` over a ring `C` with a measure (a place, or a product
of places) consists of forms `J i p q`, `i ≤ n + 1`, on pairs of sequences ("heads"), each but the
last the integral of the next one over a common entry, with bounds `B₀`, `Λ`, `β`.

* `New.SieveSystem.pi`: a product of finitely many systems on `ℂ` (one for each real
  place in the application) and one more system is a system.
* `New.SieveSystem.integrable_sum_update`, `New.SieveSystem.integral_sum_update`,
  `New.SieveSystem.norm_integral_mul_sum_update_le`: sum the forms `J (i + 1)` over all pairs of
  heads from one finite family, with a common entry at position `i ≤ n`. The sum is integrable in
  the common entry, its integral is the sum of the `J i`, and its twisted integrals are bounded by
  `β` and `Λ`. `New.SieveSystem.integrable_and_integral_sum_update` collects the three.
* `New.SieveSystem.sum_nonneg`, `New.SieveSystem.lowerSemicontinuousAt_sum`: such a sum is
  nonnegative, and its real part is lower semicontinuous in a parameter `x : C` at each point where
  every head is continuous. `New.SieveSystem.sum_nonneg_and_lowerSemicontinuousAt` collects the two.
* `New.dampedPower`, `New.headWeight`: the decay in the frequency and the weights `Λ` of the heads
  at the real places.

## Relation to the literature

See `New.Spanning.MainTerm.GlobalSieve` for related work.


### `dampedPower`

 The gain at the ratio `r`: the function `r ^ k * min 1 r ^ 6`. 

### `headWeight`

 The weight of a head `p` (with entries in `ℂˣ`) of length `i` at a real place. It is zero unless
the partial products `δ = p 0 * ⋯ * p l`, `l < i`, have modulus at most `R`, and then it is the
product of the numbers `max 1 ‖δ‖⁻¹ ^ K`. 

### `SieveSystem`

 The axioms of the sieve at a place or a product of places: `C` is a ring with a measure, `u c`
is the entry given by `c ∈ C`, and `ι` maps entries back to `C` (in the applications `x ↦ x⁻¹`,
times a constant at the finite places). The forms `J i p q`, `i ≤ n + 1`, pair two sequences of
entries, called heads, with weights `Λ i p`. The field `integrable_and_integral_update` makes each
form but the top one the integral of the next over a common entry, and bounds the same integral
twisted by `ψ (ξ * c)` at a unit `ξ` in terms of the decay `β ξ`. The top form `J (n + 1)` is
continuous, and positive semidefinite on heads with a common entry at position `n`. The bottom form
`J 0` has modulus at most `En`. 

### `SieveSystem.psi_zero`

 The function `ψ` takes the value `1` at `0`. 

### `SieveSystem.integrable_and_integral_update`

 For `i ≤ n`, give both heads the entry `u c` at position `i`. Then `ψ (ξ * c)` times the form
  `J (i + 1)` is integrable in `c`; its integral is `J i p q` if `ξ = 0`, and has modulus at most
  `β ξ * (Λ i p * Λ i q)` if `ξ` is a unit. 

### `SieveSystem.posSemidef`

 The top form `J (n + 1)` is a positive semidefinite kernel on heads with the same entry at
  position `n`. 

### `SieveSystem.continuous`

 The top form `J (n + 1)` is jointly continuous. 

### `SieveSystem.norm_bot_le`

 The bottom form `J 0` has modulus at most `En`. 

### `SieveSystem.norm_le_of_isUnit_sub`

 For `i < n`, if `ξ = ι (p i) - ι (q i)` is a unit, then `J (i + 1) p q` has modulus at most
  `β ξ * (Λ (i + 1) p * Λ (i + 1) q)`. 

### `norm_prod_mul_le_prod_mul`

 Bounds on the norms of finitely many complex factors `f v` and of one more factor `a` multiply
to a bound on the norm of their product. 

### `posSemidef_prod_mul`

 Schur's product theorem for finitely many kernels: the entrywise product of positive
semidefinite kernels `A v` over `v ∈ s` and `B` is positive semidefinite. 

### `headAt`

 The component at the complex factor `v` of a head `p` with entries in `(τ → ℂˣ) × U`: the
sequence `k ↦ (p k).1 v`. 

### `SieveSystem.integrable_mul_update`

 For `i ≤ n`, give both heads the entry `u c` at position `i`. Then `ψ (ξ * c)` times the form
`J (i + 1)` is integrable in `c`. 

### `SieveSystem.integrable_update`

 For `i ≤ n`, the form `J (i + 1)` is integrable in a common entry `u c` at position `i`. 

### `SieveSystem.integral_update`

 The recursion: for `i ≤ n`, the form `J i` is the integral of `J (i + 1)` over a common entry
`u c` at position `i`. 

### `SieveSystem.norm_integral_mul_update_le`

 For `i ≤ n` and a unit `ξ`, the integral of `J (i + 1)` over a common entry `u c` at position
`i`, twisted by `ψ (ξ * c)`, has modulus at most `β ξ * (Λ i p * Λ i q)`. 

### `SieveSystem.pi`

 A finite product of sieve systems is a sieve system.

Let `K` be such a system on `C` (with s-finite volume), and for each `v` in the finite type `τ` take
a system on `ℂ` with forms `J' v`, bounds `B₀' v`, `Λ'`, `γ v`, entry map `unitOrOne`, map `ι'` back
to `ℂ` and twist `wave`. Then the products of the forms, twists and bounds make a system on
`(τ → ℂ) × C`, each form and weight being evaluated on the components of the heads in its factor:
`headAt v p = fun k ↦ (p k).1 v` at `v`, and `Prod.snd ∘ p` in `U`. 

### `SieveSystem.integrable_sum_update`

 For `i ≤ n` and finitely many heads `a p`, the sum of `J (i + 1)` over all pairs of heads is
integrable in a common entry `u c` at position `i`. 

### `SieveSystem.integral_sum_update`

 The recursion summed over all pairs from finitely many heads `a p`: for `i ≤ n`, the sum of the
forms `J i` is the integral of the sum of the forms `J (i + 1)` over a common entry `u c` at
position `i`. 

### `SieveSystem.norm_integral_mul_sum_update_le`

 For `i ≤ n`, finitely many heads `a p` and a unit `ξ`, sum the forms `J (i + 1)` of the system
`K` over all pairs of heads with a common entry `u c` at position `i`. The integral of this sum
twisted by `ψ (ξ * c)` has modulus at most `β ξ * (∑ p, Λ i (a p)) ^ 2`, with `Λ` the head weights
and `β` the decay of `K`. 

### `SieveSystem.integrable_and_integral_sum_update`

 The summed recursion in one statement: for `i ≤ n`, let `F c` be the sum of the forms
`J (i + 1)` over all pairs from finitely many `heads` with entry `u c` put at position `i`. Then
`F` is integrable, its integral is the sum of the forms `J i`, and for a unit `ξ` the integral of
`ψ (ξ * c) * F c` has modulus at most `β ξ * (∑ p, Λ i (heads p)) ^ 2`, with `Λ` the head weights
and `β` the decay of the system. 

### `SieveSystem.sum_nonneg`

 In a sieve system `K` with forms `J`, if finitely many heads `a p` have a common entry `t` at
position `i ≤ n`, then the sum of `J (i + 1)` over all pairs of heads is a nonnegative real
number. 

### `SieveSystem.lowerSemicontinuousAt_sum`

 In a sieve system `K` with forms `J`, let finitely many heads `b y p`, depending on `y : C`,
have a common entry `c y` at position `i ≤ n` for each `y`. The sum of `J (i + 1)` over all pairs
of heads, which is a nonnegative real number, is lower semicontinuous in `y` at each point `x` where
the heads are continuous. This is stated for `ENNReal.ofReal` of its real part. 

### `SieveSystem.sum_nonneg_and_lowerSemicontinuousAt`

 In a sieve system `K` with forms `J`, let finitely many sequences `heads x p` have a common
entry `entry x` at position `i ≤ n` for each `x`. Then the sum `F x` of `J (i + 1)` over all pairs
of heads is a nonnegative real number, and `ENNReal.ofReal` of its real part is lower semicontinuous
at each `x` where the heads are continuous. 
