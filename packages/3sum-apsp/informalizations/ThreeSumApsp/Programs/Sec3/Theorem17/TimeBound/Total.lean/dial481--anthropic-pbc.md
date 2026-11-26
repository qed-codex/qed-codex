---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Total.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Total.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Total.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The time of the host of Theorem 17 obeys the bound of Theorem 17

Theorem 17 reduces Exact Triangle to at most `4ng` instances "plus O(ν n³ log n/g + n^{ω+o(1)}
D^{3/2} + n² D g) additional time".  The form for programs, `Claim.Theorem_17`, has, here,
Strassen's exponent in the second term; its right side is `bound17`.  The time
function of the host is the time of `4ng` calls of the solver plus a rest, its time over a solver
that takes no time (`hostTime_eq`), and the rest is bounded term by term, up to a constant.

* The parameters, the choice of the prime, the residues, the classes and the chunks are within the
  three terms of the bound (`steps_hostSetup`, `steps_chooseTime`, `steps_tResidues`,
  `steps_tClasses`, `steps_tChunks`).
* Writing the matrices of the instances takes `O(ng) · O(nD)` steps, the third term
  (`steps_instances_mul_tWrites`).
* Reading the answers takes a constant number of steps for each of the at most `n²/√D` query pairs
  of an instance (`steps_tAnswers`).  This is the term `C n²/√D` beside the time of the solver.
* There are at most `F(p) + 1 = O(κ n³ log n/√D)` scans, where `F(p)` is the number of false
  positives of the chosen prime, of `O(√D/g)` steps each: the first term
  (`steps_falsePositiveBound`, `steps_tScanCall`, `steps_scans`).

The sum is `steps_hostRest`, and `obeysBound17_hostTime` puts it into the form of `bound17`.


 ## The scans 

### `steps_tScanCall`

 One scan looks at the `⌈s/g⌉ ≤ 2√D/g` vertices of a piece, where `s = ⌊√D⌋`, so it takes
`O(√D/g)` steps. 

### `kappaOf_le_of_hyp`

 The exponent that the host's bound on the false positives uses is at most `κ`. 

### `steps_falsePositiveBound`

 Proof of Theorem 17: there are at most `F(p) + 1 = O(κ n³ log n/√D)` scans, where `F(p)` is the
number of false positives of the chosen prime `p`.  The host bounds it by `falsePositiveBound`. 

### `steps_scans`

 **The scans**: `O(√D/g) · O(κ n³ log n/√D)` is within the first term of the bound. 

 ## What is done for each instance 

### `steps_instances`

 The bound `4ng` on the number of instances is `O(ng)`. 

### `steps_tWrites`

 Writing the two matrices of an instance takes `O(nD)` steps. 

### `steps_instances_mul_tWrites`

 Writing the matrices of all instances, `O(ng) · O(nD)`, is within the third term of the bound.


### `steps_tAnswers`

 Reading the answers of one instance takes `O(n²/√D)` steps, a constant number for each query
pair. 

 ## The sum 

### `hostRest`

 The time of the host without the calls of the solver: its time over a solver that takes no time.


### `not_smallCase_of_hyp`

 Under the hypotheses of Theorem 17 the host does not fall back on the brute force. 

### `hostTime_eq`

 The time of the host is the time of `4ng` calls of the solver plus the rest. 

### `restBound`

 What bounds the time of the host without the calls of the solver: `ng · n²/√D`, for reading the
answers of the instances, plus the three terms of the bound of Theorem 17. 

### `Steps.toRest`

 What is within the three terms is within `restBound`. 

### `steps_hostSetup`

 The parameters, the square root of `D` and the tests at the beginning are within the bound, if
the routines that compute `D` and `g` are. 

### `steps_hostLoopBound`

 The loop over the instances, without the calls of the solver, is within the bound: writing the
matrices, no time for the solver, reading the answers, and the scans. 

### `steps_hostRest`

 **Everything but the calls of the solver** is within the bound, if the routines that compute `D`
and `g` are.  The summands stand in the order of `hostMain`. 

### `cast_supTime_le`

 A bound `T` on the time of the solver that is monotone in the number of query pairs bounds its
largest time on the instances of the host. 

### `obeysBound17_hostTime`

 **The bound of Theorem 17 for the host.**  The parameter routines compute `Dfun n` from `n` and
`Gfun D` from `D`.  These agree with the parameters `D n` and `g n` of the claim, which are defined
with real powers, and the routines run within the bound. 
