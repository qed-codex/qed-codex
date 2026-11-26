---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Insert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Insert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Insert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Inserting a string into a trie (Lemma 29)

"inserting them into the trie also takes O(L) operations per box, and adds at most L vertices per
box."  New vertices are taken from the end of the part of the trie area that is in use, whose length
is kept in the cell fp.  No routine relies on what the free part of the area holds: the eleven cells
of a new vertex are cleared.  Addresses are relative to the base of the area, so the models are
`Spec.trieNew` and `Spec.trieInsert`.

1. `Ends.clearLoop` is the rule for the loop that clears cells.  `TrieMem.new` and `TrieMem.set`
   say what the trie area holds after a new vertex has been cleared and after a cell has been
   written.
2. `newRoot_spec`: a new vertex as a root.
3. `alloc_spec`: a new vertex as a child.  `Insertion.child` is the array after the test for the
   child, and `Insertion.Progress.step` says that the insertion goes on from the child in that
   array.
4. `insert_spec`: the loop goes down one level in each round (`Insertion.Inv`,
   `Insertion.round_spec`).


 ## Clearing cells 

### `clearLoop`

 Writes 0 into the cells from the address in local x up to, and not including, the address in
local y. 

### `Ends.clearLoop`

 **The rule for clearLoop.**  The loop clears the n cells from a and changes no local but x. 

### `seg_wrote_zero`

 The cells that have been cleared. 

 ## The trie area 

### `TrieMem.new`

 The trie area after a new vertex has been cleared behind the part in use and the free pointer
has been moved. 

### `TrieMem.set`

 Writing into a cell of the part of the trie area that is in use. 

 ## A new root 

### `Area`

 The local variables of newRoot: the arguments (the base of the trie area and the address of the
free pointer), the address of the new vertex, and the two ends of its cells in the memory.  Local 0
also takes the result. 

### `newRootBody`

 newRoot(area, free): take a new vertex from the end of the part in use, clear its cells, move
the free pointer, and return the address of the vertex. 

### `newRoot_spec`

 **newRoot** appends a new vertex to the array, and returns its address. 

 ## A new child 

### `Area`

 The local variables of insert: the arguments (the base of the trie area, the root, which becomes
the current vertex, the address of the string, its length, the value, the address of the free
pointer), the level, the address of the cell with the pointer to the child, and, for a new vertex,
its address and the two ends of its cells in the memory. 

### `allocStmt`

 A new vertex as the child in the current cell. 

### `tAlloc`

 The time of allocStmt. 

### `alloc_spec`

 The new vertex becomes the child in the cell q.  Only the last three locals change. 

 ## Insertion 

### `insertRound`

 One round: find the cell with the pointer to the child, make a new child if there is none, and
go down to the child. 

### `insertBody`

 insert(area, root, key, len, value, free): go down the string, making new children where there
are none, and write the value into the vertex that is reached. 

### `getD_trieNew_set`

 The pointer to a new child, read back from the array. 

### `child`

 The array after the test for the child in the cell q: a new vertex has been appended if there
was no child. 

### `Progress`

 After i levels the array is Ti and the current vertex p: what is left is the insertion of the
rest of the string from p. 

### `Progress.len`

 Each level has added at most one vertex. 

### `Progress.inside`

 The current vertex lies inside the array. 

### `Progress.step`

 One level down: in the array with the child, the pointer to the child is positive, and the
insertion goes on from the child. 

### `Inv`

 Before round i: the area holds an array Ti, the current vertex is p, and what is left is as
`Progress` says; outside the trie area nothing has changed. 

### `tRound`

 The time of a round: the cell, the test, a new vertex, and the step down. 

### `down_spec`

 The end of a round, once the area holds the array with the child: vertex := mem[cell].  The
conclusion has the form that the rule for counting loops asks for: the loop itself then raises the
level. 

### `round_spec`

 One round goes down one level, with a new child if there was none. 

### `insert_spec`

 **insert** stores the value for the string: the area then holds `Spec.trieInsert`. 
