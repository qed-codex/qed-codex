---
{
  "module": "src/Lib/General/Groups/CharacterTheory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CharacterTheory.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CharacterTheory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Characters of finite groups: averages, virtual characters and central projections

This file sets up the character theory of a finite group `G` that is used for the characters of
`GL n` over a finite field. From Wedderburn's theorem it derives criteria for irreducibility.

## Main definitions and results

* `New.IsIrreducibleChar`: characters of norm one that satisfy the convolution identity with every
  class function.
* `New.virtualChars S G`: the `S`-span of the characters, a subalgebra of `G → ℂ`; for `S = ℤ` these
  are the virtual characters, for `S = ℕ` the characters (`New.isChar_of_mem_virtualChars`).
* `New.IsCentralProj`: central idempotents e of the group algebra ℂ[H] of any group H. Their
  coefficients are class functions; 1 − e, the image of e under a ring endomorphism of ℂ and tensor
  products are again central idempotents.
* `New.IsClassFunction.isIrreducibleChar_of_classInner_eq_intCast`,
  `New.IsClassFunction.mem_virtualChars`, `New.IsClassFunction.exists_eq_mul_groupAlgElem_mul`:
  criteria for a class function `f` to be an irreducible character, for `f` to be a combination of
  characters with coefficients in a given semiring, and for an element of `ℂ[G]` to be recovered
  from its product with `New.groupAlgElem f`. They are collected in
  `New.isIrreducibleChar_and_mem_virtualChars_and_exists_mul`.
* `New.IsCentralProj.isChar_card_mul_coeff`: for a central idempotent `e` of `ℂ[G]`, the function
  `g ↦ |G| · e(g)` is a character. Its pairing with any character is the rank of an idempotent, so a
  natural number. It is the character of a representation of dimension at most `|G|`
  (`New.IsCentralProj.exists_character_eq_and_finrank_le_card`), so the coefficients of `e` have
  norm at most `1` (`New.IsCentralProj.norm_coeff_le_one`).
* `New.IsCentralProj.self_adjoint`, `New.IsCentralProj.sum_norm_sq_conv_le`: a central idempotent of
  `ℂ[G]` acts self-adjointly for every `G`-invariant form that is sesquilinear for `σ⁻¹ ∘ conj ∘ σ`,
  complex conjugation transported along an automorphism `σ` of `ℂ`. So it acts as an orthogonal
  projection in every unitary representation. Hence convolution with it does not increase `ℓ²`
  norms.



## Averages, inner products, characters and group algebra elements

The basic definitions: `New.finMean`, `New.classInner`, `New.groupAlgElem` (a function `f` as the
element `∑ g, f g • g` of the group algebra), `New.IsChar`, `New.IsClassFunction` and
`New.IsIrreducibleChar`.


### `finMean`

 The average of a complex function f on a finite type G: the sum of its values divided by the
cardinality of G. 

### `classInner`

 The inner product ⟨f, h⟩ of complex functions on a finite set: the average over g of conj
f(g) · h(g). 

### `groupAlgElem`

 For a complex function f on a finite group G, the element Σ f(g)·g of the group algebra
ℂ[G]. 

### `IsChar`

 The function f : G → ℂ is the character of a finite-dimensional complex representation
of G. 

### `IsClassFunction`

 The function f : G → ℂ is a class function: f(xgx⁻¹) = f(g) for all g, x in G. 

### `IsIrreducibleChar`

 The function `f` is an irreducible character, in the following form: (a) `f` is a character,
(b) its norm `New.classInner f f` is `1`, and (c) for every class function `h` and every `y`,
`f 1 * finMean (t ↦ conj (f t) * h (t * y)) = classInner f h * f y`. Clause (c) says that `h`
acts by a scalar in the representation. The lemma
`New.IsClassFunction.isIrreducibleChar_of_classInner_eq_intCast` gives a criterion for all three
clauses. 

### `IsIrreducibleChar.mul_classInner_translate`

 For an irreducible character `f`, a class function `h` and `y : G`, the inner product of `f`
with the translate `t ↦ h (t * y)`, times `f 1`, is `classInner f h * f y`. 


## Averages of complex functions on finite sets

`New.finMean f` is the mean of a complex function on a finite type.


### `finMean_prod`

 Fubini: the average over a product is the iterated average. 

### `finMean_comp_surjective`

 Let `p : α →+ β` be a surjective homomorphism of finite additive groups. Then the mean of
`f ∘ p` over `α` equals the mean of `f` over `β`. 


## Characters and the algebra of virtual characters

* `New.IsChar.exists_sum_addChar_zpowers`: on a cyclic subgroup a character is a sum of linear
  characters; hence `New.IsChar.apply_inv`, `New.IsChar.isIntegral`, `New.IsChar.norm_apply_le` and
  `New.IsChar.star`.


 ### The algebra spanned by the characters 

### `IsChar.mul`

 The product of two characters is a character, that of the tensor product. 

### `virtualChars`

 For a group G and a commutative semiring S with ℂ an S-algebra, the S-subalgebra of functions
G → ℂ spanned over S by the characters of G. 

### `isChar_zero`

 The zero function is a character, that of the zero representation. 

### `IsChar.add`

 The sum of two characters is a character, that of the direct sum. 

 ### Properties of a character 

### `sum_finMean_mul_addChar`

 Fourier inversion on a finite abelian group `A`: a function `φ : A → ℂ` is the sum of the
characters `l` of `A`, weighted by the averages of `x ↦ φ x * l (-x)`. 

### `IsChar.exists_sum_addChar_zpowers`

 On the cyclic subgroup `zpowers g` generated by `g`, a character `χ` of `G` is the sum of the
linear characters `l` of that subgroup (written additively) with multiplicities `m l : ℕ`. 

### `IsChar.isIntegral`

 The values of a character of a finite group are algebraic integers. 

### `IsChar.norm_apply_le`

 The norm of a character of a finite group is largest at the identity. 

### `IsChar.star`

 The complex conjugate of a character is a character, that of the dual representation. 

### `IsChar.exists_classInner_eq`

 The inner product `classInner χ f` (the average of `conj (χ g) * f g`) of a character `χ` with
an `S`-linear combination `f` of characters lies in the image of `S` in `ℂ`. 

### `comp_mem_virtualChars`

 The pull-back along a homomorphism from a finite group of an `S`-linear combination of
characters is an `S`-linear combination of characters. 


## Central projections of group algebras and their tensor products

* `New.piTensorElem`: the tensor product ⊗ x_i in ℂ[∏ G_i] of elements x_i of ℂ[G_i], for a finite
  index type ι. If every x_i is a central idempotent, so is ⊗ x_i
  (`New.IsCentralProj.piTensorElem`).
* `New.piTensorElem_apply_eq_zero`, `New.piTensorElem_mul_eq_zero`: a tensor product kills a vector,
  or another tensor product, as soon as one factor does.


### `asAlgebraHom_eq_sum`

 An element `e` of the group algebra of a finite group `H` acts in the representation `σ` as
the sum of the operators `σ s` weighted by the coefficients of `e`. 

### `IsCentralProj`

 `e` is a central idempotent of the complex group algebra `ℂ[H]` of a group `H`: it is
idempotent and its coefficients form a class function. 

### `piTensorElem`

 The multiplicative map sending a family `x i ∈ ℂ[G i]` to its tensor product in the group
algebra of the product of the `G i`: the coefficient at `s` is the product over `i` of the
coefficients of `x i` at `s i`. 

### `asAlgebraHom_piTensorElem_mulSingle`

 The tensor `1 ⊗ ⋯ ⊗ x ⊗ ⋯ ⊗ 1`, with `x` in place `i`, acts in a representation `ρ` of the
product of the groups `G j` as `x` does in the restriction of `ρ` to the factor `G i`. 

### `piTensorElem_apply_eq_zero`

 If the factor `x i` kills the vector `v` in the restriction of `ρ` to `G i`, then the tensor
product of the `x j` kills `v` in `ρ`. 

### `piTensorElem_mul_eq_zero`

 Two tensor products multiply to zero as soon as their factors in one place `i` do. 

### `map`

 Applying a ring endomorphism `σ` of `ℂ` to the coefficients of a central idempotent `e` of
`ℂ[H]` (`H` any group) gives a central idempotent. 


## Irreducibility criteria and expansion of class functions

* `New.sum_mul_trace_block_eq_card_mul`, `New.classInner_eq_sum_of_eq_sum`: the trace computation
  behind the expansion of a class function in the block characters, and Parseval's identity.
* `New.IsChar.asAlgebraHom_groupAlgElem_eq_zero_iff`: `∑ g, conj (χ g) • g` acts as zero in `ρ` iff
  `χ` is orthogonal to the character of `ρ`. `New.IsChar.asAlgebraHom_groupAlgElem_eq_zero` is a
  sufficient condition for `∑ g, χ (i g * s) • g` to act as zero, `i` a group homomorphism.


### `blockRepresentation`

 If `e` identifies `ℂ[G]` with a product of matrix algebras, `G` acts on column vectors through
the `i`-th block. 

### `exists_isChar_trace_block`

 Let `e` identify `ℂ[G]` with a product of matrix algebras of sizes `d i`. There is a character
`χ` of degree `d i`, that of the dual of the `i`-th block, such that the `i`-th block of each
`y : G` has trace `χ y⁻¹`. 

### `IsClassFunction.exists_block_eq_algebraMap`

 Let `e` identify `ℂ[G]` with a product of matrix algebras. For a class function `φ` the element
`∑ g, φ g • g` is central, so each of its blocks under `e` is a scalar matrix. 

### `IsChar.sum_conj_mul_eq_of_block`

 Let `e` identify `ℂ[G]` with a product of matrix algebras (the blocks). If the `i`-th block of
`∑ g, φ g • g` is the scalar `c` and `χ` is a character such that the `i`-th block of each `y` has
trace `χ y⁻¹`, then `∑ x, conj (χ x) * φ (x * y) = c * χ y`. 

### `sum_mul_trace_block_eq_card_mul`

 Let `e` identify `ℂ[G]` with a product of matrix algebras (the blocks) of sizes `d i`. If the
`i`-th block of `∑ g, φ g • g` is the scalar `c i` for each `i`, then `|G| * φ g` is the sum over
`i` of `c i * d i` times the trace of the `i`-th block of `g⁻¹`. 

### `classInner_eq_sum_of_eq_sum`

 Parseval's identity: if `φ = ∑ i, ⟨χ i, φ⟩ • χ i` for the inner product `New.classInner`, then
`⟨φ, f⟩ = ∑ i, conj ⟨χ i, φ⟩ * ⟨χ i, f⟩`. 

### `eq_of_eq_sum_of_classInner_eq_intCast`

 Suppose `f = ∑ j, ⟨χ j, f⟩ • χ j` has norm `⟨f, f⟩ = 1` and `0 ≤ re (f 1)`. If the coefficient
`⟨χ i, f⟩` is a nonzero integer and `0 < re (χ i 1)`, then `f = χ i`. 

### `IsExpansionFamily`

 A finite family `χ i` of characters of a finite group `G` in which every class function expands.
The brackets `⟨ , ⟩` denote the inner product `New.classInner`. 

### `IsExpansionFamily.isChar`

 Each `χ i` is a character. 

### `IsExpansionFamily.re_apply_one_pos`

 Each `χ i` has positive degree. 

### `IsExpansionFamily.mul_classInner_translate`

 For a class function `φ`, `χ i 1 * ⟨χ i, φ (· * y)⟩ = ⟨χ i, φ⟩ * χ i y` for all `y`. 

### `IsExpansionFamily.eq_sum`

 A class function `φ` is the sum of the `⟨χ i, φ⟩ • χ i`. 

### `exists_isExpansionFamily`

 A finite group has a finite family of characters in which every class function expands. 

### `IsClassFunction.isIrreducibleChar_of_classInner_eq_intCast`

 Let `f` and `I` be class functions on a finite group `G` with `⟨I, f⟩ ≠ 0`, `⟨f, f⟩ = 1` and
`0 ≤ re (f 1)`, where `⟨ , ⟩` is the inner product `New.classInner`. Suppose `⟨χ, f⟩` is an integer
for every character `χ` with `⟨χ, I⟩ ≠ 0` and `χ 1 * ⟨χ, I (· * y)⟩ = ⟨χ, I⟩ * χ y` for all `y`.
Then `f` is an irreducible character. 

### `IsClassFunction.mem_virtualChars`

 Let `f` be a class function on a finite group `G`. If the inner product of every character with
`f` comes from the semiring `Z`, then `f` is a `Z`-combination of characters. 

### `IsClassFunction.exists_eq_mul_groupAlgElem_mul`

 Let `f` be a class function on a finite group `G`. Suppose `a ∈ ℂ[G]` acts as zero in every
finite-dimensional representation in which `New.groupAlgElem f = ∑ g, f g • g` acts as zero. Then
`a = u * New.groupAlgElem f * a` for some `u ∈ ℂ[G]`. 

### `isIrreducibleChar_and_mem_virtualChars_and_exists_mul`

 Three criteria for a class function `f` on a finite group `G`, collected in one statement:
(a) `New.IsClassFunction.isIrreducibleChar_of_classInner_eq_intCast`, for `f` to be an irreducible
character; (b) `New.IsClassFunction.mem_virtualChars`, for `f` to be a `Z`-combination of
characters, `Z` a commutative semiring with `ℂ` a `Z`-algebra;
(c) `New.IsClassFunction.exists_eq_mul_groupAlgElem_mul`, for a left multiple of
`New.groupAlgElem f` to fix an element `a` of `ℂ[G]`. 

### `IsChar.asAlgebraHom_groupAlgElem_eq_zero`

 Let `i : G →* H` be a group homomorphism with `G` finite, `χ` a character of `H` and `s ∈ H`.
If the product of `χ ∘ i` with the character of a finite-dimensional representation `ρ` of `G` has
average zero, then `∑ g, χ (i g * s) • g` acts as zero in `ρ`. 

### `IsChar.asAlgebraHom_groupAlgElem_eq_zero_iff`

 For a character `χ` and finite-dimensional `ρ`, the element `∑ g, conj (χ g) • g` acts as zero
in `ρ` iff `χ` is orthogonal to the character of `ρ` for the inner product `New.classInner`. 

 ## Integrality of central projections 

### `New.IsCentralProj.isChar_card_mul_coeff`

 If `e` is a central idempotent of the complex group algebra of a finite group `G`, then
`g ↦ |G| · e(g)`, with `e(g)` the coefficient of `g`, is the character of a finite-dimensional
representation of `G`. 

### `New.IsCentralProj.exists_character_eq_and_finrank_le_card`

 If `e` is a central idempotent of the complex group algebra of a finite group `G`, then
`g ↦ |G| · e(g)`, with `e(g)` the coefficient of `g`, is the character of a representation of `G` of
dimension at most `|G|`. 

### `New.IsCentralProj.norm_coeff_le_one`

 The coefficients of a central idempotent of `ℂ[G]` have norm at most `1`. 

 ## Central projections as orthogonal projections 

### `self_adjoint`

 Let `ρ` be a representation of a finite group `G` on a complex vector space `V` and `σ` a field
automorphism of `ℂ`. Let `B` be a `G`-invariant form on `V`, linear in the second argument and
semilinear for `σ⁻¹ ∘ conj ∘ σ` in the first. Then a central idempotent `e` of `ℂ[G]` is
self-adjoint for `B`: `B (e x) y = B x (e y)`. 

### `sum_norm_sq_conv_le`

 Convolution with a central idempotent e of ℂ[G], along a homomorphism φ : G → H of finite
groups, is a contraction of ℓ²(H, V): ∑_s ‖∑_t e(t) f(φ(t)⁻¹ s)‖² ≤ ∑_s ‖f(s)‖². 
