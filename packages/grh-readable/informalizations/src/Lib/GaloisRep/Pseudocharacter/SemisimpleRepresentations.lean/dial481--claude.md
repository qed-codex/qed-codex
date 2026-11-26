---
{
  "module": "src/Lib/GaloisRep/Pseudocharacter/SemisimpleRepresentations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Pseudocharacter/SemisimpleRepresentations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Pseudocharacter/SemisimpleRepresentations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Semisimple representations: conjugacy, continuity, cancellation and stable lattices

This file studies representations `r : G →* GL n k` over an algebraically closed field `k` of
characteristic zero, with semisimplicity expressed by `New.IsTraceNondeg r`. It proves the
Wedderburn–Artin decomposition for maps with semiprime span and Clifford's theorem for
restriction to a normal subgroup. It then shows that equal traces give conjugate
representations, and that continuity follows from the trace. It treats twists by characters
and the cancellation of characters. For continuous ℓ-adic representations of compact groups it
constructs stable lattices over rings of integers `O`.

## Main definitions and results

* `New.IsTraceNondeg.exists_conj_of_trace_eq`: equal traces give conjugate representations.
* `New.IsTraceNondeg.continuous_of_trace`: continuity from the trace.
* `New.IsTraceNondeg.exists_cancel_chars`: if two representations have the same trace after
  subtracting two families of characters with no common member, this common function is the trace
  of a representation.
* `New.eventually_exists_isLatticeIn`: a continuous representation r of a compact group has a
  lattice over every large enough O.

Notions from other files:
* `New.IsTraceNondeg`: Non-degeneracy of the trace form on the span of r(G): any x in that span with
  tr(x r(g)) = 0 for all g is zero.
* `New.CoeffRing`: Rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`, where the
  class `ThePrime ℓ` records that ℓ is the fixed prime.

## Relation to the literature

Known; see `Lib.GaloisRep.Pseudocharacter.Pseudorepresentations` for sources.



## Wedderburn–Artin, Clifford's theorem and conjugacy from traces

For a map `ρ : G →* B` into a finite-dimensional algebra, semisimplicity is used in the form
`New.HasSemiprimeSpan k ρ`. The Wedderburn–Artin theorem writes the restriction of `ρ` to a normal
subgroup as an algebra map out of a product `New.PiMatrix` of matrix algebras. Maps out of such a
product are compared through the matrix units `New.piMatrixUnit`.

* `New.exists_rep_of_trace`: a tracial form with natural values at the matrix units is a character.
* `New.IsTraceNondeg.comp`: restriction to a normal subgroup stays semisimple (Clifford).


 ### Products of matrix algebras and idempotents 

### `PiMatrix`

 The product over i of the matrix algebras M_{d_i}(k). 

### `blockDiagonalAlgHom`

 The R-algebra homomorphism from ∏_i M_{m_i}(R) to matrices indexed by the disjoint union of
the m_i, sending a family of square matrices to the block diagonal matrix. 

### `piMatrixUnit`

 The element of the product of matrix algebras M_{d_i}(k) that is the matrix unit E_ab in
factor i and zero elsewhere; a, b default to 0. 

### `exists_mul_mul_eq_of_rank_le`

 If `A'` has rank at most that of `A`, then `A' = U' * A * U` for some matrices `U`, `U'`. 

### `trace_of_idempotent`

 The trace of an idempotent matrix is its rank. In characteristic zero, the matrix is zero
exactly when its trace is zero. 

### `IsTraceNondeg.of_span_piMatrix`

 Let `k` be algebraically closed of characteristic zero. If `r = f' ∘ s`, where the image of
`s` spans a finite product of matrix algebras and `f'` is an algebra map to `M_n(k)`, then the
trace form on the span of `r(G)` is non-degenerate. 

### `exists_rep_of_trace`

 Let `k` be an algebraically closed field of characteristic zero, and let `s : G →* PiMatrix k d`
be a homomorphism into the product ∏_i M_{d_i}(k) of matrix algebras whose image spans the product.
Let `τ` be a `k`-linear form on the product with `τ (x * y) = τ (y * x)`, taking a natural number
value on `piMatrixUnit i` (the matrix unit E_00 in factor `i`, zero elsewhere) for each `i`, and
with `τ 1 = card n`. Then there is a representation `r : G →* GL n k` with trace `τ ∘ s` whose trace
form is non-degenerate on the span of the `r g`, meaning any `x` in that span with
`tr (x * r g) = 0` for all `g` is zero. 

 ### Intertwiners between algebra maps 

### `intertwiner`

 Given algebra maps f, f' from the product of the M_{d_i}(k) to matrix algebras and matrices U_i,
this is the matrix Σ_i Σ_a f(E^i_{a0}) U_i f'(E^i_{0a}). 

### `intertwiner_mul_map_piMatrixUnit`

 Multiplying `intertwiner f f' U` on the right by the image under `f'` of the matrix unit
E^i_{ab} gives f(E^i_{a0}) U_i f'(E^i_{0b}). 

### `map_piMatrixUnit_mul_intertwiner`

 Multiplying `intertwiner f f' U` on the left by the image under `f` of the matrix unit
E^i_{ab} gives the same matrix f(E^i_{a0}) U_i f'(E^i_{0b}). 

### `intertwiner_mul_piMatrixUnit`

 Multiplying `intertwiner f f' U` by the image of the matrix unit E^i_{ab}, on the right under
`f'` or on the left under `f`, gives the same matrix f(E^i_{a0}) U_i f'(E^i_{0b}). 

### `mul_intertwiner`

 `intertwiner f f' U` intertwines the two actions of the product of matrix algebras. 

### `exists_piMatrix_retract`

 Let `f` and `f'` be matrix representations of a product of matrix algebras. The rank of
`f (piMatrixUnit i)` is the multiplicity of the block `i` in `f`. If each block occurs in `f'` at
most as often as in `f`, then there is an intertwiner `P` from `f'` to `f` with a left inverse. 

### `HasSemiprimeSpan`

 The span of ρ(G) in B is semiprime: any x in it with x ρ(g) x = 0 for all g is zero. 

 ### The Wedderburn decomposition and its consequences 

### `exists_wedderburn`

 The Wedderburn–Artin theorem for the span of `ρ ∘ f`. Let `ρ : G →* B` have semiprime span and
let `f : H →* G` have normal range. Then `ρ ∘ f = F ∘ s`, where the image of `s` spans a product of
matrix algebras and the algebra map `F` kills no block of that product. 

### `IsTraceNondeg.hasSemiprimeSpan`

 If the trace form of `r : G →* GL n k` is non-degenerate on the span of `r(G)`, then this span
is semiprime: any `x` in it with `x * r g * x = 0` for all `g` is zero. This is the hypothesis of
`New.exists_wedderburn`. 

### `IsTraceNondeg.comp`

 Clifford's theorem for the trace form. Let `k` be algebraically closed of characteristic zero.
If the trace form of `r : G →* GL n k` is non-degenerate and `f : H →* G` has normal range, then
the trace form of `r ∘ f` is non-degenerate. 

### `IsTraceNondeg.exists_conj_of_trace_eq`

 Brauer–Nesbitt in the form used here: over an algebraically closed field `k` of characteristic
`0`, let `r` have non-degenerate trace form, `ρ : G →* B` into a finite-dimensional algebra have
semiprime span, and `φ : B →ₐ[k] Matrix n n k`. If `r` and `φ ∘ ρ` have equal traces, then
`r g * P = P * φ (ρ g)` for one invertible `P`. 

 ### Continuity 

### `IsTraceNondeg.continuous_of_trace`

 Let k be a field with a ring topology. Let r be a representation of a topological group into
GL_n(k) whose trace form is non-degenerate on the span of its image. If the trace of r is
continuous, then r is continuous. 


## Twists by characters and cancellation of characters

* `New.twistByChar`, `New.IsTraceNondeg.twist`: the twist by a character, which keeps nondegeneracy.

The proof of `New.IsTraceNondeg.exists_cancel_chars` decomposes both sides at once through a product
of matrix algebras (`New.exists_wedderburn`). It then shows that the common virtual character has
multiplicities in `ℕ`.


### `New.twistByChar`

 For a character μ of G and a matrix representation R over k, the representation g ↦
μ(g)R(g). 

### `New.IsTraceNondeg.twist`

 Twisting by a character `μ` keeps the trace form non-degenerate on the span of the image. 

### `New.IsTraceNondeg.exists_cancel_chars`

 Cancellation of characters over an algebraically closed field of characteristic `0`. Let `r 0`,
`r 1` of dimension `card n + card t` have nondegenerate trace form, and let no character `ψ 0 i`
equal a `ψ 1 j`. If `tr (r i) - ∑ j, ψ i j` is the same function `T` for `i = 0, 1`, then `T` is
the trace of some `s` of dimension `card n` with nondegenerate trace form. 


## Stable lattices for ℓ-adic representations of compact groups

* `New.Selmer.IsLatticeIn`: a representation u with values in matrices over O is conjugate to a
  given ℓ-adic representation r.

Auerbach's lemma (`New.exists_auerbach`) gives a basis in which all entries have norm at most 1.
Baire's theorem and compactness put them in one finite extension.


### `Selmer.IsLatticeIn`

 The `O`-valued representation `u` is a lattice in `r`: there is one `P` in `GL n ℚ̄_ℓ` with
`P⁻¹ * r g * P = u g` for all `g` in `G`, where `u g` is read in `ℚ̄_ℓ` through the inclusion
`O.val.val` of `O` into `ℚ̄_ℓ`. 

### `Selmer.IsLatticeIn.charpoly_eq_map`

 If `u` is a lattice in `r`, then for every `g` the characteristic polynomial of `r g` is the
image of that of `u g` under the inclusion `O.val.val` of `O` into `ℚ̄_ℓ`. 

### `eventually_exists_isLatticeIn`

 A continuous representation `r : G →* GL n ℚ̄_ℓ` of a compact group `G` has a lattice over
every large enough coefficient ring: for all `O` in `CoeffRing ℓ` that contain some fixed one,
there is a representation `u` with entries in `O` that is a lattice in `r`
(`Selmer.IsLatticeIn r u`, that is, `u` is conjugate to `r` in `GL n ℚ̄_ℓ`). 
