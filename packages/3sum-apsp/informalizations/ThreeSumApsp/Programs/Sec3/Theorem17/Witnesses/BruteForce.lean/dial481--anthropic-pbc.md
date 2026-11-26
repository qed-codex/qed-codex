---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/BruteForce.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/BruteForce.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/BruteForce.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Brute force (the proof of Theorem 19)

In the proof of Theorem 19, "smaller instances are solved by brute force": the procedure brute
(`bruteBody`) scans all of `C` for every pair `(a, b)` (`brute_spec`, `brute_meets`).  It takes at
most `100 n³ + 100` steps (`brute_solves`).


### `hasZero_iff`

 Brute force finds a zero triangle if and only if there is one. 

### `bruteRow`

 Some `b` below `b'` gives a zero triangle with `a`. 

### `bruteAll`

 Some `a` below `a'` is in a zero triangle. 

### `Size`

 The locals of `brute`.  The arguments: `n`, `U`, the addresses of the three arrays, and the free
pointer.  Then the vertices `a` and `b`, the result so far, and the result of a scan. 

### `brutePair`

 One pair `(a, b)`: res := scan(ab, bc, ac, n, a, b, 0, n); if res = 1 then hit := 1. 

### `bruteInner`

 The inner loop of brute: all `b` for one `a`. 

### `bruteBody`

 brute(n, U, ab, bc, ac, fr); the parameter is the procedure number of `scan`. 

### `tBrute`

 The time of brute. 

### `bruteNeed`

 What brute needs: sums of three weights, no cells, one call. 

### `_root_.Light.TriInst.Pre.weights`

 An instance of Exact Triangle gives `scan` what it assumes. 

### `brutePair_spec`

 One pair: the result so far takes the scan for `(a, b)` in. 

### `bruteInner_spec`

 The inner loop: all `b` for one `a`. 

### `tBrute_ge`

 The steps of the two loops of brute are within its time. 

### `brute_spec`

 **The brute force.**  In any program that holds `scanBody` as its procedure number `pScan`,
`bruteBody pScan` ends within `tBrute n` steps, decides whether the instance has a zero triangle,
and changes no cell. 

### `brute_meets`

 The specification of `brute`, for its callers. 

### `brute_solves`

 **brute** solves Exact Triangle. 
