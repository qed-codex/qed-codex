---
{
  "module": "src/Lib/General/Geometry/GaloisCovers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GaloisCovers.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GaloisCovers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complex points over countable rings, Zariski generic members and Galois coverings

This file collects tools for passing between points of schemes over a countable ring and complex
points, and for building Galois coverings from complex points: extensions of embeddings of countable
rings into ℂ, an injective character of the algebraic closure of a finite field, Zariski generic
members of holomorphic families, reduced closures of families of complex points, and criteria for
coverings to be étale or smooth.

## Main definitions and results

* `New.exists_ringEquiv_extend`: two embeddings of a countable ring, into `ℂ` and into an
  algebraically closed field of the same cardinality, are matched by an isomorphism of the fields
  (Steinitz's classification, relative to the ring).
* `New.exists_ringHom_complex_extend` lets one view a point over a field of cardinality at most that
  of ℂ as a complex point, compatibly with given embeddings of a countable base ring in the field
  and in ℂ.
* `New.Variety.exists_generic_member`: if `X` is locally of finite type over a countable ring and
  `φ` is a holomorphic family of complex points of `X` on a connected open set `U`, some `φ b`
  specialises, in the Zariski topology, to every `φ c`.
* `New.Variety.ReducedClosure`: the reduced closure in a finite product of schemes over `S` of a
  family of complex points; `New.Variety.ReducedClosure.exists_lift` constructs maps between two
  such closures.
* `New.Variety.isGaloisCovering_of_complex_points`: over a countable domain whose maps to fields of
  characteristic 0 are injective, a surjective map from a proper to a separated scheme, with a
  finite group acting simply transitively on its fibres of complex points, is a Galois covering.
* `New.Variety.IsGaloisCovering.smoothOfRelativeDimension_baseChange`: for a Galois covering
  `W → Z` over a domain `R`, with `W` proper and reduced and `Z` separated and smooth, the base
  change of `W` to a field of characteristic 0 containing `R` is smooth.

Notions from other files:
* `New.Variety.IsGaloisCovering`: Δ is a finite group of automorphisms of W over c : W → Z, c is
  surjective, and Δ acts simply transitively on the fibres of c on points with values in fields of
  characteristic 0.
* `New.LandsIn t U`: the morphism t lands in the open U, that is, the preimage of U is everything.
* `New.HolomorphicAt φ w`: for every function regular on an open set containing φ w, the nearby
  members of the family φ land in that open set and the function pulls back to one analytic at w.
  The parameter space is a finite-dimensional complex normed space (`FinComplexSpace`).
* `New.IsSeparatingFamily ξ`: the scheme is reduced and the complex points ξ z are dense in it.

## Relation to the literature

The isomorphisms of fields come from Steinitz's theorem, and the étaleness criterion is that of
Chase–Harrison–Rosenberg.


 ## Steinitz's theorem relative to a countable ring 

### `New.exists_ringEquiv_extend`

 Let `K` be a countable ring, `L` an algebraically closed field with the cardinality of `ℂ`, and
`f : K → ℂ`, `g : K → L` injective ring maps. Then some isomorphism `σ : ℂ ≃+* L` satisfies
`σ ∘ f = g`.

A form of Steinitz's theorem (characteristic and cardinality determine an uncountable algebraically
closed field up to isomorphism), refined so that the isomorphism respects the given embeddings. 

 ## Extension of embeddings of a countable ring into ℂ 

### `New.exists_ringHom_complex_extend`

 Let `D` be a countable ring, `K` a field with `#K ≤ #ℂ`, and `f : D → K`, `φ : D → ℂ`
injective ring maps. Then `φ` extends along `f` to a ring map `ψ : K → ℂ`. 


## A faithful character of the units of the algebraic closure of a finite field

`New.faithfulChar k` is chosen among the injective multiplicative characters from the algebraic
closure of the finite field `k` to `ℂ`. `New.exists_injective_mulChar` shows that such a character
exists, using Teichmüller lifts to Witt vectors, so the chosen character is injective
(`New.faithfulChar_injective`).


### `New.exists_injective_mulChar`

 The algebraic closure of a finite field has an injective multiplicative character to `ℂ`. 

### `New.faithfulChar_injective`

 For a finite field `k` the character `faithfulChar k`, chosen among the multiplicative
characters from the algebraic closure of `k` to `ℂ`, is injective, so it is faithful
(`IsFaithfulMulChar`). 


## Zariski generic members of holomorphic families of complex points

Idea: over a countable base, an affine open of finite type has countably many functions, so Baire's
theorem and the identity theorem give a `b` at which no function vanishes unless it vanishes along
all of `φ` nearby.


### `countable_sections`

 If `X` is locally of finite type over a countable ring, the ring of sections of `X` over an
affine open `W` is countable. 

### `exists_countable_residue_point`

 Let `X` be locally of finite type over a countable ring. Every point `t : Spec K ⟶ X` with
values in a field `K` factors through the residue field of a point `z` of `X`, as `Spec` of a ring
map `φ` (written `specMap φ`) followed by the canonical map to `X`, and this residue field is
countable. 

### `exists_mem_forall_ne_zero_of_analyticOnNhd`

 For countably many analytic functions on a connected open set `N` and an open set `V` meeting
`N`, some point of `N ∩ V` is a zero only of those functions that vanish on all of `N`. 

### `exists_mem_eventually_specializes`

 Let `X` be locally of finite type over a countable ring and `φ` a family of complex points of
`X`, parametrised by a finite-dimensional complex space and holomorphic on the open set `U`
(`HolomorphicAt`: regular functions pull back to analytic ones). If `c ∈ U` lies in the closure of
an open set `V`, there is `b ∈ V` such that the image point of `φ b` specialises to that of `φ e`
for all `e` near `c`. 

### `exists_generic_member`

 Let `X` be locally of finite type over a countable ring and `φ` a family of complex points of
`X`, parametrised by a finite-dimensional complex space and holomorphic (regular functions pull back
to analytic ones) on a connected open set `U`. There is `b ∈ U` such that the image point of
`φ b` specialises to the image point of `φ c` for every `c ∈ U`. 

 ## Reduced closures in products and Galois coverings 

### `ReducedClosure`

 Let `b` be a complex point of a scheme `S`, let `Z j` be finitely many schemes over `S`, and let
`F j a` be a complex point of `Z j` over `b` for each `a : A`. A reduced closure of the tuples
`(F j a)_j` is a reduced closed subscheme `W` (the field `scheme`) of the product of the `Z j` over
`S`, with a dense family of complex points that lift these tuples. 

### `ReducedClosure.scheme`

 The closure, a scheme over `S`. 

### `ReducedClosure.incl`

 The inclusion of `scheme` in the product of the `Z j`. 

### `ReducedClosure.point`

 The complex point of `scheme` indexed by `a`. 

### `ReducedClosure.point_incl`

 The point `point a` lies over the point `(F j a)_j` of the product. 

### `ReducedClosure.isClosedImmersion`

 `incl` is a closed immersion. 

### `ReducedClosure.isSeparatingFamily`

 `scheme` is reduced and its points `point a` are dense in it. 

### `instance (C : ReducedClosure F) : AlgebraicGeometry.IsReduced C.scheme.left`

 A reduced closure is a reduced scheme. 

### `ReducedClosure.proj`

 The morphism from the closure `C.scheme` to the factor `Z j`: the inclusion into the product
followed by the `j`-th projection. 

### `instance : Nonempty (ReducedClosure F)`

 Every family of tuples of complex points has a reduced closure. 

### `ReducedClosure.hom_ext`

 Two morphisms over `S` to a reduced closure `C.scheme` agree as soon as their composites with
all projections `C.proj j` to the factors agree. 

### `ReducedClosure.exists_lift`

 Let `C` and `C'` be reduced closures (reduced closed subschemes of `∏ᶜ Z` and `∏ᶜ Z'` over `S`
with dense complex points) of families `F` and `F'` of complex points indexed by the
same set `A`. Maps `f j` from `C'` to the factors `Z j` that send the point `a` of `C'` to
`F j (σ a)` come from a map `g` to the closure `C`, and `g` sends the point `a` to the point
`σ a`. Here `S` is the base scheme and `F j a` is a complex point of `Z j` over the fixed complex
point `b` of `S`, with `j` in the finite set `J` and `a` in `A`. 

### `etale_of_simply_transitive`

 Chase–Harrison–Rosenberg. Let `B` be a finite `A`-algebra with `A → B` injective and `G` a
finite group. Assume: (a) `σ` is a right action of `G` on `B` by `A`-algebra maps, that is
`σ 1 = id` and `σ (g * h) = σ h ∘ σ g`; (b) for every field `k` over `A` and any two `A`-algebra
maps `x y : B → k` there is exactly one `g` with `x ∘ σ g = y`; (c) every element of `B` fixed
by all `σ g` comes from `A`. Then `B` is étale over `A`. 

### `isGaloisCovering_of_complex_points`

 Let `R` be a countable domain, with a given map to `ℂ`, all of whose ring maps to fields of
characteristic 0 are injective. Let `W` be proper over `R`, `Z` separated, and `c : W ⟶ Z`
surjective and invariant under an action `s` of a finite group `Δ` on `W` that is simply transitive
on the fibres of `c` on complex points (`specOver R ℂ` is `Spec ℂ` over `Spec R`). Then `c` is a
Galois covering with group `Δ` in the sense of `New.Variety.IsGaloisCovering`: simple transitivity
holds for points with values in any field of characteristic 0. 

### `IsGaloisCovering.exists_apply_eq_of_apply_eq.`

 Let `c : W ⟶ Z` be a Galois covering with group `Δ` acting through `s`, and `π : T ⟶ Z` a map
from a scheme whose field-valued points have characteristic zero. If `p : X ⟶ W` lies over
`r : X ⟶ T`, then two points of `X` with the same image under `r` have images under `p` in the
same `Δ`-orbit. 

### `IsGaloisCovering.finite_preimage_singleton.`

 Let `c : W ⟶ Z` be a Galois covering with group `Δ`, let `π : T ⟶ Z` be a map from a scheme
whose field-valued points have characteristic zero, and let `p : X ⟶ W`, injective on points, lie
over `r : X ⟶ T`. Then the fibres of `r` are finite. 

### `exists_algHom_specMap_comp_eq`

 Let `Spec B` be the pull-back of `c : W ⟶ Z` along `u : Spec A ⟶ Z`, with projection `p` to
`W`. A point `y` of `W` with values in an `A`-algebra `K` that lies over the point
`Spec K ⟶ Spec A ⟶ Z` comes from an `A`-algebra map `B → K`. Here `specMap φ` is the morphism
of spectra induced by a ring map `φ`. 

### `IsGaloisCovering.exists_simply_transitive_action`

 Let `c : W ⟶ Z` be a Galois covering with group `Δ` acting through `s`, and let `Spec B` be its
pull-back along `u : Spec A ⟶ Z`, where the field-valued points of `A` have characteristic zero and
the projection `p : Spec B ⟶ W` is a monomorphism. Then `Δ` acts on the `A`-algebra `B` from the
right, compatibly with `s` and simply transitively on the field-valued points of `B` over `A`.
(Galois covering: `c` is surjective and `Δ` is simply transitive on its fibres of points in fields
of characteristic zero; `specMap φ` is the morphism of spectra induced by `φ`.) 

### `algebraMap_pi_injective`

 A reduced Artinian ring `N` embeds in any product over its maximal ideals `m` of faithful
algebras over the residue fields `N ⧸ m`. 

### `exists_algebraMap_pi_eq`

 An element of the product of the `Ω m` whose components all come from the residue fields of
the reduced Artinian ring `N` comes from `N`. 

### `exists_algebraMap_eq_of_isIntegral_of_smooth`

 If `A` is a smooth algebra over a normal domain `P`, then `A` is integrally closed in
`A ⊗[P] Frac P`. 

### `IsGaloisCovering.isNilpotent_of_forall_mem`

 Let `Spec B` be the pull-back of a Galois covering `c : W ⟶ Z` with group `Δ` along
`u : Spec A ⟶ Z`, where `A` has field-valued points of characteristic zero, `B` is integral over `A`
and `p : Spec B ⟶ W` is a monomorphism. Let `σ` be the action of `Δ` on `B` compatible with the
action `s` on `W` (`specMap f` is the morphism of spectra induced by `f`). If an ideal `I` of `B`
contains the image of no nonzero element of `A` and contains all the conjugates `σ g b`, then `b` is
nilpotent. 

### `mem_range_algebraMap_of_forall_apply_eq`

 Let `Ω` be a Galois extension of a field `K`, both algebras over `A`. If all `A`-algebra maps
`B → Ω` take the same value at `z`, this value lies in `K`. 

### `IsGaloisCovering.etale_of_isPullback`

 Let `c : W ⟶ Z` be a Galois covering with group `Δ`, with `W` proper and `Z` separated over
`R`. Let `A` be étale over a normal domain `P`, with field-valued points of characteristic zero, and
let `Spec B` be the pull-back of `c` along `u : Spec A ⟶ Z`. If `B` is reduced and finite over `A`
and the projection `p : Spec B ⟶ W` is a monomorphism, then `B` is étale over `A`.
(Galois covering: `c` is surjective and `Δ`, acting through `s`, is simply transitive on its fibres
of points in fields of characteristic zero; `specMap f` is the morphism of spectra induced by the
ring map `f`.) 

### `isReduced_pullback_of_flat`

 The base change of a reduced scheme along a flat preimmersion is reduced: its stalks are those
of the scheme. 

### `smoothOfRelativeDimension_pullback_snd_comp`

 If the base change of `c : W ⟶ Z` to the fibre product `Z ×_T E` is smooth of relative dimension
`0` and `Z ×_T E ⟶ E` of relative dimension `d`, then the base change of `c ≫ f : W ⟶ T` along any
map factoring through `i : E ⟶ T` is smooth of relative dimension `d`. 

### `IsGaloisCovering.smoothOfRelativeDimension_baseChange`

 Let `c : W ⟶ Z` be a Galois covering over `Spec R` for a domain `R`: `c` is surjective, and a
finite group `Δ` acts on `W` over `Z` through `s`, simply transitively on the fibres over points
with values in fields of characteristic 0. Suppose `W` is proper and reduced and `Z` is separated
and smooth of relative dimension `d`. Then for any field `k` of characteristic 0 into which `R`
injects, the base change of `W` to `k` is smooth of relative dimension `d` over `Spec k`
(`specMap f` is the morphism of spectra induced by the ring map `f`). 
