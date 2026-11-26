---
{
  "module": "src/Lib/ClassField/Global/CMSplittingCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/CMSplittingCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/CMSplittingCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# CM fields: complex conjugation, invariant ideles and splitting characters

This file treats a CM field `L` over its maximal real subfield `L⁺`. The chosen complex conjugation
`c = New.cmConj` of `Ω` acts on the Galois group `Gal(Ω/E)` of a CM field `E` by `g ↦ c g c`, and on
the places of `Ω`.

## Main definitions and results

* `New.Cohomology.upsilon_eq_quadraticIdeleChar`: on the ideles fixed by conjugation (the ideles of
  `L⁺`), a splitting character is the quadratic character `η` of `L/L⁺`
  (`New.Cohomology.quadraticIdeleChar`), which is `1` on the ideles `a z z̄` with `a = ā`
  (`New.Cohomology.IsRealTimesNorm`) and `-1` on the others.
* `New.nonempty_splittingChar`: a splitting character exists when `E` contains a primitive 5040-th
  root of unity and every root of unity of `E` is `δ / δ̄` for a unit `δ` of `𝓞 E` with
  `∏ w, Φ w δ = 1`.
* `New.artinMap_star`, `New.IsPlaceOver.conjPlace_star`, `New.IsFrob.conjPlace_conjGal`,
  `New.conjGal_mem_inertiaGroup_iff`: conjugation is compatible with the Artin map, places,
  Frobenius elements and inertia.
* `New.IsFromU1.apply_idOrConjInv`, `New.IsFromU1.eq_one_of_mem_decompGroup`,
  `New.IsFromU1.eq_one_of_mem_inertiaAbove`: a character `χ` with `χ (Art x) = η (x / x̄)`
  (`New.IsFromU1 S I χ`) is invariant under `g ↦ (c g c)⁻¹`, trivial on decomposition groups above
  `S` and unramified outside `I` and its conjugates.

Notions from other files:
* `New.SplittingChar L`: a unitary Hecke character `υ` of `L` with `υ x̄ = (υ x)⁻¹` that is
  `∏ τ, x_τ / |x_τ|` on the ideles whose finite part is a unit; `υ.atUniformizer w` is its value at
  the chosen uniformiser at the finite place `w`.
* `New.Ω`: an algebraic closure of `ℚ`; the fields `E` with a Galois group `Gal(Ω/E)` carry an
  embedding in it (`New.EmbeddedNumberField`).
* `New.IsFromU1 S I χ`: `χ` is locally constant and `χ (Art x) = η (x / x̄)` for a character `η` of
  the finite ideles that is trivial on `Eˣ` and on the ideles that are units off `S ∪ S̄` and `≡ 1`
  at the places of `I` off `S ∪ S̄`.

## Relation to the literature

Known result: Type A₀ Hecke characters and extension of a CM field's quadratic character. The
results on `New.IsFromU1` concern characters of the norm-one torus of a CM field that are tamely
ramified off `S ∪ S̄`. A splitting character extends the quadratic character and is everywhere
unramified of weight one; such an extension exists under the hypotheses of
`New.nonempty_splittingChar`, but not for every CM field. Source: A. Weil, On a certain type of
characters of the idèle-class group of an algebraic number-field, Tokyo–Nikko symposium 1955 (1956);
exposition A. Raghuram, Notes on the arithmetic of Hecke L-functions, arXiv:2207.03399, §4.

See also `Lib.ClassField.Global.AlbertBrauerHasseNoether` and `Lib.ClassField.Places.LocalFields`.



## Invariant ideles and splitting characters at inert places

Here `L⁺ = maximalRealSubfield L`, `star` (written `z ↦ z̄`) is complex conjugation on `L`, its
finite adeles `𝔸f L` and its places, `New.CMType` chooses an embedding `Φ w` for each infinite
place `w`, `New.principalIdele` is the diagonal map to the finite ideles, `adeleNorm K L` is the
norm of finite adeles from `L` to `K`, and `finAdeleIncl K L` is base change of finite adeles from
`K` to `L`. For a character `χ` of `Gal(Ω/L⁺)`, `abelianLift χ (artinMap _ b)` is its value at
the Artin symbol of the finite idele `b`, and `IsProGalois (ker χ) L Ω` says that `χ` cuts out
`L`: its kernel is `Gal(Ω/L)`. Finally `0 < c` for `c : ℂ` means that `c` is a positive real
number.


### `finAdeleIncl_adeleNorm_eq_mul_star`

 The norm to `L⁺` of a finite adele `y` of `L`, seen in the adeles of `L`, is `y ȳ`. 

### `gal_maximalReal_induction`

 A property of the identity and of complex conjugation holds on all of `Gal(L/L⁺)`, which has
these two elements only. 

### `map_finAdeleIncl_principalIdele_mul_adeleNorm`

 Base change of finite ideles from `L⁺` to `L` sends `x` times the norm of `z` to `x z z̄`. 

### `exists_map_finAdeleIncl_eq_of_star_eq`

 Galois descent: a finite idele `t` of `L` with `t̄ = t` comes from a finite idele of `L⁺`. 

### `exists_char_isProGalois_ker`

 For an embedding of `L` in `Ω`, some character `χ` of `Gal(Ω/L⁺)` cuts out `L`: its kernel is
`Gal(Ω/L)`. 

### `exists_abelianLift_artinAt_ne_one`

 Let `χ` cut out `L` over `L⁺`, and let `w = w̄` be a finite place of `L`. Then `χ` does not kill
all local Artin symbols at the place of `L⁺` below `w`, as this place does not split in `L`. 

### `bijective_cmType_restrict`

 Restricted to `L⁺`, the embeddings of the CM type are all the complex embeddings of `L⁺`,
each once. 

### `exists_maximalRealSubfield_sign_eq`

 For any signs `r w = ±1` at the infinite places `w` of `L`, there is a nonzero `a ∈ L⁺` such
that `r (mk φ) * φ a` is a positive real number for every complex embedding `φ` of `L` (weak
approximation for the signs of `L⁺`). 

### `abelianLift_artinMap_eq_one_iff_prod_pos`

 The sign law for a CM field `L` with an embedding into `Ω`, the algebraic closure of `ℚ`. If
the character `χ` of `Gal(Ω/L⁺)` cuts out `L`, then it kills the Artin symbol of `b ∈ (L⁺)ˣ`
exactly when `∏ w, Φ w b` is positive. 

### `exists_sign_eq_principalIdele_mul_adeleNorm`

 Let `L` be a CM field with an embedding into `Ω`, the algebraic closure of `ℚ`, and `χ` a
character of `Gal(Ω/L⁺)` that cuts out `L`. Let `b` be a finite idele of `L⁺`, and let `s w = ±1`
be signs whose product is `1` exactly when `χ` kills the Artin symbol of `b`. Then `b` is `x` times
a norm from `L`, where `x ∈ (L⁺)ˣ` has the signs `s`. 

### `exists_eq_principalIdele_mul_adeleNorm`

 Every finite idele of `L⁺` is an element of `(L⁺)ˣ` times a norm from `L`. 

### `exists_eq_principalIdele_mul_mul_star_of_star_eq`

 A finite idele `t` of `L` with `t̄ = t` is `x z z̄` with `x ∈ Lˣ` and `z` a finite idele. 

### `exists_sign_principalIdele_mul_norm_eq_one`

 Given signs `s w = ±1` of product `1`, there are `x ∈ Lˣ` and a finite idele `z` with
`x z z̄ = 1` such that every `φ x` is real with the sign that `s` gives to the place of `φ`. 

### `prod_Φ_pos_of_principalIdele_mul_norm_eq_one`

 If `a ∈ Lˣ` has `ā = a` and `a z z̄ = 1` for a finite idele `z`, then `∏ w, Φ w a` is
positive. 

 ### The restriction of a splitting character to the ideles of the real subfield 

### `IsRealTimesNorm`

 The idele `x` of `E` lies in `F^× N(𝔸_E^×)`, for the maximal real subfield `F` of `E`: it
is `a z z̄` for an element `a` of `E^×` fixed by conjugation and an idele `z` of `E`. Here
`a.map toAdele` is `a` as a principal idele, and `star` is complex conjugation. 

### `quadraticIdeleChar`

 The quadratic character `η` of `E/F`, for the maximal real subfield `F` of `E`. The ideles of
`F` are the ideles of `E` fixed by conjugation; `η` is `1` on `F^× N(𝔸_E^×)` and `-1` on the other
ideles of `F`. Its values at ideles of `E` that conjugation moves are not used. At a finite place
`w = w̄`, `η` is `-1` at some finite idele `t` fixed by conjugation that is `1` at the other finite
places and at infinity (`exists_quadraticIdeleChar_eq_neg_one`). 

### `exists_quadraticIdeleChar_eq_neg_one`

 Let `w = w̄` be a finite place of `E`, above the place `v` of the maximal real subfield `F`. The
quadratic character `η` of `E/F` is not trivial on `F_v^×`: it is `-1` at some finite idele `t` that
is fixed by conjugation and has the component `1` at all finite places other than `w`. Here
`finIdeleIncl t` is the idele with finite part `t` and components `1` at infinity.

This is part of the local description of `η` in class field theory: non-triviality at a non-split
finite place only, without identifying the kernel on `F_v^×` with the local norms. 

### `star_eq_of_star_principalIdele_mul_norm`

 If `a z z̄` is fixed by conjugation, for `a ∈ E^×` and a finite idele `z`, then so is `a`. 

### `upsilon_eq_one_of_isRealTimesNorm`

 A splitting character `υ` is `1` on the ideles `a z z̄` of `IsRealTimesNorm`: it is trivial
on `E^×`, and `υ(z̄) = υ(z)⁻¹`. 

### `ofReal_div_norm_eq_of_sign`

 If a real number `t` has the sign `s = ±1`, then `t / |t| = s` in `ℂ`. 

### `exists_signs_of_upsilon_eq_one`

 Let `r` be an idele of `E` with real components at infinity and finite part `1`, on which the
splitting character `υ` is `1`. Then the signs `s w` of its components at infinity have product
`1`. 

### `isRealTimesNorm_of_finPart_eq_one`

 Let `r` be an idele of `E` fixed by conjugation (an idele of the maximal real subfield), with
finite part `1`, on which the splitting character `υ` is `1`. Then `r = b v v̄` for some `b ∈ E^×`
fixed by conjugation and some idele `v` (`IsRealTimesNorm`). 

### `isRealTimesNorm_of_upsilon_eq_one`

 Let `υ` be a splitting character of the CM field `E`: a unitary Hecke character with
`υ x̄ = (υ x)⁻¹` that equals `∏ x_τ / |x_τ|` on ideles whose finite part is a unit of `Ô`. Let `x`
be an idele of `E` fixed by conjugation (an idele of the maximal real subfield) with `υ x = 1`. Then
`x = a z z̄` for some `a ∈ E^×` fixed by conjugation and some idele `z` of `E`
(`IsRealTimesNorm`). 

### `upsilon_eq_quadraticIdeleChar`

 On an idele `x` of `E` fixed by conjugation, that is, an idele of the maximal real subfield
`F`, a splitting character `υ` equals the quadratic character `η` of `E/F`
(`quadraticIdeleChar`). 

### `upsilon_locFullIdele_eq_neg_one_of_star_eq`

 Let `E` be a CM field with a CM type, and let `υ` be a splitting character of `E`. That is, `υ`
is a unitary Hecke character with `υ x̄ = (υ x)⁻¹`, and it equals `∏ x_τ / |x_τ|` on ideles whose
finite part is a unit of `Ô`. If `w` is a finite place of `E` with `star w = w` and `ϖ ∈ E_w^×` has
valuation `exp(-1)` (a uniformiser), then `υ` takes the value `-1` on `locFullIdele w ϖ`, the idele
that is `ϖ` at `w` and `1` at every other place. 

### `upsilon_atUniformizer_eq_neg_one`

 A splitting character is `-1` at the chosen uniformiser at a finite place `w = w̄`. 

### `υ_star_eq_inv_and_apply_eq`

 The four properties of a splitting character `υ` of `E` that are used: (1) `υ(ȳ) = υ(y)⁻¹`;
(2) `υ(y) = ∏_τ y_τ/|y_τ|` over the infinite places `τ` if the finite part of `y` is a unit of
`Ô E`; (3) `υ(ϖ) = -1` for every uniformiser `ϖ` at a finite place `w = w̄`, placed at `w` in an
idele by `locFullIdele`; (4) on the ideles fixed by conjugation, the ideles of the maximal real
subfield `F`, `υ` is the quadratic character `η` of `E/F`. This collects `υ_star`, `υ_unit`,
`upsilon_locFullIdele_eq_neg_one_of_star_eq` and `upsilon_eq_quadraticIdeleChar`. 


## Existence of a splitting character

`New.nonempty_splittingChar` constructs a splitting character `New.SplittingChar E` of a CM field
`E` that contains a primitive 5040-th root of unity (`New.HasPrimitiveRoot5040`) and in which every
root of unity is `δ / δ̄` for a unit `δ` of `𝓞 E` with `∏ w, Φ w δ = 1`.

The adeles `New.𝔸 E` have one factor `ℂ` for each infinite place, in which `E` is embedded by the
chosen embedding `Φ w` of `New.CMType`.


### `New.prod_div_norm_eq_one_of_mem_idelesUnitOff`

 Suppose that every root of unity of `E` is `δ / δ̄` for a unit `δ` of `𝓞 E` with
`∏ w, Φ w δ = 1`. Let `x = y b b̄` for `y ∈ E^×` and an idele `b` of `E`, where the finite part
of `x` is a unit at every finite place. Then `∏_w x_w / |x_w| = 1`, over the infinite places `w`. 

### `New.nonempty_splittingChar`

 Let `E` be a CM field with a CM type `Φ` (a complex embedding `Φ w` inducing each infinite place
`w`) that contains a primitive 5040-th root of unity (`New.HasPrimitiveRoot5040`). Suppose every
root of unity `y` of `E` (written `IsOfFinOrder y`) equals `δ / δ̄` for some unit `δ` of `𝓞 E` with
`∏ w, Φ w δ = 1`. Then `E` has a splitting character (`New.SplittingChar`), that is, a unitary Hecke
character `υ` of `E` with `υ x̄ = (υ x)⁻¹` that equals `∏ x_τ / |x_τ|` (over the infinite places) on
ideles whose finite part is a unit of `Ô`. 

 ## Complex conjugation on the Galois group, places and Artin map; characters from U(1) 

 ### Conjugation on the Galois group and on places 

### `idOrConjInv`

 The element `g` if `b` is true, and `(conjGal g)⁻¹ = (c g c)⁻¹` if `b` is false. 

### `cmConj_conjGal_smul`

 The chosen complex conjugation `c` intertwines `g^c = c g c` with `g`: `c (g^c x) = g (c x)`. 

### `artinMap_star`

 The global Artin map of a CM field `E` is compatible with complex conjugation: if the Artin
symbol of the finite idele `x` is the class of `g ∈ Gal(Ω/E)`, then that of the conjugate idele `x̄`
is the class of `conjGal g = c g c`, where `c` is the chosen complex conjugation of `Ω`. 

### `conjPlace`

 The conjugate place: the preimage of the valuation subring A of Ω under the chosen complex
conjugation. 

### `IsPlaceOver.conjPlace_star`

 Let E be a CM field. If the valuation subring A of Ω lies over the finite place v of E, then
the conjugate place of A under the chosen complex conjugation lies over the conjugate prime
v̄. 

### `IsFrob.conjPlace_conjGal`

 Conjugation maps a Frobenius element of exponent `q` at the place `A` to one at the conjugate
place. 

### `conjGal_mem_inertiaGroup_iff`

 Let E be a CM field, g in Gal(Ω/E) and c the chosen complex conjugation. Then g^c = cgc lies
in the inertia group of the conjugate place of A if and only if g lies in the inertia group
of A. 

### `Selmer.cyclotomicChar_eq_one_of_mem_inertiaAbove`

 The `ℓ`-adic cyclotomic character is unramified outside `ℓ`: it is `1` at every `g` that lies
in the inertia group of a place of `Ω` above a finite place of `E` not dividing `ℓ`. 

 ### Characters that come from U(1) 

### `IsFromU1.apply_idOrConjInv`

 Let `χ : Gal(Ω/E) →* C` come from the norm-one torus in the sense of `IsFromU1 S I χ`:
`χ(Art x) = η(x / x̄)` for an idele class character `η` of modulus `I` that is trivial on the local
components at the places of `S` and their conjugates. Then `χ(idOrConjInv b g) = χ(g)` for both
values of the boolean `b`, and in particular `χ((c g c)⁻¹) = χ(g)`. 

### `IsFromU1.eq_one_of_mem_decompGroup`

 Let `S` and `I` be sets of finite places of the CM field `E`, and let `χ` be a character of
`Gal(Ω/E)` with `IsFromU1 S I χ`. This means `χ(Art x) = η(x / x̄)` for an idele class character `η`
of modulus `I` that is trivial on the local components at `S ∪ S̄`. Then `χ` kills the decomposition
groups above `S`: if the place `A` of `Ω` lies over a place `v ∈ S` of `E` and `g` is in the
decomposition group of `A`, then `χ g = 1`. 

### `IsFromU1.eq_one_of_mem_inertiaAbove`

 Let `S` and `I` be sets of finite places of the CM field `E`, and let `χ` be a character of
`Gal(Ω/E)` with `IsFromU1 S I χ`. This means `χ(Art x) = η(x / x̄)` for an idele class character `η`
of modulus `I` that is trivial on the local components at `S ∪ S̄`. Then `χ` kills inertia outside
`I` and its conjugates: `χ g = 1` for `g` in the inertia group of a place of `Ω` above a place of
`E` not in `I ∪ Ī`. 
