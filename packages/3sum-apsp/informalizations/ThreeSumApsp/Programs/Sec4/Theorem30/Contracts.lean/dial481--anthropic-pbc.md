---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Contracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Contracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Contracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 in the light language: procedure numbers, time functions, specifications

This file contains no program, and its only proof is a short remark on the trie area when other
cells change. It states the specifications of the procedures 40 to 53 (`nineFirst` to `queryCore`).
The proof of a routine uses only the specifications of the routines that it calls.

* A routine takes its scalars and the base addresses of its arrays as arguments; no routine but
  `preCore` and `queryAt` knows the memory map. The routines for a tile assume the order in which
  their areas lie (`TileCtx.layout`).
* The specification of a routine is a proposition XSpec lim P: "procedure number Proc.x of the
  program P, started on these arguments in a memory that satisfies this, ends within tX steps with
  this result in a memory that satisfies that". The file of x proves XSpec for every program P that
  holds the body of x at the number Proc.x and meets the specifications of the routines that x
  calls. A caller assumes XSpec and feeds it to the rule for calls. XSpec holds at every depth d of
  calls that leaves the levels which x needs below itself.
* Conventions of the programs: the result of a procedure is what it leaves in its local 0; locals
  that are not arguments start at 0. In the proofs, lines such as "have hw := C.std.space_le" or
  "obtain ⟨⟩ := areas p t b0" state the facts on the limits and on the map that the later steps use.
* The larger routines have two records: XArgs holds the arguments and the data behind them, and
  XPre lim μ x says what the routine assumes about the limits and the memory.
* The pure models are those of the specifications of Section 4 (strings are lists of digits, level 1
  first: P_ij is 3(i - 1) + (j - 1), P₀ is 9, the star is 10).
* Time functions are definitions. The time function of a caller is written in terms of the time
  functions of its callees. Their constants are upper bounds, some with room to spare; only the
  shape matters. The lemmas `within8_tAllTiles` and `exists_tQueryCore_le` compare `tAllTiles` and
  `tQueryCore` with the expressions (8) and L ∑ α_d of the paper.
* Tries use addresses relative to the base tr of the trie area: the cell tr + a of the memory is the
  cell a of the trie array T. The area has cap cells, of which the first T.length are in use;
  nothing is assumed about the others (a new vertex clears its eleven cells); the number T.length
  is kept in the cell fp outside the area.

The routines, the pure functions that model them, and the lemmas that say what the models compute:

| number | routine | model | what is proved about the model |
|---|---|---|---|
| 40 | `nineFirst` | `nineFirst` | `head?_nineStrs`: it is the first string of `nineStrs` |
| 41 | `nineNext` | `nineNext` | `nineNext_getElem`: from string i of `nineStrs` to string i + 1 |
| 42 | `scatter` | `scatter`, `starRunIf` | `lowList` and `boxesOf` are built from them |
| 43 | `starFirst` | `starFirst`, `lastStar` | `starBoxes` is `nineStrs` mapped by `starFirst` |
| 44 | `horner` | `ofDigitList 10` | `ofDigitList_digitsT`: the code of a leaf |
| 45 | `lookup` | `trieLookup` | `TrieRep.lookup`, `TrieRep.walkOK` |
| 46 | `insert` | `trieInsert` | `TrieRep.insert`, `TrieRep.insertOK` |
| 47 | `newRoot` | `trieNew` | `TrieRep.new` |
| 48 | `sumTen` | sum of `tenValues` | `exists_lastStar_of_mem_starBoxes`, `abs_dp_partial_sum_le` |
| 49 | `fillList` | `fillTrie` | `fillTrie_rep`, `length_fillTrie_le` |
| 50 | `tile` | `tileTrie` | `fillUpTo_rep`, `length_tileTrie_le` |
| 51 | `allTiles` | `allTries` | `allTries_rep`, `length_allTries_le`, `lookup_allTries` |
| 52 | `outDigits` | `OutDigitsArgs.digits` | `digitsO_outStrOfPos`: the string of a position |
| 53 | `queryCore` | `trieQuery`, `queryTerms` | `trieQuery_allTries`, `abs_query_partial_sum_le` |

The last line of the table continues with `Theorem30.correct`. The model `boxValue` is computed by a
part of `fillList`, which calls `sumTen` for a box with stars.


 ## Vocabulary 

### `TrieMem`

 The trie area of cap cells from tr: its first cells hold the array T, and the cell fp holds the
length of T. Nothing is assumed about the rest of the area. 

### `TrieMem.keep`

 The trie area stays as it is if its cells and the cell fp do not change. 

### `SameOutsideTrie`

 The memory μ' agrees with μ outside the trie area and the cell fp. 

 ## Procedure numbers

The numbers 0 to 39 belong to Section 2, the numbers from 40 on to Section 4. This file fixes 40 to
53; the files of the other routines of Section 4 fix theirs. 

