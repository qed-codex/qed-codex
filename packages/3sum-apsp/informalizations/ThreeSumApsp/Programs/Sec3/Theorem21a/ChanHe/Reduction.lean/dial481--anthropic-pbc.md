---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Reduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Reduction.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Reduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: the core of the host

Theorem 21(a), after [CH20, Theorem 5.1].  core(n, V, x, b), with V = 2U,
decides 3SUM for the n numbers of absolute value at most U at x.  It has six parts.

* coreSetup computes the parameters and fills the arrays of the memory map (`coreSetup_ends`).
* coreAddr computes the addresses of the arrays that the rest uses (`coreAddr_runs`).
* coreSplit runs through the splittings (`coreSplit_ends`).
* coreDoubles and coreZero form and decide the two three-set inputs for the solutions that repeat a
  value (`coreDoubles_ends`, `coreZero_ends`).
* coreAnswer adds up the three answers (`coreAnswer_runs`).

That the three answers decide 3SUM is `threeSum_iff_trees`.  The routines that the three middle
parts call write only to the cells for the three sets of a splitting, to the cells for the doubles,
and behind the arrays; so the arrays that they read are still there at each call (`Core.Arrays`,
`Core.Arrays.of_sameOn`), and each three-set input lies in the memory as the recursive procedure
wants it (`Core.Placed`, `Core.Arrays.nodesPre`).


 ## The three answers, and the time 

### `threeSum_iff_trees`

 3SUM, through the three kinds of three-set inputs. 

### `ChCore.flag_sum_pos`

 A sum of three answers is positive if and only if one of them is yes. 

### `ChCore.time_le`

 The steps of the routine are within the time of the host. 

 ## The program 

### `Len`

 The locals of core; each is assigned once.  The arguments: n, V, x and the free pointer b.  Then
a local for a result that is not read; the parameters Λ, m and f, which params has written to the
three cells from b; the base b + 3 of the arrays; the number of distinct values; the addresses of
the sorted copy, the values, their multiplicities, the table of digits, the three sets, the doubles
and the cell that holds 0, and the free pointer behind the arrays.  Then the answer for the
splittings, the number of doubles and the answer for them, and the length of the set for a triple
zero and the answer for it. 

### `coreSetup`

 The parameters, and the arrays. 

### `coreAddr`

 The addresses of the arrays from the sorted copy on. 

### `coreSplit`

 The loop over the splittings. 

### `coreDoubles`

 The three-set input for the solutions a + a + c = 0 with a ≠ 0: the doubles of the repeated
values, {0}, and the values. 

### `coreZero`

 The three-set input for the solution 0 + 0 + 0 = 0: {0} if 0 occurs three times and the empty
set if not, {0}, and {0}. 

### `coreAnswer`

 The answer: 1 if one of the three answers is 1. 

### `coreBody`

 core(n, V, x, b), over the procedures pParams, pPrep, pGrid, pTwice, pZero, pNodes. 

### `setupFrame`

 The locals after coreSetup: a is the memory map, f the number of levels, nd the number of
distinct values. 

### `addrFrame`

 The locals after coreAddr. 

 ## The addresses 

### `coreAddr_cost`

 `coreAddr` takes 42 steps. 

### `coreAddr_runs`

 coreAddr computes the addresses. 

 ## The arrays, and a three-set input in the memory 

### `Par`

 The parameters are those of the reduction. 

### `Par.primes_nonempty`

 There is a prime up to m. 

### `Par.primeBound_pos`

 The bound on the primes is positive. 

### `Fixed`

 The cells that no routine called after coreAddr writes: those below the three sets of a
splitting, and the cell that holds 0. 

### `Arrays`

 The arrays that the parts after coreAddr read: the distinct values D, how often they occur, the
block of parameters, the primes, the zeros of the count table, and the cell that holds 0. 

### `Arrays.of_sameOn`

 The arrays are still there if the fixed cells have not changed. 

### `Placed`

 A set of at most n numbers of absolute value at most V, in the l cells from s, which lie among
the arrays from the values on. 

### `Arrays.placed_val`

 The set of the distinct values. 

### `Arrays.placed_zero`

 The set {0}. 

### `Arrays.nodesPre`

 Three sets among the arrays are a three-set input as the recursive procedure wants it. 

### `Arrays.nodes_meets`

 The recursive procedure, called for three sets among the arrays. 

 ## The three answers 

### `Ctx`

 What the parts after coreAddr assume: the parameters, the values of the input X, the arrays in
the memory μ, and what the limits must allow. 

### `Ctx.okNodes`

 The limits allow for a call of nodes. 

### `Ctx.okGrid`

 The limits allow for a call of grid. 

### `tNodes_le_tTree`

 The recursive procedure stays within the time for a tree with f levels. 

### `Ctx.placed_zeroSet`

 The set for a triple zero lies in the cell that holds 0; its length is the answer of
zeroThree. 

### `grid_meets_of_map`

 grid, called for the arrays of a map. 

### `coreSplit_ends`

 coreSplit decides whether some splitting gives a yes-instance. 

### `coreDoubles_ends`

 coreDoubles decides the three-set input for the solutions that use a value other than 0
twice. 

### `coreZero_ends`

 coreZero decides the three-set input for the solution that uses 0 three times. 

### `coreAnswer_cost`

 `coreAnswer` takes 10 steps. 

### `coreAnswer_runs`

 coreAnswer returns 1 if one of the three answers is yes, and 0 if not. 

 ## The parameters and the arrays 

### `Setup`

 What coreSetup leaves in the memory μ': the arrays for the values D of the input X, with how
often they occur; nothing below the free pointer b has changed. 

### `coreSetup_ends`

 coreSetup computes the parameters and fills the arrays. 

### `Core.Setup.ctx`

 After coreSetup the other parts find what they assume. 

 ## The routine 

### `coreBody_ends`

 The six parts one after the other, for the memory map a with the base b + 3. 

### `core_spec`

 **core meets its specification**, in every program that holds its body and meets the
specifications of the routines that it calls. 
