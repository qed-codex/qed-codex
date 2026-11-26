---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/Cubes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/Cubes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/Cubes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cubes, leaves and output strings as lists of digits (Sections 4.2 and 4.3)

A term has the digit P_ij ↦ 3(i - 1) + (j - 1), P₀ ↦ 9, and an output variable the digit
z_ij ↦ 3(i - 1) + (j - 1), z₀ ↦ 9.  A symbol of a cube that is a term keeps the digit of the term,
and the star has the digit 10.  A cube, a leaf or an output string is handled as the list of its L
digits, level 1 first: `digitsC` for cubes, `digitsT` for strings of terms (leaves), `digitsO` for
output strings.  This file translates the notions of Sections 4.2 and 4.3 into operations on such
lists:

* the inner set of an output string η (the paper's w) is the positions of its digit 9, the stars of
  π are the positions of 10, the symbols P₀ of τ the positions of 9, and their numbers are counts
  (`card_innerSetO`, `card_starLevels`, `card_P0Levels`);
* "replacing its e lowest symbols P₀ […] by stars" is `starFirst` (`digitsC_starLowest`);
* "replacing its stars with P₀" is `starsToNines` (`digitsT_starsToP0`);
* "the highest level at which π has a star" is `lastStar` (`lastStar_digitsC`), and π[ℓ ← λ] is
  `List.set` (`digitsC_replace`);
* the dynamic program of Lemma 29 is `dpValueD` (`dpValueD_digitsC`): the product `leafProduct` for
  a list without stars, and the step `sumAtLastStar`; `storedD` is what it computes for a box, at
  the number of stars of the box.


 ## Cubes, leaves and output strings 

### `cubeIdx`

 The digit of a symbol of a cube: a term keeps its digit, the star has 10. 

### `cubeOfIdx`

 The symbol with a given digit. 

### `cubeEquiv`

 The symbols of cubes and their digits. 

### `digitsC`

 The digits of a cube, level 1 first. 

### `digitsT`

 The digits of a leaf, level 1 first. 

### `digitsO`

 The digits of an output string, level 1 first. 

### `digitsC_eq_of_getD`

 A list with L members and the right digit at every level is the list of digits of the cube. 

### `exists_digitsT`

 Every list of L digits below 10 is the list of digits of a leaf. 

 ## The levels of a symbol are the positions of its digit 

### `starCount`

 The number of stars in a list of digits: the star has the digit 10. 

### `cubeIdx_eq_ten`

 The star is the only symbol with the digit 10. 

### `termIdx_eq_nine`

 P₀ is the only term with the digit 9. 

### `getD_digitsO_eq_nine`

 The levels of the inner set are the positions of the digit 9. 

### `forall_nine_digitsO`

 A statement on all positions of the digit 9 is a statement on all levels of the inner set. 

### `forall_ten_digitsC`

 A statement on all positions of the digit 10 is a statement on all levels with a star. 

### `card_innerSetO`

 The size of the inner set is the number of digits 9. 

### `card_starLevels`

 The number of stars is the number of digits 10. 

### `card_P0Levels`

 The number of symbols P₀ is the number of digits 9. 

 ## The lowest symbols P₀ turned into stars 

### `starFirst`

 The first e digits 9 turned into 10 (Section 4.2: "replacing its e lowest symbols P₀ […] by
stars"). 

### `getD_starFirst`

 The digits of `starFirst e l`: a digit 9 with fewer than e digits 9 before it becomes 10. 

### `digitsC_starLowest`

 Replacing the e lowest symbols P₀ of a leaf by stars is `starFirst e` on its digits. 

 ## Stars turned into P₀, and a symbol replaced by a term 

### `starsToNines`

 Stars turned into P₀ (proof of Lemma 29). 

### `starsToNines_of_notMem`

 A list without the digit 10 is not changed. 

### `starsToNines_starFirst`

 Turning the stars back into nines undoes `starFirst`. 

### `digitsT_starsToP0`

 Replacing the stars of a cube with P₀ is `starsToNines` on its digits. 

### `digitsC_replace`

 π[ℓ ← λ] (the proof of Lemma 29) on digits: the digit at position ℓ is set to the digit of λ. 

 ## The highest star 

### `lastStar`

 The position of the last digit 10, if there is one (proof of Lemma 29: "the highest level at
which π has a star"). 

### `lastStar_eq_none_iff`

 `lastStar` finds nothing exactly if the digit 10 does not occur. 

### `lastStar_eq_some_iff`

 `lastStar` finds the last position of the digit 10. 

### `lastStar_digitsC`

 On the digits of a cube with a star, `lastStar` finds the highest level at which it has a
star. 

### `lastStar_digitsC_eq_none_iff`

 `lastStar` finds nothing exactly if the cube has no star. 

 ## The dynamic program of Lemma 29 on digits 

### `leafProduct`

 The product of the two numbers that the encodings have for the leaf with the digits l; the
encodings are arrays indexed by the codes of the leaves. 

### `tenValues`

 The values val(π[ℓ ← λ]) for the ten terms λ, in the order of their digits; l is the list of
digits of π, and p is the position ℓ. 

### `sumAtLastStar`

 The step of the dynamic program of Lemma 29: the sum ∑_λ val(π[ℓ ← λ]), where ℓ is "the highest
level at which π has a star".  For a list without a star it is 0. 

### `sumAtLastStar_congr`

 The step of the dynamic program uses only the ten values that it adds up. 

### `dpValueD`

 The dynamic program of Lemma 29 on lists of digits; e is the number of stars. 

### `storedD`

 The value that is stored for the box l: what the dynamic program of Lemma 29 computes for it, at
its number of stars. 

### `leafProduct_digitsT`

 On the arrays of two encodings, the product at the digits of a leaf is the product of its two
numbers. 

### `dpValueD_digitsC`

 The dynamic program on digits, run on the arrays of the two encodings, is the dynamic program
of Lemma 29. 
