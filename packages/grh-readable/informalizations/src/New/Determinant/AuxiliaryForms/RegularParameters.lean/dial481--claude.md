---
{
  "module": "src/New/Determinant/AuxiliaryForms/RegularParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/RegularParameters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/RegularParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weights of regular parameters and bounds on boxes

A weight is a pair `(κ, e)`: `κ w h` is the number of columns of height `h` at the place `w`, and
`e w` is the power of the determinant. `New.IsHCParam κ e l` says that `l w` lists twice the
Harish-Chandra parameter of `(κ, e)` in some order. This file finds a weight for each regular
parameter `l = 2λ` (`New.HCParam.HasGap`). It also bounds a weight by its parameter: the number of
boxes and the power of the determinant.

## Main definitions and results

* `New.Exchange.boxes_le_card_mul_of_isHCParam`, `New.Exchange.natAbs_le_of_isHCParam`: a bound `β`
  on the entries of `l` bounds the number of boxes and, for nonempty `n`, the determinant power.
* `New.Exchange.exists_isHCParam_of_hasGap`: every regular parameter comes from a weight;
  `New.Exchange.exists_isHCParam_of_le` adds control of the determinant power from below.

Notions from other files:
* `New.boxes κ N`: the number of boxes in the columns of height below `N`, over all places.


### `abs_hcParameter_le_of_isHCParam`

 If `l` is twice the Harish-Chandra parameter of the weight `(κ, e)` and `|l w i| ≤ β` for all
`i`, then `|hcParameter κ e (card n) w p| ≤ β` at every position `p < card n`. Here
`hcParameter κ e N w p` is the entry at the position `p`, counted from `0`, of twice the
Harish-Chandra parameter of `(κ, e)` at `w` in rank `N`. 

### `hcParameter_sub_one`

 Let `hcParameter κ e N w p` be the entry at the position `p`, counted from `0`, of twice the
Harish-Chandra parameter of the weight `(κ, e)` at `w` in rank `N`. For `0 < N` its last entry, at
the position `N - 1`, is `2 e w + 1 - N`. 

### `boxes_le_card_mul_of_isHCParam`

 If `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)` (`IsHCParam`), where
`κ w h` is the number of columns of height `h` at the place `w : Φ`, and `|l w i| ≤ β` for all `w`
and `i`, then `κ` has at most `card Φ * card n * β` boxes in columns of height below `card n`. 

### `natAbs_le_of_isHCParam`

 Let `n` be nonempty. If `l` is twice the Harish-Chandra parameter of the weight `(κ, e)` and
`|l w i| ≤ β` for all `i`, then the power of the determinant at `w` satisfies `|e w| ≤ β`. 

### `exists_eq_add_card_add_sum_Ioc`

 Let `v` be injective and `g ≤ v i` on a finite set `S`. There are column multiplicities `κ`,
equal to a given `f` above the height `#S`, such that each `v i` with `i ∈ S` is
`g + (κ (p + 1) + ⋯ + κ #S) + #S - 1 - p` for a position `p < #S`. 

### `exists_isHCParam_of_le`

 Let each `l w` be a parameter of gap `c` for the signs `s`, and let
`e w ≤ l w i / 2 + card n / 2` for all `i` (integer divisions). Then `l` is twice the Harish-Chandra
parameter of a weight with column multiplicities `f` and determinant power `e w + f w (card n)`. The
parameter sees only the columns of height below `card n` and the determinant power, so above that
height `f` can be prescribed, as `κ`. 

### `exists_isHCParam_of_hasGap`

 If every `l w` is a parameter of gap `c` for the signs `s` (in particular, its entries are
distinct and have the parity of `card n - 1`), then `l` is twice the Harish-Chandra parameter of
some weight `(κ, e)`. 
