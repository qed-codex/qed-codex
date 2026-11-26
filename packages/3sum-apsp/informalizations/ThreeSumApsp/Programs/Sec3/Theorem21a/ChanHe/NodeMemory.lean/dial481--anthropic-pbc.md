---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeMemory.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM: the memory of a node, and what fits in a word

What the routines below the recursion tree of [CH20, Theorem 5.1] share (for
Theorem 21(a)).

* A set in the memory (`SetAt`), the memory of a node (`NodeMem`) and the block of parameters
  (`CtxAt`) only depend on cells below the free pointer (`SetAt.kept`, `NodeMem.kept`,
  `CtxAt.kept`).
* Each of the three sets, with the count table, is what coll and heavy ask for (`Slot.Ok.bucket`).
* A child of a node has the heavy elements of one of the three sets in place of that set
  (`NodeArgs.child₁`, `child₂`, `child₃`; `NodeMem.child₁`, `child₂`, `child₃`).
* The bound `wordNeed` on the words is monotone in n and M (`wordNeed_mono`) and covers every
  product of a number up to (n + 1)², a number up to M + 1 and a number up to 64 (V + 1)
  (`mul_le_wordNeed`; `mul_le_word` and `le_word_of_le` are the forms that the routines use).


 ## The memory 

### `SetAt.kept`

 A set below the free pointer is still there if no cell below the free pointer has changed. 

### `SetAt.card`

 The length of a set in the memory is its number of elements. 

### `SetAt.eq_empty`

 A set of length 0 is empty. 

### `card_heavy_le`

 There are at most as many heavy elements as elements. 

### `Env.Ok.kept`

 The primes and the count table only depend on the cells below the free pointer. 

### `Slot.Ok.kept`

 A set of a node only depends on the cells below the free pointer. 

### `NodeMem.kept`

 What a node needs in the memory only depends on the cells below the free pointer. 

### `Slot.Ok.bucket`

 A set of a node with the count table, as coll and heavy want them. 

 ### The children of a node

A child has the heavy elements of one of the three sets in place of that set.  They are written at
the free pointer, which moves on by the length of the set. 

### `Env.push`

 What the routines share, after `len` cells from the free pointer have been taken. 

### `Slot.heavy`

 The heavy elements of a set modulo `M`, at the address `fr`. 

### `NodeArgs.push`

 A node, after `len` cells from the free pointer have been taken. 

### `NodeArgs.child₁`

 The three children of a node with the modulus `M`. 

### `Env.Ok.push`

 The primes and the count table are not touched when cells from the free pointer on are
written. 

### `Slot.Ok.push`

 A set of a node is not touched when cells from the free pointer on are written. 

### `NodeMem.push`

 A node is not touched when cells from the free pointer on are written. 

### `Slot.Ok.heavy`

 The heavy elements of a set of a node, written at the free pointer, are a set of the child. 

### `NodeMem.child₁`

 The first child: the heavy elements of the first set, written at the free pointer, in place of
the first set. 

### `NodeMem.child₂`

 The second child: the heavy elements of the second set in place of the second set. 

### `NodeMem.child₃`

 The third child: the heavy elements of the third set in place of the third set. 

### `CtxAt.kept`

 The block of parameters, below the free pointer, is still there if no cell below the free
pointer has changed. 

 ## Words 

### `mul_le_wordNeed`

 A product of three factors that fits in the words of the routines below the tree. 

### `mul_le_word`

 The same for the limits: the product fits in a word. 

### `le_word_of_le`

 A number up to M + 1 fits in a word. 

### `wordNeed_mono`

 Larger sets and larger moduli need larger words. 
