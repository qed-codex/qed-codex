---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/TileTries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/TileTries.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/TileTries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The trie of a tile, and the tries of all tiles (Lemma 29)

"Given the two encodings of a tile, we can compute the values of all these boxes, and store them in
the trie for that tile, in O(L) time and space per box."  `tileTrie` builds this trie.

"We compute the values of the boxes in increasing order of their number of stars": `fillUpTo` goes
through the boxes with 0, 1, … stars (`starBoxes`), and `fillTrie` inserts the boxes with e stars
with their values (`boxValue`): the value of a box without stars is "the product of its two numbers
in the encodings", the value of a box with stars is computed "with ten lookups in the trie" of the
tile.  `allTries` does this for all tiles, in one array; the number of a trie is the number of its
tile.  The array and the list of the roots form a record `TrieStore`.

What the array holds at a moment is a function from pairs (the number of a trie, a box) to values:
`storedUpTo` in the middle of a tile, `storedAll` between two tiles.
1. One more box is one more entry, the state after all boxes with k stars is the state before the
   first box with k + 1 stars, and a complete tile adds its boxes to `storedAll`
   (`storedUpTo_snoc`, `storedUpTo_succ`, `storedAll_snoc`).
2. Replacing the highest star of a box with e + 1 stars by a term gives a box with e stars
   (`exists_lastStar_of_mem_starBoxes`); so, once the boxes with e stars are stored, the value
   computed for the box is that of the dynamic program (`boxValue_eq`).
3. So the array represents these functions, in the sense of `TrieRep`, after some boxes with e stars
   (`fillTrie_rep`), after all boxes with fewer than k stars (`fillUpTo_rep`) and after some tiles
   (`allTries_rep`).
4. Hence a lookup returns the value of the dynamic program of Lemma 29 (`lookup_allTries`), which is
   the value of the box: the array holds "for every tile, the values of all its boxes"
   (`lookup_allTries_eq_val`).  Every box that a query reads is there (`boxesOf_mem_starBoxes`).
5. Space: "O(L) […] space per box" (`length_tileTrie_le`, `length_allTries_le`).
6. The bottom line, for any list of tiles: the query that reads the values of its boxes from the
   trie of its tile (`trieQuery`) returns `queryValue` (`trieQuery_allTries`), and all its walks
   down the trie are safe (`walkOK_allTries`).  The tiles of the product are `tileList`, and
   `tilesBefore` is its part before a tile.

Two ladders lead from the arrays to the paper.
* A query: `trieQuery` adds up `queryTerms` with the values read from the trie; these are the values
  of the dynamic program (`queryTerms_allTries`), with which the sum is `queryValue` on cubes
  (`sum_queryTerms_storedD`), which is `querySum`, the sum of Lemma 28 (`lemma_29_values`, inside
  `Theorem30.correct`), which is the entry `(X * Y) I J` (`Theorem30.query`).
* The value of a box: `boxValue` reads from the trie; it is `dpValueD` on lists of digits
  (`boxValue_eq`), which is `dpValue` on cubes (`dpValueD_digitsC`), which is `Cube.val`
  (`lemma_29_values`).  `lookup_allTries_eq_val` is the whole ladder; no other proof rests on it.


 ## Building the tries 

### `TileEnc`

 A tile, given by the arrays of its two encodings. 

### `TrieStore`

 The tries of some tiles in one array: the array, and the addresses of the roots.  The trie of
tile number i has the root number i. 

### `root`

 The address of the root of trie number i, or 0 if there is no such trie. 

### `lookup`

 The value stored for the string l in trie number i. 

### `Holds`

 The tries hold the entries of f, in the sense of `TrieRep`. 

### `new`

 A new, empty trie behind the others. 

### `root_new`

 The new trie has the next number, and its root is at the old end of the array. 

### `Holds.new`

 A new, empty trie changes no entry. 

