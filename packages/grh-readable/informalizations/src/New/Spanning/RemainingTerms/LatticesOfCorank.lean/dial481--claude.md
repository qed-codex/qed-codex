---
{
  "module": "src/New/Spanning/RemainingTerms/LatticesOfCorank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LatticesOfCorank.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/LatticesOfCorank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sums over lattices of given corank and small discriminant

This file bounds the sum of `(disc L) ^ (-k)` over all classes and all lattices `L ⊂ Λ ∩ X₀` of
given corank and small discriminant (`sum_discriminant_inv_le`).

Notions from other files:
* `X₀ = E ^ κ` is the hermitian space with the standard form, `k` is the cardinality of `κ`, and
  `k₀ = 𝔰.k₀` is a distinguished element of `κ`. `Gf E κ` is the finite adelic unitary group of
  `X₀`, and `stdLevel E κ` is the stabiliser of the standard lattice `Ô ^ κ` in it.
* `S.piN` is the finite idele `π̄` with `π π̄ = N`, and in the bounds `f = numInfPlaces E`.
* `S.Classes` is the set of double cosets of `Gf E κ` under the rational points and the level
  `S.sourceLevel`. If `g` is the chosen representative of the class `c`, then the lattice
  `S.classLatticeX₀ c`, also written `Λ ∩ X₀`, consists of the vectors `v` for which `g⁻¹ v` is
  integral with entry `k₀` divisible by `π̄`.
* `discriminant r L` is the square root of the generalised index `genIndex` of the Gram determinant
  of a basis of the lattice `L` of rank `r`.


 ## Means over the classes, and cosets told apart by one row 

### `sum_classes_le_of_sum_translates_le`

 Let `A` be finite and nonempty with elements mapped by `a` into the finite adelic unitary group
`Gf E κ`, and let `f` be a function on `S.Classes`, the double cosets of this group under the
rational points and the level. If for every `u` the sum of `f` over the classes of the translates
`u * a φ`, `φ ∈ A`, is at most `card A * b`, then the sum of `f` over all classes is at most
`card S.Classes * b` (for `b ≥ 0`). 

### `InverseRowsCongruent`

 The rows `𝔰.k₀` of the matrices of `y⁻¹` and `y'⁻¹` are congruent modulo `S.piN`: their
difference maps every integral vector into `Ô π̄`. 

### `inv_mul_mem_of_inverseRowsCongruent`

 Let `y`, `y'` be integral unitary matrices whose inverses have congruent rows `𝔰.k₀` modulo the
idele `S.piN` of the filling `S` (`InverseRowsCongruent`). Then `y` and `y'` lie in the same coset
of the subgroup of elements that the inclusion `S.inclHFin` of `Gf E κ` in the unitary group of the
large space maps into the subgroup `S.latticeStabilizer` of integral matrices in the lattice
basis. 


## Lattices of given corank

The lattice of a class is the kernel of a row modulo `piN` on a unimodular lattice. One averages
over the rows and counts the rows that vanish modulo `piN` on a given lattice. One then sums over
the sublattices of finite index of a primitive lattice, and finally over the primitive lattices.


### `BoundedDiscSublattice`

 The lattices of rank `r` in `L₀` with discriminant at most `S.discriminantBound`. 

### `unimodularLattice`

 The unimodular lattice `u Ô ^ κ`: the vectors `v` with `u⁻¹ v` integral. 

### `RowVanishesModPiN`

 The linear form "row `k₀` of `y⁻¹ u⁻¹`" on `u Ô ^ κ`, called the form of `y`, vanishes on `L`
modulo `piN`. 

### `discWeightIfRowVanishes`

 The term `(disc L) ^ (-k)`, for the discriminant in rank `r`, if the form of `y` on `u Ô ^ κ`
vanishes on `L` modulo `piN`, and `0` otherwise. 

### `LatticeStabilizerCoset`

 The cosets in `stdLevel E κ` of the subgroup of elements that `inclHFin` maps into
`latticeStabilizer`: those whose row `k₀` is congruent to that of `1` modulo `piN`. They
parametrise the positions of the form modulo `piN`. 

 ### Unimodular lattices 

### `map_le_and_rowVanishesModPiN_of_out_eq`

 Let the chosen representative of the class `c` be `η u y` with `η` rational and `y` integral,
and let `L` lie in the lattice `Λ ∩ X₀` of `c`, which consists of the vectors `v` for which
`(η u y)⁻¹ v` is integral with entry `k₀` divisible by `π̄ = S.piN`. Then `η⁻¹ L` lies in `u Ô ^ κ`,
and the form of `y` vanishes on it modulo `π̄`. 

### `tsum_discriminant_inv_le_of_out_eq`

 Let `E` contain a primitive 5040th root of unity, let `S` be filling data over `E`, and let the
chosen representative of the class `c` be `η u y` with `η` rational and `y` integral. The sum of
`(disc L) ^ (-k)`, `k = #κ`, over the lattices `L` of rank `r` and discriminant at most
`S.discriminantBound` in `Λ ∩ X₀` is at most the same sum over those in `u Ô ^ κ` on which the form
"row `𝔰.k₀` of `y⁻¹ u⁻¹`" vanishes modulo `S.piN`. 

### `exists_mk_out_eq_embFin_mul`

 Let `u` be in `Gf E 𝔰.κ`, and let `φ` be a coset in `stdLevel E 𝔰.κ` of the preimage under
`inclHFin` of `latticeStabilizer`, with chosen element `φ.out`. Then the chosen representative of
the class of `u * φ.out` in the double cosets `S.Classes` equals `embFin η * u * y`. Here `η` is
some rational point of the unitary group `U` of the standard form on `𝔰.κ`, and `y` is some element
of `stdLevel E 𝔰.κ` lying in the coset `φ`. Of the standing hypotheses `S.IsAdmissible`, only one is
used: the level `sourceLevel` of `S`, which defines the double cosets `S.Classes`, is the preimage
of K(M). 

 ### Forms and sublattices 

### `genIndex_piN_eq_pow`

 The generalised index of `S.piN` is `N ^ f`, where `N = π π̄` and `f` is the number of
infinite places of `E`. 

### `mem_smul_intVectors_iff`

 A vector lies in `d Ô ^ ι` if and only if its multiple by `d⁻¹` is integral. 

### `sub_mem_smul_intVectors_of_values`

 Let `U` be invertible with `U` and `U⁻¹` integral, and let `m` be its first `r` columns
`firstCols e U`. Two forms `v`, `w` are congruent modulo `d` if their values on the other columns
of `U` are, and if their values on `m A`, divided by `d`, differ by a combination of the rows of
`A` with integral coefficients. 

### `encard_le_of_vecMul_mem_smul`

 **Few forms vanish on a sublattice.** Let the CM field `E` contain a primitive 5040th root of
unity. Let `m` be a basis of a primitive sublattice of rank `r` and corank `l` in `Ô ^ π`, and let
`L` be its sublattice with the basis `m A`. For `a` in a set `B` let `Y a` be integral linear forms
whose values on `L` are divisible by the integral idele `d` and which are pairwise incongruent
modulo `d`. Then `B` has at most `[det A] [d] ^ l` elements, where `[·]` is the generalised index
and `[det A]` is the index of `L` in the primitive sublattice. 

### `encard_rowVanishesModPiN_le`

 Let `E` contain a primitive 5040th root of unity, and let `S` be filling data over `E` with
prime `N = π π̄` and `π̄ = S.piN`. The set `S.LatticeStabilizerCoset` is the quotient of `stdLevel`,
the group of integral unitary matrices on `κ`, by its subgroup of matrices whose row `𝔰.k₀` is
congruent to that of `1` modulo `π̄`. Let `y φ` be an element of each such coset `φ`,
let `V` have codimension `l`, and let `A` be invertible over the finite adeles, with integral
entries. Let `m = sublatticeBasis u.val.val_inv V` be the basis of the adelic points of `V` in
`u Ô ^ κ`. Then for at most `[det A] (N ^ f) ^ l` cosets `φ` the form "row `𝔰.k₀` of
`(y φ)⁻¹ u⁻¹`" vanishes modulo `π̄` on the lattice with basis `m A`. Here `[·]` is the generalised
index and `f` is the number of infinite places. 

### `exists_saturatedLattice_encard_rowVanishesModPiN_le`

 Let `E` contain a primitive 5040th root of unity, and let `S` be filling data over `E` with
prime `N = π π̄` and `π̄ = S.piN`. The set `S.LatticeStabilizerCoset` is the quotient of `stdLevel`,
the group of integral unitary matrices on `κ`, by its subgroup of matrices whose row `𝔰.k₀` is
congruent to that of `1` modulo `π̄`. Let `y φ` be an element of each such coset `φ`, and let
`L ⊂ u Ô ^ κ` be a lattice of rank `r` and corank `l`. There is a subspace `V` of dimension `r` such
that `L` has a finite index `i` in the lattice `saturatedLattice` of adelic points of `V` in
`u Ô ^ κ`, `disc L` is `i` times the discriminant of that lattice, and for at most `i (N ^ f) ^ l`
of the `φ` the form "row `𝔰.k₀` of `(y φ)⁻¹ u⁻¹`" takes values divisible by `π̄` on `L`
(`RowVanishesModPiN`). 

### `mul_inv_pow_le_of_mul_le`

 Let `d, i ≥ 1` be real numbers with `d i ≤ H`, and let `r ≤ k`. Then `i (d i) ^ (-k)` is at most
`H ^ (μ + 2) d ^ (-k-1) i ^ (-r-μ)` for every `μ`. 

### `one_le_sublatticeDiscriminant_unimodular`

 For a finite adelic unitary `u` and a subspace `V` of `E ^ κ`, the lattice of the adelic points
of `V` in `u Ô ^ κ` has discriminant at least `1`. 

### `subspaceDiscWeight`

 The weight of the subspace `V` of `E ^ κ`: it is `d ^ (-k-1)` if `V` has codimension `l`, with
`d` the discriminant of the lattice of the adelic points of `V` in `u Ô ^ κ`, and `0` otherwise. 

### `sum_discWeightIfRowVanishes_eq_encard_mul`

 Let `u` be in `Gf E 𝔰.κ`, let `y` assign an element `y φ` of `stdLevel E 𝔰.κ` to each coset `φ`
in `S.LatticeStabilizerCoset`, and let `L` be an `Ô`-submodule of `𝔸f E ^ 𝔰.κ`. The sum over these
cosets `φ` of the weights `S.discWeightIfRowVanishes u (y φ) r L` equals the number of cosets `φ`
for which the form of `y φ` vanishes on `L` modulo `piN`, times `(discriminant r L ^ 𝔰.k)⁻¹`. 

### `exists_sum_discWeightIfRowVanishes_le`

 Let `S` be filling data over `E` with shape `𝔰`, and let `u` be in `Gf E 𝔰.κ`. The set
`S.LatticeStabilizerCoset` is the quotient of `stdLevel`, the group of integral unitary matrices on
`κ`, by its subgroup of matrices whose row `k₀` is congruent to that of `1` modulo `S.piN`. Let
`y φ` be an element of each such coset `φ`, and call row `k₀` of `(y φ)⁻¹ u⁻¹` the form of `φ`. Let
`k = #κ`, let `r + l = k`, and let `L` be a lattice of rank `r` in `u Ô ^ κ` with discriminant at
most `H`. Then `L` has a finite index `i` in the lattice of the adelic points in `u Ô ^ κ` of some
subspace `V`. Moreover, the sum of `(disc L) ^ (-k)` over the `φ` whose form vanishes on `L` modulo
`S.piN` is at most `(N ^ f) ^ l H ^ (μ + 2) * subspaceDiscWeight u l V * i ^ (-dim V - μ)`, for any
natural number `μ`. Here `subspaceDiscWeight u l V` is `d ^ (-k-1)` if `V` has codimension `l`, with
`d` the discriminant of that lattice of `V`, and `0` otherwise. `N` is the prime of `S`, `H` is
`discriminantBound` and `f` is the number of infinite places. 

### `tsum_index_saturatedLattice_le`

 Let `u` be in the finite adelic unitary group `Gf E 𝔰.κ`, let `V` be a subspace of `E ^ 𝔰.κ`,
and let `Λ = saturatedLattice u.1.val_inv V` be the lattice of adelic points of `V` in `u Ô ^ 𝔰.κ`.
Here `𝔰.k = #𝔰.κ` is the size of the index set of the shape `𝔰`, and `𝔰.ϱ` is its number of
hyperbolic planes. The sum of `[Λ : M] ^ (-dim V - 2 𝔰.ϱ - 4)` over the sublattices `M` of finite
index in `Λ` is at most `2 ^ 𝔰.k`. The filling data `S : Filling E 𝔰` are used only for a bound on
the degree of `E` in terms of `𝔰.ϱ`. 

 ### The sum over the forms and the lattices in a unimodular lattice 

### `sum_tsum_discWeightIfRowVanishes_le`

 Let `S` be filling data over the CM field `E` with shape `𝔰`, and let `u` be in the finite
adelic unitary group `Gf E 𝔰.κ`. The set `S.LatticeStabilizerCoset` is the quotient of `stdLevel`,
the group of integral unitary matrices on `κ`, by its subgroup of matrices whose row `k₀` is
congruent to that of `1` modulo `S.piN`. Let `y φ` be an element of each such coset `φ`, and call
row `k₀` of `(y φ)⁻¹ u⁻¹` the form of `φ`. Let `r + l = k = #κ`. Take the sum of `(disc L) ^ (-k)`
over the pairs of a coset `φ` and a lattice `L` of rank `r` in `u Ô ^ κ` with discriminant at most
`H` on which the form of `φ` vanishes modulo `S.piN`. This sum is at most `(N ^ f) ^ l H ^ (2 ϱ + 6)
(200 f k rd) ^ (f (k + 1) l) 2 ^ k`. Here `N` is the prime of `S`, `H` is `discriminantBound`, `ϱ`
is the number of hyperbolic planes of `𝔰`, `f` is the number of infinite places and `rd` is the root
discriminant of `E`. 

 ### The constants and the sum over all classes 

### `tailScale_nonneg`

 The number `S.tailScale = b ^ (k f / 4)` is nonnegative, as the size parameter `b` is. Here
`k = |κ|` and `f` is the number of infinite places of `E`. 

### `add_mul_succ_pow_three_le`

 For every natural number `ϱ`, with `n = ϱ + 1`, the number `1 + n ^ 3 (2 ϱ + 6) + 1` is at
most `10 ^ 5 n ^ 9`. This bounds an exponent of the size parameter in
`pow_mul_discriminantBound_pow_le`. 

### `pow_mul_discriminantBound_pow_le`

 Let `S` be filling data that satisfy the standing hypotheses `IsAdmissible`. The product
`b ^ f H ^ (2 ϱ + 6) 2 ^ k` is at most `tailScale = b ^ (k f / 4)`. Here `b` is the size parameter
of `S`, `k = #κ`, `f` is the number of infinite places of `E`, and
`H = discriminantBound = b ^ (n ^ 3 f)` with `n = ϱ + 1`. 

### `pow_mul_mul_rootDiscr_pow_le_tailScale`

 Let `S` be filling data that satisfy the standing hypotheses `IsAdmissible`, among them
`N ≤ b ^ (60 (ϱ + 1))`. The product `N ^ f (200 f k rd) ^ (f (k + 1))` is at most
`tailScale = b ^ (k f / 4)`. Here `N` is the prime and `b` the size parameter of `S`, `k = #κ`, `f`
is the number of infinite places and `rd` the root discriminant of `E`. 

### `mul_rootDiscr_pow_le_tailScale_pow_div`

 Let `S` be filling data that satisfy the standing hypotheses `IsAdmissible`, among them
`N ≤ b ^ (60 (ϱ + 1))`. For every `l`, the constant `(N ^ f) ^ l H ^ (2 ϱ + 6) (200 f
k rd) ^ (f (k + 1) l) 2 ^ k` of `sum_tsum_discWeightIfRowVanishes_le` is at most
`tailScale ^ (l + 1) / b ^ f`. Here `N` is the prime and `b` the size parameter of `S`, `k = #κ`,
`f` is the number of infinite places and `rd` the root discriminant of `E`,
`H = discriminantBound = b ^ ((ϱ + 1) ^ 3 f)` and `tailScale = b ^ (k f / 4)`. 

### `sum_discriminant_inv_le`

 **Lattices of given corank.** Let `S` be filling data, with prime `N = π π̄` and size parameter
`b`, that satisfy the standing hypotheses `IsAdmissible`; those used are the form of the level,
`N ≤ b ^ (60 (ϱ + 1))`, the lower bounds `1000 ≤ b` and `5 ≤ N`, and a lower bound for an index. Let
`k₀ = 𝔰.k₀` be the distinguished index in `κ` given by the shape `𝔰`, and let `r + l = k = #κ`. For
a class `c` in the double coset space `S.Classes` of `U(X₀)`, with chosen representative `g`, the
lattice `classLatticeX₀ c` consists of the adelic vectors `v` such that `g⁻¹ v` is integral with
entry `k₀` divisible by `π̄`. Take the sum of `(disc L) ^ (-k)` over all `c` and all lattices `L` of
rank `r` in that lattice with `disc L ≤ discriminantBound = b ^ ((ϱ + 1) ^ 3 f)`. This sum is at
most `tailScale ^ (l + 1)` times the number of classes divided by `N ^ (k f)`. 
