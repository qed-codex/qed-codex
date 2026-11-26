---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/Scan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/Scan.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/Scan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Scanning a piece (the proof of Theorem 17)

"For every query pair that the oracle accepts, scan the piece C_k of its instance for a c with
S(a,b,c) = 0".  The procedure scan (`scanBody`) goes through an interval of vertices `c` for a fixed
pair `(a, b)` (`scan_spec`, `scan_meets`).


### `bit`

 A truth value as a number: 1 for true, 0 for false. 

 ## The three arrays of weights 

### `Weights`

 What `scan` assumes: the three arrays of `n²` weights of absolute value at most `U` lie in the
memory, an address fits in a word, and so does a sum of three weights. 

 ## Scanning an interval of vertices 

### `AdrAB`

 The locals of `scan`.  The arguments: the addresses of the three arrays, `n`, the pair `(a, b)`,
the first vertex `c0` and the number `len` of vertices of the interval.  Then the counter `c`, the
result so far, the weight `w(a,b)`, and the addresses of `w(b, c0)` and of `w(a, c0)`. 

### `scanRound`

 One round of `scan`: if `w(a,b) + w(b, c0 + c) + w(a, c0 + c) = 0` then hit := 1; c := c + 1. 

### `scanBody`

 scan(ab, bc, ac, n, a, b, c0, len). 

### `tScan`

 The time of scan. 

### `scanHit_succ`

 One more vertex in a scan. 

### `scanRound_runs`

 One round of `scan`, for the weights `wbc` and `wac` that it reads. 

### `scan_spec`

 **scan** returns 1 if some `c` in the interval has `S(a,b,c) = 0`, and 0 if not; it changes no
cell. 

### `scan_meets`

 The specification of `scan`, for its callers. 
