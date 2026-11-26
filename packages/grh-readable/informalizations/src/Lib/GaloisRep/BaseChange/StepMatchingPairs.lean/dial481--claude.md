---
{
  "module": "src/Lib/GaloisRep/BaseChange/StepMatchingPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/StepMatchingPairs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/StepMatchingPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke-stable matching pairs for a step E'/E at split matched places

This file constructs sets of matching pairs of test functions (`New.IsMatchingPairAbove`) for a
step `E'/E` that are stable under Hecke operators. It works at places of `E` that are split over
`E⁺` and matched (`New.IsMatched`: `μ` is trivial there and the places above are permuted freely
by the Galois group). The pairs come from functions that are bi-invariant under the elements
integral at a set `V` of places of `E'` with one place above each pair `{w, star w}`. This file
also gives a criterion, `New.IsStep.isNormRoot_of_one_side`, for a root (`New.IsNormRoot`) that
is `1` outside the places above a set `T` of places of `E` containing no two conjugate ones.

## Main definitions and results

* `New.biInvariantPairs`, `New.isMatchingPairAbove_of_mem_biInvariantPairs`: the pairs
  `(F ∘ baseChangeGf, 1_K * F)`, where `F` is bi-invariant at `V`; they are matching pairs above
  the places below `V`.
* `New.exists_isHeckeStableMatching`: a set of matching pairs that contains the pair of indicator
  functions of the level and is stable under the Hecke operators `(T_{w,j}, T_{u,j})`.

Notions from other files:
* `New.Gf.supportedOn`, `New.Gf.trivialOn`: the elements with component `1` at every place outside
  `S ∪ S̄`, and those with component `1` at every place of `S`.
* `New.localLevel`: the elements whose component at each `w ∈ S` lies in `K w`; by default `K w` is
  `New.localIntGL`, the integral matrices with integral inverse.
* `New.IsStep`: the extension `E'/E` with a character `μ` of the finite ideles of `E` that detects
  norms.
* `New.IsMatched`: the places of `E` that split completely in `E'` and at which `μ` is trivial.
* `New.IsMatchingPairAbove`: matching pairs of functions at the places of `E'` above `S ∪ S̄`.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` and `Lib.Adelic.Hecke.ClassSums` for
sources.


### `IsStep.isNormRoot_of_one_side`

 Let `E'/E` be a step for `μ` and `σ` an element of `Gal(E'/E)`. Let `T` be a set of places of
`E` at which `μ` is trivial and which contains no place together with its conjugate, and let `B`
be the set of places of `E'` above `T` and its conjugates. Let `z` be a polynomial over the finite
adeles of `E'` that is `1` at every place not above `T`, and whose twisted norm along `σ`, with
`p` factors, is `X` modulo `P` at every place above `T`. Then:
* `z` is a norm root for `P` on `B` (`New.IsNormRoot`, for the ideles killed by `μ` after the
  norm);
* if unitary `γ` and `a` satisfy `a * ((idem B • z)(γ))ᴴ = (idem B • z)(γ)`, then at each place
  `u` above `T` the component of `a` is `z_u(γ_u)`. 

### `heckeSplit_comp_baseChangeGf`

 Let `π` be a representation of the unitary group over `E'`, let `u` be a split place of `E'`
whose place `w` below is split, and let `E_w → E'_u` be onto. Let `x` be spherical at `u` (fixed by
the elements supported at `u` and integral there) and fixed by the elements supported at the other
places above `w` and their conjugates. Then the Hecke operator `T_{w,j}` of `π ∘ baseChangeGf` and
the Hecke operator `T_{u,j}` of `π` agree on `x`. 

### `IsHeckeStableAt`

 A set `St` of pairs `(f, φ)` of functions on the finite adelic unitary groups over `E` and `E'`
is stable under the Hecke operators `(T_{w,j}, T_{u,j})` for every `j`: for each pair, the pair
`(T_{w,j} f, T_{u,j} φ)` lies in `St`, the groups acting by left translation; `T_{u,j}` is
`heckeSplit`, the Hecke operator of the indicator of `basicDoubleCoset n u j` at level
`localIntGL n u`. The condition is empty unless `w` and `u` are both split. 

### `IsHeckeStableMatching`

 A set `St` of pairs of functions on the finite adelic unitary groups over `E` and `E'`, all of
them matching pairs of level `B` above `S` for `σ` and `μ` (`New.IsMatchingPairAbove`). It contains
the indicator function of `B`, paired with its composition with `baseChangeGf`, and for each
place `w` of `S` it is stable under the Hecke operators at `w` and at some place above `w`. 

