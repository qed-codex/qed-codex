---
{
  "module": "src/New/Congruences/FirstOrder/RibetMethod.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetMethod.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetMethod.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Amitsur's formula and Ribet's method for matrices over an algebra

This file proves Amitsur's formula for block matrices and derives Ribet's method from the
Cayley–Hamilton theorem. Here `u x` (`x : Y`) is a family of matrix representations of `G`. The
coefficients of their characteristic polynomials, as functions of `x`, lie in an algebra `S` of
functions `Y → L`. 'In the image of `R`' is written `∈ (algebraMap R L).range`. The file ends with
Ribet's element for a square matrix of tied rows, a matrix whose rows give relations modulo a left
ideal whose traces are controlled.

## Main definitions and results

* `New.Selmer.exists_ribet_polynomial`: Ribet's method. Let `ρ` represent an `R`-algebra `Λ` with
  characteristic polynomials over `R`, let `𝔞` be a two-sided ideal containing its kernel, and let
  `I` be the left ideal spanned by a vector `y`. If `B y` has entries in `𝔞 + I ρ₀`, then some
  polynomial `P` has constant term `det B`, read through `ρ`, and `I P(ρ₀) ⊆ 𝔞`.
* `New.amitsur_charpoly_comp_coeff_mem_range`: Amitsur's formula for block matrices. If all
  characteristic polynomials of the `ρ w` have their coefficients in the image of `R`, the same
  holds for every square matrix `P` over `Λ`, read as the block matrix with blocks `ρ (P i j)`.
* `New.Selmer.exists_ribet_element_of_tied_rows`: Ribet's element for a matrix of tied rows, for
  representations `u x` (`x : Y`) of `O[G]` and an algebra `S` of functions `Y → L` that contains
  the constants from `O` and, as functions of `x`, the coefficients of the characteristic
  polynomials of the group elements.


### `blockFlattenAlgEquiv`

 The `R`-algebra isomorphism from `N × N` matrices whose entries are `σ × σ` matrices over `L`
onto `(N × σ) × (N × σ)` matrices over `L`, flattening blocks. 

### `amitsur_charpoly_comp_coeff_mem_range`

 Amitsur's formula for block matrices. Let `ρ` be an `R`-algebra map from `Λ` to square matrices
over `L` such that all characteristic polynomials of the `ρ w` have their coefficients in the image
of `R`. The same then holds for every square matrix `P` over `Λ`, read as the block matrix with
blocks `ρ (P i j)`.

Known result: the integrality consequence of Amitsur's formula for the characteristic polynomial of
a sum of matrices. 

### `Selmer.exists_adjugate_polynomial`

 Cramer's rule over `Λ[X]`, from the Cayley–Hamilton theorem, read through `ρ` coefficient by
coefficient. Let `ρ` be an `R`-algebra map from `Λ` to square matrices over `L` whose characteristic
polynomials all have their coefficients in the image of `R`. For a square matrix `B` over `Λ[X]`
there are a polynomial `P` over `R` and a matrix `B'` such that `P(0)` is the determinant of the
block matrix with blocks `ρ (B i j (0))`, and `B' B` is the scalar matrix `P` once `ρ` is applied to
the coefficients of the entries. 

### `Selmer.mul_aeval_eq_zero_of_adjugate`

 Let `Λ[X]` act on `Q` through a ring homomorphism `π : Λ → Q`, with `Λ` acting by left
multiplication and `X` by right multiplication with `π ρ₀`. Suppose that `B - X B₁` kills the image
of the vector `y`, that is, `B y` and `(B₁ y) ρ₀` have the same image, and that `B' (B - X B₁)` is
the scalar matrix `P`, with `P` a polynomial over `R`, once `π` is applied to the coefficients of
the entries. Then `π (y i P(ρ₀)) = 0`. 

### `Selmer.exists_ribet_polynomial`

 Ribet's method. Let `ρ` represent the `R`-algebra `Λ` by matrices over `L` such that the
characteristic polynomials of a spanning set have coefficients in the image of `R`, and let `𝔞` be
a two-sided ideal of `Λ` that contains the kernel of `ρ`. Let `I` be the left ideal spanned by `y`,
and `B` a square matrix over `Λ` such that the entries of `B y` lie in `𝔞 + I ρ₀`. Then some
polynomial `P` over `R` has constant term `det B`, read through `ρ` as a block matrix, and
`I P(ρ₀) ⊆ 𝔞`. Moreover the traces of the `ρ (ρ₁ P(ρ₀))` lie in the image of `R`, and for `δ : R`
such that some `z ∈ I` has `ρ z = δ` (the scalar matrix), `δ` times such a trace is the trace of
`ρ a` for some `a ∈ 𝔞`. 

### `exists_family_algHom_charpoly_mem`

 Let `u x` (`x : Y`) be representations of `O[G]` such that the coefficients of the
characteristic polynomials of the group elements, as functions `Y → L` of `x`, lie in the subalgebra
`S`, and let `κ : O → S` send an element of `O` to the constant function. Then the family lifts to
an `S`-algebra map `ρ` from `S[G]` to matrices over `Y → L` which (a) is `u x` at the point `x` on
elements coming from `O[G]`, and (b) has all its characteristic polynomials with coefficients in
`S` (Amitsur's formula passes from the group elements to their span). 

### `Selmer.det_comp_map_eq_mul_prod`

 Suppose that every matrix `χ c` is, after reindexing along `blockEquiv`, the block `ψ c` plus
the diagonal matrix of the `η e c`. Then the determinant of a matrix `M` over `A`, read through `χ`
as a block matrix, is the product of its determinants through `ψ` and through the `η e`. 

### `Selmer.det_mem_of_coeff_mem`

 Let `u x` (`x : Y`) be representations of `O[G]`, and let `κ : O → S` send an element of `O` to
the constant function. If the coefficients of the characteristic polynomials of the group elements,
as functions `Y → L` of `x`, lie in the subalgebra `S`, then so does the determinant of every
`w : O[G]`. 

### `Selmer.traceIdeal`

 The elements of `Λ` whose traces against every element of `Λ`, through `ρ`, lie in `𝒥`. They
form a two-sided ideal, as traces are cyclic. 

### `Selmer.mem_traceIdeal`

 An element `w` lies in `traceIdeal ρ 𝒥` if and only if the traces of all `ρ (w s)` lie in
`𝒥`. 

### `Selmer.trace_mul_mem_of_mem_span`

 Let `u x` (`x : Y`) be representations of `O[G]`, and let `ρ` be a representation of `S[G]` over
`Y → L` that is `u x` at the point `x` on elements coming from `O[G]` along `κ`. If `r` lies in the
left ideal spanned by the `w` such that the trace of `u x (w g)`, as a function of `x`, lies in `𝒥`
for every group element `g`, then the trace of `ρ (b r)` lies in `𝒥` for every `b : S[G]`. 

### `Selmer.trace_mul_aeval_apply`

 Where `ρ₁ ρ₀` acts as `0`, `ρ₁ P(ρ₀)` acts as `P(0) ρ₁`: at a point `x` where every entry of
`ρ (ρ₁ ρ₀)` vanishes, the trace of `ρ (ρ₁ P(ρ₀))` is `P(0)` times the trace of `ρ ρ₁`. 

### `Selmer.exists_mul_eq_algebraMap_det`

 Cayley–Hamilton for a family. Map `O[G]` to `S[G]` along `κ : O → S`. Let `ρ` be a
representation of `S[G]` over `Y → L` that is `u x` on `O[G]` at each point `x` and has its
characteristic polynomials over `S`. Then for `w : O[G]` the function `x ↦ det (u x w)` is an
element `D` of `S`, and `ρ` sends some left multiple of `w` to the scalar matrix `D`. 

### `Selmer.map_mem_span_range`

 A ring homomorphism `f` sends the left ideal spanned by the `y i` into the left ideal spanned by
the `f (y i)`. 

### `Selmer.map_mul_eq_zero_of_blocks`

 Let `χ` be, after reindexing by `blockEquiv`, the block sum of `ψ` and the characters `η e`. If
`ρ₁` vanishes under `ψ` and under every character but `η 0`, and `ρ₀` vanishes under `η 0`, then
`χ (ρ₁ ρ₀) = 0`. 

### `Selmer.exists_ribet_element_of_tied_rows`

 Ribet's element for a matrix of tied rows. Let `u x` (`x : Y`) be representations of `O[G]`, and
let `S` be an algebra of functions `Y → L` that contains the constants from `O` and, as functions of
`x`, the coefficients of the characteristic polynomials of the group elements. Let `𝒥` be an
`S`-module of functions `Y → L`, `I` the left ideal spanned by `y`, and `𝔞` the left ideal spanned
by the elements whose traces against every group element lie in `𝒥`. Let `B` be a square matrix,
indexed like `y` by the finite type `N`, of tied rows: the entries of `B y` lie in `𝔞 + I ρ₀`.
Suppose that for `x ∈ 𝓧`, `u x` is, after reindexing along `blockEquiv`, the block `ψ x` plus the
characters `η e`, that `ρ₁` is `μ₀` on `η 0` and zero on the other summands, and that `ρ₀` is zero
on `η 0`. Then one `f : S` multiplies `det (u x w)` into `𝒥` for every `w ∈ I`, and its value at
`x ∈ 𝓧` is `μ₀ det (ψ x B) ∏ det (η e B)`. 
