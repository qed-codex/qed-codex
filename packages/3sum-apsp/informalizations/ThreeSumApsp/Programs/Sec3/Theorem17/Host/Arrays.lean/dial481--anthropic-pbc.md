---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Arrays.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Arrays.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Arrays.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the arrays and the loop

The third part of the host procedure `et17` (Exact Triangle by Theorem 17) fills the table of
doubles and the three lists of residues (`resid_then`), sorts the pairs into classes and cuts the
classes into chunks (`classes_then`), and calls the loop over the instances.

`et17Tables_spec` is the specification of the whole part: within `hostRunTime` steps, local 0 holds
the bit `found m` of the loop over the instances, and the cells below the free pointer are
unchanged.  Three lemmas connect the calls to the loop: `ready_of` (a run of et17 provides what this
part needs), `hostMem_of` (the arrays that the loop reads are in the memory) and `hostLay_of` (they
lie where the loop expects them).


### `setLocal_res`

 A call that puts its result into the local Small. 

### `Ready`

 What the third part needs, for the data X of the loop: the limits, the prime, and the three
matrices below the free pointer. 

### `resid_places`

 The places of the lists of residues: they stand one after the other behind the table of doubles,
and end where the array of the classes begins, below the free pointer of the solver. 

### `class_places`

 The places of the arrays of the classes and the chunks: they stand one after the other behind
the lists of residues, and end at aX, the first matrix of the instance that is handed to the solver,
below the free pointer of the solver. 

### `ResidMem`

 The memory after the first four calls: the three lists of residues; only cells between the free
pointer and the array of the classes have changed. 

### `ClassMem`

 The memory after the next two calls: the pairs, class after class, and the table of the chunks;
only cells between the array of the classes and aX, the first matrix of the instance that is handed
to the solver, have changed. 

### `Ready.residuesPre`

 What residues needs, for a matrix below the free pointer and a destination between the table of
doubles and the end of the arrays. 

### `resid_then`

 **The table of doubles and the three lists of residues**, followed by the rest t of the text. 

### `Ready.chunkCount_le`

 There are at most n² + p chunks. 

### `classes_then`

 **The classes and the chunks**, followed by the rest t of the text. 

### `hostLay_of`

 Where the arrays lie, for the addresses of et17. 

### `hostMem_of`

 The arrays that the loop over the instances reads are in the memory. 

### `ready_of`

 What the third part needs holds for the data of a run of et17. 

### `et17Tables_spec`

 **The third part of et17**: the result of the loop over the instances; only cells from the free
pointer on change. 
