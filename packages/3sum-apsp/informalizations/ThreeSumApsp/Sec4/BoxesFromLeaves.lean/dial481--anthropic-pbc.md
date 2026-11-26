---
{
  "module": "ThreeSumApsp/Sec4/BoxesFromLeaves.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/BoxesFromLeaves.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/BoxesFromLeaves.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The boxes of an output string, from its leaves of order exactly `t` (Section 4.2)

Let `η` be an output string (the paper's w) with inner set `Q` of `m` levels. The boxes of `η` are
the cubes of the sets `𝓑_V`, over all `V ⊆ Q` with `|V| = m - t`. This file proves two passages of
the running text of Section 4.2 about them.

* *Every box of `η` has exactly `m - t` symbols that are `P₀` or stars*
  (`card_starLevels_add_card_P0Levels`).
* *The second description.* Take a leaf of order exactly `t` contributing to `η` and replace its
  `P₀` by a star at every level of `Q` below the lowest level of `Q` at which it chooses another
  term, or at every level of `Q` if `t = 0` (`starBelow`). For such a leaf this is the box of the
  leaf (`boxOfLeaf_eq_starBelow`), so it is a box of `η` (`starBelow_mem`). Replacing the stars with
  `P₀` gives the leaf back (`starsToP0_starBelow`), and it turns every box of `η` into a leaf of
  order exactly `t` contributing to `η` (`starsToP0_of_mem`). So each box of `η` arises exactly once
  (`existsUnique_starBelow_eq`).


### `card_starLevels_add_card_P0Levels`

 Section 4.2: "the boxes of an output string all have exactly m - t symbols that are P₀ or
stars." 

### `starBelow`

 Section 4.2, for a leaf `τ` of order exactly `t` contributing to `η`: "consider the lowest level
of Q at which it chooses a term other than P₀, and replace its P₀ by a star at every lower level of
Q (or at every level of Q, if t = 0)." With `Z` the set of the levels of `Q` at which `τ` chooses
`P₀`, these lower levels are those of `F_Z`, which is all of `Q` if `Z = Q`. 

### `card_Zof_eq`

 A leaf of order exactly `t` contributing to `η` chooses `P₀` at exactly `m - t` levels. 

### `Vof_eq_self`

 A set `Z` of `m - t` levels needs no padding: `V = Z`. 

### `boxOfLeaf_eq_starBelow`

 For a leaf of order exactly `t` contributing to `η`, the cube of the second description is the
box of the leaf. 

### `mem_leaves_starBelow`

 A leaf is a leaf of the cube of the second description. 

### `starBelow_mem`

 Section 4.2: "The result is a box of w". 

### `starsToP0_starBelow`

 The stars of `starBelow η τ` stand where `τ` chooses `P₀`, so replacing them with `P₀` gives `τ`
back. 

### `starsToP0_of_mem`

 Replacing the stars of a box of `η` with `P₀` gives a leaf of order exactly `t` contributing to
`η`. 

### `existsUnique_starBelow_eq`

 Section 4.2: "each box of w arises exactly once in this way", from the leaves of order exactly
`t` contributing to `η`. 
