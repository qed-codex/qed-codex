---
{
  "module": "src/Lib/ClassField/Local/ArtinMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Local/ArtinMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Local/ArtinMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local and global Artin maps, algebraic Hecke characters and tame inertia

The file defines the local Artin map `New.artinAt` with values in `Γ^ab`, the global Artin map
`New.artinMap` of a number field `K`, and algebraic Hecke characters. In the parts on number fields,
`Γ` is the Galois group (`IsProGalois Γ K Ω`) of an algebraically closed field `Ω` over `K`; `Ω` has
no binder here (it is fixed elsewhere), and `New.ClosurePlace` is the type of valuation subrings of
`Ω`. For a local field, the file shows that the local Artin map sends uniformisers to inverse
Frobenii. At a place of a number field, it proves the main properties of the local Artin map
`New.localArtin`: the defining formula, compatibility with norms, its image, its relation to
`New.artinAt`, and tame inertia.

## Main definitions and results

* `New.artinAt`: the local Artin map at `v`, with values in the topological abelianisation of `Γ`.
* `New.artinMap`: the global Artin map from the finite ideles of `K` to the abelianised Galois
  group. It is chosen (`Classical.epsilon`) so that each character of `Γ` takes on it the product of
  its values on the local Artin maps. This file does not prove that such a map exists;
  `New.abelianLift_artinMap_eq_finprod_of_exists` gives the product formula when one does.
* `New.algHeckeChars`, `New.AlgHeckeChar`: algebraic Hecke characters, as characters of the finite
  ideles (`New.AlgHeckeChar.character`) together with their infinity type
  (`New.AlgHeckeChar.infinityType`).
* `New.IsPlaceOver.isLocalArtin_localArtin`: the formula holds; the local theory in `ℚ̄_p` then
  applies.
* `New.IsTameGenerator`, `New.IsPlaceOver.exists_eq_pow_and_apply_conj_eq_pow`: tame generators of
  inertia, and the values on inertia of a homomorphism of exponent prime to `w`.
* `New.IsPlaceOver.tameGenerator`, `New.IsPlaceOver.tame_inertia`,
  `New.IsPlaceOver.exists_isTameUnit`: a chosen tame generator, and a unit of `K_w`
  whose symbol it is and whose residue generates the units of the residue field.

Notions from other files:
* `New.localArtin Γ A w`: a chosen homomorphism from `K_w^×` to the topological abelianisation of
  the decomposition group of `A`, pinned down on `K^×` by `New.IsLocalArtin`.
* `New.IsCompletionEmb w p Γ A j`: embeddings of `K_w` and of `Ω` (by `j`) in `ℚ̄_p` that induce `A`
  and make the decomposition group of `A` the Galois group of `ℚ̄_p` over `K_w`.
* `New.IsLocalArtin`: The homomorphism `f : Lˣ → Γ^ab` satisfies `New.Cohomology.classOfInvariant (χ
  (f x)) = −(δχ ∪ x)` for all continuous characters `χ` and all `x` in `Lˣ`.
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.IsPlaceOver`: The valuation subring `A` of `Ω` lies over the prime `w` of `K`: an integer of
  `K` is in the maximal ideal of `A` exactly when it lies in `w`.
* `New.QZChar.abelianLift`: The homomorphism induced by the continuous character χ on the
  topological abelianisation of Γ, with values in ℚ/ℤ written multiplicatively.

## Relation to the literature

Known result: Local class field theory, with Brauer invariant, Artin map, norms and tame symbol. It
is proved for henselian fields such as fixed fields of decomposition groups, with the norm index in
prime degree coming from Tate's lemma on the Herbrand quotient. Source: J.-P. Serre, Local Fields
(1979), XII–XIV; J. S. Milne, Class Field Theory (v4.03), I and III 2.

See also `Lib.ClassField.Avatar.LocalGlobalCompatibility` and `Lib.ClassField.Places.LocalFields`.



## The global Artin map and algebraic Hecke characters

* `New.star_locIdele`: complex conjugation of a CM field carries an idele with one component at `v`
  to the idele with the conjugate component at the conjugate place.


### `star_locIdele`

 The complex conjugate of the idele with component `x` at `v` and `1` elsewhere is the idele
with the conjugate of `x` at the conjugate place `star v` and `1` elsewhere. 

### `algHeckeChars`

 The group of algebraic Hecke characters: pairs `(θ, n)` of a character `θ` of the finite
ideles with open kernel and an infinity type `n`, an integer for each embedding `σ : K → ℂ`,
such that `θ x = ∏ σ, σ x ^ (-n σ)` for all `x` in `Kˣ`. The condition is asked of all `x`, not
only of the totally positive ones, so this is the usual notion when `K` is totally complex. 

### `AlgHeckeChar`

 The type of algebraic Hecke characters of K: pairs (θ, n) of a character of the finite
ideles and its infinity type, as in `New.algHeckeChars`. 

### `AlgHeckeChar.character`

 The character of the finite ideles of an algebraic Hecke character `θ = (χ, n)`: the map `χ`. 

### `AlgHeckeChar.infinityType`

 The infinity type of an algebraic Hecke character `θ = (χ, n)`: the integer `n σ` for each
embedding `σ : K → ℂ`, with `χ x = ∏ σ, σ x ^ (-n σ)` for `x` in `Kˣ`. 

### `artinAt`

 The local Artin map `K_v^× → Γ^ab` at the finite place `v` of `K`: the local Artin map
`New.localArtin` to the abelianised decomposition group of `New.placeOver v`, the chosen place of
`Ω` above `v`, followed by the map that the inclusion of that group in `Γ` induces. 

### `artinMap`

 The global Artin map from the finite ideles to the topological abelianisation of `Γ`: a
homomorphism `f`, chosen by `Classical.epsilon`, such that for every continuous character `χ` of `Γ`
the value of `χ` at `f a` is the product over the finite places `v` of its values at the local Artin
symbols of the components of `a`. This file does not prove that such an `f` exists; when one
does, `New.abelianLift_artinMap_eq_finprod_of_exists` gives that formula for `New.artinMap`. 

### `abelianLift_artinMap_eq_finprod_of_exists`

 If some homomorphism from the finite ideles of `K` to the topological abelianisation of `Γ`
takes, on every character `χ` of `Γ`, the product over the finite places `v` of the values of `χ`
at the local Artin symbols (`New.artinAt`), then `New.artinMap` is such a homomorphism. 


## The local Artin map on uniformisers

One property of a homomorphism `F` with `New.IsLocalArtin Γ k A F`, the local Artin map of a local
field `k` with absolute Galois group `Γ` (`New.IsLocalGalois`).


### `New.IsLocalArtin.exists_frob_of_isUniformiser`

 Let `F` be a local Artin map of the local field `k` (`New.IsLocalArtin`) and `π` a uniformiser
of `k`. Then `F π` is the class of `φ⁻¹` for some arithmetic Frobenius `φ` (`New.IsFrob` for
the order of the residue field of `k`). 


## The local Artin map at a place of a number field

Let `A` be a valuation subring of an algebraically closed `Ω` over the prime `w` of a number field
`K`, with decomposition group `D`. The map `New.localArtin` goes from `K_w^×` to `D^ab` and is
pinned down by `New.IsLocalArtin`: writing `Art` for `New.localArtin Γ A w`,
`χ (Art x) = -inv (χ, x)`, where `inv` is the local invariant (`New.Cohomology.classOfInvariant`
read backwards); so uniformisers go to inverse Frobenii.

`Γ` is the Galois group of `Ω / K`, and `(χ, x)` is the class `cyclicClass _ χ x` in `H²(D, Ω^×)`.
Valuations are multiplicative: `Valued.v x = exp (-n)` says that `x` has order `n` at `w`.
`New.FinPlace.q w`, written `w.q` or `q`, is the number of elements of the residue field.


 ### Continuity of homomorphisms on `K_w^×` 

### `isOpen_of_forall_pow_mem`

 For a finite place `w` of a number field `K` and `n ≠ 0`, every subgroup `T` of `K_w^×` that
contains all `n`-th powers is open. 

### `continuous_hom_locField_units`

 Every homomorphism from `K_w^×` to the topological abelianisation of a profinite group `Γ`
(compact, totally disconnected) is continuous. 

### `inertiaAbove`

 The union of all inertia groups in the Galois group of Ω over K at places of Ω above the
places in S. 

 ### The defining formula and norms 

### `isLocalArtin_comp_unitsMap`

 Let `A` lie over the finite place `w` of `K`, and let `emb` embed `K_w` continuously in `ℚ̄_p`
and give an equivariant `K`-embedding `j : Ω → ℚ̄_p` inducing `A` (`New.IsCompletionEmb`); write `D`
for the decomposition group of `A`. Suppose `f : K_wˣ → D^ab` is a local Artin map for `K_w`,
meaning `IsLocalArtin` holds with invariants taken relative to the valuation ring of `ℚ̄_p`:
`classOfInvariant (χ (f x)) = -cyclicClass χ x` for every continuous character `χ : D → ℚ/ℤ`. Then
the restriction of `f` to `Kˣ` satisfies the same identity for the fixed field of `D`, with
invariants taken relative to `A`, because `j` keeps a uniformiser and the order of the residue field
and so preserves invariants. 

### `isLocalArtin_localArtin`

 Let `A` lie over `w` (`h`) and let `emb` embed `K_w`, and `Ω` by `j`, in `ℚ̄_p`, inducing `A`
(`New.IsCompletionEmb`). Then `f = New.localArtin Γ A w` satisfies `χ (f x) = -inv (χ, x)` for every
character `χ` of the decomposition group: (a) for `x` in `K_w^×`, with the invariant of `K_w` read
in `ℚ̄_p`, relative to its valuation ring `intQpBar p`; (b) for `x` in `K^×`, with the invariant of
the fixed field of the decomposition group.

This is the characterisation of the local Artin map by invariants from the local reciprocity law,
for completions of number fields. 

### `finite_and_localNorm_eq_norm`

 Let `k` be a number field below `K` and `u` the place of `k` below `w`. The completion `K_w` is
finite over `k_u`, along `New.locMap`, the map of completions induced by `k → K`, and the local norm
`New.localNorm k w` is the norm of this extension. 

### `_root_.New.IsPadicAt.below`

 Let `j : Ω → Ω` extend `k → K`. An embedding of `K_w` in `ℚ̄_p` that induces `A` along `i`
restricts to an embedding of the completion of `k` below `w` that induces `A.comap j` along
`i ∘ j`. 

### `_root_.New.IsNormCompatible`

 Let `K / k` be number fields with Galois groups `Γ` and `Γ'`, and let `ψ : Γ → Γ'` be the map
induced by `j : Ω → Ω`. The local Artin maps at `A` over `w` and at `A.comap j` over the place of
`k` below `w` are compatible with the local norm from `K_w`. 

### `_root_.New.IsNormCompatible.localArtin_localNorm`

 If `y` has the symbol `g`, then the norm of `y` has the symbol `ψ g`. 

### `_root_.New.IsNormCompatible.exists_localNorm_eq`

 If the kernel of `χ` is the image of the decomposition group of `A` under `ψ` and `χ` kills
  the symbol of `x`, then `x` is a local norm. 

### `localArtin_localNorm_eq_of_isCompletionEmb`

 The symbol of a norm, computed in `ℚ̄_p`. Let `emb_w` and `emb_u` embed `K_w` and `k_u`, for the
place `u` of `k` below `w`, in `ℚ̄_p` through `i` and `i ∘ j`, and let `φ` be the inclusion of the
Galois group of `ℚ̄_p` over `K_w` in that over `k_u` (`hφ`, continuous by `φ_cont`). Let the local
norm be the field norm of `K_w` over `k_u` (`norm_eq`), and let both local Artin maps satisfy the
defining formula of `New.IsLocalArtin` (`art_w`, `art_u`). If `y` in `K_w^×` has the symbol `g`,
then its local norm has the symbol `φ g`. 

### `isNormCompatible`

 Let `K / k` be number fields, with `Γ` and `Γ'` acting on `Ω` as their Galois groups. Let
`j : Ω → Ω` extend `k → K` (`hj`) and induce `ψ : Γ → Γ'` (`hψ`), and let the valuation subring `A`
of `Ω` lie over the finite place `w` of `K` (`h`). Then local class field theory is norm functorial
here: the local Artin map at `A` over `w` and the local Artin map at `A.comap j` over the place of
`k` below `w` are compatible with the local norm from `K_w` and with `ψ`
(`New.IsNormCompatible`). 

### `localArtin_localNorm`

 Norm compatibility of the local Artin maps (`New.IsNormCompatible`) at `A` over `w`, as in
`New.IsPlaceOver.isNormCompatible`; `j` is the identity of `Ω` unless given, and the two hypotheses
on `j` then default to the tactic proofs `by tauto` and `by simp`, which may fail. 

 ### The image of the local Artin map 

### `denseRange_localArtin`

 If `A` lies over `w`, the local Artin map `New.localArtin Γ A w` from `K_w^×` to the abelianised
decomposition group of `A` has dense range.

A consequence of the local reciprocity law, stating only that the image is dense. 

### `exists_isFrob_localArtin_eq_inv`

 The local Artin symbol of a uniformiser of `K_w` is the class of the inverse of a Frobenius
element at `A`. This is the clause on uniformisers of the local reciprocity law, for completions of
number fields. 

### `exists_mem_inertiaGroup_localArtin_eq`

 The local Artin symbol of a unit of `K_w` is the class of an element of the inertia group of
`A`. This is the clause on units of the local reciprocity law, for completions of number fields. 

### `exists_localArtin_eq_of_isFrob_pow`

 Let `g⁻¹` stabilise `A` and act on residues as `x ↦ x ^ q ^ n`, where `q` is the residue order
of `w`. Then the class of `g` is the local Artin symbol of an element of `K_wˣ` of order `n`.

This is the surjectivity part of the local reciprocity law, onto the image of the elements of the
Weil group of non-negative degree. 

### `exists_localArtin_eq_of_mem_inertiaGroup`

 For a place `A` of `Ω` lying over the finite place `w` of the number field `K` (hypothesis `h`),
with `Γ` the Galois group of `Ω/K`, every `g` in the inertia group of `A` is hit by the local Artin
map on units. That is, there is a unit `x` of the completion `K_w` with `v x = 1` whose local Artin
symbol `localArtin Γ A w x` equals the image of `g` in the abelianised decomposition group of
`A`. 

### `exists_localArtin_eq_of_isFrob`

 For a place `A` of `Ω` lying over the finite place `w` of the number field `K` (hypothesis `h`),
with `Γ` the Galois group of `Ω/K`, suppose `g⁻¹` is an arithmetic Frobenius at `A`, i.e.
`IsFrob A w.q g⁻¹` with `w.q` the size of the residue field. Then there is a uniformiser `x` of the
completion `K_w` (`v x = exp (-1)`) whose local Artin symbol `localArtin Γ A w x` equals
the image of `g` in the abelianised decomposition group of `A`. 

### `exists_localArtin_eq`

 Let `g⁻¹` stabilise `A` and act on residues as `x ↦ x ^ q`, where `q = w.q ^ n`. Then the class
of `g` is the local Artin symbol of an element of `K_wˣ` of order `n`.

This is one inclusion of the local reciprocity law's description of the image of the Artin map:
classes of Weil group elements are attained. It covers completions of number fields and one sign of
the Frobenius exponent. 

 ### The map to the abelianised global group 

### `artinAt_eq_of_localArtin_eq`

 Let `A` lie over `w` and let the local Artin symbol of `x` be the class of `g` in the
abelianised decomposition group of `A`. Then `New.artinAt Γ w x` is the class of `g` in the
abelianisation of `Γ`: `New.artinAt Γ w` may be computed at any place over `w`. 

### `abelianLift_artinAt`

 Let `A` lie over `w`. The value of a character `χ` of `Γ` at `New.artinAt Γ w x` equals the
value of its restriction `QZChar.comap (subgroupIncl _) χ` to the decomposition group of `A` at
the local symbol of `x`. 

### `abelianLift_artinAt_principal`

 Let `A` lie over `w`, `χ` a character of `Γ` and `x` in `K^×`. The class (`classOfInvariant` of
the decomposition field) with invariant the value of `χ` at `New.artinAt Γ w x` is minus the
restriction (`resH2`) to the decomposition group of `A` of the global class `(χ, x) = δχ ∪ x` in
`H²(Γ, Ω^×)`. 

### `abelianLift_artinAt_eq_one_iff`

 Let `A` lie over `w`, `χ` a character of `Γ` and `x` in `K^×`. Then `χ` kills
`New.artinAt Γ w x` if and only if the global class `(χ, x) = δχ ∪ x` restricts to zero on the
decomposition group of `A`. 

 ### The tame symbol, the tame generator and tame inertia 

### `valuation_smul_div_sub_lt_one`

 The tame formula for a local field `k`, whose Galois group `G` acts on `E` with valuation ring
`B`, and a local Artin map `F` for it (`New.IsLocalArtin`). Let `q` be the number of residues of
`k`. If the unit `u` of `k` has symbol `F u = g` and `y ^ (q - 1) = π` for a uniformiser `π` of `k`,
then `g • y / y` is congruent to `u` modulo the maximal ideal of `B`. 

### `valuation_sub_lt_one_iff_of_localArtin_eq`

 Let `A` lie over `w`, let `π` in `K` be a uniformiser for `A` and `y ^ (w.q - 1) = π`, where
`w.q` is the number of residues of `w`, and let `u` be a unit of `K_w` (`v u = 1`, with `v` the
valuation of `K_w`) with local Artin symbol `s`. Then for `x` in `K`, `u` is congruent to `x` modulo
the maximal ideal of `K_w` if and only if `s • y / y` is congruent to `x` modulo the maximal ideal
of `A`.

A variant of the tame symbol congruence of local reciprocity. Residue classes are compared only
through elements of `K`. 

### `IsTameGenerator`

 An element `γ` of the inertia group of `A` is a tame generator: for every `n` that is a unit at
`A` (prime to the residue characteristic) it multiplies an `n`-th root `y` of a uniformiser `π` of
`K` by a primitive `n`-th root of unity. 

### `exists_tameGenerator`

 A tame generator exists: if `A` lies over `w`, some `γ` in the inertia group of `A` has the
following property for every `n` that is a unit at `A` (prime to the residue characteristic): there
are a uniformiser `π` of `K` and `y` with `y ^ n = π` such that `γ • y / y` is a primitive `n`-th
root of unity.

This is the existence of tame generators of inertia (Serre, Local Fields, IV §2), for one generator
at a place of a number field; the uniformiser may depend on `n` and the primitive root of unity is
not prescribed. 

### `tameGenerator`

 A chosen generator of tame inertia at the place `A` above `w`, as an element of the inertia
group. Its defining property is `New.IsPlaceOver.exists_isPrimitiveRoot_tameGenerator_smul_div`. 

### `exists_isPrimitiveRoot_tameGenerator_smul_div`

 For every `n` that is a unit at `A`, the tame generator multiplies some `n`-th root `y` of a
uniformiser `π` of `K` at `A` by a primitive `n`-th root of unity. 

### `isTameGenerator_tameGenerator`

 The chosen element `New.IsPlaceOver.tameGenerator` is a tame generator of inertia at `A`. 

### `exists_eq_pow_and_apply_conj_eq_pow`

 The structure of tame inertia at a place of a number field. Let `γ` be a tame generator at `A`,
and let `f` kill the elements of inertia near `1` and have `f g ^ n = 1` on inertia, with `n` prime
to `w`. For `s` in inertia, `f s` is a power of `f γ`, and conjugation by a `q`-Frobenius raises
`f s` to the power `q`. 

### `tame_inertia`

 The structure of tame inertia for the chosen tame generator. Let `f` kill the elements of
inertia near `1` and have `f g ^ n = 1` on inertia, with `n` prime to `w`. For `s` in inertia,
`f s` is a power of the image of the tame generator, and conjugation by a `q`-Frobenius raises
`f s` to the power `q`. 

### `IsTameUnit`

 For `A` over `w`: `u` in `K_wˣ` is a unit of the valuation ring whose local Artin symbol is the
tame generator and whose residue generates the units of the residue field. 

### `IsTameUnit.mem_unitGroup`

 `u` lies in the unit group of the valuation ring. 

### `IsTameUnit.localArtin_eq`

 The symbol of `u` is the class of the tame generator. 

### `IsTameUnit.mem_zpowers_residue`

 Every unit of the residue field is a power of the residue of `u`. 

### `IsTameUnit.valuation_eq_one`

 `u` has valuation `1`. 

### `exists_isTameUnit`

 Let the valuation subring `A` of `Ω` lie over the finite place `w` of the number field `K`, with
`Ω / K` Galois. Then some unit `u` of `K_w` lies in the valuation ring, has local Artin symbol equal
to the tame generator at `A`, and has a residue that generates the multiplicative group of the
residue field (`New.IsPlaceOver.IsTameUnit`).

A consequence of local reciprocity (units correspond to inertia). Weaker than the tame symbol
formula (Serre, Local Fields, XIV), which determines the residue of such a unit; here it is only
shown to be a generator. 
