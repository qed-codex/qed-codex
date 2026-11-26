---
{
  "module": "src/New/UpperBound/Seesaw/StandardLines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The standard lattice of a graded space, line by line

Let `Y` grade the hermitian space `V` by an index set `X ⊕ Unit` of grade `0` and a string of `s`
basis vectors, and let the finite frame of `V` span the same lattice `Λ` as the standard basis
`New.gradedLatticeBasis`. The intersection `Λ⁻` of `Λ` with the span of the string and its
projection `Λ⁺` to this span are sums of lines.

* `New.Grading.SpansLattice.isGraded`: `Λ` is graded.
* `New.Grading.SpansLattice.mem_latticeMinus_iff`, `New.Grading.SpansLattice.mem_latticePlus_iff`:
  the generators of the lines; they differ only by `N⁻¹` at the middle vector of the string.
* `New.Grading.SpansLattice.mem_lattice_and_stringProj_eq_zero_iff`: for odd `s`, the
  intersection of `Λ` with the span of `X ⊕ Unit`.
* `New.Grading.SpansLattice.stringSum_mem_latticeMinus_iff`,
  `New.Grading.SpansLattice.stringSum_mem_latticePlus_iff`: the generators on the lines of the
  vectors `𝔢 ^ i`, for the scale `u = (a / ā) ^ ⌊(s + 2) / 2⌋` and when the constant `c` of `Y`
  has the valuations of `a ā`.
* `New.Grading.SpansLattice.map_stringMapFin_latticePlus`: under the same conditions, the shift to
  a space with a string of `s - 1` vectors and the same constant `c` takes `Λ⁺` onto `a Λ'⁻`.
* `New.Grading.SpansLattice.odd_of_notMem_latticeMinus`: a vector of `Λ⁺` outside `Λ⁻` exists
  only for odd `s`.
* `New.Grading.SpansLattice.exists_place_generates_of_notMem_latticeMinus`: such a vector
  generates `Λ⁺` over `Λ⁻` at some place above `N`.

The results on `Λ⁺` and on the span of `X ⊕ Unit` assume that `N` is split and squarefree
(`IsSplitSquarefree P N π`).

Notions from other files:
* `Y.SpansLattice a π u`: the lattice `Λ = V.lattice 1` has the standard basis
  `New.gradedLatticeBasis Y.indexEquiv a π u` over the integral finite adeles `Ô E`. This basis
  consists of the vectors of `X`, the multiples of the string vectors `b` by `lineIdele a u b`, and
  the last vector `e₀` of `X ⊕ Unit`, replaced for odd `s` by `e₀ / π̄ + u z / (π π̄)`, where `z`
  is the middle vector of the string.
* `IsSplitSquarefree P N π`: `N = π π̄`, where `π` is a uniformiser at the places of `P`, a unit
  elsewhere, and no place of `P` has its conjugate in `P`.
* `Y.stringSum t`: the vector `∑ t i • 𝔢 ^ i`, where `𝔢 ^ i = Y.stringPower i` is a multiple of
  the string vector `i` by an element of `E`.
* `Y.genericConst`: the constant `c` of the grading, a nonzero element of `E` fixed by conjugation.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `lineIdele`

 The diagonal entry of `New.gradedLatticeBasis` at the string vector `b`, as an idele: `u` for
odd `s`; for even `s` it is `u a⁻¹` on the first half of the string and `u ā` on the second half.
It generates the part of `Λ⁻` on the line of this vector. 

### `powerIdele`

 The idele `a ^ (s - i) ā ^ (-1 - i)`. The docstrings of the membership criteria below write
`𝔩_i` for the fractional ideal that it generates. 

### `powerIdele_mul_zpow`

 Multiplying `powerIdele a s i = a ^ (s - i) ā ^ (-1 - i)` by `(a ā) ^ n` adds `n` to both
exponents. 

### `lineIdele_divStar_pow`

 Let `s` be the number of vectors in a string, indexed by `b : Fin s`, and `a` a finite idele.
For the scale `u = (a / ā) ^ ⌊(s + 2) / 2⌋`, where `divStar a = a / ā`, the idele `lineIdele a u b`
(which is `u` for odd `s`, and `u a⁻¹` or `u ā` on the two halves of the string for even `s`) is
`powerIdele a s b = a ^ (s - b) ā ^ (-1 - b)` times a power of `a ā`. 

### `Seesaw.IsSplitSquarefree.v_algebraMap`

 Let `N = π π̄`, with `π` a uniformiser at the places of `P` and a unit elsewhere, and no place
of `P` conjugate to a place of `P`. Then `N` is a uniformiser at the places of `P` and their
conjugates, and a unit elsewhere. 

### `Seesaw.IsSplitSquarefree.algebraMap_mem_Ô`

 Under `IsSplitSquarefree P N π` the element `N = π π̄` is integral, being a uniformiser or a
unit at every place. 

### `Grading.lineIdele_inv_mul_stringSum_mem_iff`

 The grading `Y` indexes a basis of a hermitian space through `Y.indexEquiv`, with a string of
`s` vectors `b : Fin s` of grade `s - 1 - 2 b`; `N` is the element of `E` in its Gram matrix, and
its constant `c = Y.genericConst` is assumed to have the valuation `v` of `a ā` at every finite
place `w` of `E`. The vector `𝔢 ^ i` is a multiple of the string vector `i` by an element of `E`,
and `Y.stringSum t = ∑ t i • 𝔢 ^ i`. The claim: a coordinate of this vector at the string vector
`b` lies in the fractional ideal of `lineIdele a u b`, where `u = (a / ā) ^ ⌊(s + 2) / 2⌋` and
`divStar a = a / ā`, if and only if `t b` lies in that of `powerIdele a s b`, times `N⁻¹` in
negative grade (`s ≤ 2 b`). The same holds with both sides multiplied by any adele `r`. 

### `gradedLatticeBasis_mulVec_apply_inl`

 The coordinates with index in `X ⊕ Unit` of a combination of the vectors of
`New.gradedLatticeBasis`: only the last one is rescaled, by `π̄⁻¹`, and only for odd `s`. 

### `gradedLatticeBasis_mulVec_apply_inr`

 The string coordinates of a combination of the vectors of `New.gradedLatticeBasis`: the
coordinate of `gradedLatticeBasis e a π u *ᵥ c` at the string vector `b` is `lineIdele a u b` times
the coefficient `c` at `b`. For the middle vector, with `b = b.rev`, there is an added term:
`u (π̄ π)⁻¹` times the coefficient `c` at the last index `.inr ()` of `X ⊕ Unit`. 

### `exists_gradedLatticeBasis_mulVec_eq`

 Suppose `hL : Y.SpansLattice a π u`, that is, the lattice `V.lattice 1` is spanned over `Ô E` by
the columns of `gradedLatticeBasis Y.indexEquiv a π u`. Then every vector `y : ι → 𝔸f E` has
coordinates `c` in this basis. Moreover, `y` lies in `V.lattice 1` if and only if every `c i` lies
in `Ô E`. 

### `mem_lattice_iff`

 The hypothesis `hL` says that `Λ` has, over the integral finite adeles `Ô E`, the standard basis
attached to the ideles `a`, `π` and the unitary scale `u`: the vectors of `X`, the string vectors
`b` times `lineIdele a u b`, and the last vector `e₀` of `X ⊕ Unit`, replaced for odd `s` by
`e₀ / π̄ + u z / (π π̄)`, with `z` the middle vector of the string. So `y` lies in `Λ` if and only
if three conditions hold, on its coordinates at `X`, at the last index, and on the string. The only
condition that links two coordinates glues the last index to the middle, the `b` with
`b = b.rev`. 

### `isGraded`

 The grading `Y` of the hermitian space `V` gives each basis vector an integer grade: `0` on
`X ⊕ Unit` and `s - 1 - 2 b` at the vector `b` of the string of length `s`. If the lattice
`V.lattice 1` has the standard basis for `a`, `π`, `u` (the basis vectors rescaled, except that for
odd `s` the last vector of `X ⊕ Unit` is combined with the middle string vector), then it contains
the part in each grade of each of its vectors, since both combined vectors have grade `0`. 

### `mem_latticeMinus_iff`

 Let the lattice be spanned by `New.gradedLatticeBasis`. Its intersection
`Λ⁻ = Y.latticeMinus 1` with the span of the string, onto which `Y.stringProj` projects, is the sum
of its lines: the multiples of the string vector `b` by the fractional ideal of
`lineIdele a u b`. 

### `mem_latticePlus_iff`

 Let `Λ = V.lattice 1` have the standard basis for the ideles `a`, `π` and the unitary scale `u`,
in which the string vector `b` is multiplied by `lineIdele a u b` and, for odd `s`, the last vector
of `X ⊕ Unit` is combined with the middle one. Let `N = π π̄` be split and squarefree, `P` being the
places of `π`. Then the projection `Λ⁺ = Y.latticePlus 1` of `Λ` by `Y.stringProj` to the span of
the string is the sum of its lines: the multiples of the string vector `b` by the fractional ideal
of `lineIdele a u b`, times `N⁻¹` at the middle vector, the `b` with `b = b.rev`. 

### `mem_lattice_and_stringProj_eq_zero_iff`

 The grading `Y` indexes the basis of the hermitian space `V`, through `Y.indexEquiv`, by
`X ⊕ Unit` and a string of `s` vectors, here with `s` odd. Let `Λ = V.lattice 1` have the standard
basis for the ideles `a`, `π` and any unitary scale `u`, in which the last vector `e₀` of
`X ⊕ Unit` is replaced by `e₀ / π̄ + u z / (π π̄)`, with `z` the middle vector of the string, and
let `N = π π̄` be split and squarefree. The intersection of `Λ` with the span of `X ⊕ Unit`, the
kernel of the projection `Y.stringProj` to the span of the string, consists of the vectors whose
coordinates on `X` are integral and whose last coordinate lies in `π Ô E`. 

### `stringSum_mem_latticeMinus_iff`

 The grading `Y` of the hermitian space `V` has a string of `s` basis vectors; `𝔢 ^ i` is a
multiple of the string vector `i` by an element of `E` and has grade `s - 1 - 2 i`, and `N` is the
element of `E` in the Gram matrix. Let the lattice `Λ = V.lattice 1` have the standard basis of
`gradedLatticeBasis` for the ideles `a`, `π` and the scale `(a / ā) ^ ⌊(s + 2) / 2⌋`, and let the
constant `c` of `Y` have the valuations of `a ā`. Then `Y.stringSum t = ∑ t i • 𝔢 ^ i` lies in
`Λ⁻ = Y.latticeMinus 1`, the intersection of `Λ` with the span of the string, if and only if each
`t i` lies in the fractional ideal `𝔩_i` of `powerIdele a s i` in grade at least `0`, and in
`N⁻¹ 𝔩_i` in negative grade. 

### `stringSum_mem_latticePlus_iff`

 The grading `Y` of the hermitian space `V` has a string of `s` basis vectors; `𝔢 ^ i` is a
multiple of the string vector `i` by an element of `E` and has grade `s - 1 - 2 i`. Let the lattice
`Λ = V.lattice 1` have the standard basis of `gradedLatticeBasis` for the ideles `a`, `π` and the
scale `(a / ā) ^ ⌊(s + 2) / 2⌋`, let the constant `c` of `Y` have the valuations of `a ā`, and let
`N = π π̄`, with `π` a uniformiser at the places of `P`, a unit elsewhere, and no place of `P`
conjugate to another or to itself. Then `Y.stringSum t = ∑ t i • 𝔢 ^ i` lies in
`Λ⁺ = Y.latticePlus 1`, the projection of `Λ` to the span of the string, if and only if each `t i`
lies in the fractional ideal `𝔩_i` of `powerIdele a s i` in positive grade, and in `N⁻¹ 𝔩_i` in
grade at most `0`. 

### `map_stringMapFin_latticePlus`

 `sh Λ⁺ = a Λ'⁻`: let `Y`, `Y'` be gradings of the hermitian spaces `V`, `V'` with strings of
`s`, `s - 1` basis vectors and the same constant `genericConst`, which has the valuations of `a ā`.
Let `N = π π̄` be split and squarefree, with `P` the places where `π` is a uniformiser. Suppose
`Y.SpansLattice` and `Y'.SpansLattice` hold: the lattices `Λ`, `Λ'` of `1` have, up to `GL(Ô)`, the
bases `gradedLatticeBasis` at the scales `(a / ā) ^ ⌊(s + 2) / 2⌋` and
`(a / ā) ^ ⌊(s - 1 + 2) / 2⌋`. The shift `sh = Y.stringMapFin Y'` kills `X ⊕ Unit` and sends each
string vector of `V` to a multiple of the string vector of `V'` with the same number, if there is
one. It takes the projection `Λ⁺` of `Λ` to the span of the string onto `a` times the intersection
`Λ'⁻` of `Λ'` with the span of the string. 

### `exists_pole_of_notMem_latticeMinus`

 Let `Λ⁻ = Y.latticeMinus 1` and `Λ⁺ = Y.latticePlus 1` be the intersection with and the
projection to the span of the string of the lattice with standard basis `gradedLatticeBasis` for
`a`, `π` and any unitary scale `u`, in which the string vector `b` is multiplied by
`lineIdele a u b`. Let `N = π π̄` be split and squarefree. For `y` in `Λ⁺` outside `Λ⁻`, the string
has a middle index `m = m.rev`, and the coordinate of `y` there, divided by `lineIdele a u m`, which
generates `Λ⁻` on this line, has a pole at a place `w` above `N`: a place of `P` or a conjugate of
one. 

### `odd_of_notMem_latticeMinus`

 Let `Λ⁻ = Y.latticeMinus 1` and `Λ⁺ = Y.latticePlus 1` be the intersection with and the
projection to the span of the string of the lattice with basis `New.gradedLatticeBasis`, and let
`N = π π̄` be split and squarefree. If some vector of `Λ⁺` lies outside `Λ⁻`, then the length `s`
of the string is odd. 

### `exists_place_generates_of_notMem_latticeMinus`

 Suppose `Y.SpansLattice a π u`: the lattice of `1` has, up to `GL(Ô)`, the basis
`gradedLatticeBasis` built from `a`, `π` and the unitary scale `u`. Let `Λ⁻ = Y.latticeMinus 1` and
`Λ⁺ = Y.latticePlus 1` be its intersection with and its projection to the span of the string. Let
`N = π π̄` be split and squarefree. A vector `y` of `Λ⁺` outside `Λ⁻` generates `Λ⁺` over `Λ⁻` at
some place `w` above `N`: every `z` in `Λ⁺` differs from a multiple `c • y` with `c ∈ Ô E` by a
vector whose component at `w` lies in `Λ⁻`. 

### `odd_and_exists_place_of_notMem_latticeMinus`

 Let `Λ⁻ = Y.latticeMinus 1` and `Λ⁺ = Y.latticePlus 1` be the intersection with and the
projection to the span of the string of the lattice with basis `New.gradedLatticeBasis`. If `y` is
a vector of `Λ⁺` outside `Λ⁻`, then `s` is odd and `y` generates `Λ⁺` over `Λ⁻` at some place `w`
above `N = π π̄`, that is, a place of `P` or a conjugate of one. 
