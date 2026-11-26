---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/ScanPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/ScanPairs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Witnesses/ScanPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Reading the answers of one instance and scanning for witnesses

Proof of Theorem 17: "For every query pair that the oracle accepts, scan the piece C_k of its
instance for a c with S(a,b,c) = 0 [...].  We stop as soon as a zero triangle is found."

scanPairs(out, qa, qb, w, f, ab, bc, ac, n, c0, len): for every query pair number `i < w` whose
answer `out[i]` is not 0, scan the piece `{c0, …, c0 + len - 1}` for a zero triangle through the
pair `(qa[i], qb[i])`, as long as none has been found (`f = 0`).  The result is the new value of `f`
(`scanPairs_spec`).  No scan is made after the first successful one, so the number of scans is at
most the number of failed scans plus one (`execsUpto_le`).


 ## The pure side 

### `foundAt`

 Whether a zero triangle has been found before the pair number i; acc j: the answer for the pair
j is not 0; hit j: its scan succeeds. 

### `execAt`

 Whether the pair number i is scanned. 

### `execsUpto`

 The number of scans among the first w pairs. 

### `failsUpto`

 The number of accepted pairs among the first w whose scan would fail. 

### `execsUpto_le`

 **All scans but one fail.** 

 ## The routine 

### `Out`

 The locals of `scanPairs`.  The arguments: the addresses of the answers and of the rows and the
columns of the query pairs, their number `w`, the flag `f`, the addresses of the three arrays of
weights, `n`, and the first vertex and the number of vertices of the piece.  Then the counter. 

### `scanPairsStep`

 One query pair: if out[i] ≠ 0 and f = 0 then f := scan(ab, bc, ac, n, qa[i], qb[i], c0, len). 

### `scanPairsBody`

 scanPairs(out, qa, qb, w, f, ab, bc, ac, n, c0, len); the parameter is the procedure number of
`scan`. 

### `tAnswers`

 The time for reading w answers. 

### `tScanCall`

 The time of one scan of a piece of len vertices, with its call. 

### `tScanPairs`

 The time of scanPairs, given the number of scans. 

### `Answers`

 What `scanPairs` assumes about the answers of the solver and the `w` query pairs of an instance:
three arrays in the memory, and the query pairs are pairs of vertices. 

### `accOf`

 The answer for the query pair number `i` is not 0. 

### `hitOf`

 The scan for the query pair number `i` succeeds. 

### `scanPairsState`

 The state of `scanPairs` when `i` query pairs have been treated and the counter is `j`. 

### `scanPairsStep_spec`

 One query pair: a scan is made if the pair is accepted and nothing has been found yet. 

### `sum_scanPairs_rounds`

 The time of the rounds, added up: 19 steps for each query pair, and the scans. 

### `scanPairs_spec`

 **scanPairs** returns the new value of `f`; no cell changes; the time depends on the number of
scans that are made. 
