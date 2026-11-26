---
{
  "module": "src/Lib/GLn/SchurModule/SchurNorm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurNorm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurNorm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Norm bound for Schur matrices and basic facts on the weight representations

Let `S(z) = New.schur κ z` be the Schur matrix of rectangular complex matrices `z τ` of size
`n' τ × n τ`, assuming `New.FitsRanks n n' κ`. Let `G` and `G'` be the integral Gram matrices
`New.weylGram` for `n` and for `n'`. The file gives a formula for `S(w)ᴴ G' S(z)` and bounds the
norm of `S(z)` for these forms. It then proves base change, integrality and invariance of the Gram
pairing for the matrices `New.weylRep` and the action `New.Space.weightRep` of the rational unitary
group of `New.stdSpace`.

## Main definitions and results

* `New.GL.schur_conjTranspose_weylGram_schur`: `S(w)ᴴ G' S(z) = ∏ det(wᴴ z) ^ d · G S(wᴴ z)`, with
  `d = New.schurDetExp n n' κ` the number of columns of height `#(n τ)` if `#(n τ) < #(n' τ)`, and
  `0` otherwise.
* `New.weylNormSq_schur_le`: there are numbers `ρ τ i ≥ 0` (in the proof, the squares of the sorted
  singular values). Their sum over `i < #(n τ)` is at most the sum of the squared absolute values of
  the entries of `z τ`. The Schur matrix multiplies the squared norm by at most the product of the
  `ρ τ i`, to the powers given by the weight `New.diagramWeight`.
* `New.stdSpace_weightRep_apply`, `New.map_weightRep`: γ acts by `New.weylRep` at the matrices
  Φ_τ(γ̄), also after a ring map σ out of ℂ. Here Φ_τ is the embedding that the CM type chooses at
  τ.
* `New.gramForm_conjWeylRep`, `New.gramForm_map_weightRep`: the Gram pairing `New.gramForm` is
  invariant under the compact unitary groups, and under rational γ after any ring endomorphism σ of
  ℂ.

Notions from other files:
* `New.schur`: The Schur matrix S_κ(z) of matrices z_τ of size n'_τ×n_τ. Row i holds chosen
  coordinates of b'_i(zy) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}. Here b'_i and b_j are the
  standard basis polynomials in the rows n' and n, and d is given by `New.schurDetExp`.
* `New.conjWeylRep`: The action of ∏_τ U(s) on coordinate vectors of weight κ by `New.weylRep` at
  the complex conjugate matrices; `New.Space.weightRep` is its restriction to rational points.

## Relation to the literature

Known result: The contravariant form on Weyl's lattice, the Fischer product, and irreducibility
under U(n). This file treats only the contravariant form: its adjoint formula, its invariance under
U(n), and a bound of operator norms by singular values. Source: Jantzen, Representations of
Algebraic Groups, 2nd ed. 2003; Goodman, Wallach, Symmetry, Representations, and Invariants, 2009,
ch. 5; Howe, Perspectives on invariant theory, 1995.



## Adjoint formula for Schur matrices and the norm bound

The Hermitian forms are `New.weylNormSq` (`ξ ↦ re (ξ* G ξ)`), and `z τ` has size `n' τ × n τ`.
`New.FitsRanks n n' κ` is assumed: `#(n τ) ≤ #(n' τ)`, and `κ τ` has no column of height strictly
between the two.


### `GL.schur_conjTranspose_weylGram_schur`

 The adjoint formula: let `w`, `z` be families of complex `n' τ × n τ` matrices, and assume
`FitsRanks n n' κ`: at each `τ`, `#(n τ) ≤ #(n' τ)` and `κ τ h = 0` for `#(n τ) < h < #(n' τ)`. Let
`G` and `G'` be the integer Gram matrices `weylGram` for `n` and `n'`, taken in `ℂ`, and let
`S = schur κ` be the Schur matrix map between the Weyl coordinate spaces for `n` and `n'`. Then
`S(w)ᴴ G' S(z) = (∏ τ, det ((w τ)ᴴ z τ) ^ d τ) • G S(wᴴ z)`, where `d τ = schurDetExp n n' κ τ` is
`κ τ (#(n τ))` if `#(n τ) < #(n' τ)` and `0` otherwise. 

### `exists_enum_prod_le`

 Sorting: for numbers `d a ≥ 0`, `a ∈ S`, there is a sequence `ρ 0, ρ 1, …` whose first `#S`
terms sum to `∑ a ∈ S, d a`. Also, the product of `d` over any `A ⊆ S` is at most the product of the
first `#A` terms. 

### `fillingRows_injective`

 The rows in one column of a column filling are distinct. 

### `minorsMatrix_diagonal`

 Diagonal matrices act diagonally on tensors: `minorsMatrix` multiplies the basis tensor of a
column filling `T` by the product of the diagonal entries at the rows that occur in `T`. 

### `dotProduct_weylGram_schur_diagonal_le`

 Let `d τ a ≥ 0`, and let `ρ τ 0 ⋯ ρ τ (h - 1)` bound every product of `h` of the `d τ a`. For
the diagonal matrices `D τ` with entries `d τ a`, the form `η* G S(D) η` is at most `η* G η` times
the product of these bounds over the columns of the diagram of height `h < #(n τ)`, each taken at
its height. Here `G` is the Gram matrix, `S = schur κ`, and `κ τ h` is the number of columns of
height `h` at `τ`. 

### `prod_pow_diagramWeight_eq`

 Count the boxes of the diagram by rows and by columns. Assume `FitsRanks n n' κ`. The exponent
`diagramWeight (rankAt n') κ (τ, i)` is the number of columns of height `h` with
`i < h < #(n' τ)`. For `i < #(n τ)` these are the `schurDetExp n n' κ τ` columns of height `#(n τ)`
(none if `#(n τ) = #(n' τ)`) and the columns of height `h` with `i < h < #(n τ)`. 

### `weylNormSq_schur_le`

 Let `z τ` be complex `n' τ × n τ` matrices, and assume `FitsRanks n n' κ`: at each `τ`,
`#(n τ) ≤ #(n' τ)` and `κ τ h = 0` for `#(n τ) < h < #(n' τ)`. There are numbers `ρ τ i ≥ 0` (in the
proof, the squares of the sorted singular values of `z τ`) with two properties. (a)
`∑ i < #(n τ), ρ τ i` is at most `∑ a b, ‖z τ a b‖ ^ 2`. (b) For every complex coordinate vector `ξ`
on `WeylIndexFamily n κ`, the squared Gram norm `weylNormSq` of the Schur matrix image
`schur κ z *ᵥ ξ` is at most `∏ τ, ∏ i < #(n τ), ρ τ i ^ λ(τ, i)` times `weylNormSq ξ`, where
`λ(τ, i) = diagramWeight (rankAt n') κ (τ, i)` is the sum of `κ τ h` over `i < h < #(n' τ)`. 


## Base change, integrality and invariant metric of weight representations

`New.weylRep κ e g` is ∏_τ det(g_τ)^e_τ times the Schur matrix of g.


### `weylRep_map`

 Base change: applying a ring map f entrywise to the matrices g_τ applies f entrywise to the
matrix `New.weylRep` κ e g (∏_τ det(g_τ)^{e_τ} times the Schur matrix of g). 

### `weylRep_entry_mem`

 Integrality: if every g_τ is an invertible matrix over the subring A (with inverse over A,
`New.intGL`), then every entry of `New.weylRep` κ e g lies in A. 

### `stdSpace_ratEmbed_apply`

 The component at the infinite place w of the rational embedding of γ, as a matrix, is γ with
the embedding Φ_w chosen by the CM type applied to its entries. 

### `stdSpace_weightRep_apply`

 On the definite space `New.stdSpace`, γ acts by `New.weylRep` at the family of matrices
Φ_τ(γ̄). 

### `gramForm_conjWeylRep`

 The Gram pairing on coordinate vectors of weight κ is invariant under the product of the
compact groups U(n), acting in weight (κ, e). 

### `map_weightRep`

 After a ring map σ out of ℂ, γ acts by `New.weylRep` at the matrices σ(Φ_τ(γ̄)). 

### `gramForm_map_weightRep`

 The Gram pairing of the σ-conjugates of two coordinate vectors, σ a ring endomorphism of ℂ,
is unchanged when a rational unitary matrix γ acts on both vectors first. 
