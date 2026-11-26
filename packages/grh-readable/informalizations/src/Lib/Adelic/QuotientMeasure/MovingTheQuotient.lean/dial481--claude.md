---
{
  "module": "src/Lib/Adelic/QuotientMeasure/MovingTheQuotient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/MovingTheQuotient.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/MovingTheQuotient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moving a quotient from one variable to another

Let `Λ → R` be a homomorphism from a countable group to a subgroup `R` of a group `G`, and let `F`
on `R × G` be invariant under the diagonal action of `Λ`. The integral of `F` over
`Λ \ (R × G)` may be computed as an integral over `R × (Λ \ G)` or over `(Λ \ R) × G`
(`New.integral_cutoff_swap`).

Notions from other files:
* `New.orbitMeasure ν μ`: the measure `μ` weighted by a chosen cutoff; it computes integrals over
  the quotient.

## Relation to the literature

A consequence of a known result: the integral over a quotient does not depend on the cutoff. See
`Lib.Adelic.QuotientMeasure.Basic`.


### `IsCutoff.integrable_orbitMeasure_iff`

 Let `ν` be an inversion invariant measure on a group `H`, `μ` an `H`-invariant measure on `X`
and `β` a cutoff, that is, a measurable weight with `∫_H β (h • x) dν = 1` for every `x`. A
measurable `H`-invariant function `f` is integrable for the quotient measure `orbitMeasure ν μ`
(the measure `μ` weighted by a chosen cutoff) if and only if `β • f` is integrable for `μ`. 

### `integral_cutoff_swap`

 **Moving the quotient from one variable to the other.** Let `R` be a subgroup of `G`, with left
invariant measures `ν` and `μ`, and let `i` be a homomorphism from a countable group `Λ` to `R`.
Let the translates under `Λ` of the measurable weight `β` on `G` add up to one, so that `β μ` and
`β ν` compute integrals over `Λ \ G` and `Λ \ R`. If `F` on `R × G` is measurable, invariant under
the diagonal action of `Λ` and integrable over `(Λ \ R) × G`, then
`∫_{Λ \ G} ∫_R F = ∫_{Λ \ R} ∫_G F`. 

### `integrable_mul_comp_inv_mul`

 If `a` is integrable on a subgroup `R` of `G` and `e` is integrable on `G` for a left invariant
measure, then `(s, x) ↦ a s * e (g * s⁻¹ * x)` is integrable on `R × G`. 
