---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Need.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Need.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Need.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the limits

The host procedure `et17` (Exact Triangle by Theorem 17) states what it needs of the limits of a
run: word size, memory, depth of calls (`hostNeedAt`).  This file shows that this need covers what
the procedures that it calls ask for.

* The arrays of the host lie one behind the other and fit into the cells that `hostLayout` counts
  (`aFr_le`).
* Every number that is at most `hostWord` fits in a word (`le_word_of_le_hostWord`).
* So the preconditions of the choice of the prime and of the loop over the instances hold
  (`choosePre_of_ok`, `hostLim_of_ok`).  For the solver this uses that an instance has at most
  `⌊n²/√D⌋` query pairs (`HostData.w_le_cap`, `need_le_supNeed`).


 ## The case that n is not small 

### `not_smallCase_iff`

 The host falls back on the brute force exactly if the hypotheses of Theorem 17 fail. 

### `hostData_p_le`

 The chosen prime is at most √D. 

### `two_le_hostData_p`

 The chosen prime is at least 2. 

### `hostData_m_le`

 There are at most `4ng` instances. 

### `hostData_valid`

 The data of a run are valid. 

 ## The addresses 

### `aFr_eq`

 The free pointer of the solver, written out. 

### `aFr_le`

 The arrays of et17 fit into the cells that hostLayout counts. 

 ## The words 

### `hostWord_le`

 The numbers of the host fit in a word. 

### `le_word_of_le_hostWord`

 A number that is at most hostWord fits in a word. 

### `choosePre_of_ok`

 What choosePrime needs. 

### `need_le_supNeed`

 The need of the solver on an instance with at most cap query pairs is at most supNeed. 

### `hostLim_of_ok`

 What hostLoop asks of the limits. 
