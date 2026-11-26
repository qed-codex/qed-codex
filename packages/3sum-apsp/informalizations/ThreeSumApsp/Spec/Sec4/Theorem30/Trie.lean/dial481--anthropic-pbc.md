---
{
  "module": "ThreeSumApsp/Spec/Sec4/Theorem30/Trie.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/Trie.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec4/Theorem30/Trie.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tries in one array (Section 4.3)

"for each tile we store its boxes, with their values, in a standard trie on their strings of L
symbols.  Thus […] looking up or inserting a box, takes O(L) operations."  Here a string is a list
of L digits below 11, for the ten terms and the star.

All tries live in one array of integers and are numbered; the number of a trie is the number of its
tile.  A vertex is a block of eleven consecutive cells, one for each symbol, holding the address of
the child, or 0 if there is none; a vertex at depth L holds the value of its box in its first cell.
A box is stored if the pointers for its L symbols lead from the root of the trie to such a vertex
(`trieWalk`).  A new vertex is appended at the end of the array (`trieNew`).  The two operations
are `trieInsert` and `trieLookup`.

The interface is `TrieRep`: "the array holds tries with these roots and these stored values".  It
holds for an array without tries (`TrieRep.empty`), it is kept by a new trie (`TrieRep.new`) and by
an insertion (`TrieRep.insert`), and it says what a lookup returns (`TrieRep.lookup`).  `WalkOK` and
`InsertOK` say in addition that every address met on the way lies inside the array
(`TrieRep.walkOK`, `TrieRep.insertOK`).

The proof.  The pair (i, w) names the vertex of trie number i to which the prefix w leads.  The
invariant `TrieInv` gives every vertex its address nd (i, w), 0 if there is none.  `TrieRep` says
that such an nd exists, with nd (i, []) = roots i and the value v in the cell nd x for every entry
f x = some v.
1. Three steps keep the invariant: a new root, a new child, a value written at depth L
   (`TrieInv.newRoot`, `TrieInv.newChild`, `TrieInv.setVal`).  The first gives `TrieRep.new`.
2. An insertion is a sequence of new children and then one write.  Each step extends the tries
   (`TrieExt`): no vertex moves, no root appears, no value of another string changes.  `Inserted`
   collects what holds at the end, and `trieInsert_spec` proves it by induction on the rest of the
   string.  This gives `TrieRep.insert` and `TrieRep.insertOK`.
3. A lookup goes from the vertex of a prefix to the vertex of the next prefix (`trieWalk_spec`).
   This gives `TrieRep.lookup` and `TrieRep.walkOK`.


 ## The operations 

### `trieWalk`

 The vertex reached from the vertex p by following the symbols of a string. 

### `trieLookup`

 The value stored for a string in the trie with the given root (for a string that is stored; see
`TrieRep.lookup`). 

### `trieNew`

 The array with a new vertex (without children) at its end; its address is the old length. 

### `trieInsert`

 The array after storing the value v for a string, starting from the vertex p. 

### `WalkOK`

 Following a string from the vertex p, every vertex met is inside the array and every pointer
read is positive. 

### `InsertOK`

 An insertion of a string from the vertex p follows the array as it changes: every vertex met is
inside the array, and every pointer read is 0 or positive. 

### `length_trieNew`

 A vertex has eleven cells. 

### `length_trieInsert_le`

 An insertion adds at most one vertex for each symbol (proof of Lemma 29: "adds at most L
vertices per box"). 

 ## Arrays as functions 

### `cells`

 The cells of an array, as a function; beyond the end of the array it is 0. 

 ## The invariant 

### `TrieInv`

 The cells μ hold tries for strings of length L.  The pair (i, w) names the vertex of trie number
i for the prefix w, and nd (i, w) is its address, or 0 if there is no such vertex.  The vertices are
blocks of eleven cells in the region from lo to fr, the first free cell. 

### `TrieInv.child`

 The cell number a of a vertex above depth L points to the child for the symbol a. 

### `TrieInv.range`

 The vertices are aligned blocks between lo and fr. 

### `TrieInv.inj`

 Different prefixes have different vertices. 

### `TrieInv.closed`

 The parent of a vertex is a vertex. 

### `TrieInv.fresh`

 The cells from fr on are free. 

### `TrieInv.lo_pos`

 The address 0 means: no vertex. 

### `TrieInv.fr_aligned`

 The free region starts at a block boundary. 

### `inside`

 A vertex lies below the first free cell, and its address is not 0. 

### `cell_inj`

 The blocks of different vertices are disjoint. 

### `prefix_ne`

 The prefixes of a prefix that has a vertex have vertices. 

### `addVertex`

 A new vertex x at the address fr; its parent, if x is not a root, is a vertex already.  The
cells may change, as long as those from fr on stay free and the cells of the old vertices point to
the children, x among them. 

### `newRoot`

 A new trie number i: its root is a new vertex at the address fr. 

### `newChild`

 A new vertex for the prefix w ++ [a], at the address fr, with the pointer to it in the vertex
of w. 

### `setVal`

 Writing a value into the vertex of a string of full length. 

 ## Insertion 

### `TrieExt`

 The tries (μ', nd') extend the tries (μ, nd): no vertex moves, there is no new root, and the
value of every string other than x is kept. 

### `Inserted`

 T' with the vertices nd' is T with the vertices nd after the value v was stored for the string
x: the invariant holds, x has a vertex, the vertex holds v, and the tries have been extended. 

### `Inserted.of_step`

 An insertion after a step that extends the tries. 

### `TrieInv.inserted_set`

 The end of an insertion: the value is written into the vertex of the string. 

### `TrieInv.step_newChild`

 A step of an insertion where there is no child: a new vertex at the end of the array keeps the
invariant and extends the tries. 

### `trieInsert_spec`

 **Insertion.**  Below the vertex of the prefix w, the insertion of the rest of a string meets
only addresses inside the array, and it achieves what `Inserted` says. 

 ## Lookup 

### `trieWalk_spec`

 **Lookup.**  Following the symbols of a string whose vertex exists leads to that vertex, through
addresses inside the array. 

 ## The interface 

### `TrieRep`

 The array T holds, from the address lo on, tries number 0, 1, … for strings of L symbols.  The
root of trie number i is at the address roots i (0 if the trie does not exist yet), and every entry
f (i, key) = some v is stored: the string key has the value v in trie number i.  The array may hold
more than f lists. 

### `empty`

 An array without tries: any array of positive length.  The tries will be built behind it: lo is
its length. 

### `length_pos`

 The array is not empty: the address 0 means that there is no vertex. 

### `mono`

 Fewer stored values are a weaker claim. 

### `new`

 A new, empty trie number i. 

### `insert_spec`

 What `trieInsert_spec` says about an insertion from the root of trie number i. 

### `insert`

 Storing a value. 

### `insertOK`

 During an insertion, every cell read holds 0 or the address of a vertex inside the array. 

### `walk_spec`

 What `trieWalk_spec` says about the way from the root of trie number i down a stored string. 

### `lookup`

 Looking up a stored value. 

### `walkOK`

 On the way down a stored string, every cell read holds the address of a vertex inside the
array. 
