---
{
  "module": "ThreeSumApsp/Sec4/Boxes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Boxes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Boxes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cubes and boxes (Section 4.2)

A cube is a string of `L` symbols, each of them one of the ten terms or a star, and its leaves are
obtained by replacing each star by any term. A box is a cube with at most `m - t` symbols `P₀` or
stars whose stars are all below its symbols `P₀`. This file proves what the paper says about cubes
and boxes before it turns to the boxes of one output string, in this order:

* from "Notions from Section 2": `M ≤ 10^L` (`M_le_ten_pow`);
* a cube with `e` stars has `10^e` leaves (`Cube.card_leaves`);
* the leaves, the stars and the symbols `P₀` of three cubes: a leaf read as a cube (`Cube.ofLeaf`),
  a cube with a star replaced by a term (`Cube.replace`), and a leaf with stars put at a set of
  levels (`Cube.starAt`); every cube that Section 4.2 makes from a leaf is of this third form;
* the leaves contributing to an output string `η` (w in the paper) are the leaves of the cube of `η`
  (`mem_leaves_cubeOf`), so the entry `(X_Q Y_Q)[η]` is the value of that cube
  (`mul_apply_eq_val_cubeOf`); Section 4.2 starts from this remark, and nothing else rests on it;
* the leaf obtained by replacing the stars of a cube with `P₀` chooses `P₀` where the cube has `P₀`
  or a star (`P0Levels_starsToP0`);
* a box only contains leaves of order at least `t` (`le_order_of_mem_leaves`);
* the `k` lowest levels of a set `S` lie below the other levels of `S` (`lowest_lt`), this property
  characterizes them (`eq_lowest_of_lt`), and there are `min k |S|` of them (`card_lowest`);
* a box is a leaf with its lowest symbols `P₀` replaced by stars (`eq_starLowest_starsToP0`), and
  every cube obtained in this way from a leaf with at most `m - t` symbols `P₀` is a box
  (`isBox_starLowest`).


### `M_le_ten_pow`

 Section 4, "Notions from Section 2": "we will use that M = β₀ ≤ 10^L". The equation is
`beta_zero_eq_M`; this is the inequality. 

 ### Cubes and their leaves (Section 4.2) 

### `Cube.mem_leaves`

 Membership in the set of leaves of a cube, level by level. 

### `Cube.eq_of_mem_leaves`

 Where a cube has a term, its leaves have that term. 

### `Cube.mem_starLevels`

 Membership in the set of star levels of a cube. 

### `Cube.mem_P0Levels`

 Membership in the set of levels at which a cube has `P₀`. 

### `Cube.disjoint_starLevels_P0Levels`

 No level of a cube has both a star and `P₀`. 

### `symbolTerms`

 The terms that a leaf of a cube may have at a level with the given symbol. 

### `leaves_eq_piFinset`

 The leaves of a cube form a product set: the choices at the levels are independent. 

### `Cube.card_leaves`

 Section 4.2: "a cube with e stars has 10^e leaves". 

 ### A leaf as a cube without stars (Section 4.2) 

### `Cube.ofLeaf`

 Section 4.2: "a cube without stars is a single leaf"; this is the cube without stars whose
single leaf is `τ`. 

### `Cube.leaves_ofLeaf`

 The only leaf of the cube without stars made from `τ` is `τ`. 

### `Cube.starLevels_ofLeaf`

 The cube made from a leaf has no stars. 

### `Cube.P0Levels_ofLeaf`

 The cube made from a leaf has `P₀` where the leaf chooses `P₀`. 

 ### Replacing a star by a term (proof of Lemma 29) 

### `Cube.mem_leaves_replace`

 The leaves of `π[ℓ ← λ]`, for a star of `π` at level `ℓ`, are the leaves of `π` that choose `λ`
at level `ℓ`. 

### `Cube.starLevels_replace`

 Replacing a star by a term removes its level from the star levels. 

### `Cube.P0Levels_replace_subset`

 After a star is replaced by a term, the symbols `P₀` are at the old levels and possibly at the
level of that star. 

 ### Putting stars into a leaf (Section 4.2) 

### `Cube.starAt`

 The cube that agrees with the leaf `τ` except for stars at the levels of `F`. 

### `Cube.mem_leaves_starAt`

 `τ` is a leaf of the cube obtained from `τ` by putting stars at some levels. 

### `Cube.starLevels_starAt`

 The stars of `Cube.starAt F τ` are at the levels of `F`. 

### `Cube.P0Levels_starAt`

 The symbols `P₀` of `Cube.starAt F τ` are at the levels outside `F` at which `τ` chooses `P₀`.


### `Cube.starsToP0_starAt`

 If `τ` chooses `P₀` at the levels of `F`, then replacing the stars of `Cube.starAt F τ` with
`P₀` gives back `τ`. 

 ### The cube of an output string (Section 4.2)

Section 4.2 starts from this remark. Nothing else rests on it. 

### `cubeOf`

 Section 4.2: "the cube of w, the cube π^w that has a star at each level where w has z₀ (the
levels of Q) and the term P_ij at each level where w has z_ij". Here w is `η`, `Q` is its inner set,
and the term P_ij is the term of the private leaf of `η`. 

