---
{
  "module": "proof/rates/GeneralPieces/Tied/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Tied/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Tied/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parts (b) and (c) of Theorem A, for named programs: definitions and statements only

`AppRunningTime.PartB` and `SatM.CountInRate` say "there is a program" and "there is a machine";
they do not name the recursion, so by their wording they say nothing about the route of a proof. The
statements of this file name
the programs: the recursion `solveG` on the schedule of display (40) with the x₀ of the theorem,
every step of which meets the hypotheses of case (ii) of Lemma 8, and the top
level `AM` with its exponent `eM`, run on that recursion. These statements name the programs and
their parameters; a statement cannot name a proof. That the proof given in this folder goes through
case (ii) of
Lemma 8 is seen in the proofs (`GeneralPieces.Level.child_spec2` calls
`GeneralPieces.Level.cases_ii` and `GeneralPieces.grouping_general`).
The program `runB` and the exponent `needB` are functions of the programs of the pieces and of x₀
only:
«The algorithm uses … neither ρ nor e_ℓ.» Nothing is proved here. 

### `x₀Of`

 The least integer x₀ ≥ 18 with 2^x₀ ≥ c + 5. 

### `runB`

 The program of part (b), a function of (pad, ℓ in unary, instance): with K the number of rows of
the instance, `ClauseBound.Gen.Pick.pick` builds the schedule of the largest level with at most K
nodes, and `solveG` descends
along it. The ℓ of the input is not read. 

### `needB`

 The logarithm of the number of units that the pad must have at level ℓ. 

### `PartB`

 Part (b) for the named program. 

### `PartB.poly`

 the program is polynomial-time in (pad, ℓ, instance) 

### `PartB.sched_eq`

 on a (K_ℓ, λ)-clique it is the recursion on the schedule of display (40), from K_ℓ nodes down
  to K₀ nodes (`sched P x₀ ℓ` is, by definition, the list step ℓ−1, …, step 0) 

### `PartB.step_eq`

 the step from K_{ℓ+1} = g_ℓ² nodes to K_ℓ nodes has the numbers of display (40) 

### `PartB.caseII`

 and meets the hypotheses of case (ii) of Lemma 8 (fields `dvd` and `hoeffding` of `LevelOK2`)
  at every label length 

### `PartB.value`

 the program returns the value of the clique if the pad has 2^needB units 

### `PartB.rate`

 2^needB ≤ 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ + B))^{C₀K_ℓ²} 

### `TopM`

 The bound in m for the named top level: the function `AM S pick` of (input, pad) and the
exponent `eM S pick` of the input, for an algorithm S for cliques and a way to pick its level. 

### `TopM.poly_A`

 both are polynomial-time 

### `TopM.correct`

 the function returns the number of satisfying assignments, in n + 1 bits, if the pad has 2^eM
  units 

### `TopM.rate`

 the exponent is O(k·m·r(m)), the O not depending on k 

### `TopM.machine`

 one machine computes, on every input x, the named function at (x, 2^{eM x} units) within
  q·(|x| + 2^{eM x} + 1)^q steps, and it counts within C·2^{C·k·m·r(m)} steps 

### `PartCm`

 Part (c), first sentence, for the named programs: the top level in m, run on the recursion of
part (b) for the pieces P with the schedule of display (40) for x₀. 
