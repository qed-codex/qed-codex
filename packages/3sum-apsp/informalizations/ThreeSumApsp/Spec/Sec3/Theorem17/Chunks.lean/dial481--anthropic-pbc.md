---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Chunks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Chunks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Chunks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of the chunks (proof of Theorem 17)

"For ϱ ∈ ℤ_p let W_ϱ be the set of edges (a,b) ∈ A × B with w(a,b) ≡ ϱ (mod p), and cut it into
chunks of at most n²/√D query pairs."  The routine lists the pairs class after class (`sortedIdx`).
Then a class is a segment of the list, from `classStart ϱ` to `classStart (ϱ + 1)`, and a chunk is a
segment of a class.  The table `chunkTab` has one entry for each chunk: its residue, the place where
it starts, and its number of pairs.

* The list has every pair once (`sortedIdx_nodup`, `classStart_eq_sq`), and the places of a class
  hold pairs of that class (`getD_sortedIdx_class`).
* An entry of the table is a nonempty segment of at most `cap` places (`chunkTab_entry`) whose pairs
  have the residue of the entry (`chunkTab_class`).
* The chunks follow each other (`chunkTab_pairwise`), so every place lies in exactly one chunk
  (`chunkTab_cover`, `chunkTab_unique`).
* "There are at most p + √D ≤ 2√D chunks in all" (`length_chunkTab_le`).


 ## The classes and the list of all the pairs 

### `classIdx`

 The places `a n + b` of the pairs of the class `W_ϱ`, in increasing order; `RAB` holds the
residues. 

### `sortedIdx`

 All the places, class after class. 

### `queryRows`

 The rows of the pairs, class after class. 

### `queryCols`

 The columns of the pairs, class after class. 

### `mem_classIdx`

 The places of a class. 

### `lt_of_mem_sortedIdx`

 The list holds places of pairs. 

### `sortedIdx_nodup`

 No pair is listed twice. 

 ## The starts of the classes 

### `classStart`

 The place where the class `rho` starts: the number of pairs with a residue below `rho`. 

### `classStarts`

 The table of the places where the classes start: entry `ϱ ≤ p` is `classStart n RAB ϱ`. 

### `classStart_succ`

 The next class starts where the class ends. 

### `classStart_mono`

 Later classes start later. 

### `getD_classStarts_eq`

 The list `classStarts` holds the starts of the classes. 

### `length_sortedIdx_eq`

 The list of all the pairs ends where the class `p` would start. 

### `classStart_eq_length_filter`

 The class `p` starts after the pairs with a residue below `p`. 

### `classStart_eq_sq`

 All the pairs are listed if all the residues are below `p`. 

### `exists_class`

 A place below the start of the class `p` lies in one of the classes before. 

### `getD_sortedIdx_class`

 The places from the start of the class `rho` to the start of the next class hold pairs with the
residue `rho`. 

 ## The chunks 

### `Chunk`

 A chunk: a segment of the list of all the pairs that lies within one class. 

### `Chunk.residue`

 The residue of the class. 

### `Chunk.start`

 The place in the list where the chunk starts. 

### `Chunk.len`

 The number of places of the chunk. 

### `Chunk.Contains`

 The place `j` lies in the chunk. 

### `Chunk.Fits`

 The chunk has a residue below `p`, and it is a nonempty segment of at most `cap` of the `n²`
places. 

### `chunksOf`

 The segment `[lo, hi)` of the class `rho`, cut into chunks of `cap` places; the last one may be
shorter. 

### `chunkTabOf`

 The chunks of `p` segments, of which number `rho` goes from entry `rho` to entry `rho + 1` of
the list `C`. 

### `chunkTab`

 The table of the chunks, with one entry for each chunk of each class. 

### `chunkAt`

 Chunk number `i` of the class `rho`. 

### `chunkTab_eq`

 The table, in terms of the starts of the classes. 

### `mem_chunkTab`

 The entries of the table: chunk number `i` of the class `rho`. 

### `chunkTab_entry`

 An entry of the table has a residue below `p`, and it is a nonempty segment of at most `cap`
places of the list. 

### `chunkTab_class`

 The pairs of a chunk have the residue of its entry. 

### `chunkTab_pairwise`

 The chunks follow each other: a chunk ends where a later one starts, or before. 

### `chunkTab_cover`

 Every place lies in a chunk. 

### `chunkTab_unique`

 A place lies in one chunk only. 

### `length_chunkTab`

 The number of chunks, class by class. 

### `length_chunkTab_le`

 Proof of Theorem 17: "There are at most p + √D ≤ 2√D chunks in all", in the form: at most `p +
n²/cap`. 