### `mem_leaves_cubeOf`

 Section 4.2: the leaves contributing to `η` "are the leaves of the cube of w". 

### `mul_apply_eq_val_cubeOf`

 Section 4.2: "Every output entry is the value of a cube": the leaves of the cube of `η` are
those contributing to `η`, "so that (X_Q Y_Q)[w] = val(π^w)", for the input arrays `a`, `b` built
from the matrices `X_Q`, `Y_Q` as in Section 2.3.3. 

 ### Replacing the stars of a cube with `P₀` (proof of Lemma 29) 

### `Cube.starsToP0_mem_leaves`

 The leaf obtained by replacing the stars of a cube with `P₀` is a leaf of the cube. 

### `Cube.starAt_starLevels_starsToP0`

 A cube is the leaf obtained by replacing its stars with `P₀`, with stars at the star levels of
the cube. 

### `Cube.eq_ofLeaf_of_starLevels_eq_empty`

 Section 4.2: "a cube without stars is a single leaf", namely the leaf `Cube.starsToP0 π`. 

### `P0Levels_starsToP0`

 The leaf obtained by replacing the stars of a cube with `P₀` chooses `P₀` where the cube has a
star or `P₀`. 

### `card_P0Levels_starsToP0`

 Proof of Lemma 29: the leaf obtained by replacing the stars of a cube with `P₀` chooses `P₀` at
as many levels as the cube has symbols `P₀` or stars. 

 ### A box only contains leaves of order at least `t` (Section 4.2) 

### `le_order_iff`

 Section 4.2: "the leaves of order at least t, i.e., the leaves that choose P₀ at most m - t
times". 

### `P0Levels_subset_of_mem_leaves`

 Section 4.2: "A leaf of π chooses P₀ at the f - e levels where π has P₀ and possibly at some of
its e star levels", and nowhere else. 

### `le_order_of_mem_leaves`

 Section 4.2: "so a box only contains leaves of order at least t". 

 ### The `k` lowest levels of a set (Section 4.2) 

### `lowest_subset`

 The `k` lowest levels of `S` are levels of `S`. 

### `mem_lowest`

 Membership in the set of the `k` lowest levels of `S`. 

### `card_below_strictMonoOn`

 The number of levels of `S` below a level of `S` grows strictly with the level. 

### `lowest_lt`

 Each of the `k` lowest levels of `S` is below every other level of `S`. 

### `eq_lowest_of_lt`

 A subset `T` of `S` all of whose levels are below all the other levels of `S` consists of the
`|T|` lowest levels of `S`. 

### `image_card_below`

 The numbers of levels of `S` below the levels of `S` are `0, …, |S| - 1`. 

### `card_lowest`

 The set of the `k` lowest levels of `S` has `min k |S|` elements. 

 ### Replacing the lowest symbols `P₀` of a leaf by stars (Section 4.2 and the proof of Lemma 29)


### `starLowest`

 Section 4.2: the cube "obtained from a leaf […] by replacing its e lowest symbols P₀ […] by
stars". 

### `starLevels_starLowest`

 The stars of `starLowest e τ` are at the `e` lowest levels at which `τ` chooses `P₀`. 

### `P0Levels_starLowest`

 The symbols `P₀` of `starLowest e τ` are at the other levels at which `τ` chooses `P₀`. 

### `starsToP0_starLowest`

 Replacing the stars of `starLowest e τ` with `P₀` gives back `τ`. 

### `eq_starLowest_starsToP0`

 Section 4.2: "By (ii), a box is obtained from a leaf of order at least t by replacing its e
lowest symbols P₀ (rather than an arbitrary subset of them) by stars." The leaf is
`Cube.starsToP0 π`, and only condition (ii) is used. 

### `isBox_starLowest`

 The converse: replacing the `e` lowest symbols `P₀` of a leaf with at most `m - t` symbols `P₀`
by stars gives a box. 
