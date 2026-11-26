---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: the time and the need of the host

The host s3(n, U, x, fr) has a parameter `κ` (a natural number, fixed with the program): it first
replaces the bound `U` by `max U (n^κ)`. So on all inputs with `U ≤ n^κ` it asks the
Convolution-3SUM solver for instances of one and the same length and bound, `8 m²` and
`120 n^κ + 40` with `m = mPar n (2 n^κ)`. (A running time `T N B` of an arbitrary solver need not be
monotone in `N`.)

The time is split into the host's own work and the number of calls of the solver. This file has the
definitions and one identity (`tNodes_eq`); the arithmetic (`claim_CH20_Theorem_5_1_of_host`) starts
from them.


### `callsB`

 An upper bound on the number of calls of the recursive procedure for one three-set input. 

### `nodeOwn`

 The cost of one call of the recursive procedure without the call of the solver. 

### `tNodes_eq`

 The time of the recursive procedure, split into its own work and the calls of the solver. 

### `tParams`

 The time of params: four logarithms and a square root. 

### `tPrep`

 The time of prep: primes, count table, a copy, sorting, distinct values, binary digits. 

### `tSetup`

 The time of params and prep. 

### `inputsB`

 The number of three-set inputs. 

### `coreCalls`

 The number of calls of the solver, for the bound `V = 2U`. 

### `coreOwn`

 The host's own work, for the bound `V = 2U`. 

### `coreTime`

 The time of the host after the bound has been fixed. 

### `chTime`

 **The time of the host.** 

### `coreCells`

 The cells of the host's own arrays: the block of parameters, the primes, the count table, the
sorted copy, values and multiplicities, the binary digits, three sets for a splitting, the doubles,
and one cell for the set {0}. 

### `coreNeed`

 The need of the host after the bound has been fixed. 

### `chNeed`

 **The need of the host.** 