### `nineFirst`

 The numbers of the fourteen routines, in the order in which they call each other. 

 ## Time functions 

### `tNineFirst`

 The routines with one loop over a string of n or L digits: a constant number of steps for each
digit. 

### `tNewRoot`

 Eleven cells are cleared. 

### `tSumTen`

 Ten times: write a digit, look up, add. 

### `tFillRound`

 A round for one box: stars, value (both branches are paid for), insertion, next leaf. 

### `tFillStep`

 One box: the test of the loop and a round. 

### `tFillList`

 The boxes with a given number of stars, cnt of them. 

### `tTile`

 The trie of a tile: its root, then the boxes with 0, …, m - t stars. 

### `tAllTiles`

 All tiles. 

### `tQueryCore`

 A query, once the digits of its output string are known. 

 ## The enumeration of the strings with a bounded number of nines 

### `NineFirstSpec`

 nineFirst(a, n, lo) writes the least string of n digits with lo nines. 

### `NineNextSpec`

 nineNext(a, n, lo, hi) replaces the string at a by the next one and returns 1, or leaves it and
returns 0 if it is the last one. 

 ## Strings 

### `ScatterSpec`

 scatter(w, s, out, L, star) writes at out the string at w with its nines replaced by the digits
of the string at s, whose leading nines are first turned into stars if star = 1. 

### `StarFirstSpec`

 starFirst(cur, box, L, e) writes at box the string at cur with its first e nines turned into
stars; it returns the position of the last star (0 if e = 0). 

### `HornerSpec`

 horner(a, L) returns the number with the L decimal digits at a, most significant first. 

 ## Tries 

### `LookupSpec`

 lookup(tr, root, key, L) returns the value stored for the string at key in the trie with the
given root. 

### `InsertArgs`

 The arguments of insert(tr, root, key, L, val, fp), and the data behind them: the trie area of
cap cells at tr holds the array T, the cell fp holds its length, and the string kl is at key. 

### `InsertArgs.vals`

 The values of the arguments of `insert`. 

### `InsertPre`

 What `insert` assumes: the tries and the string are in the memory, the walk down the string is
safe, there is room for one new vertex at each level, the string lies apart from the trie area and
from the free pointer, and everything lies within the memory. 

### `InsertSpec`

 insert(tr, root, key, L, val, fp) stores val for the string at key in the trie with the given
root. A new vertex is taken from the free part of the trie area, and its eleven cells are
cleared. 

### `NewRootSpec`

 newRoot(tr, fp) takes a new vertex from the free part of the trie area, clears its eleven cells,
and returns its address. 

 ## The dynamic program of Lemma 29 

### `SumTenArgs`

 The arguments of sumTen(tr, root, box, L, p), and the data behind them: the array T of the tries
is at tr, and the string l, which has a star at the position p, is at box. 

### `SumTenArgs.vals`

 The values of the arguments of `sumTen`. 

### `SumTenArgs.values`

 The ten values that `sumTen` adds up. 

### `SumTenPre`

 What `sumTen` assumes: the array of the tries and the box, which do not meet and lie within the
memory, the position of the star, that the ten strings are stored, and that the partial sums of
their values fit in a word. 

### `SumTenSpec`

 sumTen(tr, root, box, L, p) returns the sum of the ten values, looked up in the trie with the
given root, of the strings obtained from the string at box by writing 0, …, 9 at the position p; it
leaves the memory as it was. 

### `TileCtx`

 What the routines for a tile assume about their surroundings: the parameters, the two encodings
of the tile and where they are, the trie area, two scratch strings, and the limits. 

### `TileCtx.value_le`

 Every value and every partial sum fits in a word. 

### `TileCtx.layout`

 The two encodings, the two scratch strings, the cell fp and the trie area lie in this order,
  and the last cell of the memory lies behind them. 

### `SameOutsideTile`

 The memory μ' agrees with μ outside the trie area, the cell fp, and the two scratch strings. 

### `FillListArgs`

 The arguments of fillList(e, root, aA, aB, tr, fp, cur, box, L, mt), with mt = m - t, and the
data behind them: the encodings encA and encB of the tile are at aA and aB; the trie area of cap
cells at tr holds the array T, and fp holds its length; cur and box (L cells each) are scratch. The
array is described as in `fillTrie_rep`: tile is the number of the trie (the number of the tile),
roots tile its root, old what the other tries hold, and lo the address from which the tries stand
in the array. 

### `root`

 The root of the trie of the tile. 

### `vals`

 The values of the arguments of `fillList`. 

### `boxes`

 The boxes that `fillList` inserts. 

### `stored`

 What the tries hold when the boxes in pre have been inserted. 

### `FillListPre`

 What `fillList` assumes: the surroundings of a tile, a trie that holds the boxes with fewer
