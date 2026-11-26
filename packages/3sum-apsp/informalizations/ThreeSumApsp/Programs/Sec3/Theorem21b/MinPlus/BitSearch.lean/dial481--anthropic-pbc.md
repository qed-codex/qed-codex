---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/BitSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/BitSearch.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/BitSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The (min,+)-product from "all pairs", bit by bit

Theorem 21(b), after [VW18, Theorem 4.2].  The host below computes the
(min,+)-product over an arbitrary solver of the task "all pairs": for three matrices X, Y, V, which
pairs (i, j) have X[i,k] + Y[k,j] < V[i,j] for some k.

mp(n, U, a, b, c, fr).  All entries of the product lie between −2U and 2U.  The output array starts
as −2U everywhere.  Let R be least with 2^R > 4U; the powers 1, 2, …, 2^(R−1) are written to the R
cells from fr while R is found by doubling.  For t = R − 1, …, 0: V := lo + 2^t (the n² cells from
fr + R), the solver writes its flags to the next n² cells, and lo grows by 2^t where the flag is 0.
Before the round for t, lo ≤ C[i,j] < lo + 2^(t+1): lo is C[i,j] with the lowest t + 1 bits of
C[i,j] + 2U cleared (lows x (t + 1)).  The entries of V have absolute value at most 6U.

The result is isHost_mp : IsHost pairsTask mpTask mpTime mpNeed.  First the lists: the lower bounds
lows x t, which start as −2U (lows_top), end as the product (lows_zero), and change in a round as
bump changes them (lows_round, from bitLo_step).  Then the program: the powers of two (powers_spec),
a round (round_spec, with the invariant Inv), all rounds (rounds_spec), the host (mp_spec).


 ## The program 

### `mpRounds`

 The number of rounds: the least R with 2^R > 4U. 

### `N`

 The local variables of mp: the arguments n, U, a, b, c, fr (Free); n² (Area), 2U, 4U, −2U (Low)
and 6U; Count counts the powers up and then the rounds down; Power is the power of two; then the
addresses fr + R of V (Asked), fr + R + n² of the flags and fr + R + 2n², the free pointer of the
solver (SolverFree); and the results of the calls, which are not used. 

### `mpConsts`

 The numbers n², 2U, 4U, −2U, 6U. 

### `mpPowers`

 The powers 1, 2, …, 2^(R−1) are written to the cells from fr, while R is found by doubling. 

### `mpRound`

 The round for t = Count − 1: V := lo + 2^t, the solver's flags, and lo grows by 2^t where the
flag is 0. 

### `mpBody`

 mp(n, U, a, b, c, fr), over the procedures number pPairs (a solver of "all pairs"), pFill, pAddc
and pBump. 

### `Mp.roundTime`

 The number of steps of one round, given the time of the solver. 

### `mpTime`

 The time of the host, given the time of the solver: R calls at the bound 6U, and O(n²) steps for
each call. 

### `mpNeed`

 The need of the host, given the need of the solver: the numbers up to 8U + 1, room for the R
powers of two, for V and for the flags, and one more level of calls. 

 ## The number of rounds 

### `pow_range`

 The powers of two below 2^R are at most 4U. 

### `lt_pow_rounds`

 2^R is above 4U. 

 ## The lists of a round 

### `lows`

 The lower bounds when t rounds remain: bitLo U t c for every entry c of the product, that is c
with the lowest t bits of c + 2U cleared.  So lo ≤ c < lo + 2^t. 

### `asked`

 The matrix V of the round for t: the lower bounds plus 2^t. 

### `flags`

 The flags that the solver returns in the round for t. 

### `getElem_lows`

 An entry of the lower bounds. 

### `entry_range`

 The entries of the product lie between −2U and 2U. 

### `lows_range`

 The lower bounds lie between −2U and 2U. 

### `lows_top`

 At the beginning all lower bounds are −2U. 

### `lows_zero`

 At the end the lower bounds are the product. 

### `getElem_flags`

 A flag of the round for t: is the entry of the product below the lower bound plus 2^t? 

### `lows_round`

 **One round**: each lower bound grows by 2^t where the flag is 0. 

### `flags_eq_zero_or_one`

 A flag is 0 or 1. 

### `absLe_lows`

 The lower bounds have absolute value at most 2U. 

### `abs_asked_le`

 The entries of V have absolute value at most 6U. 

 ## The surroundings 

### `Ctx`

 The surroundings of mp: a solver of "all pairs", and the three passes in the program. 

### `Lim`

 What the limits have to allow for: the numbers of the solver and those up to 8U + 1; room for
the powers of two, V, the flags and the solver; one level of calls more than the solver needs. 

### `consts`

 The first eleven local variables, which do not change after mpConsts. 

### `locals`

 The local variables during the rounds. 

 ## Before the rounds 

### `consts_spec`

 mpConsts computes the five numbers. 

### `powers_spec`

 mpPowers finds R and writes the powers of two to the R cells from fr. 

 ## A round 

### `Mem`

 The memory when t rounds remain: the lower bounds stand at c, the powers of two at fr, and below
the free pointer no cell outside c has changed. 

### `Inv`

 The state when t rounds remain. 

### `pairsInst`

 The instance that the solver gets in the round for t: the two matrices, V at fr + R, and the
place for the flags behind it. 

### `pairsInst_pre`

 It is an instance, once V stands at its place and the two matrices are still at theirs. 

### `round_spec`

 **One round** goes from the state with t + 1 remaining rounds to the state with t. 

### `rounds_spec`

 **The rounds** go from the state with R remaining rounds to the state with none. 

 ## The host 

### `mp_spec`

 **The host is correct**, in every program that begins with the solver's program and has the
three passes. 

### `polyNeed_mpNeed`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_mp`

 **The (min,+)-product from "all pairs"**, as a host. 
