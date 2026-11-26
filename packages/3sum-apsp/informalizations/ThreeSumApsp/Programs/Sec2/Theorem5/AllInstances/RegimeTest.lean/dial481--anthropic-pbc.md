---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/RegimeTest.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/RegimeTest.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/AllInstances/RegimeTest.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The regime of Theorem 5

"Let D ≥ 4 be a power of four and N ≥ D^18 … a set W of at most N²/√D positions".  The procedure
regime(N, D, w), where w is the number of positions in W, tests whether the sizes of an instance are
in this regime.  It returns the exponent m with D = 4^m if they are, and 0 if they are not.  With
√D = 2^m, the condition on W reads w 2^m ≤ N².

The program has these parts, each with its own lemma.  regimeExp multiplies by four until D is
reached, which gives the only candidate m = ⌈log₄ D⌉ together with 4^m and 2^m = √D.  regimePow
compares D^18 with N by at most eighteen multiplications, none of which exceeds N D (but for the
first product, which is D).  regimeTests combines the four tests, the last two of which are
regimeSizes.  That the candidate is the only one is RegimeAnswer.zero.


### `RegimeAnswer`

 The number r is the exponent m of the regime if the sizes are in the regime, and 0 if not. 

### `RegimeSpec`

 regime(N, D, w) changes no cell.  It returns m if 1 ≤ m, D = 4^m, D^18 ≤ N and w 2^m ≤ N², and
0 if there is no such m. 

 ## The local variables 

### `Rows`

 The argument N. 

### `Cols`

 The argument D. 

### `Wanted`

 The argument w. 

### `PowFour`

 The power 4^m. 

### `PowTwo`

 The power 2^m. 

### `Expo`

 The exponent m. 

### `Result`

 The result. 

### `Power`

 A power of D. 

### `Count`

 The exponent of that power. 

### `Fits`

 1 as long as no power of D has exceeded N, then 0. 

 ## The text 

### `regimeExp`

 The search for the exponent m, with 4^m and 2^m. 

### `regimePowRound`

 One round of regimePow: if the next power of D exceeds N, give up; if not, go on to it. 

### `regimePow`

 The test D^18 ≤ N: the power of D is at most N unless it is D^0. 

### `regimeSizes`

 The last two tests, after regimePow: D^18 ≤ N and w 2^m ≤ N².  If both hold, the result becomes
m. 

### `regimeTests`

 The four tests: 4^m = D, m ≥ 1, D^18 ≤ N and w 2^m ≤ N².  If all hold, the result becomes m. 

### `regimeBody`

 regime(N, D, w). 

### `cRegime`

 The constant of the running time. 

 ## What the procedure returns 

### `RegimeAnswer.zero`

 The only candidate for the exponent is ⌈log₄ D⌉: if it fails one of the tests, the sizes are not
in the regime. 

 ## The exponent 

### `regimeExp_spec`

 regimeExp ends with 4^m, 2^m and m in the locals 3, 4 and 5, for m = ⌈log₄ D⌉. 

 ## The eighteenth power 

### `PowInv`

 The states of the loop of regimePow.  The memory and the locals below 7 are as at the start.
Either the loop is still counting: local 8 is an exponent j ≤ 18, local 7 is D^j, which is at most N
unless j = 0, and local 9 is 1.  Or it has stopped because a power exceeded N: local 8 is 18 and
local 9 is 0. 

### `regimePowRound_spec`

 A round of regimePow keeps PowInv and brings local 8 closer to 18. 

### `regimePow_spec`

 regimePow leaves the memory and the locals below 7 as they are.  Afterwards local 9 is 1 if
D^18 ≤ N and 0 if not. 

 ## The four tests 

### `regimeSizes_spec`

 regimeSizes, started after the first two tests have succeeded and regimePow has run, puts the
answer into local 6. 

### `regimeTests_spec`

 regimeTests, started with 4^m, 2^m and m for m = ⌈log₄ D⌉ in the locals 3 to 5 and with 0 in
local 6, puts the answer into local 6. 

 ## The whole procedure 

### `regime_entry`

 **regime** meets its specification. 