### `boxValue`

 The value of a box l (the paper's π) with e stars, computed from the array T: for e = 0 "the
product of its two numbers in the encodings"; for e ≥ 1 the sum val(π) = ∑_λ val(π[ℓ ← λ]), where ℓ
is "the highest level at which π has a star", computed "with ten lookups in the trie" of the tile,
which has the given root.  The function looks only at whether e = 0. 

### `boxValue_zero`

 The value of a box without stars is the product at the leaf with its digits. 

### `fillTrie`

 "Generating the boxes with e stars and inserting them into the trie": the array after some boxes
with e stars have been inserted into the trie of the tile, which has the given root, each with its
value, computed from the array as it is before the box is inserted. 

### `fillUpTo`

 "We compute the values of the boxes in increasing order of their number of stars": the array
after the boxes with 0, …, k - 1 stars have been inserted, in this order, into the trie with the
given root. 

### `tileTrieUpTo`

 The tries s with a new trie that holds the boxes with fewer than k stars. 

### `tileTrie`

 Lemma 29: "Given the two encodings of a tile, we can compute the values of all these boxes, and
store them in the trie for that tile".  The trie is added to an array that may hold the tries of
other tiles already: a new root, and then all the boxes, which have at most m - t stars. 

### `allTries`

 The tries of all tiles in one array: the trie of tile number i has the number i.  Cell 0 is left
unused, since the address 0 means: no vertex. 

### `trieQuery`

 The query of Theorem 30.  For every box of the output string "we look up its value in the trie
of the tile", which has the given root. 

### `allTries_snoc`

 The trie of one more tile is built on top of the tries of the tiles before it. 

### `boxesOf_mem_starBoxes`

 Every box that a query reads is a box of the tile. 

 ## What the tries hold 

### `storedUpTo`

 What the tries hold in the middle of tile number i: on top of the entries old, trie number i
holds the boxes with fewer than k stars and the boxes in pre (some boxes with k stars).  The entry
for the key (i, l) is the value `storedD encA encB l` of the dynamic program. 

### `storedAll`

 What the tries of all tiles hold, the third component of the data structure: "for every tile,
the values of all its boxes (the boxes are the same strings in every tile, but their values depend
on the input arrays of the tile)".  Trie number i holds the values of all boxes for tile number i.
The array holds at least these entries (`allTries_rep`, in the sense of `TrieRep`). 

### `storedUpTo_of_lt`

 The boxes with fewer than k stars are stored with the values of the dynamic program. 

### `storedUpTo_zero`

 Before the first box, there are the old entries only. 

### `storedUpTo_snoc`

 One more box is one more entry. 

### `storedUpTo_succ`

 The state after all boxes with k stars is the state before the first box with k + 1 stars. 

### `storedAll_of_mem`

 The boxes of tile number i are stored with the values of its dynamic program. 

### `storedAll_snoc`

 One more tile: what is stored then was stored before or belongs to the new tile. 

 ## The array represents what it should hold 

### `boxValue_eq`

 With the boxes with fewer stars stored, the value computed for a box is the value of the dynamic
program. 

### `fillTrie_rep`

 Inserting boxes with e stars into the trie of the tile: if the array represents the state after
the boxes of pre, then after inserting the boxes of rest it represents the state after
pre ++ rest. 

### `fillUpTo_rep`

 After k rounds the trie of the tile holds the values of the dynamic program for the boxes with
fewer than k stars, and the older entries are kept. 

### `length_roots_allTries`

 There is one root for each tile. 

### `allTries_rep`

 The tries of all tiles hold the values of the dynamic programs of the tiles. 

### `lookup_allTries`

 Looking up a box of tile number i. 

### `lookup_allTries_eq_val`

 **Lemma 29**, and the third component of the data structure: "for every tile, the values of all
its boxes".  The trie of tile number i, which is given by the encodings of its two input arrays a
and b, holds for every box its value. 

 ## Space 

### `length_fillTrie_le`

 Inserting boxes "adds at most L vertices per box". 

### `length_fillUpTo_le_sum`

 The boxes with fewer than k stars take at most 11 L n cells, where n is their number. 

### `length_tileTrie_le`

 Lemma 29, space: "O(L) […] space per box"; eleven cells more for the root. 

### `length_allTries_le`

 All tiles together: cell 0, and for each tile the space of Lemma 29. 

 ## The list of all tiles 

### `tileList`

 The tiles in row-major order, each given by the arrays of its two encodings: tile (β, β') has
the number β nB + β'. 

### `length_tileList`

 There are nB² tiles. 

### `getElem`

 Tile (β, β') has the number β nB + β'. 

### `tilesBefore`

 The tiles before the tile (β, β'), in row-major order. 

### `tilesBefore_zero`

 No tile stands before the first one. 

### `tilesBefore_succ`

 The tiles before the next tile of the row are the tiles before the tile, and the tile. 

### `tilesBefore_row`

 The end of a row is the beginning of the next one. 

### `tilesBefore_all`

 After the last row all tiles have been taken. 

### `length_tilesBefore`

 β nB + β' tiles stand before the tile (β, β'). 

 ## What the tries of all tiles give to a query

The query for tile number i gets the root of the trie of this tile. 

### `walkOK_allTries`

 Every box of the query is stored: the walk down the trie is safe. 

### `queryTerms_allTries`

 The numbers that the query adds up, read from the trie, are those of the dynamic program. 

### `trieQuery_allTries`

 **The query on the tries of all tiles** returns the value of the query of the proof of
Theorem 30, which is the entry of the product (`Theorem30.correct`). 
