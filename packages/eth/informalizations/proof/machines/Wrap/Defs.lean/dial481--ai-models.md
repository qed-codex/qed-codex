---
{
  "module": "proof/machines/Wrap/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From ANY machine that meets the bound for counting to a machine for 3-SAT on the plain input code: definitions and statements

**The sentence answered** (the paper's introduction, after the Main Theorem): «Our main theorem
refutes the exponential time hypothesis».

**The gap.** The proposition `MainTheoremForms.MainTheoremCompact` (the bound for counting, all
widths k) says that SOME machine exists that reads the compact code of a formula.
`Sat3.ThmEveryDelta` and `Sat3.ETH_TM`
speak of machines that read another code, `Sat3.enc φ`, on all formulas. Without a way to put
anything around a machine that is only known to
exist, there is no implication from the first proposition to the second that uses its hypothesis.
This file states such a way (`EveryMachineCanBeWrapped`).

**What is stated here.**
* `Outputs M x y t`: the machine M, started on the bit string x, halts within t steps with the bit
  string y as output.
* `Wraps M pre post N q`: whenever M puts out y on `pre x` within t steps, N puts out `post y` on x
  within q·(t + |x| + 1)^q steps. For all bit strings x, y and all t.
* `EveryMachineCanBeWrapped`: for EVERY machine M with finite alphabets and all polynomial-time
  functions `pre`, `post` on bit strings there are a machine N with finite alphabets and a number q
  with `Wraps M pre post N q`.
* `pad4 φ`: the formula φ on x₀ … x_(n−1) with four more variables x_n … x_(n+3) and the four
  clauses (x_n), …, (x_(n+3)). It is a 3-CNF without repeated clauses if φ is, it has four clauses
  more than φ, between 4 and n + 4 variables occur in it, and it is satisfiable if and only if φ is
  (`Pad4KeepsSatAndMeetsSideConditions`). So the
  side conditions m ≥ 2 and n ≥ 4 of the bound for counting are always met after padding, and no
  small case is left over.
* `MapsPlainToPaddedCompact pre`: `pre` maps `Sat3.enc φ` to the compact code of (3, `pad4 φ`), for
  every 3-CNF φ without repeated clauses. `IsFrontEnd pre`: it is also polynomial-time.
  `FrontEndExists`: there is one.
* `EveryWrapperOfACounterDecidesEveryDelta` (the main statement): let M and C satisfy the body of
  `MainTheoremForms.MainTheoremCompact`. Then EVERY machine N that wraps M (with such a
  `pre` before it and «some bit is 1» after it) decides 3-SAT on `Sat3.enc`, for every n ≥ 0 and
  every 3-CNF on n variables without repeated clauses, with any number of clauses, within c·2^{δn}
  steps for every δ > 0. Nothing is known of N but that it wraps M.
* `EveryWrapperOfACounterDecidesAtRateInN`: such an N even keeps the rate n·log log n/√(log n) in
  the exponent, up to the constant.
* `CounterCanBeWrappedAndEveryWrapperDecides`: existence of a front end and of a wrapper, and the
  statements on every wrapper, in one statement. (A statement «there is an N that wraps M and is
  fast» would be weaker than it looks: such an N could run M and some other fast machine side by
  side. Hence «every N».)
* `CountingBoundImpliesFailureOfETH`: the implication between the propositions.

**What it does not say.** The steps of N are bounded by a polynomial in the steps of M and the
length of the input, so the exponent of the bound is multiplied by a constant q, which may depend on
M, `pre` and `post`. Only the bound in n of the minimum is used; deriving the result for 3-SAT from
the bound
in m together with the Sparsification Lemma would be another route, which is not followed here. The
statements fix what N puts out and a bound on its steps, not the steps themselves. 

 ### A machine around a machine 

### `Outputs`

 The machine M, started on the bit string x, halts within t steps with the bit string y on its
output stack, every other stack empty and its internal state back at the initial one (Mathlib's
`TM2OutputsInTime`). A run that ends in any other way does not count, so
for given M and x there is at most one such y. 

### `Wraps`

 For all bit strings x, y and all t: if M puts out y on `pre x` within t steps, then N puts out
`post y` on x within q·(t + |x| + 1)^q steps. This is asked for every x, whether or not it is the
code of anything. Nothing is asked of N on x if M does not halt in this way
on `pre x`. 

### `EveryMachineCanBeWrapped`

 Every machine with finite alphabets can be given a polynomial-time front end and a
polynomial-time last step: for all such M, `pre`, `post` there are a machine N with finite alphabets
and a number q with `Wraps M pre post N q`. «Polynomial-time» is `Groundwork.PolyT`
(proof/machines/ToTuring/PolyT.lean), the notion of this development: computed by a program fragment
on a fixed machine with four stacks, within a polynomial in the length of the word that stands for
the argument. 

 ### The front end for 3-SAT 

### `pad4`

 φ with four more variables x_n, …, x_(n+3) and the four clauses (x_n), …, (x_(n+3)) behind its
own clauses. 

### `Pad4KeepsSatAndMeetsSideConditions`

 For every n ≥ 0 and every 3-CNF φ on n variables without repeated clauses: `pad4 φ` is a 3-CNF
without repeated clauses; it has four clauses more than φ; at least 4 and at most n + 4 variables
occur in it; it is satisfiable if and only if φ is. 

### `MapsPlainToPaddedCompact`

 `pre` maps the plain code of φ to the compact code of (3, `pad4 φ`), for every n ≥ 0 and every
3-CNF φ on n variables without repeated clauses. Nothing is asked of `pre` on other bit strings. 

### `IsFrontEnd`

 `pre` is polynomial-time and maps plain codes to compact codes of padded formulas. 

### `FrontEndExists`

 There is a front end. 

### `someBit`

 The one bit «some bit of w is 1». 

 ### The body of a proposition of `MainTheoremFormsStatement.lean`, for a given machine and constant 

### `CountsCompactKCNFWithinMinBound`

 The body of `MainTheoremForms.MainTheoremCompact`: for every k ≥ 1 and every k-CNF φ with m ≥ 2
clauses in which n ≥ 4 variables occur, M, started on the compact code of (k, φ), puts out the
number of satisfying assignments of these n variables within
2^{C·min{km/√(log m), k²·n·log log n/√(log n)}} + C·(length of the compact code)^C steps. 

 ### The statements for an arbitrary machine 

### `DecidesEveryDelta`

 N decides 3-SAT on the plain code (`Sat3.DecidesTM`: every n ≥ 0, every 3-CNF on n variables
without repeated clauses, any number of clauses, variables need not occur) within c·2^{δn} steps,
for every δ > 0; only c depends on δ. 

### `DecidesAtRateInN`

 N decides 3-SAT on the plain code, for every n ≥ 0, within c·2^{9c·n·log₂
log₂(n+4)/√(log₂(n+4))} steps, for some constant c: the bound in n for all widths of this
development (`SatM.boundNK`) at k = 3. n is the number of all variables. 

### `EveryWrapperOfACounterDecidesEveryDelta`

 The main statement. Let `pre` map plain codes to compact codes of padded formulas, and let M,
with the constant C, count on the compact code, for all widths, as in the body of
`MainTheoremForms.MainTheoremCompact`. Then EVERY machine N that wraps M,
with `pre` before it and «some bit is 1» after it, decides 3-SAT on the plain code within c·2^{δn}
steps for every δ > 0. Of the hypothesis on M only the case k = 3 is needed. 

### `EveryWrapperOfACounterDecidesAtRateInN`

 Under the hypotheses of `EveryWrapperOfACounterDecidesEveryDelta`, every machine N that wraps M
decides 3-SAT on the plain code within c·2^{9c·n·log₂ log₂(n+4)/√(log₂(n+4))} steps for some c. 

### `LastStepsArePolynomialTime`

 The last steps «nothing» and «some bit is 1» are polynomial-time, so `EveryMachineCanBeWrapped`
applies with them. 

### `CounterCanBeWrappedAndEveryWrapperDecides`

 Existence and the main statements in one, for M with finite alphabets that counts as in the body
of `MainTheoremForms.MainTheoremCompact`, with «some bit is 1» after M. 

 ### The implication between propositions 

### `OneMachineEveryDeltaAndETHFails`

 Five statements: one machine decides 3-SAT within c·2^{δn} steps for every δ > 0
(`Sat3.SubexpTM`); for every δ > 0 a machine does (`Sat3.ThmEveryDelta`,
`PaperSentences.ThmEveryDelta`); the exponential time hypothesis fails (`Sat3.ETH_TM`,
`PaperSentences.ETH`). 

### `CountingBoundImpliesFailureOfETH`

 If the bound for counting holds (`MainTheoremForms.MainTheoremCompact`), so do the five
statements. What an arbitrary machine as in the hypothesis gives is said by
`CounterCanBeWrappedAndEveryWrapperDecides`. 
