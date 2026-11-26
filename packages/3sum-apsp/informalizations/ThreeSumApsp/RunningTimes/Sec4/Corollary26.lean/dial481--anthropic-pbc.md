---
{
  "module": "ThreeSumApsp/RunningTimes/Sec4/Corollary26.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary26.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary26.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26 on the word RAM

In the paper it is Theorem 30 with `L = 21m` and `t = ⌈m/9⌉` (the entry `c = 21`, `q = 0.43` of
Table 2), "with the logarithmic factors absorbed into the exponents".  The program is
`Light.Sec4.program26`: the program with rational parameters in its text (`Light.Sec4.program31`)
at 21, 1/9 and the threshold 60 (`Light.Sec4.ratParams26`).

The preprocessing finds `m = ⌈log₄ D⌉` and compares it with 60 (`Light.Sec4.program26_pre31`).
"For m ≥ 60, Theorem 30 thus applies": the preprocessing finds `L = 21m` and `t = ⌈m/9⌉`
(`Light.Sec4.program26_levels31`, `Light.Sec4.program26_switch31`), pads the inner dimension to
`4^m`, calls the preprocessing of Theorem 30, and stores the flag 1
(`Light.Sec4.pre31_program26_above`); a query calls the query of Theorem 30
(`Light.Sec4.query31_program26_above`).  "(For m < 60, D is bounded by a constant, and the corollary
holds trivially.)": the preprocessing stores the flag 0, and a query computes an inner product
(`Light.Sec4.program26_query31`, `Light.Sec4.pre31_program26_below`,
`Light.Sec4.query31_program26_below`).

On the inputs with `N ≥ D^18` and `m ≥ 60` the two costs of Theorem 30 at these parameters are
`O(N²/D^{0.063})` and `O(D^{0.437})` (`Light.Sec4.regime26`, from `Corollary26.costs`), which is
what the two lemmas about the compiled program with parameters ask for
(`Light.Sec4.isDataStructure_of_costsWithin`, `Light.Sec4.solves_of_costsWithin`).  So the compiled
`Light.Sec4.program26` meets the bounds of the corollary (`isDataStructure_program26`,
`solves_program26`), and `wordRam_corollary_26` and `wordRam_corollary_26_wanted`, which say that
there are programs, follow.

The last sentence of the corollary is proved once more in another form,
`Light.Sec4.claim_corollary_26_wanted`: a procedure that other procedures can call, at any place of
the memory, and that is right on every instance.  Corollary 16, and through it the second bounds of
Theorems 19 and 22, rest on that form, not on `wordRam_corollary_26_wanted`.


### `isDataStructure_program26`

 **The compiled `program26` is the data structure of Corollary 26.**  For entries of absolute
value at most `N^c`, on the inputs with `D ≥ 1` and `N ≥ D^18`: the program compiled with the main
procedure preMain31 preprocesses in `O(N²/D^{0.063})` time and space, and the program compiled with
queryMain31 answers a query, put and answered through the cells -1, -2 and -3, in `O(D^{0.437})`
time. 

### `solves_program26`

 **The compiled `program26` computes the wanted entries within the bound of Corollary 26.**  On
the same inputs, the program compiled with the main procedure offlineMain32 takes
`O(|W| D^{0.437} + N²/D^{0.063})` time. 

### `wordRam_corollary_26`

 **Corollary 26**, on the word RAM: the two-stage data structure. 

### `wordRam_corollary_26_wanted`

 **Corollary 26**, on the word RAM: the offline form. 
