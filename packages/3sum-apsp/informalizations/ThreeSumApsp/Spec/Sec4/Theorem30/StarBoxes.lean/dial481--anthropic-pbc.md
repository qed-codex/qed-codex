---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/StarBoxes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/StarBoxes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/StarBoxes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The boxes with e stars, as a list (proof of Lemma 29)

"A box in which f of the symbols are P₀ or stars is obtained from a leaf of order m - f (namely the
leaf we get by replacing its stars with P₀) by turning the e lowest symbols P₀ of that leaf into
stars, for some e ≤ f."  So the boxes with exactly e stars are the leaves with between e and m - t
symbols P₀, with the first e digits 9 turned into 10: this is `starBoxes`.

The list contains exactly the boxes with e stars (`mem_starBoxes`, `exists_of_mem_starBoxes`), each
of them once (`starBoxes_nodup`), so it has as many members as there are such boxes
(`length_starBoxes`), and all lists together have as many members as there are boxes
(`sum_length_starBoxes`).

The lists are the order of work of Lemma 29: "We compute the values of the boxes in increasing order
of their number of stars", "Generating the boxes with e stars and inserting them into the trie".
All of them go into the trie of the tile.  The number of stars can be read off a box
(`starCount_of_mem_starBoxes`), so boxes from different lists are different strings, and a string
is a box exactly if it is in the list for its number of stars (`isBoxDigits_digitsC`).  There are
boxes with e stars only for e ≤ m - t (`le_of_mem_starBoxes`).  Replacing the highest star of a box
with e + 1 stars by a term gives a box with e stars (`exists_lastStar_of_mem_starBoxes`).


### `starBoxes`

 The boxes with e stars, as lists of digits. 

### `starFirst_mem_starBoxes`

 Box number i comes from leaf number i. 

### `exists_leaf_of_mem_starBoxes`

 A member of the list comes from a leaf with between e and m - t symbols P₀. 

### `mem_starBoxes`

 The list contains exactly the boxes with e stars. 

### `exists_of_mem_starBoxes`

 Every member of the list is a cube. 

### `starCount_of_mem_starBoxes`

 The number of stars can be read off a member of the list: the star is a symbol of its own, the
digit 10.  So boxes with different numbers of stars are different strings. 

### `IsBoxDigits`

 The string l is a box: it is in the list of the boxes with its number of stars. 

### `isBoxDigits_digitsC`

 A string of symbols is in the list of the boxes with its number of stars exactly if it is a
box. 

### `le_of_mem_starBoxes`

 There are boxes with e stars only for e ≤ m - t. 

### `starBoxes_digits`

 The members of the lists are strings of L digits below 11. 

### `exists_lastStar_of_mem_starBoxes`

 Replacing the highest star of a box with e + 1 stars by a term gives a box with e stars (proof
of Lemma 29). 

### `starBoxes_nodup`

 No box occurs twice in the list: turning the stars back into nines gives the leaf. 

### `length_starBoxes`

 The list has as many members as there are boxes with e stars. 

### `sum_length_starBoxes`

 All lists together have as many members as there are boxes (Lemma 29). 
