---
{
  "module": "src/Lib/General/NumberTheory/EmbeddingsAndDifferent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/EmbeddingsAndDifferent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/EmbeddingsAndDifferent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Embeddings, differents and the maximal real subfield of a CM field

The file collects general lemmas on differents and root discriminants of number fields. It then
compares a CM field `E` with its maximal real subfield E⁺ (`maximalRealSubfield E`), covering the
trace, the norm, the different and the discriminant.

* `star` is complex conjugation on the CM field `E` and on its integers `𝓞 E`.
* `Φ v` is the complex embedding chosen at the infinite place `v`: by `New.PlaceEmbedding` in
  general, and by `New.CMType`, which extends it, for CM fields.
* `New.volÔ E` is `2 ^ r₂ / √|disc E|`, with `r₂` the number of complex places of `E`.

## Main definitions and results

* `New.differentIdeal_eq_span_of_dvd`: a criterion for `f'(x)` to generate the different and for
  `𝓞 L = A[x]`.
* `New.mem_maximalRealSubfield_iff_star_eq`, `New.trace_maximalRealSubfield_eq_add_star`,
  `New.norm_maximalRealSubfield_eq_mul_star`: E⁺ is the fixed field of conjugation, and the trace
  and norm from `E` to E⁺ are `x + x̄` and `x x̄`.
* `New.differentIdeal_eq_top`, `New.abs_discr_eq_discr_maximalRealSubfield_sq`: under
  `New.HasPrimitiveRoot5040` the relative different is trivial and |disc E| = (disc E⁺)².
* `New.volÔ_eq`: the mass `New.volÔ` of the integral finite adeles in terms of the root
  discriminant.
* `New.exists_mixedEquiv_maximalRealSubfield`: the Minkowski space of E⁺ as real functions on the
  infinite places of `E`.
* `New.Variety.prod_embeddings_eq_prod_pairs`: a product over the complex embeddings of a totally
  complex field, grouped into conjugate pairs.


 ## Differents and root discriminants 

### `differentIdeal_eq_span_of_dvd`

 Let `A` be a Dedekind domain with fraction field `K`, with `𝓞 L` finite over `A`. Let `x ∈ 𝓞 L`
generate `L` over `K`, and let `f` be a polynomial over `A` with root `x`. If `y = f'(x)` generates
an ideal that divides the different of `𝓞 L` over `A`, then `y` generates the different and
`𝓞 L = A[x]`. 

### `ne_zero_of_differentIdeal_eq_span`

 A generator `x` of the different of `𝓞 L` over `ℤ` is nonzero. 

### `dvd_differentIdeal_of_mem_sq`

 An ideal `P` of the integers of a number field `L` whose square contains a rational prime `p`
divides the different of `L` over `ℚ`. 

### `Core.numInfPlaces`

 The number of infinite places of the number field `K`. 

### `rootDiscr_pos`

 The root discriminant `|disc K| ^ (1 / [K : ℚ])` of a totally complex field is positive. 

### `abs_discr_eq_rootDiscr_pow`

 For a totally complex number field `K` with `r` infinite places and root discriminant `rd`,
the absolute discriminant is `(rd ^ r) ^ 2`. 

 ## The maximal real subfield: trace, norm, different and discriminant 

### `mem_maximalRealSubfield_iff_star_eq`

 The maximal real subfield of a CM field is the fixed field of complex conjugation. 

### `pair_complexConj_eq_univ`

 The automorphisms of a CM field over its maximal real subfield are the identity and complex
conjugation. 

### `trace_maximalRealSubfield_eq_add_star`

 The trace from a CM field `E` to its maximal real subfield is `x + x̄`. 

### `norm_maximalRealSubfield_eq_mul_star`

 The norm from a CM field `E` to its maximal real subfield is `x * x̄`. 

### `isIntegral_sub_star_mul_of_mem_traceDual`

 If `x` lies in the trace dual of the integers of the CM field `E` over those of its maximal
real subfield, then `(y - ȳ) * x` is an algebraic integer for every integer `y` of `E`. 

### `differentIdeal_eq_top_of_add_star_eq_one`

 Let the integers of the CM field `E` contain `i` with `i² = -1`, `ī = -i` and `β` with
`β + β̄ = 1`. Then `E` has trivial different over its maximal real subfield, so it is unramified at
all finite places. 

### `differentIdeal_eq_top`

 A CM field that contains a primitive root of unity of order `5040` has trivial different over
its maximal real subfield. 

### `abs_discr_eq_discr_maximalRealSubfield_sq`

 If the CM field `E` contains a primitive root of unity of order `5040`, its discriminant is, up
to sign, the square of that of its maximal real subfield. 

### `volÔ_eq`

 The mass `volÔ E = 2 ^ r₂ / √|disc E|` of the integral finite adeles of a CM field `E` is
`(rd / 2) ^ (-r)`, with `rd` the root discriminant of `E` and `r` the number of its infinite
places. 

### `exists_mixedEquiv_maximalRealSubfield`

 Let `E` be a CM field with a chosen complex embedding `Φ v` at each infinite place `v`. There is
a measure-preserving real-linear isomorphism from the Minkowski space of the maximal real subfield
E⁺ to the real functions on the infinite places of `E` that sends the image of `a ∈ E⁺` to
`v ↦ Re (Φ v a)`. 

 ## Complex embeddings of a totally complex field in conjugate pairs 

### `prod_embeddings_eq_prod_pairs`

 For a totally complex number field `E`, a product over all complex embeddings is a product over
the infinite places `v` of the factors at the embedding `Φ v` chosen at `v` and at its conjugate. 

### `roots_map_conjugate`

 For a polynomial `P` over a totally complex field, the roots of `P` under the conjugate of an
embedding `σ` are the complex conjugates of its roots under `σ`, with multiplicity. 
