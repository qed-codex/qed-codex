---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/Alphabets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Alphabets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/Alphabets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The alphabets of Schönhage's identity as digits

Section 2.2 names seven left variables, seven right variables, ten output variables and
ten terms; Section 2.3.1 indexes arrays by strings over these alphabets.  Here every
letter gets a digit, so that a string becomes a number (`codeStr`).

* The left variables `x₁ x₂ x₃ p₁₁ p₁₂ p₂₁ p₂₂` are the digits `0, …, 6`; likewise the right
  variables.
* The output variables `z₁₁ z₁₂ … z₃₃ z₀` are the digits `0, …, 9`, and the terms `P₁₁ … P₃₃ P₀`
  likewise, so that `z_ij` and `P_ij` have the same digit `3(i-1) + (j-1)`, and `z₀` and `P₀` have
  the digit 9.
* Left and right strings are numbers in base 7 (`codeL`, `codeR`), output strings, vertices and
  leaves in base 10 (`codeO`, `codeT`), strings of indices of outer variables in base 3
  (`codeOuter`) and of inner variables in base 4 (`codeInner`), always with level 1 most
  significant.
* Which output variables are inner, and which term contributes to which output variable (Section
  2.2), is read off the digits (`outVar_isInner_iff`, `contributes_iff`).
* The coefficients of the linear forms `φ_λ` and `ψ_λ` (Section 2.2) are written out as the rows of
  two 10 × 7 tables, `phiTable` and `psiTable`, which the programs store row after row
  (`phiFlat_spec`, `psiFlat_spec`).


 ## Digits 

### `leftIdx`

 The digit of a left variable. 

### `leftOfIdx`

 The left variable with a given digit. 

### `rightIdx`

 The digit of a right variable. 

### `rightOfIdx`

 The right variable with a given digit. 

### `outIdx`

 The digit of an output variable. 

### `outOfIdx`

 The output variable with a given digit. 

### `termIdx`

 The digit of a term. 

### `termOfIdx`

 The term with a given digit. 

### `pairIdx`

 The digit of an index pair `(i, j)` of an inner variable. 

### `pairOfIdx`

 The index pair with a given digit. 

### `leftEquiv`

 The left variables and their digits. 

### `rightEquiv`

 The right variables and their digits. 

### `outEquiv`

 The output variables and their digits. 

### `termEquiv`

 The terms and their digits. 

### `termOfNat`

 The term with the digit `t`, for a natural number `t` below 10 (and `P₀` from 10 on). 

### `termIdx_termOfNat`

 The digit of the term with the digit `t`. 

### `termOfNat_termIdx`

 The term with the digit of `λ` is `λ`. 

### `pairEquiv`

 The index pairs and their digits. 

 Applying one of the five bijections gives the digit. 

 ## Codes of strings 

### `codeL`

 The code of a left string, in base 7. 

### `codeR`

 The code of a right string, in base 7. 

### `codeO`

 The code of an output string, in base 10. 

### `codeT`

 The code of a vertex or a leaf, in base 10. 

### `codeOuter`

 The code of a string of indices of outer variables, in base 3. 

### `codeInner`

 The code of a string of index pairs of inner variables, in base 4. 

### `decodeO`

 The output string with a given code. 

### `decodeT`

 The vertex or leaf with a given code. 

 ### Codes of output strings and of vertices

The general facts about `codeStr`, under names of their own for the two codes that occur most. 

### `codeO_cons`

 The code of the output variable `z` followed by the output string `w'`. 

### `codeO_lt`

 The code of an output string of length `n` is less than `10^n`. 

### `decodeO_codeO`

 Decoding undoes coding. 

### `codeO_decodeO`

 Coding undoes decoding, for a number below `10^n`. 

### `codeO_injective`

 Different output strings have different codes. 

### `decodeO_cons`

 The output string with the code `z · 10^n + c`, where `c` is the code of `w'`, is `z w'`. 

### `codeT_cons`

 The code of the term `λ` followed by the vertex `τ'`. 

### `codeT_lt`

 The code of a vertex at depth `n` is less than `10^n`. 

 ## The structure of the identity, in digits 

### `outVar_isInner_iff`

 An output variable is inner exactly if its digit is 9. 

### `contributes_iff`

 A term contributes to an output variable exactly if the variable has the digit 9 or the two
digits are equal. 

### `outIdx_z`

 The digit of `z_ij` is `3 (i - 1) + (j - 1)`. 

### `termIdx_P`

 The digit of `P_ij` is `3 (i - 1) + (j - 1)`. 

### `outIdx_z0`

 The digit of `z₀` is 9. 

### `termIdx_P0`

 The digit of `P₀` is 9. 

### `leftIdx_p`

 The digit of the inner left variable `p_ij` is 3 plus the digit of the pair `(i, j)`. 

### `rightIdx_q`

 The digit of the inner right variable `q_ij` is 3 plus the digit of the pair `(i, j)`. 

 ## The coefficients of the linear forms, as tables 

### `phiTable`

 The coefficients of the forms `φ_λ`: row `λ`, column `s`, both by digits. 

### `psiTable`

 The coefficients of the forms `ψ_λ`: row `λ`, column `t`, both by digits. 

### `phiFlat`

 The table of the coefficients `φ_λ(s)`, row after row, as a program stores it. 

### `psiFlat`

 The table of the coefficients `ψ_λ(t)`, row after row, as a program stores it. 

### `length_phiFlat`

 The table of the `φ_λ(s)` has 70 entries. 

### `length_psiFlat`

 The table of the `ψ_λ(t)` has 70 entries. 

### `phiFlat_spec`

 The entry number `7 λ + s` of the table, by digits, is the coefficient `φ_λ(s)`. 

### `psiFlat_spec`

 The entry number `7 λ + t` of the table, by digits, is the coefficient `ψ_λ(t)`. 
