---
{
  "module": "src/Lib/Adelic/Adeles/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite adeles of number fields: topology, idempotents, functoriality and base change

This file develops the finite adeles `New.𝔸f E` of a number field `E` and their subring `New.Ô E` of
integral adeles. The valuation `Valued.v` of a completion, written `v`, is multiplicative with
values in `ℤᵐ⁰` (the integers, written multiplicatively by `exp`, with a zero adjoined), so that
integral elements have `v ≤ 1`. The file covers the topology of completions and finite adeles, and
the idempotents `New.idem` of sets of places. It also covers functoriality along embeddings of
number fields through `New.adeleMap`, and base change along an extension `L / K`. For CM fields,
complex conjugation `star` is extended to places and finite adeles, and commutes with
`New.adeleMap`; it induces maps `New.conjLoc` between the completions at conjugate places.

## Main definitions and results

* `New.FinPlace`, `New.LocField`, `New.LocInt`, `New.ResField`: finite places, completions, their
  integers and residue fields; `New.𝔸f`, `New.Ô`: finite adeles and integral finite adeles;
  `New.evalAt w` is the ring homomorphism taking a finite adele to its component in the completion
  `New.LocField w`.
* `New.isCompact_Ô`, `New.isOpen_Ô`: the integral adeles `New.Ô E` are compact and open.
* `New.denseRange_algebraMap_Ô`, `New.denseRange_algebraMap_finAdele`: `𝓞 E` is dense in `Ô E` and
  `E` is dense in the finite adeles (strong approximation), which are a Polish space.
* `New.adeleCombination`: for a basis `b` of `L / K`, the map `(a i) ↦ ∑ a i • b i` from `ι → 𝔸f K`
  to `𝔸f L`.
* `New.isHomeomorph_adeleCombination`: this map is a homeomorphism.
* `New.mem_range_finAdeleIncl_iff`: for `L / K` Galois, the adeles fixed by `Gal(L/K)` are those
  from `K`.

## Relation to the literature

Known result: the topology of the finite adeles of a number field, strong approximation and base
change. Base change is proved for finite adeles only, and the full adeles are those of totally
complex fields with chosen embeddings.

Source: J. W. S. Cassels, Global Fields, in Cassels-Fröhlich, Algebraic Number Theory, 1967, ch. II
§§14-16; A. Weil, Basic Number Theory, ch. IV.



## Places, completions, adeles and CM fields

* `New.𝔸`: the adeles with one factor `ℂ` for each infinite place (meant for totally complex
  fields). The diagonal embedding `New.toAdele` depends on the choice of embeddings
  `New.PlaceEmbedding`; `New.CMType` is a CM number field with such a choice.
* For a CM field, `star` is complex conjugation on the integers and the places, and `New.conjLoc`
  is the map that it induces between the completions at conjugate places;
  `New.HasPrimitiveRoot5040` is the class of CM fields that contain a primitive root of unity of
  order `5040`.


### `PlaceEmbedding`

 A choice, for each infinite place w of E, of a complex embedding Φ w of E that induces w. 

### `PlaceEmbedding.Φ`

 For each infinite place w, a complex embedding of E. 

### `PlaceEmbedding.mk_Φ`

 The embedding Φ w induces the place w. 

### `CMType`

 A CM number field E together with a choice, for each infinite place w of E, of a complex
embedding of E that induces w.
So `[CMType E]` includes the hypothesis that E is a CM number field. 

### `isIntegral_rat`

 A number field is integral over `ℚ`. The instance `Star E` on a CM field needs this fact, and
instance search is too slow to find it. 

### `FinPlace`

 The set of finite places of E, that is, nonzero prime ideals of its ring of integers. 

### `𝔸f`

 The ring of finite adeles of the number field E. 

### `𝔸`

 The product of one copy of ℂ for each infinite place of E with the finite adeles of E. It is the
adele ring of E when E is totally complex. 

### `toAdele`

 The diagonal embedding of E in its adeles, given at the infinite places by the embeddings chosen
in `New.PlaceEmbedding`. 

### `LocField`

 The completion E_w of E at the finite place w. 

### `LocInt`

 The ring of integers of the completion E_w of E at the finite place w. 

### `ResField`

 The residue field of the completion E_w of E at the finite place w. 

### `FinPlace.q`

 The absolute norm of the prime ideal w, that is, the order of its residue field. 

### `FinPlace.q_bounds`

 The four consequences of `1 < w.q` for the order `w.q` of the residue field at `w`, collected
for `simp`. 

### `uniformizer`

 A chosen uniformiser of the completion of E at the finite place w. 

### `v_uniformizer`

 The chosen uniformiser at w has valuation exp (-1), the largest value less than 1. 

### `evalAt`

 The ring homomorphism sending a finite adele to its component in E_w. 

### `singleAdele`

 The map sending a in E_w to the finite adele with component a at w and 0 elsewhere, a ring
homomorphism that does not preserve 1. 

### `Ô`

 The subring Ô of finite adeles of E that are integral at every finite place. 

### `mem_Ô`

 A finite adele x is integral if and only if each of its components has valuation at most 1. 

### `reduceAt`

 Reduction modulo w: the ring homomorphism from the integral finite adeles to the residue
field at w. 

### `starRingOfInvolution`

 The structure of ring with involution on a commutative ring R given by a ring endomorphism
whose square is the identity. 

 ### Valuations on the completions 

### `v_algebraMap_eq_valuation`

 The valuation v of the completion at w extends the w-adic valuation of K. 

### `v_algebraMap_eq_intValuation`

 On the ring of integers of K, the valuation of the completion at w is the w-adic valuation. 

### `finite_natCast_mem`

 Only finitely many finite places of K divide a given nonzero natural number n. 

 ### Functoriality in the number field 

### `FinPlace.comap`

 For f: K → L and a finite place w of L, the finite place of K below w: the preimage under f
of the prime ideal w. 

### `FinPlace.below`

 For an extension L/K, the finite place of K below the finite place w of L. 

### `_root_.DenseRange.eq`

 Let `e` be a map with dense range in a space `X`. Two maps `f`, `g` from `X` to a Hausdorff
space that are continuous (hypotheses `hf_cont`, `hg_cont`) and agree at every point `e i`
(hypothesis `h_agree`) agree at every point `x`. This is the pointwise form of
`DenseRange.equalizer`; by default continuity is proved by `fun_prop`. 

### `locMap`

 For a finite place w of L above the finite place u of K, the continuous extension of
`f : K → L` to a homomorphism of the completions at u and at w. 

### `locMap_algebraMap`

 For a finite place `w` of `L` above the place `u` of `K`, the map of completions `locMap f hw`
extends the field homomorphism `f : K →+* L`. 

### `exists_v_locMap_eq_pow`

 Let `f : K →+* L` be an embedding of number fields and `w` a finite place of `L` above the place
`u` of `K`. Along the induced map `locMap f hw` of completions, the valuation `v` is raised to some
nonzero power `e`. 

### `v_locMap_le_one_iff`

 The map of completions induced by a field homomorphism preserves and reflects integrality. 

### `isEquiv_comap_locMap`

 The pullback of the valuation at w along the map of completions is equivalent to the valuation
at the place u below w. 

### `v_locMap_eq_of_isUnit_log`

 If some value `log v (locMap f hw z)` is `±1`, then the map of completions `locMap f hw` induced
by f: K → L at a place w above u preserves the valuation. 

### `v_locMap_eq_of_surjective`

 For a surjective field homomorphism f, the map of completions preserves the valuation. 

### `tendsto_place_comap_cofinite`

 The map taking a place of L to the place of K below it along f: K → L tends to the cofinite
filter along the cofinite filter, as its fibres are finite. 

### `adeleMap`

 For an embedding f: K → L of number fields, the induced ring homomorphism from the finite
adeles of K to those of L; it gives base change and the Galois action. 

### `finAdeleIncl`

 For an extension of number fields L over K, the inclusion of the finite adeles of K in those
of L. 

### `adeleMap_apply`

 The component at w of the image of a finite adele x is the image of the component of x at the
place u below w. 

### `adeleMap_algebraMap`

 The homomorphism of finite adeles induced by f extends f. 

 ### CM fields: complex conjugation and roots of unity 

### `map_star_complex`

 A complex embedding φ of a CM field E commutes with complex conjugation: φ (x̄) is the complex
conjugate of φ x. 

### `map_star_CM`

 An embedding f : K → L of CM fields commutes with complex conjugation. 

### `FinPlace.IsSplit`

 The finite place w of the CM field E is split over the maximal real subfield: it differs
from its complex conjugate. 

### `HasPrimitiveRoot5040`

 The CM field `E` contains a primitive root of unity of order `7! = 5040`. Then the integers of
`E` contain an element `i` with `i² = -1` and `ī = -i`
(`New.HasPrimitiveRoot5040.exists_mul_self_eq_neg_one`), and an element `ω` with `ω + ω̄ = 1` and
`ω ω̄ = 2` (`New.HasPrimitiveRoot5040.exists_add_star_eq_one_mul_star_eq_two`).
So `y = i ω` has `y - ȳ = i`, a unit
(`New.HasPrimitiveRoot5040.exists_isUnit_sub_star`), and `E` is unramified at the finite places
over its maximal real subfield `E⁺`. In the comments such a field `E` is called stably unramified.
A place over `2` divides exactly one of `ω`, `ω̄`, so it is not fixed by conjugation. 

### `HasPrimitiveRoot5040.exists_primitive_root`

 `E` contains a primitive root of unity of order `7! = 5040`. 

### `star_mul_self_of_isPrimitiveRoot`

 Complex conjugation `star` inverts the roots of unity in the ring of integers `𝓞 E` of a CM
number field `E`. 

### `HasPrimitiveRoot5040.exists_isPrimitiveRoot_of_dvd`

 If the CM field `E` contains a primitive 5040-th root of unity, then its integers contain a
primitive `n`-th root of unity for each divisor `n` of `5040`. 

### `HasPrimitiveRoot5040.exists_mul_self_eq_neg_one`

 If the CM field `E` contains a primitive 5040-th root of unity, then its integers contain a
square root of `-1`, and conjugation negates it. 

### `HasPrimitiveRoot5040.exists_add_star_eq_one_mul_star_eq_two`

 If the CM field `E` contains a primitive 5040-th root of unity, then its integers contain an
element of trace `1` and norm `2` over the maximal real subfield, that is, one of the numbers
`(1 ± √-7) / 2`. 

### `HasPrimitiveRoot5040.exists_mul_self_eq_neg_one_and_mul_star_eq_two`

 If the CM field `E` contains a primitive 5040-th root of unity, then its ring of integers `𝓞 E`
contains a square root `i` of `-1`, negated by complex conjugation `star`, and an element `ω` of
trace `1` and norm `2` over the maximal real subfield of `E`. 

### `HasPrimitiveRoot5040.exists_isUnit_sub_star`

 If the CM field `E` contains a primitive 5040-th root of unity, then some algebraic integer `y`
of `E` differs from its complex conjugate `star y` by a unit. 

### `conjLoc`

 For finite places u, w with ū = w, the homomorphism E_u → E_w of completions induced by
complex conjugation. 

### `valuation_star`

 The valuation of x̄ at the conjugate place w̄ equals the valuation of x at w. 


## Topology of local fields and finite adeles

* Local fields: the residue field has order `w.q` (`New.card_ResField`), so `New.LocField w` is
  proper and its ring of integers `New.LocInt w` is compact.
* `New.mem_nhds_zero_finAdele_iff`: the sets `N * Ô E`, for `N ≠ 0` natural, are a basis of
  neighbourhoods of `0`.


### `residue_eq_iff_valuation_sub_lt_one`

 Two elements of the valuation ring of v have the same residue exactly when the valuation of
their difference is less than 1. 

 ### The completions at finite places 

### `algebraMap_ResField_eq_zero`

 An algebraic integer x maps to 0 in the residue field at w exactly when x lies in w. 

### `exists_int_approx`

 Every element `x` of `LocInt w`, the ring of integers of the completion of `E` at `w`, is
approximated by algebraic integers `a` of `E` to any order: `a - x` has valuation `v` less than
`exp n`, the image of the integer `n` in the value group. 

### `algebraMap_ResField_surjective`

 Every element of the residue field at w is the residue of an algebraic integer of E. 

### `card_ResField`

 The residue field at w has `w.q` elements, the absolute norm of w. 

### `instFiniteResField`

 The residue field at a finite place is finite. 

### `compactSpace_LocInt`

 The ring of integers of the completion at a finite place is compact. 

 ### The topology of the finite adeles 

### `continuous_singleAdele`

 The map sending a in E_w to the finite adele with component a at w and 0 elsewhere is
continuous. 

### `algebraMap_mem_Ô`

 An element of `E` that lies in `Ô E`, the finite adeles integral at every finite place, is an
algebraic integer, and conversely. 

### `coe_mem_Ô`

 The image of an algebraic integer in the finite adeles is integral at every finite place. 

### `exists_natCast_smul_mem_of_isCompact`

 Let M be a module over the finite adeles of E with a topology making scalar multiplication
continuous. For K compact and U a neighbourhood of 0 in M, some nonzero natural number N has
Nx in U for all x in K. 

### `mem_nhds_zero_finAdele_iff`

 A set `U` is a neighbourhood of `0` in the finite adeles `𝔸f E` exactly when it contains
`N * Ô E` for some nonzero natural number `N`, where `Ô E` is the ring of integral finite adeles. 

### `exists_forall_mul_mem_Ô`

 Finitely many finite adeles are carried into Ô E by one nonzero natural number. 

### `exists_mem_nhds_isIntegral_sub_div`

 Let `c ≠ 0` be a natural number. Every finite adele `y₀` of a number field `E` has a
neighbourhood `U` such that `(x - x') / c` is integral for any two elements `x`, `x'` of `E` whose
images lie in `U`. 

### `exists_eq_mul_iff_v_le`

 A finite adele x equals c y for some y in `Ô E`, that is, integral at every finite place, if and
only if v (x w) ≤ v (c w) at every finite place w. 

 ### Density of `𝓞 E` and `E`, and complex conjugation 

### `exists_forall_sub_mem_asIdeal_pow`

 Chinese remainder theorem at the finite places. Let `m` be a finitely supported family of
natural numbers and `c` a family of algebraic integers, both indexed by the finite places of `E`.
Then some algebraic integer `b` is congruent to `c w` modulo `w ^ m w` at every place `w`. 

### `exists_dvd_algebraMap_sub`

 For a nonzero algebraic integer a, every integral finite adele x (an element of the ring `Ô E`
of finite adeles integral at every finite place) is congruent modulo a to an algebraic integer b. 

### `denseRange_algebraMap_Ô`

 The algebraic integers of `E` are dense in `Ô E`, the ring of finite adeles that are integral at
every finite place. 

### `denseRange_algebraMap_finAdele`

 The number field `E` is dense in its ring `𝔸f E` of finite adeles (strong approximation). 

### `exists_sub_mem_Ô`

 Every finite adele is the sum of an element of `E` and an integral finite adele. 

### `finAdele_star_apply`

 For a CM field `E`, the component of `star x` at the finite place `w` is the conjugate, by the
map of completions `conjLoc`, of the component of `x` at the conjugate place `star w`. 

### `star_algebraMap_finAdele`

 Complex conjugation of finite adeles extends that of `E`. 

### `star_toAdele`

 Complex conjugation of adeles, given by that of `ℂ` at the infinite places and by `star` on the
finite adeles, extends that of the CM field `E` along the diagonal embedding `toAdele`. 

### `star_mem_Ô`

 The integral finite adeles are stable under complex conjugation. 


## Idempotents of sets of places and units of the integral adeles

* `New.idem`: the idempotent of a set of places; `New.isUnit_Ô`: a unit of the integral adeles is
  an element with valuation `1` at every place.
* For a CM field, complex conjugation `star` acts on places and on adeles (through `New.conjLoc`).
  It carries the valuation at a place to that at the conjugate place, keeps the order of the residue
  field and permutes the idempotents (`New.v_star_apply`, `New.q_star`, `New.star_idem`).


 ### Components of finite adeles 

### `idele_inv_apply_and_ne_zero`

 The component of the inverse of a finite idele is the inverse of its component, which is
nonzero. 

 ### Idempotents, reduction and units 

### `idem`

 The finite adele with component 1 at the places in S and 0 at the other places. 

### `reduceAt_algebraMap`

 Reduction at `w` of integral finite adeles extends reduction of algebraic integers
modulo `w`. 

### `idem_mem_Ô`

 The adele `idem S`, with components 1 and 0, is integral at every finite place. 

### `reduceAt_idem`

 The integral adele `idem S`, with component 1 on the set of places `S` and 0 elsewhere, is sent
by `reduceAt w`, reduction to the residue field at `w`, to 1 if `w` is in `S` and to 0 otherwise. 

### `exists_idele_eq_uniformizer_zpow`

 For a finitely supported family of integers `d` on the finite places of `E` there is a finite
idele (a unit of the finite adeles `𝔸f E`) whose component at each place `w` is the chosen
uniformiser `uniformizer w` of the completion at `w` to the power `-d w`. 

### `idem_mul_mem_Ô`

 The product `idem S * x` is an integral finite adele if and only if `x` is integral at every
place in `S`. 

### `reduceAt_eq_zero`

 The reduction at `w` of an integral finite adele vanishes if and only if its component at `w`
has valuation less than 1. 

### `isUnit_Ô`

 An element `x` of `Ô E`, the ring of finite adeles integral at every finite place, is a unit of
`Ô E` if and only if its component has valuation 1 at every finite place. 

 ### Complex conjugation 

### `v_star_apply`

 The valuation of a conjugate adele at a place is that of the adele at the conjugate place. 

### `q_star`

 Conjugate places have residue fields of the same order. 

### `star_idem`

 Complex conjugation carries the idempotent of a set of places to that of its conjugate. 

### `star_singleAdele`

 If `w` is the conjugate of the place `u`, complex conjugation carries the adele supported at
`u` with component `x` to the adele supported at `w` with component the conjugate of `x`. 


## Functoriality under embeddings of number fields

* `New.FinPlace.comap_surjective`: every place has a place above it.

Identities between adelic maps are checked on the field, which is dense
(`New.denseRange_algebraMap_finAdele`).


### `FinPlace.mem_comap`

 An integer of `K` lies in the place below `w` if and only if its image lies in `w`. 

### `adeleMap_adeleMap`

 The maps of finite adeles induced by embeddings of number fields compose as the embeddings
do. 

### `FinPlace.comap_surjective`

 For an embedding `f: K →+* L`, every finite place of `K` has a place of `L` above it. 

### `FinPlace.exists_gal_comap_eq`

 In a Galois extension `L / K`, two finite places `u`, `v` of `L` that lie above the same place
of `K` (`u.below K` is the place below `u`) are conjugate: `v` is the preimage of `u` under an
element of the Galois group. 

### `adeleMap_mem_Ô`

 A finite adele of `K` is integral if and only if its image in the finite adeles of `L` is. 

### `star_eq_adeleMap`

 Complex conjugation of the finite adeles of a CM field is the map induced by complex conjugation
of the field. 

### `below_star`

 For CM fields, the place below the conjugate of `u` is the conjugate of the place below `u`. 

### `adeleMap_star`

 For CM fields, the map of finite adeles induced by an embedding commutes with complex
conjugation. 


## Base change of finite adeles and Galois descent

Base change of finite adeles along an extension `L / K` of number fields.


### `adeleMap_injective`

 The map of finite adeles induced by an embedding of number fields is injective. 

### `instance (priority`

 The finite adeles `𝔸f L` are an algebra over `𝔸f K`, via the inclusion `finAdeleIncl K L`. 

### `adeleCombination`

 For a finite basis b of L over K, the linear map sending a family (a_i) of finite adeles of
K to the finite adele ∑ a_i b_i of L. 

### `adeleCombination_repr`

 On the coordinates of `x : L` in the basis `b`, viewed as adeles of `K`, the map
`New.adeleCombination` returns `x`, viewed as an adele of `L`. 

### `apply_mem_of_adeleCombination_mul_traceDual_mem_Ô`

 Let `b` be a basis of `L / K` with dual basis `b.traceDual` for the trace form, and let `U` be a
closed set of finite adeles of `K` that contains `N * Ô K`, with `N ≠ 0` (`Ô K` is the ring of
integral finite adeles). If `(∑ a j • b j) * (b.traceDual i / N)` is integral, then `a i ∈ U`. 

### `isInducing_adeleCombination`

 For a finite basis `b` of `L / K`, the topology on families of finite adeles of `K` is induced
from the finite adeles of `L` by the map `adeleCombination b`, `(a i) ↦ ∑ a i • b i`. 

### `isHomeomorph_adeleCombination`

 For a finite basis `b` of `L` over `K`, the map `adeleCombination b`, `(a i) ↦ ∑ a i • b i`,
from families of finite adeles of `K` to the finite adeles of `L` is a homeomorphism.

Known result: base change for the finite adeles of a number field. 

### `adeleBasis`

 A finite basis of L over K, viewed as a basis of the finite adeles of L over the finite
adeles of K. 

### `mem_range_finAdeleIncl_iff`

 For `L / K` Galois, a finite adele of `L` comes from one of `K` if and only if it is fixed by
the action of the Galois group on finite adeles. 
