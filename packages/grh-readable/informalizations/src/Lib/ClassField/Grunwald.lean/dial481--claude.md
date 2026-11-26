---
{
  "module": "src/Lib/ClassField/Grunwald.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Grunwald.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Grunwald.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Grunwald's theorem in prime degree and CM steps with prescribed local behaviour

The file studies continuous characters `χ : Γ → ℚ/ℤ` of absolute Galois groups `Γ = Gal(Ω/E)` (`Ω`
the algebraic closure; `New.EmbeddedNumberField E`: a number field with an embedding into `Ω`) of CM
fields `E` that are killed by a prime `p`, and the cyclic extensions of degree `p` they cut out.
Grunwald's theorem in prime degree produces such characters with prescribed local behaviour. If `E`
is stably unramified (here: `New.HasPrimitiveRoot5040 E`, a primitive 5040th root of unity lies in
`E`) and the symmetrised character is nonzero and kills inertia above `p`, the field cut out by the
symmetrised character is a step of degree `p` over `E`. Weil data lift to stably unramified CM
extensions `L` whose CM type restricts to that of `E` and whose relative different is prime to the
places fixed by conjugation. Together these results give a step of prime degree with Weil data and a
prescribed completion at a split place.

## Main definitions and results

* `New.grunwald`: a character of the finite ideles of a totally complex field, killed by `p`, agrees
  with a Galois character killed by `p` at finitely many given places, and on the units at every
  place whose norm is not prime.
* `New.QZChar.symmetrise`, `New.QZChar.abelianLift_symmetrise`: for a CM field, the character
  `g ↦ χ g + χ (gᶜ)`; on the Artin symbol of an idele `a` it is `χ a + χ (star a)`.
* `New.QZChar.stepField`: the fixed field of the kernel of `New.QZChar.symmetrise χ`. Instances show
  that it is CM, that a CM type of `E` extends to it (`New.CMTypeOver`) and that it inherits
  `New.HasPrimitiveRoot5040`.
* `New.isStep_stepField`: it is a step of degree `p` over `E` if `New.HasPrimitiveRoot5040 E` holds,
  `χ` is killed by a prime `p`, and `New.QZChar.symmetrise χ` is not zero and kills inertia above
  `p`.
* `New.nonempty_weilData_of_not_dvd_differentIdeal`: if `L` also satisfies
  `New.HasPrimitiveRoot5040`, then `L` has Weil data; in the construction `j` stays, `υ` is composed
  with the norm, and a new idele absorbs the relative different, which is assumed prime to the
  places fixed by conjugation.
* `New.GaloisRep.exists_isStepOfLocalChar`, `New.GaloisRep.exists_step_of_local_char`: given a split
  place `w` below `A` and a nontrivial tame character `χ` of `E_wˣ` killed by a prime `p`, a step
  `E' / E` of degree `p`, again with Weil data, cut out by the symmetrisation of a Galois character
  `ν` that is trivial at `w` and has symmetrisation `χ` there; the only place of `E'` above `w` is
  split and lies under `A`.

Notions from other files:
* `New.locIdele`: The homomorphism sending x ∈ K_v^× to the finite idele with component x at v and 1
  elsewhere; `New.ideleAt v` takes the component at v.
* `New.CMTypeOver`: a CM type of L that restricts to the given CM type of E; the embedding chosen at
  a place extends the one chosen at the place below.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.

## Relation to the literature

Known result: Grunwald–Wang theorem in prime exponent. It is proved over a totally complex field,
and the character also agrees with the given one on units at all primes of degree above one. It
yields a CM extension of prime degree with prescribed tame completion at a split place. Source:
Artin–Tate, Class Field Theory (1968), ch. X; S. Wang, Grunwald–Wang theorem, an effective version,
arXiv 1401.0389 (2014).

See also `Lib.Weil.MixedModel.ZeroTerm`.



## Grunwald's theorem in prime degree and the symmetrised character

`New.QZChar Γ` is the group of continuous characters `Γ → ℚ/ℤ`, `New.QZChar.abelianLift χ` the
induced map on `Γ^ab` (written multiplicatively), `New.artinMap` the global Artin map on finite
ideles.


### `exists_mem_ker_cyclotomicCharMod_smul_ne_of_forall_pow_ne`

 Let `p` be prime, `x ∈ Eˣ` not the `p`-th power of an element of `Eˣ`, and `r ∈ Ω` a `p`-th root
of `x`. Then some element of the absolute Galois group of `E` that fixes the `p`-th roots of unity
(it lies in the kernel of the cyclotomic character `New.cyclotomicCharMod Ω p`) moves `r`. 

### `exists_nsmul_eq_zero_abelianLift_artinMap_eq_of_apply_principalIdele_eq_one`

 Let `E` be totally complex and `ψ` a character of the finite ideles with values in `ℚ/ℤ`
(written multiplicatively), with open kernel and killed by `p`. Let `T` be a set of finite places
such that the principal ideles and the ideles that are units outside `T` (`New.idelesUnitOff T`)
generate all finite ideles, and let `U` be an open subgroup of the finite ideles that contains the
`p`-th powers of the ideles that are units outside `T`. If `ψ` is trivial on the principal ideles
in `U`, then some continuous character `χ` of the absolute Galois group, killed by `p`, has
`χ ∘ Art = ψ` on `U`. 

### `locIdele_mem_idelesUnitOff_of_mem_or_v_eq_one`

 The idele `New.locIdele u x`, with single component `x` at `u`, is a unit outside `T` if `u ∈ T`
or if `x` is a local unit (`v x = 1`). 

### `grunwald`

 Grunwald's theorem in prime exponent. Let `E` be totally complex, `p` prime, `S` a finite set of
finite places, and `ψ` a character of the finite ideles with values in `ℚ/ℤ` (written
multiplicatively), with open kernel and killed by `p`; it need not be trivial on `Eˣ`. Then some
continuous character `χ` of the absolute Galois group, killed by `p`, has `χ ∘ Art = ψ` on the
ideles `New.locIdele u x` with single component `x` at `u`. This holds for all `x` if `u ∈ S`, and
for local units `x` (`v x = 1`) if the norm `u.q` of `u` (the size of its residue field) is not
prime. 

### `QZChar.symmetrise`

 For a character `χ` of the absolute Galois group of a CM field, the character
`g ↦ χ g + χ (gᶜ)`, where `gᶜ` is the conjugate of `g` by complex conjugation (`New.conjGal`). 

### `QZChar.ideleChar`

 For a `ℚ/ℤ`-valued character `χ` of `Gal(Ω/E)`, the character `exp (2πi χ ∘ Art)` of the
finite ideles of `E`. 

### `QZChar.symmetrise_val_apply`

 The value of `New.QZChar.symmetrise χ` at `g` is `χ g + χ (gᶜ)`. 

### `QZChar.abelianLift_symmetrise`

 On the Artin symbol of an idele `a`, the symmetrised character `New.QZChar.symmetrise χ` takes
the value of `χ` at `a` times the value of `χ` at the conjugate idele `star a`. 


## The CM field cut out by the symmetrised character, and when it is a step

`New.HasPrimitiveRoot5040 E`: `E` contains a primitive root of unity of order `5040`.
`New.IsStep E' μ`: among other things `[E' : E]` is prime and `μ (z z̄) = 1` exactly when `z` is a
norm from `E'` times an element of `Eˣ`.


### `QZChar.stepField`

 The extension of the CM field `E` inside `Ω` cut out by the character `g ↦ χ g + χ (gᶜ)`, that
is, the fixed field of its kernel. 

### `instance : IsCMField (stepField χ)`

 The field `New.QZChar.stepField χ` is a CM field: the complex conjugation `cmConj` of `Ω` maps
it to itself and restricts on it to complex conjugation under every embedding into `ℂ`. 

### `noncomputable instance [CMType E] (χ : QZChar Gal(Ω/E)) : CMTypeOver E (stepField χ)`

 A CM type of `E` extends to `New.QZChar.stepField χ`: at each infinite place take the embedding
whose restriction to `E` is the embedding chosen at the place below. 

### `instance [h : HasPrimitiveRoot5040 E] : HasPrimitiveRoot5040 (stepField χ)`

 `New.QZChar.stepField χ` contains the image of a primitive `5040`-th root of unity of `E`. 

### `QZChar.not_dvd_differentIdeal_stepField`

 If `New.QZChar.symmetrise χ` kills the inertia groups at the places `A : ClosurePlace` of `Ω`
(valuation subrings) over (`IsPlaceOver`) the prime of `E` below `u`, then `u` does not divide the
different of `New.QZChar.stepField χ` over `E`. 

### `range_intTrace_stepField_eq_top`

 Suppose that `New.QZChar.stepField χ` has degree `p` over `E` and that `New.QZChar.symmetrise χ`
kills the inertia groups at the places above `p`. Then the trace from the integers of
`New.QZChar.stepField χ` to the integers of `E` is onto. 

### `isStep_stepField`

 Let `E` be a CM field containing a primitive 5040th root of unity (`New.HasPrimitiveRoot5040`),
and let `p` be prime. Write `New.QZChar.symmetrise χ` for the character `g ↦ χ g + χ gᶜ`, where `gᶜ`
is the conjugate of `g` by complex conjugation. Suppose that (a) `p • χ = 0`, (b)
`New.QZChar.symmetrise χ` is not zero, and (c) it kills the inertia groups at the places above `p`.
Then the field `New.QZChar.stepField χ`, the fixed field of the kernel of `symmetrise χ`, has degree
`p` over `E`. It is a step (`New.IsStep`: a CM field Galois of prime degree over `E`, with an
integer of trace `1`) for the Hecke character `New.QZChar.ideleChar χ = exp (2πi χ ∘ Art)`. This
character has open kernel, is trivial on `Eˣ`, and is `1` at `z z̄` exactly when `z` is a principal
idele times a norm from the field. 


## Lifting Weil data to CM extensions unramified at non-split places

Weil data (`New.WeilData E`) on a CM field `E` consist of an element `j = -j̄` with positive
imaginary part under the CM type `Φ` and with `(1 - j⁻¹) / 2` integral, a finite idele `α` such that
`j α ᾱ` generates the inverse different, and a splitting character `υ` (`New.SplittingChar`) that is
`-1` at the uniformisers of the places fixed by conjugation.


### `New.Φ_algebraMap_eq_Φ_comap`

 Let the CM type of `L` restrict to that of `E` (`New.CMTypeOver E L`). Then the embedding `Φ u`
of `L` into `ℂ` that the CM type chooses at the infinite place `u` extends the embedding chosen at
the place of `E` below `u`. 

### `New.prod_Φ_eq_Φ_norm`

 Let the CM type of `L` restrict to that of `E` (`New.CMTypeOver E L`), and let `w` be an
infinite place of `E`. The embeddings `Φ u` chosen at the places `u` of `L` above `w` are exactly
the embeddings of `L` that extend `Φ w`; so for `x` in `L` the product of the `Φ u x` is `Φ w` of
the norm of `x` from `L` to `E`. 

### `New.nonempty_splittingChar_of_cmTypeOver`

 Let the CM type of `L` restrict to that of `E` (`New.CMTypeOver E L`), and let `E` carry a
splitting character `υ` (`New.SplittingChar`: a unitary Hecke character with `υ x̄ = (υ x)⁻¹` that
is `∏ x_τ / |x_τ|` on ideles whose finite part is a unit of `Ô`). Then `L` has a splitting
character: `υ` composed with the norm of ideles from `L` to `E`, which at an infinite place `w` of
`E` is the product of the components at the places of `L` above `w`. 

### `New.multiplicity_star_differentIdeal`

 The different of a CM field `L` is invariant under complex conjugation: a finite place `u`
and its conjugate `star u` have the same multiplicity in it. 

### `New.multiplicity_differentIdeal_eq_ramificationIdx'_mul_of_not_dvd`

 Let `u` be a finite place of `L` that does not divide the relative different of `L / E`. Then
the multiplicity of `u` in the different of `L` is the ramification index of `u` over the place
`w` of `E` below it times the multiplicity of `w` in the different of `E`. 

### `New.WeilData.log_valuation_j_of_star_eq`

 Let `E` carry Weil data and let the finite place `w` be fixed by complex conjugation. Then the
log of the valuation of `j` at `w` is the multiplicity of `w` in the different of `E` minus twice
the log of the valuation of `α` at `w` (this is the condition `self_dual` at `w`, where `α` and
`star α` have the same order). 

### `New.nonempty_weilData_of_not_dvd_differentIdeal`

 Let `L / E` be an extension of CM fields with compatible CM types, where `E` carries Weil data
and `L` contains a primitive 5040th root of unity. Weil data consist of such a root of unity, an
element `ȷ = −ȷ̄` with `Im τȷ > 0` and `(1 − ȷ⁻¹)/2` integral, a finite idele making the integers
self-dual for the standard additive character, and a splitting character equal to `−1` at
uniformisers of places fixed by conjugation. If no finite prime of `L` fixed by complex conjugation
divides the relative different ideal of `𝓞 L` over `𝓞 E`, then `L` also carries Weil data. 

 ## A CM step of prime degree with prescribed completion at a split place 

### `New.GaloisRep.IsStepOfLocalChar`

 Let `A` be a place of the algebraic closure `Ω` (a valuation subring), `w` a finite place of
`E`, `χ` a character of `E_wˣ` (`LocField w`) with values in `ℚ/ℤ`, `ν` a Galois character of `E`
with `E' = stepField ν` the fixed field of the kernel of `symmetrise ν`, and `u` a finite place of
`E'`. The predicate says that `E' / E` is a step (`New.IsStep`: CM, Galois of prime degree, an
integer of trace `1`, for `ideleChar ν = exp (2πi ν ∘ Art)`) of degree `p` and `E'` has Weil data,
that `u` is split, lies below `A` and is the only place of `E'` above `w`, and that under the local
Artin map at `w` the character `ν` is trivial and `symmetrise ν` is `χ`. 

### `New.GaloisRep.IsStepOfLocalChar.nonempty_weilData`

 The field `E'` has Weil data. 

### `New.GaloisRep.IsStepOfLocalChar.isStep`

 The extension `E' / E`, with the idele character of `ν`, is a step. 

### `New.GaloisRep.IsStepOfLocalChar.finrank_eq`

 The extension `E' / E` has degree `p`. 

### `New.GaloisRep.IsStepOfLocalChar.isSplit`

 The place `u` is split. 

### `New.GaloisRep.IsStepOfLocalChar.below_eq_iff`

 The place `u` is the only place of `E'` above `w`. 

### `New.GaloisRep.IsStepOfLocalChar.isPlaceOver`

 The place `u` lies below `A`. 

### `New.GaloisRep.IsStepOfLocalChar.abelianLift_artinAt`

 Under the local Artin map at `w`, the character `ν` is trivial. 

### `New.GaloisRep.IsStepOfLocalChar.abelianLift_symmetrise_artinAt`

 Under the local Artin map at `w`, the character `symmetrise ν` is `χ`. 

### `New.GaloisRep.apply_eq_one_of_natCast_mem_asIdeal`

 Let `χ` be a character of `E_wˣ` (`LocField w`) with values in `ℚ/ℤ` that is killed by `p` and
kills the `(q - 1)`-th powers of units, `q = w.q` being the norm of `w`. If `w` lies above `p`,
then `χ` kills the units of `E_w`, since `p` divides `q` and so is prime to `q - 1`. 

### `New.GaloisRep.IsGrunwaldChar`

 The local behaviour of the Galois character `ν` of `E` that Grunwald's theorem gives in the
proof of `New.GaloisRep.exists_isStepOfLocalChar`, for a character `χ` of `E_wˣ` (`LocField w`)
and a number `p`: `ν` is killed by `p`; under the local Artin map at `w` it is trivial and
`symmetrise ν` is `χ`; and it kills the local units at every finite place that is fixed by
complex conjugation or lies above `p`. 

### `New.GaloisRep.IsGrunwaldChar.nsmul_eq_zero`

 The character `ν` is killed by `p`. 

### `New.GaloisRep.IsGrunwaldChar.abelianLift_artinAt`

 Under the local Artin map at `w`, the character `ν` is trivial. 

### `New.GaloisRep.IsGrunwaldChar.abelianLift_symmetrise_artinAt`

 Under the local Artin map at `w`, the character `symmetrise ν` is `χ`. 

### `New.GaloisRep.IsGrunwaldChar.abelianLift_artinMap_locIdele`

 At a place `u` fixed by conjugation or above `p`, the character `ν` kills the local units. 

### `New.GaloisRep.exists_isGrunwaldChar`

 Let `w` be a split finite place of the CM field `E`, `p` a prime, and `χ` a character of `E_wˣ`
killed by `p` that kills the `(w.q - 1)`-th powers of units (`E` also satisfies
`New.HasPrimitiveRoot5040`). Then some Galois character of `E` has the local behaviour of
`New.GaloisRep.IsGrunwaldChar`. 

### `New.GaloisRep.exists_isStepOfLocalChar`

 Grunwald's theorem for CM extensions of prime degree. Let `E` be a CM field with Weil data. Let
`w` be a split finite place of `E` (one that differs from its conjugate) lying below the place `A`
of `Ω`. Let `χ ≠ 1` be a character of `E_wˣ` that is killed by the prime `p` and kills the
`(q - 1)`-th powers of units, `q = w.q` being the norm of `w`. Then there are a Galois character `ν`
of `E` and a place `u` of `stepField ν` (the fixed field of the kernel of `g ↦ ν g + ν gᶜ`) forming
a step of degree `p` with local character `χ` at `w` (`New.GaloisRep.IsStepOfLocalChar`). This says
that `stepField ν / E` is a step of degree `p`, `stepField ν` has Weil data, and `u` is split. 

### `New.GaloisRep.exists_step_of_local_char`

 `New.GaloisRep.exists_isStepOfLocalChar` with `χ ≠ 1` given by a point `x₀` where `χ x₀ ≠ 1`. 