stars, the tries and the two encodings in the memory, and room for L vertices for each box. 

### `FillListSpec`

 fillList(e, root, aA, aB, tr, fp, cur, box, L, mt), with mt = m - t, inserts the boxes with e
stars, with their values, into the trie of the tile, which has the given root and holds the boxes
with fewer stars; for e ≥ 1 the values are sums of ten values looked up in it. 

### `TileArgs`

 The arguments of tile(aA, aB, ra, tr, fp, cur, box, L, mt), with mt = m - t, and the data behind
them: the encodings encA and encB of the tile are at aA and aB; the trie area of cap cells at tr
holds the tries s.cells of the earlier tiles, in which the values old are stored, and fp holds their
length; their roots s.roots, one for each tile, are in the cells from aR, and ra is the address of
the cell behind them; cur and box (L cells each) are scratch; the tries stand in the trie array from
the address lo on. 

### `TileArgs.tries`

 The trie array and the roots after the trie of the tile has been built. 

### `TileArgs.cells`

 The number of cells for the roots, the older ones and the new one. 

### `TileArgs.Kept`

 The cells that `tile` keeps: those outside the trie area, the cell fp, the two scratch strings
and the cell of the new root. 

### `TilePre`

 What `tile` assumes: the surroundings of a tile, the older tries and roots and the two encodings
in the memory, room for the new trie, and the place of the cells of the roots. 

### `TilePre.rootsPlace`

 The cells of the roots lie between the cell fp and the trie area. 

### `TileSpec`

 `tile` builds the trie of one tile, with the values of all its boxes, on top of the older tries,
and writes its root into the cell behind the older roots. It changes only the trie area, the cell
fp, the two scratch strings and this cell. 

### `AllTilesArgs`

 The arguments of allTiles(aENCA, aENCB, nB, T, aR, tr, fp, cur, box, L, mt), with T = 10^L and
mt = m - t, and the data behind them: the encodings of the nB row bands from aENCA and of the nB
column bands from aENCB (band β at the offset β 10^L), the cells of the roots from aR (one for each
tile), the trie area of cap cells from tr, the cell fp for its length, and two scratch strings cur
and box. 

### `AllTilesArgs.tries`

 The tries of all tiles, and their roots. 

### `AllTilesArgs.Kept`

 The cells that `allTiles` keeps: those below cur and those behind the trie area. 

### `AllTilesPre`

 What `allTiles` assumes: the limits, room in the trie area for the tries of all tiles, the order
of the areas, the encodings in the memory, and the trie array [0]. 

### `AllTilesPre.value_le`

 Every value and every partial sum fits in a word. 

### `AllTilesPre.order`

 The areas lie in this order, without overlap, below the end of the memory. 

### `AllTilesSpec`

 `allTiles` builds the tries of all tiles, starting from the trie array [0], and changes nothing
below cur or behind the trie area. 

 ## A query 

### `OutDigitsArgs`

 The arguments of outDigits(gI, gJ, dI, dJ, aMASK, K0, L, wd) and the data behind them: gI and gJ
are the numbers of the blocks of I and J within their bands, dI and dJ the addresses of the base-3
digits rI and rJ of their offsets, aMASK the address of the list of the subsets (a mask of L cells
for each), k0 the number of blocks of a band, L the number of levels, m of which belong to a subset,
and wd the address of the result. 

### `mask`

 The mask of the subset of the block product (gI, gJ). 

### `base`

 The address of that mask in the list of the subsets. 

### `digits`

 The digits of the output string: 9 at the levels of the subset, and elsewhere 3 a + b for the
next digits a of rI and b of rJ. 

### `OutDigitsPre`

 What `outDigits` assumes: the mask of the subset and the digits of the two offsets stand in the
memory, and the L cells from wd are apart from all three. 

### `OutDigitsSpec`

 `outDigits` writes the digits of the output string at wd and changes nothing else. 

### `QueryCoreArgs`

 The arguments of queryCore(aA, aB, tr, root, wd, ss, box, L, m, t) and the data behind them: the
encodings encA and encB of the tile are at aA and aB, the trie array T at tr, root is the root of
the trie of the tile, the digits of the output string η are at wd; ss (m cells) and box (L cells)
are scratch. 

### `QueryCoreArgs.terms`

 The numbers that the query adds up, in the order in which it adds them. 

### `QueryCorePre`

 What `queryCore` assumes: the data stand in the memory, every box of the query is found in the
trie of the tile, all partial sums fit in a word, and the two scratch strings are apart from each
other and from the data. 

### `QueryCoreSpec`

 `queryCore` returns the sum `trieQuery` for the output string whose digits are at wd: the
products at its leaves of order below t, read from the two encodings, and what the trie with the
given root holds for its boxes. This is the sum of Lemma 28 if the trie holds the values of the
boxes (`trieQuery_allTries`). The routine changes only the two scratch strings. 
