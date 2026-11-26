---
{
  "module": "ThreeSumApsp/Util/Digits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Digits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Digits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strings of digits as numbers

The paper indexes its arrays by strings (Section 2.3.1).  A program indexes them by numbers: the
string `d₁ d₂ ⋯ d_n` of digits in base `b` is coded by the number `d₁ b^{n-1} + ⋯ + d_n`.  The first
digit (the paper's level 1) is the most significant one, so the strings that begin with a given
digit have consecutive codes, and a slice of an array is a contiguous part of it.

* `code` is the number of a string, `digit` reads one digit of a number, `digitList` all of them,
  and `ofDigitList` is Horner's rule.
* `code` and `digit` undo each other (`digit_code`, `code_digit`), so the strings of length `n`
  correspond to the numbers below `b^n` (`codeEquiv`).
* For lists of digits, `digitList` undoes `ofDigitList` (`digitList_ofDigitList`). A list of `n`
  digits has a value below `b^n` (`ofDigitList_lt`), which determines it (`eq_of_ofDigitList_eq`).
  One more digit at the end is one more step of Horner's rule (`ofDigitList_append_singleton`,
  `ofDigitList_take_succ`).
* For an alphabet `α` whose letters are numbered by `e : α ≃ Fin b`, `codeStr e` and `decodeStr e`
  go from strings over `α` to numbers and back, so these strings, too, correspond to the numbers
  below `b^n` (`strEquiv`).  `digitsStr e` is the list of the digits of such a string; Horner's rule
  computes the code from it (`ofDigitList_digitsStr`).

Mathlib's `Nat.ofDigits` and `finFunctionFinEquiv` put the least significant digit first, so they
would make a slice a scattered part of an array; this is why the codes are defined here.


 ## Strings of numbers below `b` 

### `code`

 The number with the digits `d 0, d 1, …, d (n-1)` in base `b`, most significant digit first. 

### `digit`

 The digit number `ℓ` (counted from 0, most significant first) of the `n`-digit number `c` in
base `b`. 

### `digitList`

 The `n` digits of `c` in base `b`, most significant first, as a list. 

### `ofDigitList`

 Horner's rule: the number with the given list of digits, most significant first. 

### `code_cons`

 The code of the digit `s` followed by the string `d`. 

### `foldl_ofFn`

 Horner's rule, started with `acc`, shifts `acc` by `n` digits and adds the code. 

### `code_eq_ofDigitList`

 The code is computed by Horner's rule, with one multiplication by `b` and one addition for each
digit. 

### `code_lt`

 An `n`-digit number is less than `b^n`. 

### `code_div_mod`

 The first digit and the rest, by division. 

### `digit_succ`

 The digits after the first one are the digits of the remainder modulo `b^n`. 

### `digit_code`

 The digits of the code are the digits. 

### `digit_lt`

 A digit is less than the base. 

### `code_digit`

 A number below `b^n` is the code of its digits. 

### `eq_of_code_eq`

 Different strings have different codes. 

### `pos_of_lt_pow`

 If some number is below `b^n` and `n` is not 0, the base is not 0. 

### `codeEquiv`

 The strings of `n` digits in base `b` correspond to the numbers below `b^n`. 

 ## Lists of digits 

### `length_digitList`

 The list of the `n` digits of a number has `n` entries. 

### `getElem_digitList`

 Entry `i` of the list of digits is digit `i`. 

### `lt_of_mem_digitList`

 The digits are below the base. 

### `digitList_code`

 The list of digits of a code. 

### `ofDigitList_nil`

 The empty list of digits has the value `0`. 

### `ofDigitList_append_singleton`

 One more digit at the end multiplies the value by `b` and adds the digit. 

### `ofDigitList_take_succ`

 The value of the first `i + 1` digits, from the value of the first `i` digits. 

### `ofDigitList_eq_code`

 The value of a list of digits is the code of the list, read as a string. 

### `ofDigitList_lt`

 A number with `n` digits below `b` is below `b^n`. 

### `digitList_ofDigitList`

 The digits of the value of a list of digits below `b` are the list. 

### `eq_of_ofDigitList_eq`

 Two lists of the same length of digits below `b` with the same value are equal. 

 ## Strings over a numbered alphabet 

### `codeStr`

 Strings over an alphabet `α` whose letters are numbered by `e : α ≃ Fin b`: the code of a
string. 

### `decodeStr`

 The string with a given code. 

### `codeStr_cons`

 The code of the letter `s` followed by the string `u'`. 

### `codeStr_lt`

 The code of a string of length `n` is less than `b^n`. 

### `decodeStr_codeStr`

 Decoding undoes coding. 

### `codeStr_decodeStr`

 Coding undoes decoding, for a number below `b^n`. 

### `codeStr_injective`

 Different strings have different codes. 

### `digitList_codeStr`

 The list of digits of the code of a string. 

### `decodeStr_cons`

 The string with the code `s · b^n + c` is the letter with the digit `s` followed by the string
with the code `c`. 

### `strEquiv`

 The strings of length `n` over `α` correspond to the numbers below `b^n`. 

 ## The list of the digits of a string 

### `digitsStr`

 The digits of a string over an alphabet with numbered symbols, level 1 first. 

### `exists_digitsStr`

 Every list of n digits below b is the list of digits of a string. 

### `getD_digitsStr`

 The digit at a level. 

### `digitsStr_eq_of_getD`

 A list with n members and the right digit at every level is the list of digits of the
string. 

### `forall_getD_digitsStr`

 A statement on all positions of a digit a ≠ 0 is a statement on levels (beyond the end of the
list `getD` gives 0, so a position of the digit a is a level). 

### `ofDigitList_digitsStr`

 The code is computed from the digits by Horner's rule. 
