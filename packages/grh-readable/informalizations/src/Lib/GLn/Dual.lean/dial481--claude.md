---
{
  "module": "src/Lib/GLn/Dual.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Dual.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Dual.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Duality of integral GL(n) representations, mixed weights and the Cartan product

The integral representations of `∏_τ GL(n_τ)` act on lattices with bases of products of minors, and
a weight `κ` counts the columns of each height. For the reversed weight `κ'_τ(h) = κ_τ(|n_τ| - h)`,
the representation of weight `κ` composed with `g ↦ g⁻¹ᵀ` is that of weight `κ'` twisted by a power
of the determinant, through a unimodular, isometric, equivariant integer matrix. With this matrix,
the representation of mixed weight with positive part `kp` and negative part `km` embeds integrally
into the tensor product of the representation of weight `kp` with that of weight `km` composed with
`g ↦ g⁻¹ᵀ`. For a splitting `ε : N ⊕ m ≃ n` of the letters, this embedding sends the Cartan product
of vectors of weights `kp` and `km` to their tensor, and the squared norm of the product is
multiplicative. Finally, the representations of `GL n` with parameters `l` and `-l` are paired
invariantly by an integer matrix.

## Main definitions and results

* `New.GL.exists_star_matrix`: the product of the Hodge stars of the columns, a signed bijection
  between basis tensors that replaces each column by its complement.
* `New.GL.exists_int_duality_matrix`: the integer matrix by which the star maps one Weyl module to
  the other.
* `New.GL.IsDualIsometry`, `New.exists_isDualIsometry`: this matrix is unimodular, isometric and
  equivariant; `New.exists_dual_isometry` states these properties as one conjunction.
* `New.GL.MixedCartanEmbedding`: the integer matrix of the embedding and the four properties asked
  of it; `New.GL.weylEvalAt` is the evaluation vector at the array `New.permArray` of a map of rows.
* `New.mixedWeight`: the weight with `kp τ i + km τ (card n - i)` columns of height `i`.
* `New.nonempty_mixedCartanEmbedding`, `New.mixedCartan`: such an embedding exists for this weight,
  and a chosen one.
* `New.Rows.cartanProduct`: the product; `New.Rows.mixedCartan_mulVec_cartanProduct`: `mixedCartan`
  sends it to the tensor of the factors.
* `New.exists_isDualPairing_of_isHCParam`: the pairing is invariant and computes `New.ofAlgForm` at
  `-l`. It is invertible up to the hook number. It is isometric for the Gram norms `New.weylNormSq`.

Notions from other files:
* `New.permArray`: For maps e_τ from rows to natural numbers, the array over R whose entry at row
  (τ,a), column i is 1 if e_τ(a)=i and 0 otherwise.
* `New.nablaFamily`: The module of Borel semi-invariant polynomials of weight `New.diagramWeight`,
  in which `New.nablaBasis` gives coordinates (`New.sum_coords_nablaBasis`).
* `New.weylRep`: The monoid homomorphism from ∏_τ GL(n_τ,R) to square matrices sending g to ∏_τ
  det(g_τ)^{e_τ} times the Schur matrix of g, for integers e_τ.
* `New.schur`: The Schur matrix S_κ(z) of matrices z_τ of size n'_τ×n_τ. Row i holds chosen
  coordinates of b'_i(zy) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}. Here b'_i and b_j are the
  standard basis polynomials in the rows n' and n, and d is given by `New.schurDetExp`.
* `New.weylEval`: The vector of values of the basis minor products at an array y.

## Relation to the literature

Known result: Dual of a Weyl module by Jacobi's complementary minors, and the Cartan component. Here
the results are stated for products of GL_n. The duality and the Cartan map are given by integer
matrices that are isometric and equivariant over fields of characteristic 0. The duality has an
integral inverse and the Cartan map has an integral left inverse. Source: Fulton, Harris,
Representation Theory, 1991, section 15.5; Jantzen 2003; for Jacobi's identity, Grinberg, An
Introduction to Algebraic Combinatorics, Thm 6.4.48.



## A unimodular isometry between the Weyl lattices of dual weights

Coordinates refer to the basis `New.nablaBasis` of products of minors, indexed by
`New.WeylIndexFamily`, and `New.weylGram` is the Gram matrix. Throughout, `rankAt n τ` is `|n_τ|`,
the number of rows at `τ`, and `e'` is the enumeration `e` reversed. The diagrams `κ` and `κ'` are
complementary if `κ'_τ(h) = κ_τ(|n_τ| - h)` for `1 ≤ h < |n_τ|`. Basis tensors are indexed by
`New.ColumnFilling`, and the Weyl modules lie in the tensors through `New.fillingMatrix`.


### `GL.sign_mul_det_complementary_minor`

 Jacobi's formula for complementary minors: split the indices by `ρ` and permute the rows by
`π`; for invertible `A`, the minor of `A` on the second part is, up to the sign of `π`,
`det A` times the minor of `A⁻¹ᵀ` on the first part. 

### `GL.exists_squarePart_eq`

 For an enumeration `e` of the rows, every family `A` of square matrices is the square part
`New.GL.squarePart e y` of some array `y`, the family whose matrix at `τ` has the entry
`y ((τ, a), e_τ b)` at `(a, b)`. 

### `GL.diagramWeight_zero_eq_sum_min_mul`

 The value at `(τ, 0)` of the weight of the diagram `κ` counts the columns of height `h` with
`0 < h < N τ`; the factor `min 1 h` drops the term `h = 0`. 

### `GL.complementary_columns_symm`

 If `c'` counts the columns of the diagram complementary to that of `c`, then `c` counts those
of the diagram complementary to that of `c'`. 

### `GL.prod_columns_eq_prod_complementary`

 A product over the columns of a diagram with `c h` columns of height `h < N` may be taken over
those of the complementary diagram, which has `c' h = c (N - h)` columns of height `h`: the factors
of matching columns agree, and the factors of empty columns are `1`. 

### `columnComplement`

 The increasing sequence of the indices outside an increasing sequence. 

### `GL.exists_sign_minor_columnComplement`

 The rule of the Hodge star on one column. Number the columns by `e` and the rows by `pos`, and
let `I` be an increasing sequence of `a` row numbers. There is a sign `u` such that for every
invertible `A`, `u` times the minor of `A` on the rows outside `I` and the first `b` columns is
`det A` times the minor of `A⁻¹ᵀ` on the rows `I` and the last `a` columns in reverse order.

This is Jacobi's identity for complementary minors of a matrix and its inverse, for an arbitrary set
of rows and an initial segment of columns, with a sign that is independent of `A` but not
computed. 

### `fillingComplement`

 For complementary diagrams `κ`, `κ'`, the filling of `κ'` whose column of height `h' > 0` is the
complement of the matching column of `T`, of height `|n_τ| - h'`. Columns of height `0` are
empty. 

### `fillingComplement_apply`

 The column `j` of height `h'` of the complementary filling is the complement of the column `j`
of height `h`, when `h + h' = |n_τ|`. 

### `fillingComplement_bijective`

 For complementary diagrams `κ`, `κ'`, replacing every column by its complement
(`New.fillingComplement`) is a bijection from the fillings of `κ` to those of `κ'`. 

### `GL.exists_star_matrix`

 The product of the Hodge stars of all columns. Let `κ`, `κ'` be complementary diagrams and `e'`
the enumeration `e` of the rows reversed. There is an integer matrix `P` from the basis tensors of
`κ'` to those of `κ`, with `Pᵀ P = 1`, such that the following holds over every commutative ring.
If the square part `g` of the array `y` for `e` is invertible and the square part of `z` for `e'`
is `g⁻¹ᵀ`, then `P` sends the tensor of `y` to `∏_τ det (g_τ)^(λ_τ)` times the tensor of `z`, where
`λ_τ` is the value at `(τ, 0)` of the weight of `κ`. 

### `GL.exists_int_duality_matrix`

 The star maps one Weyl module to the other. Let `κ`, `κ'` be complementary diagrams and `e'`
the enumeration `e` of the rows reversed. There are an integer matrix `P` between the basis tensors,
with `Pᵀ P = 1`, and an integer matrix `J`, from coordinates of weight `κ'` to those of weight `κ`,
that is the restriction of `P` along the embeddings `New.fillingMatrix`. Over every commutative ring
and for every invertible `g`, `J S_κ'(g) ev_e = ∏_τ det (g_τ)^(λ_τ) S_κ(g⁻¹ᵀ) ev_{e'}`. Here `S` is
`New.schur`, `ev_e` is the evaluation vector at the frame `permArray e`, and `λ_τ` is the value at
`(τ, 0)` of the weight of the diagram `κ`. 

### `GL.IsDualIsometry`

 For an enumeration `e` of the rows, the integer matrix `J`, from coordinates of weight `κ'` to
those of weight `κ`, identifies the lattice of weight `κ'` with that of weight `κ` composed with
`g ↦ g⁻¹ᵀ` (this is the dual only over `ℚ`, since the Gram matrix is not unimodular): it is
unimodular and isometric for the Gram matrices `New.weylGram`, sends the evaluation vector at the
frame `e` to that at the reversed frame, and intertwines `g` with its inverse transpose up to a
power of the determinant. 

### `GL.IsDualIsometry.exists_inv`

 `J` has a two-sided integer inverse. 

### `GL.IsDualIsometry.gram_eq`

 `J` is an isometry for the Gram matrices: `Jᵀ G_κ J = G_κ'`. 

### `GL.IsDualIsometry.mulVec_weylEval`

 Over a field of characteristic zero, `J` sends the evaluation vector at the frame `e` to
  that at the reversed frame. 

### `GL.IsDualIsometry.equivariant`

 Over a field of characteristic zero, `S_κ(g⁻¹ᵀ) J = ∏_τ det (g_τ)^(-d_τ) J S_κ'(g)` for
  invertible `g`, where `S` is `New.schur` and `d_τ = ∑_{1 ≤ h < |n_τ|} κ_τ(h)`. 

### `exists_isDualIsometry`

 Suppose `κ' τ h = κ τ (|n_τ| - h)` for `1 ≤ h < |n_τ|` at every place `τ`. Then for every
enumeration `e` of the rows there is an integer matrix `J`, from coordinates of weight `κ'` to those
of weight `κ`, with the properties `New.GL.IsDualIsometry`. That is, `J` is unimodular and isometric
for the Gram matrices, sends the evaluation vector at the frame `e` to that at the reversed frame,
and intertwines `g` with its inverse transpose up to a power of the determinant. This is the
description of the dual of a Weyl module by the Hodge star in each column. 

### `exists_dual_isometry`

 Let `e'` be the enumeration `e` of the rows reversed, and let `κ'_τ(h) = κ_τ(|n_τ| - h)` for
`1 ≤ h < |n_τ|`. There are integer matrices `J` and `K`, inverse to each other, such that `J` is an
isometry for the Gram matrices `New.weylGram`, and over every field of characteristic zero `J`
sends the evaluation vector at the frame `e` to that at `e'` and satisfies
`S_κ(g⁻¹ᵀ) J = J W(g)`, where `S` is `New.schur` and `W = New.weylRep κ' (-d)` is
`∏_τ det(g_τ)^(-d_τ)` times `S_κ'`, with `d_τ = ∑_{1 ≤ h < |n_τ|} κ_τ(h)`. These are the fields of
`New.GL.IsDualIsometry` written out. 

### `GL.exists_weylGram_mul_eq_hookNumber_dual_smul`

 Let the column counts of `κ'` be those of `κ` reversed. Then the hook number
`hookNumber κ' (rankAt n)` of `κ'`, by which the matrix of Fock pairings inverts the Gram matrix of
`κ'`, times the inverse of the Gram matrix of `κ` is an integer matrix. 

### `GL.exists_toPoly_eq_hookNumber_dual_smul`

 The hook number of the dual weight clears denominators. Let `κ'` be `κ` with its column counts
reversed, `κ' τ h = κ τ (|n_τ| - h)` for `1 ≤ h < |n_τ|`, and let `f` be a Borel semi-invariant
polynomial of weight `κ` over a commutative ring `R` (`f ∈ nablaFamily R n κ`). Then
`hookNumber κ' (rankAt n) • f` equals `toPoly n κ ζ = Σ_i (Gζ)_i b_i` for some vector `ζ` of the
Weyl module, where `ζ` has coordinates indexed by `WeylIndexFamily n κ`, `G` is the integer Gram
matrix `weylGram`, `b_i` are the basis minor products `nablaBasis`, and the hook number is the Fock
norm `F(∂)F(0)` of the product `F` of the leading principal `h×h` minors raised to `κ'_τ(h)`. 


## Integral embedding of a mixed weight into a tensor product with an inverse-transpose twist

The embedding is the product of the multiplication table `New.GL.comulMatrix` of the bases of minor
products and the duality matrix of `New.exists_isDualIsometry`. Here `WeylIndex n κ` is
`WeylIndexFamily (fun _ : Φ ↦ n) κ`, with the same rows `n` at every place.


### `mixedWeight`

 The column multiplicity function sending (τ,i) to kp_τ(i) + km_τ(|n|−i), with truncated
subtraction of natural numbers. 

### `GL.weylEvalAt`

 The vector of values of the basis of weight `κ` (`New.weylEval`) at the array over `R` that
has, for every index `τ`, a `1` in row `(τ, a)` and column `p (equivFin n a)` and `0` elsewhere
(`New.permArray`). 

### `GL.MixedCartanEmbedding`

 For rows `n` and weights `kp`, `km` and `l`, the integer matrix `M` embeds the lattice of weight
`l` into the tensor product of those of weights `kp` and `km`: it has an integral left inverse, is
an isometry for the Gram matrices, and over every field of characteristic zero it matches the
evaluation vectors and intertwines the Schur matrices up to a determinant power. 

### `GL.MixedCartanEmbedding.matrix`

 The integer matrix `M` from the basis of weight `l` to the tensor product of the bases of
  weights `kp` and `km`. 

### `GL.MixedCartanEmbedding.hasLeftInv`

 `M` has an integral left inverse. 

### `GL.MixedCartanEmbedding.gram_eq`

 `M` is an isometry for the Gram matrices: the tensor product of those of `kp` and `km` pulls
  back to that of `l`. 

### `GL.MixedCartanEmbedding.top`

 Over a field of characteristic zero, M ev₁ = ev₁ ⊗ ev_{w₀}: `M` sends the evaluation vector
  `New.GL.weylEvalAt` of weight `l` at the identity to the tensor of that of weight `kp` at the
  identity and that of weight `km` at the reversal w₀. Here `(vecMulVec x y).vec` has the entry
  `x j * y i` at `(i, j)`. 

### `GL.MixedCartanEmbedding.intertwines`

 Over a field of characteristic zero, `M` intertwines the Schur matrix of `g` for `l`, twisted
  by ∏_τ det(g_τ)^(-∑_{1 ≤ i < |n|} km τ i), with S_kp(g) ⊗ S_km(g⁻ᵀ). This identity of matrices is
  stated after applying both sides to an arbitrary vector `v`. 

### `nonempty_mixedCartanEmbedding`

 For rows `n` and column multiplicities `kp`, `km`, let `mixedWeight n kp km` be the weight with
`kp τ i + km τ (card n - i)` columns of height `i` (truncated subtraction). Then there is an integer
matrix embedding its lattice into the tensor product of the lattices of weights `kp` and `km`, in
the sense of `New.GL.MixedCartanEmbedding`. That is, the matrix has an integral left inverse, is an
isometry for the Gram matrices, and over every field of characteristic zero matches the evaluation
vectors and intertwines the Schur matrices up to a power of the determinant. 

### `mixedCartan`

 A chosen embedding with the properties `New.GL.MixedCartanEmbedding`, from the lattice of the
weight `New.mixedWeight n kp km`, with `kp τ i + km τ (card n - i)` columns of height `i`, into the
tensor product of the lattices of weights `kp` and `km`. 


## The Cartan product in the mixed Weyl module

A splitting `ε : N ⊕ m ≃ n` of the letters `n` gives a product of a vector of weight `kp` in the
letters `N` and a vector of weight `km` in the letters `m`, with values in the mixed weight.

* `New.Rows.HasColumnsBelow`: `card N ≤ card n`, and the weight has no column of height h with
  `card N ≤ h < card n`.
* `New.Rows.cartanProduct`: the product, moved by a tuple `g` of invertible matrices.
* `New.Rows.mixedCartan_mulVec_cartanProduct`: `New.mixedCartan` sends the product to the tensor
  product of the two factors.


### `_root_.New.map_intCast_mul_mulVec`

 Casting an integer matrix product entrywise to `R` and applying it to `v` is applying the
casts of the two factors in turn. 

### `mixedCartanLeftInv`

 A chosen left inverse, with integer entries, of the matrix of `mixedCartan n kp km`. 

### `mixedCartanLeftInv_mul`

 `mixedCartan n kp km` embeds the lattice of weight `mixedWeight n kp km` into the tensor product
of the lattices of weights `kp` and `km`. The chosen integer matrix `mixedCartanLeftInv n kp km` is
a left inverse of the matrix of this embedding. 

### `mixedCartanLeftInv_mulVec_mixedCartan_mulVec`

 The chosen integral left inverse of `New.mixedCartan` undoes it over any ring. 

### `_root_.Matrix.kronecker_mulVec_vec_transpose_vecMulVec`

 The Kronecker product `P ⊗ₖ Q` sends the tensor of `a` and `b`, written `(vecMulVec a b)ᵀ.vec`,
to the tensor of `P *ᵥ a` and `Q *ᵥ b`. 

### `_root_.Matrix.star_vec_transpose_vecMulVec_dotProduct`

 The Hermitian product of the tensors of `a` and `b` and of `c` and `d`, each written
`(vecMulVec _ _)ᵀ.vec`, is the product of the Hermitian products of `a` with `c` and of `b`
with `d`. 

### `norm_schur_mulVec_le`

 Let `n × N` matrices act on the weight `kp` (`New.FitsRanks`: `card N ≤ card n` and `kp` has no
column of height strictly between the two). Over an ultrametric normed field, the Schur matrix
of such matrices with entries of norm at most `1` does not increase the sup norm. 

### `HasColumnsBelow`

 `New.FitsRanks` holds and `New.schurDetExp` vanishes: `card N ≤ card n`, and `kp τ h = 0` for
every column height `h` with `card N ≤ h < card n`. 

### `HasColumnsBelow.fitsRanks`

 If `HasColumnsBelow n N kp`, then `kp` fits the ranks (`New.FitsRanks`): `card N ≤ card n`,
and `kp` has no column of height strictly between the two. 

### `HasColumnsBelow.schurDetExp_eq_zero`

 If `HasColumnsBelow n N kp`, then the determinant exponent `New.schurDetExp` of `kp` for
`n × N` matrices is zero. 

### `cartanProduct`

 The product of a vector of weight `kp` in the letters `N` and a vector of weight `km` in the
letters `m`, for the splitting `ε : N ⊕ m ≃ n` of the letters, moved by `g`: apply the Schur
matrix of the `N`-columns of `g` to the first and that of the `m`-columns of the inverse
transpose of `g` to the second, take the tensor product, and apply the left inverse of
`mixedCartan`. 

### `cartanProduct_apply`

 `cartanProduct ε g y η` is the left inverse of `New.mixedCartan` applied to the tensor
product of the Schur images of `y` and `η`. 

### `HasColumnsBelow.schur_mul_schur`

 For a weight that is `HasColumnsBelow`, the Schur matrices are multiplicative with no
determinant factor: `S(A) S(B) = S(A B)` for `n × N` matrices `A τ` and square matrices `B τ`. 

### `map_cartanProduct`

 For weights that are `HasColumnsBelow`, a ring homomorphism `f` from `ℂ` to a field `K` of
characteristic zero, applied entrywise, commutes with the product at `g = 1`. 

### `mixedCartan_mulVec_cartanProduct`

 Let `ε : N ⊕ m ≃ n` split the letters. Let `kp` satisfy `HasColumnsBelow n N kp`:
`card N ≤ card n` and `kp` has no columns of height `h` with `card N ≤ h < card n`; let `km`
likewise satisfy `HasColumnsBelow n m km`. Let `K` be a field of characteristic zero, `y` a vector
of weight `kp` in the letters `N` and `η` one of weight `km` in `m`, and take the images of `y` and
`η` under the Schur matrices of `inclMatrix K (ε ∘ inl)` and `inclMatrix K (ε ∘ inr)`. Then the
matrix of the embedding `mixedCartan n kp km` sends `cartanProduct ε 1 y η`, which is its left
inverse applied to the tensor product of these images, back to that tensor product (written
`(vecMulVec _ _)ᵀ.vec`), so the left inverse loses nothing. 

### `weylRep_mulVec_cartanProduct`

 Let `ε : N ⊕ m ≃ n` split the letters, suppose `kp` and `km` satisfy `HasColumnsBelow`
(`card N ≤ card n` with `kp τ h = 0` for `card N ≤ h < card n`, likewise for `m`, `km`), and let `K`
be a field of characteristic zero. Take `y` of weight `kp`, `η` of weight `km`, and
`g : Φ → GL n K`. Then `weylRep` of `g` for the weight `mixedWeight n kp km` (column multiplicities
`kp τ i + km τ (card n - i)`), twisted by `∏_τ det(g_τ)^(-∑_{1 ≤ i < card n} km τ i)` and applied to
`cartanProduct ε 1 y η`, equals `cartanProduct ε g y η`, where the Schur matrices of the `N`-columns
of `g` and of the `m`-columns of `g⁻ᵀ` first act on `y` and `η`. 

### `weylNormSq_cartanProduct`

 Let ε : N ⊕ m ≃ n split the letters, and let `kp`, `km` satisfy `HasColumnsBelow`: card N, card
m ≤ card n, and there are no columns of height from card N (resp. card m) up to below card n. Then
for y, η of weights kp, km, the squared Gram norm `New.weylNormSq` of their product
`cartanProduct ε 1 y η` at g = 1 is `weylNormSq y * weylNormSq η`. 


## The invariant integral pairing of opposite weights

`New.IsHCParam κ e l` says that `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)`.
`New.ofAlgForm` passes from vector-valued algebraic forms to functions on the adelic group.


### `hcParameter_sub_succ`

 In rank `N`, for `p + 1 < N`, entries `p` and `p + 1` of the parameter `New.hcParameter`
differ by twice the number `κ w (p + 1)` of columns of height `p + 1`, plus two. 

### `IsHCParam.hcParameter_rev`

 If `l` and `-l` list the parameters (`New.IsHCParam`) of `(κ, e)` and `(κ', e')`, then each
parameter is the negative of the other read backwards: for `p + q + 1 = card n`, entry `p` of the
parameter of `(κ', e')` is minus entry `q` of that of `(κ, e)`. 

### `IsHCParam.columns_eq_of_neg`

 If `l` and `-l` list the parameters of `(κ, e)` and `(κ', e')`, the diagrams are dual: for
`1 ≤ j < card n`, `κ` has as many columns of height `j` as `κ'` has of height `card n - j`. 

### `IsHCParam.add_eq_neg_sum_of_neg`

 If `l` and `-l` list the parameters of `(κ, e)` and `(κ', e')`, the determinant exponents
add up to minus the length of the first row of `κ'`: `e' w + e w = -∑_{1 ≤ j < card n} κ' w j`. 

### `IsDualPairing`

 The pairing `v' ⬝ᵥ A *ᵥ v` of the integer matrix `A` is a duality between the weights
`(κ', e')` and `(κ, e)`, normalised at the highest vector of `l`. 

### `IsDualPairing.invariant`

 The pairing is invariant under `GL n` at all places, over every field of characteristic
  zero. 

### `IsDualPairing.ofAlgForm_eq_bilin`

 The function of a form of weight `(κ', e')` is the pairing of its value with a translate of
  the highest vector of `l`. Here the pairing is written as a bilinear map; see
  `New.IsDualPairing.ofAlgForm_apply`. 

### `IsDualPairing.exists_mul_eq_hookNumber`

 `A` has an integral left inverse up to the hook number of `κ'`. 

### `IsDualPairing.exists_eq_gramForm`

 Pairing with `v` is the Hermitian product with a vector of the same norm as `v`. 

### `exists_isDualPairing_of_isHCParam`

 Let `l` list twice the Harish-Chandra parameter of `(κ, e)`, and `-l` that of `(κ', e')`, in the
sense of `New.IsHCParam`: at each place the entries are distinct values of `hcParameter` at
positions `< card n`. Then some integer matrix `A` makes `v' ⬝ᵥ A *ᵥ v` a duality between the
weights `(κ', e')` and `(κ, e)`, normalised at the highest vector of `l` (`New.IsDualPairing`). It
does so invariantly, computing `New.ofAlgForm` at `-l`, invertibly up to the hook number, and
isometrically. 
