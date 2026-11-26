---
{
  "module": "src/New/Spanning/RemainingTerms/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Count.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The sum over pairs of near terms

For a fixed class `c`, a pair of near terms over a block `(c, s, c')` is sorted by its label, a
component of `s` in the reduced image of the Bessel subgroup, and by its common lattice. Over a
given lattice and label there are few terms, and the sum over the lattices is bounded.

The main notions used in the statements:
* a class `c : S.Classes` is a double coset of the unitary group of the definite space `X₀` at the
  finite adeles, with representative `h_c`;
* a block is a triple `(c, s, c')`, with `s` in the finite group `S.ResidueGL`. A rational isometry
  `γ` is a term over it if `h_c⁻¹ γ h_c'` is integral with reduction `s`;
* `S.IsNearPairOverAgreeingBlock c c' q`: the two terms in `q` are near, are the chosen
  representatives of their double cosets, have a cell rank, and lie over one block `(c, s, c')`
  whose `s` agrees (`S.Agrees s`);
* `commonLink γ γ'`: the subspace of `X₀` that two terms have in common; its dimension is the rank
  of their common lattice `L₁₂ = S.pairLattice c c' γ γ'`, which has corank `l` if this dimension is
  `k - l`;
* `S.termLattice c c' γ`: the lattice `L_γ ⊆ Λ ∩ X₀` of a term, where `Λ` is the adelic lattice of
  the class `c` and `Λ ∩ X₀` is `S.classLatticeX₀ c`.

The main result is `New.Filling.sum_pairDiscriminant_inv_le`.


### `tsum_le_tsum_mul_of_encard_le`

 If every index `i` is related by `R` to some `y` of the same weight, and at most `x` indices are
related to each `y`, then the sum over the indices is at most `x` times the sum over the `y`. 

### `two_mul_count_exponent_le`

 For positive `n` and `l ≤ n ^ 3`, twice the exponent `2000 n ^ 6 (l + 1) f` in the
count of the terms over a lattice is at most `10 ^ 5 n ^ 9 f`. 

### `IsLabelledPair`

 The terms `γ` and `γ'` from the class `c'` to the class `c` both have the label `t`
(`S.IsNearTermAt`), and their common lattice `S.pairLattice c c' γ γ'` is a lattice in `Λ ∩ X₀` that
lies in the lattices `S.termLattice` of both terms and whose rank is the dimension of
`commonLink γ γ'`, the subspace of `X₀` that the terms share. 

### `IsLabelledPair.isNearTermAt_left`

 The first term is near and has the label `t`. 

### `IsLabelledPair.isNearTermAt_right`

 The second term is near and has the label `t`. 

### `IsLabelledPair.le_termLattice_left`

 The common lattice lies in the lattice of the first term. 

### `IsLabelledPair.le_termLattice_right`

 The common lattice lies in the lattice of the second term. 

### `IsLabelledPair.le_classLatticeX₀`

 The common lattice lies in `Λ ∩ X₀`. 

### `IsLabelledPair.isLatticeOfRank`

 The rank of the common lattice is the dimension of the subspace that the terms share. 

### `exists_isLabelledPair_of_isNearPairOverAgreeingBlock`

 Let `E` be a CM field with a primitive 5040th root of unity, `S` admissible filling data of
shape `𝔰` over `E`, and `c`, `c'` classes. A near pair consists of two rational isometries `γ`, `γ'`
that are near, chosen in their double cosets and of some cell rank, and lie over one block
`(c, s, c')`: both `h_c⁻¹ γ h_c'` and `h_c⁻¹ γ' h_c'` are integral with the same reduction `s`,
which agrees (`S.Agrees s`). Such a pair has a common label `t`, and the lattices `S.termLattice` of
both terms contain their common lattice `S.pairLattice c c' γ γ'`. This is a lattice in
`Λ ∩ X₀ = S.classLatticeX₀ c`. 

### `ClassBoundedDiscLattice`

 The lattices `L ⊆ Λ ∩ X₀` of rank `r` with discriminant at most `S.discriminantBound`. 

### `boundedDiscNearPairs`

 The near pairs over a block `(c, s, c')` with agreeing `s`
(`S.IsNearPairOverAgreeingBlock c c'`) whose common lattice has corank `l` and discriminant at most
`S.discriminantBound`. 

### `sum_pairDiscriminant_inv_le_tsum`

 Let `E` be a CM field with a primitive 5040th root of unity and `f` infinite places, `S`
admissible filling data of shape `𝔰` over `E` with size parameter `b = S.b`, and `c` a class, with
adelic lattice `Λ`. Let `n = 𝔰.n`, let `k = 𝔰.k` be the dimension of the definite space `X₀`, and
let `l ≤ n³`, `r + l = k`. A near pair over `(c, c')` is two near, chosen terms over one block
`(c, s, c')` with `s` agreeing; its common lattice `L₁₂ ⊆ Λ ∩ X₀` has rank the dimension of the
subspace of `X₀` that the terms share, and corank `l` if this rank is `r`. The sum of
`(disc L₁₂) ^ (-k)` over all classes `c'` and all such pairs with corank `l` and discriminant at
most `S.discriminantBound = b ^ (n³ f)` is at most the number of labels, times the sum of
`(disc L) ^ (-k)` over the lattices `L ⊆ Λ ∩ X₀` of rank `r` with the same bound on the
discriminant, times `S.tailScale = b ^ (k f / 4)`. 

### `sum_pairDiscriminant_inv_le`

 **Count.** Let `E` be a CM field with a primitive 5040th root of unity and `f` infinite places,
and let `S` be admissible filling data of shape `𝔰` over `E`, with size parameter `b = S.b` and
prime `N = S.N`. Let `n = 𝔰.n`, let `k = 𝔰.k` be the dimension of the definite space `X₀`, and let
`l ≤ n³`. For classes `c`, `c'` a near pair is two near, chosen terms over one block `(c, s, c')`
with `s` agreeing; its common lattice `L₁₂` is a lattice in `X₀` of rank the dimension of the
subspace that the terms share, and has corank `l` if this rank is `k - l`. The sum of
`(disc L₁₂) ^ (-k)` over all `c`, `c'` and all such pairs with corank `l` and discriminant at most
`S.discriminantBound = b ^ (n³ f)` is at most `tailScale ^ (l + 2) * pairCountScale`. Here
`tailScale = b ^ (k f / 4)`, and `pairCountScale` is the number of labels times the number of
classes, divided by `N ^ (k f)`. 
