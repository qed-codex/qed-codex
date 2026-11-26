---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26, 31 and 32: the concrete program for given parameters

program31 G = base58 (Theorem 5's and Theorem 30's procedures, numbers 0 to 57) followed by the
procedures 58 to 73 of Section 4.4 (`procs31`): copying, filling, m = ⌈log₄ D⌉, padding and the
inner product; the preprocessing pre31Body G at 64 and the query; their main procedures; the offline
routine and its main procedure; the solver of Corollary 26 for all instances with its test; and the
two procedures for L = ⌈am/b⌉ and t = ⌈pm/q⌉ at 72 and 73. The specifications of the preprocessing,
the query and the offline routine hold for it, for all limits, without hypotheses. At the parameters
of Corollary 26 it is `program26`.

With the two end theorems for light programs and the compiler this gives the two statements about
the word RAM from which Corollaries 26, 31 and 32 follow: on every domain of inputs, and for all
bounds that dominate the two costs of Theorem 30 at the parameters G (`CostsWithin`), the compiled
program is a data structure (`isDataStructure_of_costsWithin`) and solves the offline problem
(`solves_of_costsWithin`).


 ## Two procedures for Corollary 26

The program carries them for all parameters G. What they do at the parameters of Corollary 26 is
proved in `regimeTest26_meets` and `allInstances26_solves`. 

### `regimeTest26Body`

 regimeTest26(N, D) returns 1 if D^18 ≤ N and 0 if not. It changes no cell. 

### `allInstances26Body`

 allInstances26(N, D, w, U, x, y, wi, wj, out, fr). Locals 0 to 9 are the arguments, which are
passed on as they are; local 10 is the result of the test. 

 ## The program 

### `procs31`

 The bodies of the procedures number 58, 59, …, 73 (61 is not used). 

### `program31`

 The program for the parameters G. 

### `program31_at`

 The routines stand at their numbers. 

### `pre31_program31`

 **The preprocessing**, for all limits. 

### `query31_program31`

 **A query**, for all limits. 

### `offline32_program31`

 **The offline routine**, for all limits. 

 ## The program on the word RAM 

### `isDataStructure_of_costsWithin`

 **The program with the parameters G, compiled, is a data structure** on every domain of inputs
with entries bounded by N^e, for all bounds Tp (preprocessing time and space) and Tq (query time)
that dominate the two costs of Theorem 30. The preprocessing program is compiled with the main
procedure preMain31, the query program with queryMain31; queries are put and answered through the
cells -1, -2 and -3. 

### `solves_of_costsWithin`

 **The program with the parameters G, compiled** with the main procedure offlineMain32,
**computes the wanted entries** in time O(|W| Tq + Tp), on every domain of inputs with entries
bounded by N^e and for all bounds Tp and Tq that dominate the two costs of Theorem 30. 
