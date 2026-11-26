---
{
  "module": "proof/statements/KSatFreeCodeStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/KSatFreeCodeStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/KSatFreeCodeStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 with a code of the formula that does not mention k (definitions only)

`KSatStatement.lean` writes an instance of k-SAT with «k slots per clause», so one and the same
formula has different codes as a k-CNF and as a (k+1)-CNF, and the paper's sentence «A k-CNF is also
a (k+1)-CNF, so s_k ≤ s_{k+1}» (after Definition 6) cannot be proved there for the paper's reason.
Here the code does not depend on k: every clause is written with its own literals and an end mark.
Then a machine that decides (k+1)-SAT IS a machine that decides k-SAT.
This file has no theorem and imports only `KSatStatement.lean` (and through it
`ThreeSatStatement.lean`) and Mathlib. From these two files come: `Sat3.CNF n` (a list of clauses, a
clause a list of literals, a literal a variable in `Fin n` with the value that makes it true),
`Sat3.Satisfiable`,
`Sat3.slot` (a literal as a number: 2i+1 = ¬xᵢ, 2i+2 = xᵢ), `SatK.IsKCNF k φ` (at most k literals
per clause, no clause written twice).

## How to read it
* `enc φ`: 1ⁿ 0; then for each clause: 1, then for each of its literals 1 followed by the literal's
  number in ⌊log₂(2n)⌋ + 1 bits, low bit first, then 0; at the end of the formula 0. Example: n = 2,
  φ = (x₀ ∨ ¬x₁): ⌊log₂ 4⌋ + 1 = 3 bits; x₀ is 2 = 010 (low bit first), ¬x₁ is 3 = 110; the code is
  11 0 · 1 · 1 010 · 1 110 · 0 · 0.
  The code tells where it ends, so that further bits can follow it (used for random bits below).
* `DecidesTM k M t`, `InTime k δ`, `s k`: as `SatK.DecidesTM`, `SatK.InTimeTM`, `SatK.sTM` of
  `KSatStatement.lean`, with this code. «A deterministic algorithm» is a Turing machine of Mathlib
  with finite alphabets; time is its number of steps; n is the number of variables.
* `sInfty`, `ETH`, `SETH`: the paper's words. `SETH` is the paper's «s_∞ = 1»; by `AtMostOne` it is
  the same as «s_∞ ≥ 1»; `KSatStatement.lean` negates the analogous form for its own numbers
  `SatK.sTM k` (a code with k slots per clause, supremum over k ≥ 1).
* `DecidesRandTM p k M r t`: a randomized algorithm with error at most p. The machine gets the code
  of the formula followed by r(n) random bits. A machine of Mathlib halts with its output alone on
  its stacks, so it takes every random bit off the input (all but possibly the last, if the input
  stack is also the output stack). For EVERY string of random bits it halts within t(n) steps with
  one bit as output; for at least the fraction 1 − p of the strings the bit is right. With r = 0 the
  input is the code alone: «A deterministic algorithm is a randomized algorithm that uses no random
  bits».
  In `InTimeRand` the number of random bits is r(n) = ⌊a·2^{βn}⌋ for a natural number a and a
  rational β ≥ 0 that are fixed with the machine (a = 0: no random bits). A free function r would be
  a loophole: the machine can count the random bits, so it could read advice about n off their
  number. β is rational, not real, for the same reason: the digits of a real β could carry advice.
  `sRand p k` is s_k with such algorithms.

## Where it differs from the paper
* The paper fixes no code and no machine model. The paper's s_k is a real number; here it lies in
  [0, ∞] and is ∞ if no δ works.
* Lists for sets, as in `KSatStatement.lean`: the empty clause and repeated literals are allowed,
  and the same literals in another order count as another clause.
* n is the declared number of variables x₀ … xₙ₋₁, not the number of those that occur. The time is
  bounded in n alone; this makes sense only because `IsKCNF` forbids repeated clauses, so that for
  fixed k the code of a k-CNF on n variables has length polynomial in n.
* k ranges over all natural numbers; the paper has k ≥ 1. At k = 0 this code still tells the formula
  without clauses from the one with the empty clause.
* The paper's O(2^{δn}) is written with one constant c for every n.
* The literature's randomized conventions differ in the error that they allow; p is a parameter here
  (p = 1/3 is bounded two-sided error, p = 0 no error at all). Only 0 ≤ p < 1/2 is a meaningful
  convention: for p ≥ 1/2 a machine that puts out its first random bit meets the definition, so that
  sRand p k = 0 for a trivial reason. `RandomnessHelps` and `AllZeroRandomized` are stated for all p
  ≥ 0; their case p = 0 implies the others, because an algorithm with error at most 0 has error at
  most p.
  One-sided error, and algorithms whose running time is bounded only in expectation, are not written
  separately; a deterministic machine is each of these. The random bits follow the code on the
  input, so a machine meets them in order, after the code, and must take all of them off, which
  costs steps. A machine of the usual kind, which flips at most O(2^{δn}) coins, fits this form once
  its number of coins is rounded up to ⌊a·2^{βn}⌋ for a rational β a little above δ: it moves the
  code aside, reads coins as it needs them and takes the unused rest off at the end, in time
  O(2^{βn}).
  So `sRand p k` is the usual s_k for randomized algorithms with error p (standard; not proved
  here).
* Corollary 5 here (`AllZero`) is proved along the reduction that its printed proof cites: the
  algorithm of Theorem 2, run on the 3-CNFs obtained by sparsifying and splitting long clauses. The
  statements that tie it to that route are in proof/consequences/FreeCode/Defs.lean (this file
  imports only `KSatStatement.lean`, so it cannot name the machines).
  The implication «s_3 = 0 implies s_k = 0» that the paper cites from Impagliazzo, Paturi and Zane,
  the equivalence cited from Impagliazzo and Paturi, and «SETH implies ETH» are not stated. As
  propositions about the numbers s k they follow at once from `AllZero` and would show nothing.
  Their content is a statement about every algorithm for 3-SAT, and that would need a machine that
  calls an arbitrary Turing machine once per leaf without loss in the exponent.
  For machines cut into steps that content is `SplitSat.StImplication`
  (proof/consequences/SplitSat/Defs.lean).
* `AtMostOne`, `LimitAndEth` and `SethGivesSomeK` would also follow from `AllZero`. So that the
  paper's reasons can be seen, each has a companion that cannot be had that way: `BruteForce` (a
  machine), `HenceForEverySequence` and `SupOneGivesPositive` (for every nondecreasing sequence, not
  only for s).
