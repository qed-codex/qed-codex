---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/LibraryContracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/LibraryContracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/LibraryContracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Three routines of the library, as their callers see them

The programs for Theorem 5 call their procedures by number, and a caller assumes a specification of
the procedure that does not name its body: PowSpec for the tables of powers, FillSpec for filling a
segment, SqrtSpec for the square root.  Each follows from the specification of the routine in the
library; pow first puts its arguments in the order of the library's routine.


 ## The tables of powers 

### `powBody`

 pow(b, n, dst): the arguments are put in the order of powTable(dst, n + 1, b), whose body
follows.  Local 5 is a temporary. 

### `pow_entry`

 **pow(b, n, dst)** writes the powers b^0, …, b^n to the cells from dst, within 35 (n + 1) steps.


 ## Filling a segment 

### `fill_entry`

 **fill(dst, n, x)** writes x to the n cells from dst, within 13 (n + 1) steps. 

 ## The square root 

### `sqrt_entry`

 **sqrt(K)** returns ⌊√K⌋, within 18 (⌊√K⌋ + 1) steps. 
