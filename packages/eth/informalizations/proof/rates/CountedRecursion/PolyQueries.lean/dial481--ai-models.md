---
{
  "module": "proof/rates/CountedRecursion/PolyQueries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyQueries.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyQueries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The plain functions of the procedure

Every plain function of GridProcedures.lean is polynomial-time jointly in all that it reads. K, g,
λ, B are lengths of lists in the context, so they are given in unary; the counter of a loop, the
numbers of the rows, the pattern y and the grouping x are given in binary. 

 ### The parts of a parent and of a context 

 K, g, the caller's λ and B are lengths of lists, so they are given in unary (and are
polynomial-time); the lists, the direction, y and x are read off. 

### `pK_unary`

 K is given in unary. 

### `pG_unary`

 g is given in unary. 

### `pLam_unary`

 The caller's λ is given in unary. 

### `pB_unary`

 The caller's B is given in unary. 

### `pK_polyT`

 K is polynomial-time. 

### `pG_polyT`

 g is polynomial-time. 

### `pLam_polyT`

 The caller's λ is polynomial-time. 

### `pB_polyT`

 The caller's B is polynomial-time. 

### `pLists_polyT`

 The lists are read off. 

### `pTr_polyT`

 The direction is read off. 

### `pY_polyT`

 The number of the pattern is read off. 

### `pX_polyT`

 The number of the grouping is read off. 

### `parentOf_polyT`

 The parent of a context. 

### `cLam_unary`

 The label length of a context is given in unary. 

 ### The queries 

### `pointQuery_polyT`

 The entry of the caller's tables at a grid point. 

### `toTable_polyT`

 A setting as one string. 

### `ordered_polyT`

 The smaller row first. 

### `straightOK_polyT`

 The test of the straight edges between two rows. 

### `rectStrings_polyT`

 The four strings of a rectangle. 

### `pieceAt_polyT`

 ι(q). 

### `colDiv_polyT`

 The two columns j / g and j % g of the rectangle number j of a loop. (Written out by hand: on «j
/ g» with g the length of a list, `fun_prop` runs out of time.) 

### `colMod_polyT`

 The second column, j % g. 

### `isRect_polyT`

 The number j names a rectangle when j / g < j % g. 

### `rectQuestion_polyT`

 The question for a rectangle in Ψ. 

### `labelOK_polyT`

 The test of the straight edges against a label. 

### `factorQuestion_polyT`

 The question for a rectangle in a function of a factorization. 

 ### The numbers of the network, and what the callee's query becomes 

### `netP_unary`

 P = g³λ is given in unary. 

### `netB_unary`

 B₁ is given in unary. 

### `netLen_unary`

 P_a is given in unary. 

### `netCap_unary`

 c_{a,a'} is given in unary. 

### `inputOf_polyT_data`

 What an algorithm for networks is given (`Printed.inputOf`: P, B and the numbers P_a, c_{a,b},
in unary) is written down in polynomial time from numbers given in unary, the number g of nodes
among them. 

### `netData_polyT`

 K, g and what an algorithm for networks is given, for the network of a parent. 

### `toLists_polyT_data`

 Cutting a setting into its K − 1 strings of λ bits, for K given in unary. 

### `calleeInput_polyT`

 From the callee's context and its query to the context of the four procedures and the input of
`entryData`. 
