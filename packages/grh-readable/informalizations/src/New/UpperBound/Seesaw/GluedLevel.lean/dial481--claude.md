---
{
  "module": "src/New/UpperBound/Seesaw/GluedLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GluedLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GluedLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Congruence levels inside the stabilizer of a glued lattice

A grading `Y` of a hermitian space `V` (a choice of basis vectors with a fixed Gram matrix) embeds
the finite adelic unitary group on `X ⊕ Unit` into that of `V`. When the lattice of `V` is the glued
lattice of `Y`, this file gives congruences on an element of the small group that put its image
into the stabilizer of the lattice, or into a congruence level of it.

Notions from other files:
* `Grading V N (X ⊕ Unit) s` splits the index set `ι` of the basis of `V` into `X ⊕ Unit`, on
  which the Gram matrix is `1`, and a string of `s` vectors, orthogonal to it and with a fixed Gram
  matrix that depends on `N`; `Y.inclXFin` is the resulting map on finite adelic unitary groups.
* The glued lattice of `Y` is the `Ô`-span of the columns of
  `gradedLatticeBasis Y.indexEquiv a π u`. For odd `s` it glues the last vector of `X ⊕ Unit` to
  the middle vector of the string.
* `Y.SpansLattice a π u`: the frame `V.xFin` of `V` spans the glued lattice. So in coordinates of
  this frame the glued lattice is the standard lattice `Ô^ι`.
* `IsSplitSquarefree P N π`: `N = π π̄`, the idele `π` is a uniformizer at the places in `P` and a
  unit elsewhere, and `P` contains no place together with its conjugate.
* `congruenceGL M e`: the integral invertible matrices whose rows `e i` agree with those of `1`
  modulo `M`.
* `stdLevel E ι` is the stabilizer of `Ô^ι` in the finite adelic unitary group `Gf E ι`, and
  `levelOf w ⊥` is the subgroup of its elements congruent to `1` at every place `w i`.

## Relation to the literature

Related work: `Grading.inclXFin_mem_stdLevel` is related to Nikulin's criterion for extending
isometries to an overlattice: the congruence on `h` plays the part of the condition that an isometry
preserve the gluing.


### `Grading.exists_inclXFin_sub_one_eq`

 Let the grading `Y` split the index set `ι` of a basis of the hermitian space `V` over `E` into
`X ⊕ Unit` and a string of `s` vectors with a fixed Gram matrix depending on `N`. It gives the map
`Y.inclXFin` from the finite adelic unitary group `Gf E (X ⊕ Unit)` to `Gf E ι`, that of `V` in the
coordinates of its frame `V.xFin`. Assume that this frame spans the glued lattice of `Y`, that is,
the `Ô`-span of the basis `gradedLatticeBasis Y.indexEquiv a π u`, with ideles `a`, `π` and a
unitary adele `u` as parameters (`SpansLattice`).

Then there is an integral matrix `R` such that the image of every `h` is the matrix `1 + Rᴴ M R`.
Here `M = h - 1` if `s` is even; if `s` is odd, the last row (index `Sum.inr ()`) of `h - 1` is
divided by `π` and its last column by `star π` (`scaleAt p o` is the diagonal matrix with `p` at
`o` and `1` elsewhere). 

### `Grading.inclXFin_mem_stdLevel`

 Suppose that the frame `V.xFin` of `V` spans the glued lattice, the `Ô`-span of the explicit
basis `gradedLatticeBasis Y.indexEquiv a π u` (`SpansLattice`). Suppose also that `N = π π̄` and
that the idele `π` is a uniformizer at the places of `P`, a set without conjugate pairs, and a unit
elsewhere (`IsSplitSquarefree`).

If a unitary `h` on `X ⊕ Unit` is integral and its last row (index `Sum.inr ()`) is that of `1`
modulo `π` (`congruenceGL`), then its image `Y.inclXFin h` in `Gf E ι` stabilizes the glued lattice:
in the coordinates of `V.xFin` this is `Ô^ι`, with stabilizer `stdLevel E ι`. 

### `mem_levelOf_bot`

 An element of the finite adelic unitary group lies in `levelOf w ⊥`, the integral elements whose
reduction modulo every place `w i` is trivial, if and only if it is integral (`stdLevel`) and each
entry of its matrix minus `1` has valuation less than `1` in the completion at each `w i` (taken by
`evalAt`). 

### `Grading.inclXFin_mem_levelOf`

 Suppose that the frame `V.xFin` of `V` spans the glued lattice, the `Ô`-span of the explicit
basis `gradedLatticeBasis Y.indexEquiv a π u` (`SpansLattice`), that `N = π π̄` with `π` a
uniformizer at the places of `P` and a unit elsewhere, `P` being without conjugate pairs
(`IsSplitSquarefree`), and that the places `w i` and their conjugates lie outside `P`.

If a unitary `h` on `X ⊕ Unit` is integral, its last row (index `Sum.inr ()`) is that of `1` modulo
`π` (`congruenceGL`) and it is congruent to `1` at every `w i`, then so is its image `Y.inclXFin h`
in the coordinates of `V.xFin`: it is integral and congruent to `1` at every `w i`. 
