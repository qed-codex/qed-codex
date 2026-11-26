---
{
  "module": "ThreeSumApsp/Lang/Compiler/Conditions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Conditions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Conditions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The compiler is correct on tests

The code of a test goes on to the next position if the test holds and jumps to a given position if
it does not, in at most as many steps as it has instructions, and it changes scratch cells only.
This behaviour is called `Decides`, and `decides_compileCond` proves it.

Both tests first evaluate a into T₀ and b into T₁ (`steps_pair`, which also serves the statement
that stores into the memory).  For a < b the code forms D = b - a - 1 and leaves if D < 0
(`decides_lt`).  For a = b it forms D = a - b and leaves if D < 0, then forms -D and leaves if that
is negative (`decides_eq`).  No difference overflows, because words hold twice the largest value and
one more (`inRange_sub`).


 ## Two expressions 

### `codeAt_after_pair`

 What follows the code of two expressions. 

### `steps_pair`

 The code of two expressions, one after the other, leaves their values in T₀ and T₁ and changes
scratch cells only. 

 ## Tests 

### `Decides`

 What the code of a test does, if it has size instructions, begins at pos, and tests p: in at
most size steps the machine reaches the position after the code if p holds, and the position l if
not.  Only scratch cells change. 

### `Decides.of_holds`

 The test holds. 

### `Decides.of_fails`

 The test fails. 

### `inRange_sub`

 No overflow: the difference of two values fits in a word, and so does one less. 

### `decides_lt`

 The test a < b. 

### `decides_eq`

 The test a = b. 

### `decides_compileCond`

 The code of a test decides the test. 
