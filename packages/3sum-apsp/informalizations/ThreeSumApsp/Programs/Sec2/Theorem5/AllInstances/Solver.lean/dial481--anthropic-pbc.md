---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Solver.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Solver.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/Solver.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The thin matrix product, on all instances

The task thinTask: given an N × D matrix X and a D × N matrix Y with entries of absolute value at
most U, and w positions (rows at wi, columns at wj), write the entries of XY at these positions to
the cells from out on. Theorem 5 is about instances with D ≥ 4 a power of four, N ≥ D^18
and at most N²/√D wanted positions. A solver that other procedures call has to be right on every
instance. thin(N, D, w, U, x, y, wi, wj, out, fr) tests the regime, calls the solver of Theorem 5 in
the regime and the brute force outside it.

The file proves that thin solves the task thinTask (thin_solves), within a need that is polynomial
in the parameters (thinNeed_poly) and covers what the solver of Theorem 5 asks of the limits
(thin_limits5, "Word size" in Section 2.4.4), and within the time of Theorem 5 in the regime
(thin_shape_le, thinTimeBound_le). Together these are the running-time claim "Theorem 5" for the
light model (thin_claim).


### `Thin.Expo`

 Local 10 of thin: the result of the test of the regime. 

### `thinBody`

 thin(N, D, w, U, x, y, wi, wj, out, fr). 

### `thinWord`

 The largest number that thin forms. 

### `thinNeed`

 What thin needs, for the parameters N, D, w, U: the largest number formed, the cells from the
free pointer on, the levels of calls. 

### `bound5`

 The bound of Theorem 5, without its constant. 

### `thinSteps`

 The time of thin on sizes N, D, w, if the solver of Theorem 5 takes at most K · thm5Shape
steps. 

### `thinTime`

 The time of thin, for the parameters N, D, w, U. 

### `thinTimeBound`

 The time as a function of N, D and of upper bounds on w and U; it is monotone in the bound on
w. 

 ## The need 

### `le_prod_four`

 Each factor of a product of four positive numbers is at most the product. 

### `thinNeed_poly`

 The need is polynomial in the parameters: each of them is at most
Q = (N + 1) (D + 1) (w + 1) (U + 1), and the three numbers are polynomials of degree at most 8. 

 ## The regime 

### `InRegime.mono`

 The regime is closed under taking fewer wanted positions. 

### `bound5_nonneg`

 The bound of Theorem 5 is not negative. 

### `le_bound5`

 In the regime, D is at most the bound of Theorem 5: D ≤ N ≤ N² / D^{1/18}, and log D ≥ 1. 

 ## The time 

### `thinTime_le`

 The time for w and U is at most the time for upper bounds on them. 

### `thinTimeBound_le`

 In the regime the time is within the bound of Theorem 5. 

 ## The solver of Theorem 5 may be called 

### `card_thinW_of_pre`

 The set ThinW x of the wanted positions has x.w elements. 

### `thin_limits5`

 **The limits that thin asks for are those that the solver of Theorem 5 asks for**, in the
regime; the encoded numbers are at most N² U. 

### `thin_shape_le`

 In the regime the time of the solver of Theorem 5 is within the bound of the theorem. 

### `thin_solves`

 **thin solves the task on all instances**, in the program P5 ++ [regime, thinBrute, thin], where
P5 is a program of 26 procedures whose number pThm5 is the solver of Theorem 5, which does its task
within K · thm5Shape steps also after more procedures are appended. 

### `thin_claim`

 **The running-time claim "Theorem 5" for programs of the light language**, from a program as in
thin_solves. 
