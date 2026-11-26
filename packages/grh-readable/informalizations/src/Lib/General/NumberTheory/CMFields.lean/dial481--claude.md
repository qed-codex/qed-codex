---
{
  "module": "src/Lib/General/NumberTheory/CMFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CMFields.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CMFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Criteria for CM fields

This file gives two ways to show that a number field is CM. The first asks that the field contain a
totally complex field, and that complex conjugation be induced, in all embeddings at once, by a map
of the field to itself. The second shows that adjoining to a CM field a root of a suitable
polynomial gives a CM field, whose finite adeles it also describes.

We write `𝔸f K` for the ring of finite adeles of a number field `K`. For an extension `L / K` of
number fields, `𝔸f L` is an algebra over `𝔸f K`, and complex conjugation `star` of a CM field
extends to its finite adeles.

## Main definitions and results

* `New.isCMField_of_forall_exists_conj`: a number field is CM if it contains a totally complex field
  and complex conjugation is induced, in all embeddings at once, by a map of the field to itself.
* `New.isCMField_adjoinRoot_of_forall_root_mul_star_eq`: let `E` be a CM field and `P` an
  irreducible polynomial over `E`. If all complex roots of `P` have the same rational square
  absolute value `ν`, then `L = E[X]/(P)` is again CM.
* `New.aeval_root_finAdele_surjective`, `New.aeval_root_finAdele_eq_zero_iff`: for monic `P`, the
  finite adeles `𝔸f L` are obtained from `𝔸f E` by adjoining a root of `P`.
* `New.IsFinAdelePresentation`: a map from polynomials over `𝔸f E` presents `𝔸f L` as the quotient
  by `P`, compatibly with `E[X] → L` and with complex conjugation.
* `New.adjoinRoot_cm_presentation`: these facts about `L` and `𝔸f L` in one statement.


 ## A CM criterion via a conjugation on the field 

### `New.isCMField_of_forall_exists_conj`

 Let L be a number field extending a totally complex field E. If every x ∈ L has a y ∈ L with
φ(y) equal to the complex conjugate of φ(x) for all embeddings φ : L → ℂ, then L is a CM
field. 

 ## CM fields obtained by adjoining a root, and their finite adeles 

### `instance : NumberField (AdjoinRoot P)`

 Adjoining a root of an irreducible polynomial to a number field `E` gives a number field. 

### `adjoinRoot_embedding_root_mul_star`

 If all complex roots of the irreducible polynomial `P`, under all embeddings of `E`, satisfy
`r * star r = ν`, then so does the image of the root of `P` under every embedding of
`E[X]/(P)`. 

### `isCMField_adjoinRoot_of_forall_root_mul_star_eq`

 If all complex roots of the irreducible polynomial `P` over the CM field `E` have the same
rational square absolute value `ν`, then `E[X]/(P)` is a CM field. 

### `adjoinRoot_root_mul_star`

 If all complex roots of the irreducible polynomial `P` have the rational square absolute value
`ν`, then the root of `P` in the CM field `E[X]/(P)` times its conjugate is `ν`. 

### `aeval_root_finAdele_map`

 At the root of `P`, a polynomial over `E` takes the same value whether it is evaluated in
`E[X]/(P)` or in the finite adeles of this field. 

### `adjoinRootAdelePowerBasis`

 For a monic irreducible `P`, the powers of its root below the degree of `P` are a basis of the
finite adeles of `E[X]/(P)` over those of `E`. 

### `aeval_root_finAdele_surjective`

 For a monic irreducible `P`, every finite adele of `E[X]/(P)` is the value at the root of `P` of
a polynomial over the finite adeles of `E`. 

### `aeval_root_finAdele_eq_zero_iff`

 A polynomial over the finite adeles of `E` vanishes at the root of a monic irreducible `P` in
the finite adeles of `E[X]/(P)` exactly when `P` divides it. 

### `aeval_root_finAdele_map_conj_comp`

 Let `star` and `conj` be complex conjugation, extended to finite adeles. If `c` represents the
conjugate of the root of `P` in the CM field `E[X]/(P)`, then conjugating the coefficients of a
polynomial over `𝔸f E` and substituting `c` for `X` conjugates its value at the root, seen as a
finite adele of `E[X]/(P)`. 

### `IsFinAdelePresentation`

 Let `L = E[X]/(P)` be a CM field. An algebra map `ε` from the polynomials over the finite adeles
`𝔸f E` to `𝔸f L` presents `𝔸f L` as `(𝔸f E)[X]/(P)`, compatibly with `E[X] → L` and with complex
conjugation. 

### `IsFinAdelePresentation.surjective`

 Every finite adele of `L` is a value of `ε`. 

### `IsFinAdelePresentation.eq_zero_iff`

 The kernel of `ε` consists of the multiples of `P`. 

### `IsFinAdelePresentation.apply_map`

 On polynomials over `E`, the map `ε` agrees with `E[X] → L`. 

### `IsFinAdelePresentation.apply_map_conj_comp`

 If `c` represents the conjugate of the root of `P`, then conjugating the coefficients of `q`
  and substituting `c` for `X` conjugates `ε q`. 

### `adjoinRoot_cm_presentation`

 Let `P` be a monic irreducible polynomial over the CM field `E` such that every complex root `r`
of `P`, under every embedding of `E`, satisfies `r * star r = ν` for a fixed rational `ν`. Then
`L = E[X]/(P)` is a CM field, the root of `P` in `L` times its conjugate is `ν`, and evaluation at
the root presents the finite adeles of `L` as the polynomials over `𝔸f E` modulo `P`, compatibly
with `E[X] → L` and with complex conjugation. 
