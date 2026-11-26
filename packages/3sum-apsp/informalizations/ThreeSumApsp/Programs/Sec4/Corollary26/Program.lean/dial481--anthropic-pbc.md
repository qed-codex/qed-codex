---
{
  "module": "ThreeSumApsp/Programs/Sec4/Corollary26/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26: the program

Proof of Corollary 26: "Let L := 21m and t := ⌈m/9⌉. We will apply Theorem 30 with these
parameters". `program26` is the program with rational parameters in its text (`program31`) at 21,
1/9 and the threshold 60 (`ratParams26`). Its preprocessing finds m = ⌈log₄ D⌉ and compares it with
60 (`program26_pre31`).

Only the definition `program26` is used elsewhere. The lemmas of this file show a reader of the
paper what the general program does at the parameters of Corollary 26; nothing rests on them.

* "For m ≥ 60, Theorem 30 thus applies": the preprocessing calls the procedures for L and t, which
  find ⌈21 m / 1⌉ and ⌈1 m / 9⌉ by counting (`program26_levels31`, `program26_switch31`), writes the
  padded matrices, calls the preprocessing of Theorem 30, and stores the base address and the flag
  1; this leaves the data structure of Theorem 30 with L = 21 m and t = ⌈m/9⌉
  (`pre31_program26_above`). A query reads the flag and calls the query of Theorem 30
  (`program26_query31`, `query31_program26_above`).
* "(For m < 60, D is bounded by a constant, and the corollary holds trivially.)": the preprocessing
  stores the flag 0 (`pre31_program26_below`), and a query reads the flag and computes an inner
  product (`program26_query31`, `query31_program26_below`).


### `program26`

 **The program of Corollary 26**: the parameters in its text are 21, 1/9 and 60. 

 ## The parameters in the text 

### `program26_pre31`

 pre31(N, D, aX, aY, fr) in the program of Corollary 26 finds m and 4^m; for m < 60 it stores the
flag 0, for m ≥ 60 it runs preLarge31. 

### `program26_levels31`

 "L := 21m": the procedure that preLarge31 calls for L counts up to 21 m in steps of 1. 

### `program26_switch31`

 "t := ⌈m/9⌉": the procedure that preLarge31 calls for t counts up to m in steps of 9. 

### `program26_query31`

 query31(I, J, N, D, aX, aY, fr) in the program of Corollary 26 reads the flag: if it is 1, it
calls the query of Theorem 30, and otherwise the inner product. 

 ## From the threshold on 

### `DSReady.of_eq`

 The data structure of Theorem 30 with L and t written in another way. 

### `Built26`

 The cells from fr on hold the flag 1, the base address, and the data structure of Theorem 30
with L = 21 m and t = ⌈m/9⌉ for the padded matrices. 

### `pre31_program26_above`

 "For m ≥ 60, Theorem 30 thus applies": the preprocessing leaves the flag 1, the base address,
and the data structure of Theorem 30 with L = 21 m and t = ⌈m/9⌉, which makes the cells ready for
queries, and changes no cell outside the structure. 

### `query31_program26_above`

 For m ≥ 60 a query returns the entry in the time of a query of Theorem 30 with L = 21 m and t =
⌈m/9⌉, keeps the cells ready, and changes only cells of the structure behind its first three. 

 ## Below the threshold 

### `pre31_program26_below`

 "(For m < 60, D is bounded by a constant, and the corollary holds trivially.)" The preprocessing
takes the time of finding m and 4^m, stores the flag 0, which makes the cells ready for queries, and
changes no cell but the three from fr on. 

### `query31_program26_below`

 "(For m < 60, D is bounded by a constant, and the corollary holds trivially.)" A query returns
the entry in the time of an inner product of length D, and changes no cell. 
