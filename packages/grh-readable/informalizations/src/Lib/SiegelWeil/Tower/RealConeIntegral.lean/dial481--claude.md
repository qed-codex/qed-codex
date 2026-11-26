---
{
  "module": "src/Lib/SiegelWeil/Tower/RealConeIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/RealConeIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/RealConeIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The real cone integral

The archimedean Tate integral of a Fock vector over the cone of real isotropic vectors of
`V' = V ⊕ H`, and its convergence in every moment for positive real exponents.

Throughout, `A` and `X` split a hyperbolic plane off `W'` and `V'`, with complements `W` and `V`.

* `PairFock E s t` is the Fock space of `Hom(W, V)` at the infinite places, the type
  `fockSpace (realSigns E (homSigns s t))` that `coneIntegrand` takes values in.
* `lineTermReal A X β a` maps the Fock space of `Hom(W', V')` to that of `Hom(W, V)`; it is the
  archimedean part of the term at `a` in Poisson's formula on the line, on the side that the Boolean
  `β` names.
* `fockMoment N v = ∫ (1 + ‖y‖) ^ N ‖v y‖ dy` is the `N`-th moment of `v`, and `IsSchwartzVector v`
  says that all moments of `v` are finite.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` for sources.


### `realIdele`

 The idele with archimedean component `a` and finite component `1`. 

### `ideleAbs_realIdele_eq_prod`

 The idele norm of the idele with archimedean component `a` and finite component `1` is
`∏ w, ‖a w‖ ^ 2`. 

### `coneIntegrand`

 The integrand of the cone integral at `p = (k, a)`, with `k` in the maximal compact subgroup of
`U(V')`: the line term `lineTermReal A X β a` of `k v`, times the character
`∏ w, (a w / |a w|) ^ (2 μ w)` and the power `z` of the idele norm of `a`. Here `k` acts through its
archimedean component, as the element `(1, k)` of `U(W') × U(V')` in the Weil representation with
weight `targetWeight n' μ` on `U(V')` and `0` on `U(W')`. The two values of `β` give the terms on
the two sides of Poisson's formula on the line (`tsum_lineTerm`). 

### `cone`

 The cone integral: the real Tate integral of `v`, with exponent `z`, over the cone of the
isotropic vectors `k⁻¹ x a`, where `x` spans the isotropic line `X.k` of `V'`, `k` runs over the
maximal compact subgroup of `U(V')` and `a` over the archimedean ideles `(E ⊗ ℝ)ˣ`. 

### `dualCone`

 The cone integral formed with the terms on the other side of Poisson's formula on the line. 

### `exists_sq_rpow_mul_one_add_log_sq_le`

 For `z > 0` the function `y ^ (2 z) (1 + log² y)` of `y > 0` is at most a constant times a power
of `1 + y`. 

### `exists_prod_norm_sq_rpow_le`

 For `z > 0` the power `(∏ w, ‖a w‖ ^ 2) ^ z` is at most a power of `1 + ‖a‖` times a constant
multiple of `∏ w, (1 + log² ‖a w‖)⁻¹`, for `a` with nonzero coordinates. 

### `exists_fockMoment_lineTermReal_le`

 The line term `lineTermReal A X β a v`, the slice of the Fock vector `v` at the point `a` of the
isotropic line, decays rapidly in `a`, in every moment: `(1 + ‖a‖) ^ M` times its `N`-th moment
`fockMoment N` is at most a finite constant, independent of `a` and `v`, times the `(N + M)`-th
moment of `v`. 

### `fockMoment_coneIntegrand`

 The `N`-th moment of the cone integrand at `(k, a)` is `(∏ w, ‖a w‖ ^ 2) ^ z` times the moment
of the line term at `a` of `k v`: the phases and determinants have modulus `1`. On the right the
archimedean component `(k : G E t').1` of `k`, paired with `1 : GInf E s'` on the `W'` side, acts on
`Hom(W', V')` by composition (`pairHomInf`), and on the Fock space by the Weil representation
`realWeil`. 

### `exists_integrable_fockMoment_coneIntegrand_le`

 Let `A` and `X` be base-adapted splittings, by one hyperbolic plane, of `W'` over `W` and of
`V'` over `V`. For `p = (k, a)`, with `k` in the maximal compact subgroup of `U(V')` and
`a ∈ (InfinitePlace E → ℂ)ˣ`, `coneIntegrand A X μ β z v p` is the line term `lineTermReal A X β a`
of `k v` (`k` acting through the Weil representation), times `∏ w, (a w / |a w|) ^ (2 μ w)` and the
`z`-th power of the idele norm of `a`. For `z > 0` and a Schwartz Fock vector `v` (all moments
`fockMoment N v` finite), there is a function `φ` of `p`, integrable for the product Haar measure,
such that the `N`-th moment of `coneIntegrand A X μ β z v p` is at most `‖φ p‖ₑ` for every `p`. 

### `continuous_coneIntegrand`

 For `z > 0` the cone integrand is continuous in `p = (k, a)`. 

### `integrable_coneIntegrand`

 Convergence of the cone integral. Let `A` and `X` be base-adapted splittings, by one hyperbolic
plane, of `W'` over `W` and of `V'` over `V`. For `p = (k, a)`, with `k` in the maximal compact
subgroup of `U(V')` and `a ∈ (InfinitePlace E → ℂ)ˣ`, `coneIntegrand A X μ β z v p` is the line term
`lineTermReal A X β a` of `k v` (`k` acting through the Weil representation), times
`∏ w, (a w / |a w|) ^ (2 μ w)` and the `z`-th power of the idele norm of `a`. For `z > 0` and a
vector `v` all of whose moments are finite (`IsSchwartzVector v`), this integrand is integrable for
the product Haar measure, and its integral over all `p` again has all moments finite. 

### `isSchwartzVector_integral_coneIntegrand`

 For `z > 0` and a vector `v` all of whose moments are finite, all moments of the integral of the
cone integrand are finite. 
