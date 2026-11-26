---
{
  "module": "src/New/UpperBound/Objects/LabelsAndIndexTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Good labels, index types of hermitian spaces, the group 𝖦 and idempotent e₀

This file introduces primitive polynomials and good tuples of labels at one prime. Then, for
admissible data D, it introduces the index types and signs for the bases of the hermitian spaces
X_j, Y_j and W_j.

## Main definitions and results

* `New.IsPrimitivePolynomial`: irreducible labels with a root of order |k|^r − 1. They are stable
  under scaling the roots by an M-th root of unity if M² ∣ |k| − 1
  (`New.IsPrimitivePolynomial.scaleRoots`). The product of their roots has order |k| − 1
  (`New.IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots_and_exists_pow_eq`).
* `New.goodTuples`: tuples of labels, each without roots among the M-th roots of unity of its base
  field, of which at least one is primitive.
* `New.Data.X`, `New.Data.RowIndex`, `New.Data.Y`: the basis indices of X_j (rank `New.Data.n`), of
  Y_0 (rank r, `New.Data.card_rowIndex`) and of Y_j (`New.Data.RowIndex` and j blocks of size
  `New.Data.t`).
* `New.Data.chosenGL`, `New.Data.e₀`: the product of the groups GL_r over the residue fields at the
  chosen places above p₀, p₁, and the good idempotent in its group algebra. The idempotent is the
  sum of the idempotents `New.tupleIdem` over `New.Data.goodTupleFamilies`.
* `New.Data.isCentralProj_e₀`: `e₀` is a central idempotent.
* `New.Data.hyperplaneSum_mul_e₀`: `e₀` kills pure tensors with a factor `New.hyperplaneSum χ l`,
  `l ≠ 0`, `χ ^ q₂ = 1`.

Notions from other files:
* `New.Data`: the data D, with m lifts, block size t and ranks k, n_j = k + j (t + 1) and
  r = k + m − 1; s is its parameter `D.towerExp`, and q₂ = q₂(s) the integer `New.Parameters.q₂`.
* `New.Data.ChosenPlace`: the chosen places above the level prime p_i (i = 0, 1), the finite places
  of E that divide both p_i and the conjugate `D.piM` of an integer of K of norm p₀p₁.
* `New.IsLabel`: a label of degree r is a monic squarefree polynomial c of degree r with c(0) ≠ 0.
* `New.tupleIdem`: the tensor product of the label idempotents e_c of a tuple of polynomials.
* `New.piTensorElem`: the pure tensor ⊗ x_i in ℂ[∏ G_i] of elements x_i of ℂ[G_i].


 ## Primitive polynomials and good tuples at one prime 

### `IsPrimitivePolynomial`

 The polynomial `c` is a primitive polynomial: an irreducible label of degree `r` over `k` with a
root of order `|k| ^ r - 1`, that is, a root that generates the units of the field with `|k| ^ r`
elements. 

### `IsPrimitivePolynomial.two_le_card_pow`

 If there is a primitive polynomial of degree `r` over `k`, then `|k| ^ r ≥ 2`. 

### `IsPrimitivePolynomial.scaleRoots`

 Let `k` be a finite field and `c : k[X]` a primitive polynomial of degree `r`: a monic
irreducible polynomial of degree `r` with `c(0) ≠ 0` that has a root of order `|k| ^ r - 1` in the
algebraic closure of `k`. If `M ^ 2` divides `|k| - 1` and `a` is an `M`-th root of unity of `k`,
then `c.scaleRoots a`, whose roots are those of `c` multiplied by `a`, is again a primitive
polynomial of degree `r`. 

### `IsPrimitivePolynomial.pow_geom_sum_eq_prod_aroots`

 With `q = |k|`, the product of the roots of a primitive polynomial of degree `r` is
`ξ ^ (1 + q + ⋯ + q ^ (r - 1))` for each root `ξ`. 

### `IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots`

 The norm of a generator is a generator: the product of the roots of a primitive polynomial has
order `|k| - 1`. 

### `IsPrimitivePolynomial.isPrimitiveRoot_prod_aroots_and_exists_pow_eq`

 The product of the roots of a primitive polynomial has order `|k| - 1`, and it is one and the
same power of every root. This power is the norm from the field with `|k| ^ r` elements to `k`; see
`New.IsPrimitivePolynomial.pow_geom_sum_eq_prod_aroots` for the exponent. 

### `IsAllowedPolynomial`

 The polynomial `c` is an allowed polynomial: a label of degree `r` over `k` that has no root `x`
in `k` with `x ^ M = 1`. 

### `IsAllowedPolynomial.not_isRoot`

 An allowed polynomial does not vanish at an `M`-th root of unity of `k`. 

### `goodTuples`

 The good tuples of labels of degree `r`, one label over each field `k w`: every label is
allowed (no root of it in its base field is an `M`-th root of unity), and at least one is
primitive. 

### `mem_goodTuples`

 A tuple `(c_w)` of polynomials over finite fields `k w` is good for `M` and `r` exactly when
every `c_w` is allowed and some `c_w` is primitive. 


## Basis indices and signs of the hermitian spaces, the group 𝖦 and the idempotent e₀
For admissible data D, the spaces X_j, Y_j and W_j (`New.Data.spaceY`, `New.Data.spaceW`; W_j has
rank r) are hermitian spaces whose bases are indexed by the types defined here.


 ### A block followed by j equal blocks 

### `BlockIndex`

 The disjoint union of S and j copies of T, the index type of Y_j. 

### `BlockIndex.firstBlock`

 The inclusion of the first block S into the union of S and j copies of T. 

### `BlockIndex.nonempty_equiv_sum`

 If `S` is in bijection with `α`, then `BlockIndex S T j` is in bijection with
`α ⊕ Fin j × T`. 

### `BlockIndex.equivSum`

 A bijection from `BlockIndex S T j`, the union of `S` and `j` copies of `T`, to
`α ⊕ Fin j × T`, for a bijection `ν : S ≃ α`. For `j = 0` it is given by `ν`
(`New.BlockIndex.equivSum_zero_apply`); for `j > 0` it is an arbitrary such bijection, chosen from
`New.BlockIndex.nonempty_equiv_sum`, and need not respect the blocks. 

### `BlockIndex.equivSum_zero_apply`

 For `j = 0` the bijection `equivSum ν 0` from `BlockIndex S T 0` to `α ⊕ Fin 0 × T` sends `x` to
`Sum.inl (ν x)`, that is, it is `ν` followed by the left inclusion. 

### `instFintypeBlockIndex`

 The index type `BlockIndex S T j` is finite. 

### `decEqBlockIndex`

 Equality in `BlockIndex S T j` is decidable if it is in `S` and `T`, by recursion on `j`. 

### `BlockIndex.card`

 The union of `S` and `j` copies of `T` has `|S| + j |T|` elements. 

 ### Index types 

### `ϱ`

 The number ϱ = ⌊m/2⌋ − 1 of hyperbolic planes of Y₀, where m is the number of lifts. 

### `InitIndex`

 The basis indices of X_j other than the last: a set with n_j − 1 elements. 

### `X`

 The basis index set of X_j: n_j − 1 indices together with one extra point for the last basis
vector. 

### `shape`

 The shape of Y₀: ϱ = `New.Data.ϱ` hyperbolic planes, the basis indices of X₀, and the last
of them as distinguished index. 

### `RowIndex`

 The basis index set of Y₀: e₁, …, e_ϱ, the indices of X₀, the middle vector z, and e*₁, …,
e*_ϱ. 

### `Y`

 The basis index set of Y_j: `New.Data.RowIndex` followed by j blocks of t indices each. 

### `card_rowIndex`

 The index set `New.Data.RowIndex` of the basis of the hermitian space Y₀ over E has `r = D.r`
elements. For the admissible data `D`, Y₀ is the first space of the chain of `m = D.m` theta lifts
from U(Y₀) to U(Y_m). 

### `instance {u : Bool} {l : ℝ} [D.HasLogBound u D.r l] : D.HasLogBound u (card D.RowIndex) l`

 A logarithmic bound on the rank `r` (`New.Data.HasLogBound`: `r ≤ exp l` if `u` is `true`,
`exp l ≤ r` if `u` is `false`) also holds for the number of basis indices of Y₀, which is `r`. 

 ### Parameters and signs 

### `basisNumber`

 A chosen numbering of the basis indices of Y₀: a bijection from `New.Data.RowIndex` to
{0, …, r − 1}. 

### `paramW`

 Twice the entry numbered `D.basisNumber i` of the target parameter `New.Data.targetParameter` at
the place τ: the doubled parameter on W_j and on Y₀. The entries of the target parameter at τ are
k/2 − 1, k/2 − 2, … (k − 1 of them), then h₂ − w₁(τ), …, h₂ − w_m(τ), with
w_a = `New.Data.liftWeight` a the weights of the lifts and h₂ = `D.halfGap` half the gap between
consecutive weights. 

### `entrySign`

 The sign `(-1) ^ (o + a + min (a - o) j)`, with the subtraction truncated at zero
(`New.Data.entrySign_eq_neg_one_pow`). In `New.Data.gridSigns` it is the sign, at the node `(i, j)`
with offset `o`, of the base index with number `n`, where `a = n + 1 - k` (truncated at zero) and
`k` is the rank `D.k`. The first branch, for `j = 0` and positive `o`, agrees with the formula. It
makes the signs for `o + 1` the negatives of those for `o` by definition, as the passage to the
opposite space in `New.Data.gridSpace` requires. 

### `entrySign_eq_neg_one_pow`

 Closed form of `entrySign`, the sign `±1` of a basis vector of the hermitian space at a node
`(i, j)` of a grid or triangle. Here `offset` is the offset of the node, `j` is its second
coordinate, and `excess = n + 1 - k` for the basis vector with number `n` and the rank `k = D.k`.
The sign is `(-1) ^ (offset + excess + min (excess - offset) j)`, with subtraction truncated at
zero. 

### `signsW`

 The signs ±1 of W_j on the indices i in `New.Data.RowIndex`: −1 when the number
`D.basisNumber i` in {0, …, r − 1} is at least `D.posRank j` = k + j − 1, and +1 otherwise. 

### `chosenPlace`

 The map sending a pair (i, w), with w a chosen place above the prime p_i = `D.levelPrime i`, to
the underlying finite place w of E. The chosen places above p_i (`New.Data.ChosenPlace`) are the
finite places of E that divide both p_i and `D.piM`, the complex conjugate of the integer
`D.piMBar` of K of norm p₀p₁. 

 ### The finite group and the good idempotent 

### `chosenGL`

 The finite group 𝖦 = ∏ GL_r(𝔽_w), over the chosen places w (`New.Data.ChosenPlace`) above the
two level primes p₀ and p₁ (`D.levelPrime`), where 𝔽_w is the residue field at w and the r rows are
indexed by `New.Data.RowIndex`. 

### `instance : Fintype (D.ChosenPlace i)`

 There are only finitely many chosen places above the prime p_i = `D.levelPrime i`. 

### `goodTupleFamilies`

 The finite set of families (c_w) of polynomials over the residue fields at the chosen places w
above p₀, p₁. For each p_i, the tuple of the c_w with w above p_i lies in `New.goodTuples` for the
integer `New.Parameters.q₂` at s and the rank r. 

### `mem_goodTupleFamilies`

 Let `c = (c_w)` be a family of polynomials over the residue fields at the chosen places `w`, the
finite places of E that divide `D.piM` and one of the two level primes p₀, p₁ of the data `D`. Then
`c` lies in `New.Data.goodTupleFamilies` exactly when, for `i = 0, 1`, the `c_w` with `w` above p_i
form a good tuple (`New.goodTuples`): each is a label of degree `r = card D.RowIndex` with no
`q₂`-th root of unity of the residue field as a root, and at least one is primitive. 

### `e₀`

 The element e₀ of ℂ[𝖦]: the sum of the idempotents `New.tupleIdem` over the families in
`New.Data.goodTupleFamilies`. 

 ## Centrality of e₀ and hyperplane sums 

### `isCentralProj_e₀`

 The element `D.e₀` of the group algebra ℂ[𝖦], the sum of the idempotents `New.tupleIdem` over
the families in `D.goodTupleFamilies`, is a central idempotent (self-adjoint by
`New.IsCentralProj.self_adjoint`). 

### `hyperplaneSum_mul_e₀`

 The idempotent `e₀` kills a pure tensor that has a hyperplane sum as a factor. Let `x = (x_v)`
be a family of elements of the group algebras ℂ[GL_r(𝔽_v)], where `v` runs over the chosen places
(the finite places of E that divide `D.piM` and one of the two level primes p₀, p₁) and 𝔽_v is the
residue field. Suppose that at one place `v` the member `x_v` is `New.hyperplaneSum χ l`, the sum of
`χ(det h)⁻¹ h` over the invertible `h = 1 + u lᵀ`, where `l ≠ 0` and `χ` is a character of 𝔽_v with
`χ ^ q₂ = 1` for `q₂ = (q₀ d) ^ (s + 6)` (`q₀`, `d` the parameters of `P`, `s = D.towerExp`). Then
`(⊗ x_v) * e₀ = 0`. 
