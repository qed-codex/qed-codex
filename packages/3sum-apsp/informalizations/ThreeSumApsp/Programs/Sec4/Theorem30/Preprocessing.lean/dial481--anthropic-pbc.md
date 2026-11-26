---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Preprocessing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Preprocessing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Preprocessing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The preprocessing of Theorem 30, at a given place of the memory

Proof of Theorem 30, "Preprocessing". The routine first runs the stage that it shares with
Theorem 5: the list of the subsets, the tables for the rows and columns, and the encodings of all
row bands and column bands. It notes t in the directory, computes the addresses of the areas of
Section 4 (preCoreAddr), starts the trie area with the array [0], and computes the values of all the
boxes of all tiles, by Lemma 29 (preCoreFinish). There is one lemma for each of the two named parts;
preCore_spec puts them behind the shared stage.


 ## The program 

### `Levels`

 The local variables of preCore: the arguments L, m, t, N, D, aX, aY, b0; a local for results
that are not used; the address of WD, the number nB, the addresses of CUR, BOX, FP, ROOTS, the
number m - t, and the address of TR. 

### `preCoreAddr`

 The addresses of the areas of Section 4, which lie one behind the other from WD on. 

### `preCoreFinish`

 The trie array starts as [0], of length 1; then the tries of all tiles. 

### `preCoreBody`

 preCore(L, m, t, N, D, aX, aY, b0) builds the data structure for the matrices at aX and aY in
the block from b0 on. 

### `preShared`

 What the locals hold after the shared stage; r is its result. 

### `preLocals`

 What the locals hold after the addresses have been computed. 

 ## The addresses 

### `preCoreAddr_spec`

 The addresses of the areas of Section 4 are computed as the map says. 

 ## The tries 

### `allArgs`

 The arguments of the call of allTiles, and the data behind them. 

### `allArgs_pre`

 The block, after the shared stage and with the trie array [0], holds what allTiles assumes. 

### `trieMem_start`

 The trie area with the array [0], after the two stores. 

### `preCoreFinish_spec`

 After the shared stage, the last part completes the data structure; it changes only cells from
CUR to the end of the block. 

 ## The routine 

### `preCore_spec`

 **preCore** meets its specification. 
