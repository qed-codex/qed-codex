---
{
  "module": "ThreeSumApsp/Sec2/Levels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Levels.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Levels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strings cut along a set of levels

Section 2.3.3 cuts a string of `L` variables along a set `Q` of `m` levels: its variables
at the levels of `Q`, in the order of the levels, form a string of length `m`, and its variables at
the other levels form a string of length `L - m`. The first three parts of this file hold for every
alphabet; the last part specializes them to left, right and output strings.

* Every level is the `k`-th lowest level of `Q` or the `k`-th lowest level outside `Q` for some `k`.
  So a statement about all levels is checked on these two kinds of levels (`forall_level_iff`), and
  so is the statement that a set of levels is `Q` (`filter_eq_iff_forall_level`).
* `glue Q hQ f g` is the string with the letters of `f` at the levels of `Q` and the letters of `g`
  at the other levels. It is the only such string (`eq_glue_iff`), and `f` and `g` can be read off
  it (`glue_inj`).
* If the letters are of two kinds, inner and outer, and each is given by its kind and an index, then
  a string can be rebuilt from its inner set and the indices of its letters (`glue_index`).
* "A string is determined by its inner set, its outer part, and its inner part": the strings
  `leftStrOf Q hQ r π`, `rightStrOf Q hQ π c` and `outStrOf Q hQ r c` have the parts that their
  names say, and no other string has them (`existsUnique_leftStr`, `existsUnique_rightStr`,
  `existsUnique_outStr`). No later proof uses these three statements; the later proofs use the
  lemmas from which they follow.


 ### The levels of a set and of its complement, in order 

### `innerLevel_mem`

 The `k`-th lowest level of `Q` is a level of `Q`. 

### `outerLevel_notMem`

 The `k`-th lowest level outside `Q` is not a level of `Q`. 

### `exists_innerLevel`

 Every level of `Q` is the `k`-th lowest level of `Q` for some `k`. 

### `exists_outerLevel`

 Every level outside `Q` is the `k`-th lowest level outside `Q` for some `k`. 

### `innerLevel_congr`

 The levels of `Q` in order depend only on the set `Q`. 

### `outerLevel_congr`

 The levels outside `Q` in order depend only on the set `Q`. 

### `forall_level_iff`

 A property holds at every level if and only if it holds at the levels of `Q` and at the levels
outside `Q`. 

### `filter_eq_iff_forall_level`

 A property cuts out the set `Q` if and only if it holds at the levels of `Q` and fails at the
other levels. 

### `filter_eq_of_forall_innerLevel`

 A property that holds at the `m` levels of `Q`, and at `m` levels in all, cuts out `Q`. 

 ### Gluing two strings along a set of levels 

### `glue`

 The string that has the letters of `f` at the levels of `Q` and the letters of `g` at the other
levels, both in the order of the levels. 

### `glue_innerLevel`

 At the `k`-th lowest level of `Q`, the glued string has the `k`-th letter of `f`. 

### `glue_outerLevel`

 At the `k`-th lowest level outside `Q`, the glued string has the `k`-th letter of `g`. 

### `glue_innerLevel_of_eq`

 At the `k`-th lowest level of a set `Q'` that is equal to `Q`, the string glued along `Q` has
the `k`-th letter of `f`. 

### `glue_outerLevel_of_eq`

 At the `k`-th lowest level outside a set `Q'` that is equal to `Q`, the string glued along `Q`
has the `k`-th letter of `g`. 

### `eq_glue_iff`

 The glued string is the only string with the letters of `f` at the levels of `Q` and the letters
of `g` at the other levels. 

### `glue_inj`

 The two strings can be read off the glued string. 

### `map_glue`

 A map applied to a glued string, letter by letter. 

 ### Alphabets with inner and outer letters 

### `filter_glue`

 If the letters of `f` are inner and those of `g` are outer, then the glued string has its inner
letters exactly at the levels of `Q`. 

### `glue_index`

 Let every inner letter `s` be `inner i` for its index `i = innerIndex s`, and every outer letter
be `outer o` for its index `o = outerIndex s`. Then a string whose inner letters are at the levels
of `Q` is rebuilt by gluing the letters `inner i` and `outer o` for the indices of its letters. 

 ### Left, right and output strings with a given inner set, outer part and inner part 

### `leftStrOf`

 The left string with inner set `Q`, outer part `r` and inner part `π`. 

### `rightStrOf`

 The right string with inner set `Q`, inner part `π` and outer part `c`. 

### `outStrOf`

 The output string with inner set `Q`, row `r` and column `c` (Section 2.3.3: "the output strings
with inner set Q index the entries of the product X_Q Y_Q"): it has `z₀` at the levels of `Q`, and
at the `k`-th lowest level outside `Q` it has `z_{r_k c_k}`. 

### `innerSetL_leftStrOf`

 The inner set of `leftStrOf Q hQ r π` is `Q`. 

### `innerSetR_rightStrOf`

 The inner set of `rightStrOf Q hQ π c` is `Q`. 

### `innerSetO_outStrOf`

 The inner set of `outStrOf Q hQ r c` is `Q`. 

### `outerPartL_leftStrOf`

 The outer part of `leftStrOf Q hQ r π` is `r`. 

### `innerPartL_leftStrOf`

 The inner part of `leftStrOf Q hQ r π` is `π`. 

### `innerPartR_rightStrOf`

 The inner part of `rightStrOf Q hQ π c` is `π`. 

### `outerPartR_rightStrOf`

 The outer part of `rightStrOf Q hQ π c` is `c`. 

### `outStrOf_outerLevel`

 The variable of `outStrOf Q hQ r c` at the `k`-th lowest level outside its inner set. 

### `rowO_outStrOf`

 The row of `outStrOf Q hQ r c` is `r`. 

### `colO_outStrOf`

 The column of `outStrOf Q hQ r c` is `c`. 

### `leftStr_eq_leftStrOf`

 A left string with inner set `Q` is the string `leftStrOf` of its outer part and its inner
part. 

### `rightStr_eq_rightStrOf`

 A right string with inner set `Q` is the string `rightStrOf` of its inner part and its outer
part. 

### `outStr_eq_outStrOf`

 An output string with inner set `Q` is the string `outStrOf` of its row and its column. 

### `leftStrOf_inj`

 Left strings with the same inner set and different outer or inner parts are different. 

### `outStrOf_inj`

 Output strings with different inner sets, rows or columns are different. 

### `existsUnique_leftStr`

 Section 2.3.3: "A string is determined by its inner set, its outer part, and its inner part",
and "the left strings with inner set Q index the entries of such a matrix": for each set `Q` of `m`
levels, each row `r` and each column `π` there is exactly one left string with inner set `Q`, outer
part `r` and inner part `π`. 

### `existsUnique_rightStr`

 Section 2.3.3: "Similarly, the right strings v with inner set Q index the entries of a D × N₀
matrix". 

### `existsUnique_outStr`

 Section 2.3.3: "Finally, the output strings with inner set Q index the entries of the product
X_Q Y_Q". 
