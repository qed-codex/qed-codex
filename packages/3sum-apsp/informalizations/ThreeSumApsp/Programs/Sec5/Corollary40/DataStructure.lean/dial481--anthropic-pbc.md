---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/DataStructure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/DataStructure.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/DataStructure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A data structure for the entries of a thin matrix product, placed anywhere in the memory

The proof of Corollary 40 uses the data structure of Corollary 26 (for τ < 1/18) and that of
Corollary 31 (for general τ) in the same way; the first is the second at c = 21, θ = 1/9.  A kit
(`DsKit`) collects what the phase programs of Corollary 40 use: the preprocessing
pre(N, D, aX, aY, fr) works on matrices at any addresses below fr and changes only the cells from fr
up to (not including) fr + size N D; the query query(I, J, N, D, aX, aY, fr) returns the entry
(XY)[I, J] and keeps the structure ready.

The kit is an interface: it keeps Section 4 out of the proofs about the phase programs.  It has one
instance, `kit31`.


### `KitInput`

 **What both routines of a kit are given**: matrices X and Y of sizes at least 1 with entries
bounded by U, the addresses aX and aY of their cells, which lie below the address fr of the
structure, and limits that suffice; `Lim` is the kit's condition on the limits. 

### `DsKit`

 **The kit**: a relocatable data structure for the entries of XY in the program P, at the
procedure numbers `Proc.pre31` and `Proc.query31`. 

### `DsKit.Ready`

 The cells from fr on hold what a query to XY needs; X and Y lie at aX and aY. 

### `DsKit.Lim`

 The limits that the two routines need, for a structure at fr and entries of absolute value at
  most U. 

### `DsKit.size`

 The number of cells of a structure. 

### `DsKit.depPre`

 The levels of calls that the preprocessing needs. 

### `DsKit.tPre`

 The time of the preprocessing. 

### `DsKit.tQ`

 The time of a query. 

### `DsKit.pre`

 The preprocessing makes the structure ready and changes only its cells. 

### `DsKit.query`

 A query returns the entry (I, J) of XY, keeps the structure ready and changes only its cells.
  

### `DsKit.ready_congr`

 What a query needs depends only on the cells of X, of Y, and on the cells from fr on. 

### `DsKit.Input`

 What both routines of the kit K are given. 

### `DsKit.Ready.keep`

 A structure stays ready if neither X, nor Y, nor the cells from fr on change. 

### `DsKit.basics`

 What the limits of a kit imply: an address fits in a word, so do the constants of the programs,
and the structure, of at least three cells, fits in the memory. 

 ## The lengths of the structures do not depend on where they lie, and are at least 3 

 ## The instance 

### `KitInput.input31`

 What the routines of the kit are given is what the routines of Corollary 31 are given. 

### `kit31`

 **The data structure of Corollary 31** with the parameters G, in the program for G followed by
further procedures R. 
