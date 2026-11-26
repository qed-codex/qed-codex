---
{
  "module": "src/Lib/General/Algebra/PerfectAlgebras.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/PerfectAlgebras.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/PerfectAlgebras.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Perfect algebras, étale algebras over perfect rings, and constant Laurent polynomials

Fix a prime p (the class `ThePrime p`). An algebra is perfect when x ↦ x^p is bijective; for hp :
p = 0, `frobPow hp 1` is this map x ↦ x^p as a ring endomorphism, and O♭ denotes the tilt of the
ring of integers of ℂ_p. The file constructs perfections of quotients and perfected blow-up charts,
and it shows that étale algebras lift along surjections and are perfect over a perfect base in which
p = 0. It also proves that a Laurent polynomial that is a polynomial both in T and in T⁻¹ is
constant.

## Main definitions and results

* `New.Variety.perfectRing_monoidAlgebra`: O♭[G] is perfect when G is a module over the non-negative
  rationals.
* `New.Variety.PerfectAlg.isClosedUnderColimitsOfShape_widePushoutShape`,
  `New.Variety.perfectRing_tensor`: if p = 0 in S, perfect S-algebras are closed under wide
  pushouts, so, for perfect S, under tensor products.
* `New.Variety.exists_perfection_quotient`: the perfection of B/t, for p = 0 in the base.
* `New.Variety.exists_perfect_blowup_charts`: for f, g in a perfect algebra B over a perfect ring
  with p = 0, perfected charts B₁ (where g ∣ f) and B₂ (where f ∣ g) form an exact sequence
  B → B₁ × B₂ → B₀ → 0; the proof splits Laurent polynomials by
  `New.Variety.surjective_toLaurent_add_invert`.
* `New.Variety.exists_etale_lift`: an étale algebra over a quotient of C lifts to an étale algebra
  over C.
* `New.Variety.perfectRing_of_etale`: an étale algebra over a perfect ring in which p = 0 is
  perfect.

Notions from other files:
* `New.Variety.PadicTest.tilt`: The functor from p-adic tests to commutative O^♭-algebras sending a
  test S to its tilt S^♭.

## Relation to the literature

Known; see `Lib.PadicComparison.Descent.AlmostDescent` for sources.


 ## Constant Laurent polynomials 

### `New.Variety.eq_C_of_toLaurent_eq`

 `H⁰(ℙ¹, 𝒪) = k`: if `P(T) = Q(T⁻¹)` as Laurent polynomials over the commutative ring `k`, then
`P` and `Q` are the same constant. 


## Perfect algebras, tensor products and blow-up charts

The category `New.Variety.PerfectAlg S` of perfect S-algebras, mostly for a ring S with p = 0. The
tilt of a p-adic test (`New.Variety.PadicTest`) is a perfect O♭-algebra.


 ### Perfect algebras and Frobenius 

### `PerfectAlg`

 The full subcategory of commutative S-algebras on which x ↦ x^p is bijective. 

### `instance (b : PerfectAlg S) : PerfectRing b.obj p`

 The underlying ring of a perfect S-algebra is perfect. 

### `MaxIdealFlat`

 The maximal ideal 𝔪 of the local ring O^♭. 

### `PadicTest.perfectTilt`

 The functor from p-adic tests to perfect O^♭-algebras sending S to its tilt S^♭. 

### `natCast_eq_zero_of_algebra_oFlat`

 The prime p is zero in every O^♭-algebra, as O^♭ has characteristic p. 

### `perfectRing_monoidAlgebra`

 For a commutative additive monoid G that is a module over the non-negative rationals, the
monoid algebra O♭[G] is perfect: x ↦ x^p is bijective on it. Here p is the fixed prime and
O♭ = `OFlat` is the tilt of the ring of integers of ℂ_p, a perfect ring of characteristic p. 

### `surjective_toLaurent_add_invert`

 Every Laurent polynomial over S is a polynomial in T plus a polynomial in T⁻¹ without
constant term: the map (P, Q) ↦ P(T) + T⁻¹ Q(T⁻¹) from S[X] × S[X] to S[T, T⁻¹] is surjective,
that is, H¹(ℙ¹, 𝒪) = 0. 

 ### Algebras over a ring with p = 0: colimits and perfection 

### `PerfectAlg.isClosedUnderColimitsOfShape_widePushoutShape`

 If p = 0 in S, a wide pushout (indexed by any type J) of perfect S-algebras is perfect. 

### `exists_perfection_quotient`

 For a prime `p` (fixed by the class `ThePrime p`) with `p = 0` in the commutative ring `S`, an
`S`-algebra `B` and an element `t ∈ B`, there is a perfection of `B/t`: a perfect `S`-algebra `c`
(one on which x ↦ x^p is bijective) with an `S`-algebra map `e : B → c` such that (a) every
`S`-algebra map `φ` from `B` to a perfect `S`-algebra with `φ t = 0` factors as `ψ ∘ e`; (b)
`e r = e s` implies `t ∣ r^{p^n} − s^{p^n}` for some `n`; (c) `e t = 0`; (d) every `y` in `c` has
some power `y^{p^n}` in the image of `e`. 

### `perfectRing_of_pow_surjective`

 If p = 0 in the reduced ring S and every element is a p-th power, then S is perfect. 

 ### Tensor products and blow-up charts 

### `injective_rTensor_of_field_maps_factor`

 Let S be perfect with p = 0 and i a map from a perfect S-algebra B to an S-algebra A. Suppose
that for every field k and every map a : B → k some injective map η from k to a perfect S-algebra
makes η ∘ a factor through i. Then i is injective after tensoring with any perfect S-algebra. 

### `invert_toLaurent_C_sub_C_mul_X`

 The relation f = g T in terms of T⁻¹: (g - f T⁻¹) = -(f - g T) T⁻¹. 

### `exists_C_of_toLaurent_sub_invert_eq`

 If P(T) - Q(T⁻¹) = (f - g T)(U(T) + T⁻¹ V(T⁻¹)), then P - (f - g X) U and Q - (g - f X) V are
the same constant. 

### `exists_injective_algHom_perfect`

 If p = 0 in S, every S-algebra k that is a field maps injectively to a perfect S-algebra. 

### `exists_blowup_gluing_maps`

 Let B, B₁, B₂, B₀ be perfect S-algebras with maps E₁ : B[X] → B₁, E₂ : B[X] → B₂ and
E₀ : B[T, T⁻¹] → B₀. Suppose E₀ kills f - g T, maps B[X] → B₀ that kill f - g X factor through E₁,
and those that kill g - f X factor through E₂. Then X ↦ T and X ↦ T⁻¹ induce maps j₁ : B₁ → B₀ and
j₂ : B₂ → B₀. 

### `surjective_blowup_difference`

 Let p = 0 in S and B, B₁, B₂, B₀ be perfect S-algebras. Let E₁, E₂ map B[X] to B₁, B₂, let E₀
map B[T, T⁻¹] to B₀, and let j₁, j₂ map B₁, B₂ to B₀ with j₁ (E₁ P) = E₀ (P(T)) and
j₂ (E₂ P) = E₀ (P(T⁻¹)). If every element of B₀ has a p^n-th power in the image of E₀, then
(y, z) ↦ j₁ y - j₂ z maps onto B₀. 

### `exists_eq_of_blowup_glue_eq`

 Let B, B₁, B₂, B₀ be perfect S-algebras (x ↦ x^p is bijective on them). Let E₁, E₂ map B[X] to
B₁, B₂, let E₀ map B[T, T⁻¹] to B₀, and let j₁, j₂ satisfy j₁ (E₁ P) = E₀ (P(T)) and j₂ (E₂ P) = E₀
(P(T⁻¹)). Suppose E₁, E₂ kill f - g X, respectively g - f X, every element of B₁, B₂ has a p^n-th
power in the image of E₁, E₂, and elements with the same image under E₀ have p^n-th powers congruent
modulo f - g T. Then y in B₁ and z in B₂ with j₁ y = j₂ z are E₁ r and E₂ r for one constant r in
B. 

### `exists_factor_through_blowup_charts`

 Let p = 0 in S. Suppose maps from B[X] to perfect S-algebras that kill f - g X factor through
E₁ : B[X] → B₁, and those that kill g - f X factor through E₂ : B[X] → B₂. Then every point
a : B → k of B in a field becomes, after some injective map η from k to a perfect S-algebra, a
point that factors through B → B₁ × B₂. 

### `exists_perfect_blowup_charts`

 The two charts of the blow-up of (f, g), perfected. For S perfect with p = 0 and f, g in a
perfect S-algebra B there are perfect S-algebras B₁, B₂ under B, and B₀, such that (a) g ∣ f in
B₁ and f ∣ g in B₂; (b) B → B₁ × B₂ → B₀ → 0 is an exact sequence of S-modules; (c) the first
map is injective after tensoring over S with any perfect S-algebra. 

 ## Étale algebras over quotients and over perfect rings 

### `exists_etale_lift`

 Étale algebras lift along surjections: if C → D is onto and B is étale over D, then
B ≅ D ⊗_C T as D-algebras for some étale C-algebra T. 

### `bijective_of_etale_of_inverse_up_to_pow`

 Let `D` be étale over `C` with `p = 0` in `D`, and `f : D → E` a ring map with `C → E` étale.
If `s` is inverse to `f` up to the `p`-th power on both sides, then `f` is bijective. 

### `perfectRing_of_etale`

 An étale algebra over a perfect ring in which p = 0 is perfect. 