* How `s k` here and `SatK.sTM k` are related for arbitrary machines is not stated: it would need a
  re-coding machine in front of an arbitrary machine without loss in the exponent. 

 ### The code 

### `encLit`

 A literal: its number in ⌊log₂(2n)⌋ + 1 bits, low bit first. 

### `encClause`

 A clause: 1, then 1 and the literal for each of its literals, then 0. 

### `enc`

 A formula: 1ⁿ 0, its clauses, 0. 

 ### Definition 6 

### `DecidesTM`

 `M`, started on the code of a k-CNF on n variables, halts within `t n` steps with the bit
«satisfiable» as output. 

### `InTime`

 «some deterministic algorithm decides k-SAT on n variables in time O(2^{δn})»: one machine,
finite alphabets, one constant. 

### `s`

 «Let s_k be the infimum of all δ ≥ 0 such that some deterministic algorithm decides k-SAT on n
variables in time O(2^{δn})» (∞ if there is no such δ). 

### `sInfty`

 «and let s_∞ = sup_{k≥3} s_k.» 

### `ETH`

 «The Exponential Time Hypothesis (ETH) is the statement that s_k > 0 for all k ≥ 3.» 

### `SETH`

 «The Strong Exponential Time Hypothesis (SETH) is the statement s_∞ = 1.» 

 ### Randomized algorithms 

### `DecidesRandTM`

 A randomized algorithm for k-SAT with error at most p, r(n) random bits and time t(n). 

### `InTimeRand`

 Some randomized algorithm with error at most p decides k-SAT on n variables in time O(2^{δn}):
one machine, finite alphabets, one constant c; the number of random bits is ⌊a·2^{βn}⌋, with a
natural number a and a rational β ≥ 0 fixed with the machine, so that it tells the machine nothing
that it could not compute itself. 

### `sRand`

 s_k with randomized algorithms with error at most p. 

 ### The paper's sentences 

### `CodeReadable`

 The code determines the number of variables and the formula, and it tells where it ends:
whatever bits follow it can be read off. 

### `BruteForce`

 «Trying all assignments»: ONE machine decides k-SAT for every k, within c·(n+2)^c·2^n steps,
with c depending on k. 

### `AtMostOne`

 «Trying all assignments gives s_k ≤ 1, so s_∞ ≤ 1.» Proved from `BruteForce`, not from
`AllZero`. 

### `SameMachine`

 «A k-CNF is also a (k+1)-CNF»: a machine that decides (k+1)-SAT decides k-SAT, in the same time. 

### `Increasing`

 «so s_k ≤ s_{k+1}.» 

### `HenceForEverySequence`

 The paper's «Hence», for EVERY nondecreasing sequence u in [0, ∞] in the place of s: it tends to
sup_{k≥3} u_k, and «u_k > 0 for all k ≥ 3» is the same as u_3 > 0. 

### `LimitAndEth`

 «Hence s_∞ = lim_{k→∞} s_k, and ETH is the same as s_3 > 0.» Proved from `Increasing` and
`HenceForEverySequence`, not from `AllZero`. 

### `DeterministicIsRandomized`

 «A deterministic algorithm is a randomized algorithm that uses no random bits»: a machine that
decides k-SAT in time t is a randomized algorithm with no random bits and no error. 

### `RandomnessHelps`

 «so allowing randomness can only make s_k smaller». 

### `AllZero`

 Corollary 5: «s_k = 0 for every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false.» 

### `AllZeroRandomized`

 «and Corollary 5 holds under each of these conventions.» 

### `SupOneGivesPositive`

 For EVERY sequence u in [0, ∞]: if sup_{k≥3} u_k = 1 then u_k > 0 for some k ≥ 3. 

### `SethGivesSomeK`

 In the proof of Corollary 5: «s_∞ = 1 gives s_k > 0 for some k»; immediate from the definition
of `sInfty`. (The next step, «hence s_3 > 0», is the cited theorem for arbitrary algorithms and is
not among these statements.) 
