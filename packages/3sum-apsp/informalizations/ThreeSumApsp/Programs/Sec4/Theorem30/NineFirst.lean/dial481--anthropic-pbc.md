---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/NineFirst.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/NineFirst.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/NineFirst.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The least string with a given number of nines

nineFirst(a, n, lo) writes n - lo zeros and then lo nines into the cells from a: the first string of
the enumeration `Spec.nineStrs n lo hi`.  The two loops that write zeros and then nines up to the
end of the string are also the end of nineNext, so they are a statement of their own, `fillTail`.

Each of the two loops writes one digit again and again while a test holds (`fillRun`,
`Ends.fillRun`).  Together they write the least string from the current position on
(`fillTail_spec`), and `nineFirst_spec` is the case of the position 0.


### `Str`

 The local variables that nineFirst and nineNext share: the address of the string, its length,
the least number of nines, the current position, and the number of nines that are still to be
written.  Local 0 also takes the result. 

 ## One digit again and again 

### `fillRun`

 While the test holds: mem[str + pos] := c; pos := pos + 1. 

### `segN_wrote_const`

 The cells that have been written hold the digit. 

### `Ends.fillRun`

 **The rule for fillRun.**  The test is safe and holds in the first cnt rounds and no longer; it
may depend on the position, not on the memory.  Then the digit c is written into cnt cells.  (A
constant up to 100 fits in a word.) 

 ## Zeros and then nines up to the end of the string 

### `fillTail`

 Writes zeros from the current position on as long as more than need cells remain, and nines into
the remaining cells. 

### `fillTail_spec`

 fillTail writes the least string with need nines into the cells from the position i₀ on. 

 ## The least string 

### `nineFirstBody`

 nineFirst(str, len, minNines): the least string from the position 0 on. 

### `nineFirst_spec`

 **nineFirst** writes the least string of n digits with lo nines. 
