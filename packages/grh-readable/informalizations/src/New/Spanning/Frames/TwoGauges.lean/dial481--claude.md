---
{
  "module": "src/New/Spanning/Frames/TwoGauges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TwoGauges.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TwoGauges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparing the lengths at two points; minors and heads

Each isometry g of the form `T.splitGram` gives a gauge, the size of g⁻¹ y, on vectors y. The
gauges at two points differ little on Y^(l-1) if they differ little on Y^(l), the frame vector
e_(l-1) has short lifts at both points, and it has a short dual that looks nearly the same from both
points. Over a head, such duals come from determinants of blocks of the isometries (Cramer's rule).

Notions from other files:
* `S.ofSize i`, `S.vecsOfSize i`, `S.HasMatrixSize i`: the numbers x of size i (|x| ≤ L^i at a real
  place, L^i x integral at the finite places, for a fixed scale L), and the vectors and matrices all
  of whose entries have size i.
* Y^(l): the vectors orthogonal to e_0, …, e_(l-1) (`IsOrthogonalBelow l`) modulo the span of these
  (`CongrBelow l`). The basis vectors e_a and e*_a have the indices `inl a` and `eStar a`.
* `S.GaugesDifferLe r g g' l t`: for each ω orthogonal to e_0, …, e_(l-1) with g⁻¹ ω of size i, the
  class of ω in Y^(l) has a lift ω' such that (g⁻¹ ω - g'⁻¹ ω') / r has size i + t.
* R^(l) = `partialUnitriangularGroup l`: the isometries that change each frame vector of index below
  l by a combination of the earlier ones. U_(<l) = `unipotentBelow l`: the isometries that are
  unitriangular when all basis vectors other than e_a, e*_a (a < l) are put on one middle level.
* `S.IsHead j p`: the inverses of the products p₀ ⋯ p_(l-1), l ≤ j, have size 1. The Weyl element
  w_p = `weylElem j p` sends e_a to p_a e*_a for a < j.

## Main definitions and results

* `New.Floors.Size.GaugesDifferLe.of_succ`,
  `New.Floors.Size.GaugesDifferLe.on_whole_space_of_hasShortDual`: the recursion down the quotients.
* `New.Floors.Size.GaugesDifferLe.hasMatrixSize_sub_one`: a bound on the whole space bounds the
  matrix `(x - 1) / r`.
* `New.Floors.Size.leadingMinor_mem_ofSize`, `New.Floors.Size.head_products_mem_ofSize`: the leading
  minors have bounded size.
* `New.Floors.Size.dual_mem_vecsOfSize`, `New.Floors.Size.hasMatrixSize_of_isHead`: short duals over
  a head, and bounds for the sizes of g and w_p⁻¹ g.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `leadingMinor_mem_ofSize`

 Let the isometries `ξ` and `ξ'` change each frame vector of index below `l` by a combination of
the earlier ones (`partialUnitriangularGroup l`). If all entries of `ξ g` and `ξ' γ⁻¹ g` have size 1
(size i: in `S.ofSize i`), then the leading minors of order `j ≤ l` of `T.frameGram γ`, the matrix
of the products ⟨f_a, γ f_b⟩ of the `𝔰.n = ϱ + 1` frame vectors f_a, have size `9 * 𝔰.n`. 

### `GaugesDifferLe.of_succ`

 Let g, g' be isometries and r a self-adjoint unit of size 1. Write Y^(l) for the vectors
orthogonal to e_0, …, e_(l-1) modulo the span of these. Assume that the class of
e_a = `Pi.single (inl a) 1` in Y^(a) has lifts f, f' with g⁻¹ f and g'⁻¹ f' of size c. Assume also
that e_a has a short dual ζ in Y^(a): ⟨e_a, ζ⟩ = 1, and g⁻¹ ζ and (g⁻¹ ζ - g'⁻¹ ζ') / r have size c
for some lift ζ' of ζ. Suppose the lengths at g and g' differ by at most L^t modulo r on Y^(a+1):
each class [ω] with g⁻¹ ω of size i has a lift ω' with (g⁻¹ ω - g'⁻¹ ω') / r of size i + t. Then
they differ by at most L^(t + 4 c + 12) modulo r on Y^(a). 

### `GaugesDifferLe.on_whole_space_of_hasShortDual`

 Let g, g' be isometries, r a self-adjoint unit of size 1 and j ≤ ϱ. For each a < j, let the
class of e_a = `Pi.single (inl a) 1` in Y^(a) have lifts f, f' with g⁻¹ f and g'⁻¹ f' of size c. Let
e_a also have a short dual ζ in Y^(a): ⟨e_a, ζ⟩ = 1, and g⁻¹ ζ and (g⁻¹ ζ - g'⁻¹ ζ') / r have size c
for some lift ζ' of ζ. Suppose the lengths at g and g' differ by at most L^t modulo r on Y^(j): each
class [ω] with g⁻¹ ω of size i has a lift ω' with (g⁻¹ ω - g'⁻¹ ω') / r of size i + t. Then they
differ by at most L^(t + (4 c + 12) j) modulo r on Y^(0), the whole space. 

### `GaugesDifferLe.hasMatrixSize_sub_one`

 Let g, x be isometries and r a unit with star r = r. Suppose `S.GaugesDifferLe r g (g * x) 0 i`:
the lengths at g and g x differ by at most L^i modulo r on the whole space. Then r⁻¹ • (x - 1) has
size i + 4. Size i means entries in `S.ofSize i`, for the scale L of `S`. 

### `head_prod_mul_dual_mem_ofSize`

 A bound by Cramer's rule. Let K be a set of isometries of the form (elements of `T.G`) whose
entries all have size 1, and let a < j ≤ ϱ, where ϱ is the number of hyperbolic pairs e_b, e*_b. Let
s ∈ R^(j) with s g ∈ K, and let η w_p⁻¹ g ∈ K for some η ∈ R^(j). Then p₀ ⋯ p_a times the i-th entry
of the column s e*_a has size 8 ϱ. 

### `head_products_mem_ofSize`

 The leading minors at a Weyl element have bounded size. Let `K` be a set of isometries whose
matrices have size 1, and let j ≤ ϱ. Let η w_p⁻¹ g ∈ K for some η ∈ R^(j), and let s ∈ R^(j) with s
g ∈ K. Then the products p₀ ⋯ p_(l-1), l ≤ j, which are the leading minors of `T.frameGram w_p`,
have size 9 n, where n = `𝔰.n` = ϱ + 1. 

### `dual_mem_vecsOfSize`

 A bound for s e*_a, by Cramer's rule. Let `K` be a set of isometries whose matrices have size 1,
and let a < j ≤ ϱ. Let η w_p⁻¹ g ∈ K for some η ∈ R^(j), and let s ∈ R^(j) with s g ∈ K. Let `p` be
a head: the inverses of the products p₀ ⋯ p_(l-1), l ≤ j, have size 1. Then all entries of the
vector s e*_a have size 8 ϱ + 1. 

### `head_entries_mem_ofSize`

 The entries of a head and of the dual vectors have bounded size. Let `K` be a set of isometries
whose matrices have size 1, and let a < j ≤ ϱ. With R^(j) = `partialUnitriangularGroup j` and the
Weyl element w_p = `weylElem j p`, let η w_p⁻¹ g ∈ K for some η ∈ R^(j), and let s ∈ R^(j) with s g
∈ K. Let `p` be a head: the inverses of the products p₀ ⋯ p_(l-1), l ≤ j, have size 1. Then p_a, its
inverse and the entries of the column s e*_a have size 10 n, where n = `𝔰.n` = ϱ + 1. 

### `hasMatrixSize_weylElem_inv`

 If p_a and its inverse have size i for all a < j with a < ϱ, then the inverse of the Weyl
element w_p = `weylElem j p` has size i: its entries are 0, 1, star p_a and p_a⁻¹. 

### `hasMatrixSize_inv_of_mem_unipotentBelow`

 Let j ≤ ϱ and let the isometry s lie in R^(j) = `partialUnitriangularGroup j` and in
`unipotentBelow j`. If the columns s e*_a, a < j, have size d, then s⁻¹ has size (4 (d + 1) + 12)
j + 5. 

### `hasMatrixSize_of_isHead`

 Let `K` be a set of isometries whose matrices have size 1, and let j ≤ ϱ. Let η w_p⁻¹ g ∈ K for
some η ∈ R^(j), and let s ∈ R^(j) with s g ∈ K. Let `p` be a head: the inverses of the products p₀ ⋯
p_(l-1), l ≤ j, have size 1. If s also lies in `unipotentBelow j`, then g has size 60 n² and w_p⁻¹ g
has size 99 n², with n = `𝔰.n` = ϱ + 1. 
