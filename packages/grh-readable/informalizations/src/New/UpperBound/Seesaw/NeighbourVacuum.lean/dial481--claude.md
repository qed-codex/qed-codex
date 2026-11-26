---
{
  "module": "src/New/UpperBound/Seesaw/NeighbourVacuum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourVacuum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourVacuum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The vacuum of the neighbour lattice

The sum of the translates of the vacuum by the representatives of the neighbour lattice is computed
on the two edges of the pair. A representative is `neighbourTranslation X X'' y + t`, for residues
`y` and a vector `t` that vanishes above `N`. The translations by the `neighbourTranslation X X'' y`
add up to `doubleLiftGluing`, and they commute with the translations that vanish above `N`. So a
translate of the sum by such a vector is a sum of roots of unity times vectors `gluedTranslate`,
one for each class of the `t`. The result is
`isAdmissibleCombination_finHeisenbergOp_sum_neighbourCosetRep`.

Notions from other files:
* `PairIndex X X''`: the indices of a basis of `X⁻ ⊕ X''`, where each of the two definite spaces
  has a last basis vector.
* `neighbourTranslation X X'' y`: the matrix attached to residues `y` modulo `N` at the places of
  `P`, with `η ȳ / N` (`η` the unit of norm `-1`) in the row of the last basis vector of `X`,
  `-ȳ / N` in that of `X''`, and zero elsewhere. It is supported at the places conjugate to `P`.
* `vanishingAbove ι P`: the vectors that vanish at the places of `P` and their conjugates (for
  split `N`, the places above `N`).
* `AwayLatticeQuotient`, `neighbourCosetRep`: the classes, modulo the integral ones, of the
  elements of the neighbour lattice that vanish above `N`, and the sum
  `neighbourTranslation X X'' y + t` for a chosen representative `t` of such a class.
* `Z.finHeisenbergOp x`, `Z.vacElem`: the translation by a finite adelic vector `x` and the vacuum
  in the space `𝒮 Z`.
* `IsAdmissibleCombination v A n d p B z`: `z` is a finite combination of the `v x` with `x ∈ A`,
  whose coefficients times `d` are integral away from `n` and, if `p` holds, have absolute sum at
  most `B` under every automorphism of `ℂ`.
* `arrowTensor`: the map that joins data on `Hom(V, V')` and `Hom(V', V'')` to one datum on
  `Hom(V', V⁻ ⊕ V'')`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `stdPairSpace`

 The space `Hom (X', (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))` of the standard spaces, the target of
`arrowTensor` for a pair of standard edges. 

### `gluedTranslate`

 The glued translate attached to a pair of finite adelic matrices `t = (t₁, t₂)`: translate the
vacuum of the edge `Hom(X ⊕ Unit, X')` by `t₁` and that of `Hom(X', X'' ⊕ Unit)` by `t₂`, and apply
`doubleLiftGluing` (the sum over residues modulo `N` at `P`) to the tensor of the two. 

### `IsAdmissibleEval`

 There is a constant `C` such that, for every `n` prime to `N` and every proposition `p`, the map
`L` sends each translate of the vacuum of `Hom(V', V⁻ ⊕ V'')` by a matrix `y`, whose row `i` times
`d i` is integral away from `n`, to an admissible combination of the vectors
`C • gluedTranslate N P (t₁, t₂)`, where `β̄ t₁`, `β̄ t₂` are integral away from `n`. The
coefficients are integral away from `n` after multiplication by the number of classes of integral
matrices modulo `β`, and if `p` holds their absolute sum is at most `1` under every automorphism
of `ℂ`. 

 ### Translations above `N` and away from `N` 

### `semichar_eq_one_of_smul_eq`

 Let `N = π π̄` with no place of `P` conjugate to one in `P` (`hπ`). A vector `x` fixed by
multiplication by the conjugate of `idem P` (the adele with component `1` on `P` and `0` elsewhere)
is supported at the places conjugate to `P`, so `x* x = 0`. Hence `semichar x`, an additive
character of a multiple of `x* x`, is `1`. 

### `star_neighbourTranslation_dotProduct_eq_zero`

 Let `N = π π̄` with `π` a uniformiser at the places of `P`, none conjugate to another, and a
unit elsewhere (`hπ`). The matrix `neighbourTranslation X X'' y`, whose only nonzero rows are
multiples of `ȳ / N` at the two last basis vectors and which is supported at the places conjugate
to `P`, is orthogonal to every matrix `x` that vanishes at the places of `P` and their
conjugates. 

### `finHeisenbergOp_neighbourTranslation_add`

 Let `N = π π̄` with `π` a uniformiser at the places of `P`, none conjugate to another, and a
unit elsewhere (`hπ`). The matrix `neighbourTranslation X X'' y`, made from residues `y` modulo
`N`, is supported at the conjugates of these places. So if `x` vanishes at the places of `P` and
their conjugates, the translation of `f ∈ 𝒮 Z` by `neighbourTranslation X X'' y + x` is the
product of the translations by the two summands. 

### `finHeisenbergOp_comm_neighbourTranslation`

 Let `N = π π̄` with `π` a uniformiser at the places of `P`, none conjugate to another, and a
unit elsewhere (`hπ`). The matrix `neighbourTranslation X X'' y`, made from residues `y` modulo
`N`, is supported at the conjugates of these places. So the translation of `𝒮 Z` by it commutes
with the translation by any `x` that vanishes at the places of `P` and their conjugates. 

### `v_selfOrConj_eq_one`

 If the scaling data `β`, `δ`, `κ` are away from `N` (`hκ`), then `β` is a unit above `N`, hence
so are `β̄` and every denominator `selfOrConj β b` (`β` on the first block, `β̄` on the second). 

### `exists_finHeisenbergOp_vacElem_eq_of_coprime`

 Let `P` contain one place of each conjugate pair above the prime `N`, let `β` be a unit above
`N` and `n` prime to `N`. Let `W` be a hermitian space on the entries of a matrix with two blocks of
rows. If the rows of `y` have denominator at most `β` in the first block and `β̄` in the second
(`selfOrConj β`) away from `n`, the translate of the vacuum of `W` by `y` is a root of unity times
the translate by a matrix `y'` that has the same denominators and vanishes above `N`. 

 ### The two edges of the pair 

### `arrowTensor_tmul`

 On a pure tensor `Φ ⊗ Ψ` of data on the two edges, `arrowTensor` is `arrowProduct Φ Ψ`. 

### `finHeisenbergOp_vacElem_eq_smul_arrowTensor`

 The translate by `z` of the vacuum of `Hom(V', V⁻ ⊕ V'')` is the square of `semichar` of the
first block of `z` times the image under `arrowTensor` of the tensor of two translates. These are
the vacuum of `Hom(V, V')` translated by `normNegOne` (the unit of norm `-1`) times the adjoint of
the first block of `z`, and the vacuum of `Hom(V', V'')` translated by the second block of `z`. 

 ### The sum over the neighbour lattice 

### `arrowTensor_doubleLiftGluing`

 Let `N` be a prime that splits as `N = π π̄`. Let `t` be a tensor of finite data (`finitePart`)
on the two edges `Hom(X ⊕ Unit, X')` and `Hom(X', X'' ⊕ Unit)` of standard spaces. The map
`arrowTensor` joins it to one datum on `stdPairSpace`, the space
`Hom(X', (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))`. There the operator `doubleLiftGluing` (the sum over residues
`y` of the translation of the first datum by the last column `-y / N` and of the second by the last
row `-ȳ / N`) becomes the sum of the translations by `neighbourTranslation X X'' y`, the matrices
whose only nonzero rows are `η ȳ / N` and `-ȳ / N` at the two last basis vectors. 

### `exists_sum_finHeisenbergOp_neighbourTranslation_eq`

 Let `N` be a prime that splits as `N = π π̄`, where `π` is a uniformiser at the places of `P`
and a unit elsewhere. Let `z` be a matrix on `PairIndex X X''` times `X'` whose rows have
denominator at most `β` in the first block and `β̄` in the second (`selfOrConj β`), away from `n`.
In `stdPairSpace`, the space `Hom(X', (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))`, add up over residues `y` modulo
`N` at `P` the translates, by `neighbourTranslation X X'' y`, of the translate of the vacuum by `z`.
The sum is a root of unity times the image under `arrowTensor` of `gluedTranslate N P (t₁, t₂)`, the
glued tensor of the translates by `t₁`, `t₂` of the vacua of the two edges, for some `t₁`, `t₂` with
`β̄ t₁`, `β̄ t₂` integral away from `n`. 

### `isAdmissibleCombination_finHeisenbergOp_sum_neighbourCosetRep`

 Let `N = π π̄` be a split prime with places `P`. By `hκ`, `β` is a unit above `N` and each row
factor `κ` is `1` or `δ`, with denominator at most `β̄`. The classes
`q : AwayLatticeQuotient X' hπ hκ` are those, modulo integral matrices, of the elements of the
neighbour lattice that vanish above `N`; for residues `y` modulo `N` at `P`,
`neighbourCosetRep (y, q)` is `neighbourTranslation X X'' y` plus a chosen representative of `q`.

Let `x` vanish above `N` and have rows of denominator at most `β` in the first block and `β̄` in the
second, away from `n`. Translate by `x` the sum over `(y, q)` of the translates of the vacuum by
these representatives, and read the result on the two edges `Hom(X ⊕ Unit, X')`,
`Hom(X', X'' ⊕ Unit)`. With `K` the number of classes `q`, it is a finite combination of
`K • gluedTranslate N P (t₁, t₂)`, where `gluedTranslate` glues the translates by `t₁`, `t₂` of the
vacua of the edges and `β̄ t₁`, `β̄ t₂` are integral away from `n`. Its coefficients, times the
number of integral matrices modulo `β`, are integral away from `n`. The proposition `boundHyp` is
arbitrary; if it holds, the absolute sum of the coefficients is at most `1` under every automorphism
of `ℂ`. 