### `IsHeckeStableMatching.indicator_mem`

 `St` contains the indicator function of `B`, paired with its composition with
  `baseChangeGf`. 

### `IsHeckeStableMatching.isMatchingPairAbove`

 Every member of `St` is a matching pair of level `B` above `S`. 

### `IsHeckeStableMatching.exists_isHeckeStableAt`

 Above each `w` in `S` there is a place `u` such that `St` is stable under
  `(T_{w,j}, T_{u,j})`. 

### `belowPair`

 The unordered pair made of the place of `E` below `u` and its conjugate. 

### `exists_places_above_one_side`

 Let `S` be a set of split places of `E`. There is a set `V` of places of `E'` with exactly one
place above each pair `{w, star w}` with `w ∈ S`. In detail:
* every place of `V` lies above a place of `S`;
* no two places of `V` lie above the same place of `E`;
* the places below `V` include no place together with its conjugate;
* `S` and the places below `V` have the same closure under conjugation. 

### `atPlace_baseChangeGf_mem_localIntGL`

 Let `u` and `v` be places of `E'` above the same place of `E`. If the base change of `g` is
integral at `v` (its component lies in `localIntGL`, the integral matrices with integral inverse),
then it is integral at `u`. 

### `atPlace_iterate_galoisGf_mem_localIntGL`

 Let `galoisGf σ` be the action of `σ` on the finite adelic unitary group, entry by entry. If
`k` is integral at the place `u.comap (σ ^ i)`, then its `i`-th image under `galoisGf σ` is
integral at `u`. 

### `locMap_surjective_of_comap_ne`

 If every `g ≠ 1` in the Galois group moves `u`, then `E_w → E'_u` is onto, where `w` is the
place below `u`. 

### `otherConjugates`

 The places of `E'` outside `V` that lie above the same place of `E` as a place of `V`. 

### `IsBiInvariantAt`

 `F` is invariant on both sides under the elements `k` that are integral at `V`:
`F (k⁻¹ * g) = F g` (left translation) and `F (g * k) = F g` for every `g`. 

### `biInvariantPairs`

 The pairs `(F ∘ baseChangeGf, 1_K * F)`, where `F` is bi-invariant at `V` and `K` is the
group of elements integral at `otherConjugates E V`. 

### `mem_localLevel_placesAbove_image`

 An element is integral at every place above the places below `V` and their conjugates if
and only if it is integral at the places of `V` and at the other places above the same places of
`E` (`New.otherConjugates`). 

### `isMatchingPairAbove_of_mem_biInvariantPairs`

 Let `E'/E` be a step for `μ` and `σ ≠ 1`. Let `V` be a set of places of `E'` above matched
places of `E` (`New.IsMatched`), with at most one place above each place of `E`, and such that the
places below `V` include no place together with its conjugate. Then every pair in
`biInvariantPairs E n V` is a matching pair above the places below `V`, of level the group of
elements integral at the places above them and their conjugates. These pairs are
`(F ∘ baseChangeGf, 1_K * F)`, with `F` bi-invariant at `V` and `K` the elements integral at
`otherConjugates E V`. 

### `isHeckeStableAt_biInvariantPairs`

 Let `V` be a set of places of `E'` with at most one place above each place of `E`, such that the
places below `V` include no place together with its conjugate. Let `u` lie in `V` or be conjugate to
a place of `V`, with `E_w → E'_u` onto for the place `w` below `u`. Then the set
`biInvariantPairs E n V` is stable under the Hecke operators at `(w, u)`: this set consists of the
pairs `(f, φ) = (F ∘ baseChangeGf, 1_K * F)`, with `F` bi-invariant at `V` and `K` the group of
elements integral at `otherConjugates E V`, and for every such pair and every `j` the pair
`(T_{w,j} f, T_{u,j} φ)` of Hecke operators for left translation again lies in the set. 

### `exists_isHeckeStableMatching`

 Let `E'/E` be a step for `μ` (`New.IsStep`: `E'` CM, Galois of prime degree over `E`, with
conditions on `μ`), `σ ≠ 1` in `Gal(E'/E)`, and `S` a set of split places of `E` that are matched
(`μ` trivial on `E_w^×`; places above `w` have residue degree 1 and are moved by `σ`). Then some set
of matching pairs of level `B` above `S` contains the indicator of `B` paired with its composition
with `baseChangeGf`, and is Hecke-stable at each `w ∈ S` and at some place above it. Here `B` is the
group of elements integral at the places above `S` and their conjugates. 
