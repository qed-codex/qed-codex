---
{
  "module": "proof/machines/Wrap/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From any machine that meets the bound for counting to a machine for 3-SAT on the plain input code: the end theorems

The statements are those of proof/machines/Wrap/Defs.lean. The pieces: every machine with finite
alphabets has a coding of its configurations (CodingExists.lean); from a coding, a fixed host
machine runs the given machine step by step, with a polynomial-time function before and one
after (Sim.lean); the front end that pads a 3-CNF with four forced variables and writes its compact
code (FrontEnd.lean); a power of the time bound is below c·2^{δn} (Arith.lean) and below the bound
in n at width 3 with a larger constant (ArithRate.lean). Here they are put together. The steps from
«one machine for every δ» to the other four
statements are those of proof/maintheorem/WidthThree/Rates.lean. 

### `everyMachineCanBeWrapped`

 Every machine with finite alphabets can be given a polynomial-time front end and a
polynomial-time last step. 

 ### What a wrapper does on the plain code of a formula 

### `Covers`

 The condition on a time bound T under which the lemma below gives `Sat3.DecidesTM N T`: T n is
at least q·(time + X + 1)^q, where the time is the bound of the wrapped machine with the constants
C₁ and C₂ on a formula with m' ≥ 2 clauses in which n' variables occur,
4 ≤ n' ≤ n + 4, whose compact code has length L, X is the length of the plain code, and L and X are
at most a·(n+2)^d. 

### `decidesTM_of_wraps_counter`

 A wrapper N of a machine M that counts on the compact code within the bound, with «some bit is
1» after it, decides 3-SAT on the plain code within every time bound T that `Covers` allows.
M is used at width 3; the count of `pad4 φ`, written in binary, has a bit 1 if and only if `pad4 φ`
is satisfiable. At width 3 the bound with the constant C is at most the bound for width 3 with the
constant 9·C. 

 ### The main statements 

### `everyWrapperOfACounterDecidesEveryDelta`

 Every wrapper of a machine that counts, with «some bit is 1» after it, decides 3-SAT on the
plain code within c·2^{δn} steps, for every δ > 0: by `wrapped_time_le`, c·2^{δn} covers the time. 

### `everyWrapperOfACounterDecidesAtRateInN`

 Every wrapper of a machine that counts, with «some bit is 1» after it, decides 3-SAT on the
plain code within the bound in n at width 3 with a suitable constant: by `wrapped_time_le_rate`, it
covers the time. 

 ### With the existence of the front end and of the wrapper 

### `lastStepsArePolynomialTime`

 «Nothing» and «some bit is 1» are polynomial-time. 

### `counterCanBeWrappedAndEveryWrapperDecides`

 Existence, by `frontEndExists` and `everyMachineCanBeWrapped`, and the two statements on every
wrapper of a machine that counts. 

 ### The implications between propositions 

### `oneMachineEveryDeltaAndETHFails_of`

 A machine that decides 3-SAT on the plain code within c·2^{δn} steps for every δ > 0 gives the
five statements. 

### `countingBoundImpliesFailureOfETH`

 If the bound for counting holds, so do the five statements: the machine of the hypothesis is
wrapped, and its wrapper decides for every δ, by `counterCanBeWrappedAndEveryWrapperDecides`. 
