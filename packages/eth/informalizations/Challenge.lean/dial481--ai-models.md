---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 What is claimed: 2 theorems, with `sorry` in place of their proofs.
This file imports `MainResults.lean` alone, and that file imports Mathlib alone. So whoever has read `MainResults.lean` knows all that the two statements mean. Nothing imports this file. 

### `MainResults.ethIsFalse`

 **The Exponential Time Hypothesis is false.** Let s₃ be the infimum of all δ ≥ 0 such that some deterministic Turing machine decides 3-SAT on n variables, with any number of clauses, none written twice, within c·2^{δn} steps for some constant c and every n. The hypothesis (Impagliazzo and Paturi) says s₃ > 0. The theorem says that this fails: s₃ = 0, that is, for every δ > 0 there is such a machine. Its proof derives it from the Main Theorem by two arguments, each proved for every machine that has the bound of the Main Theorem. 

### `MainResults.mainTheorem`

 **The Main Theorem.** There are ONE deterministic multi-stack Turing machine (Mathlib's `Turing.FinTM2`, all stack alphabets finite) and ONE constant C, both chosen before k and the formula, such that: for every k ≥ 1, every n ≥ 4 and every formula φ on the variables x₀ … x_{n−1}, each of which occurs in φ, with at most k literals in each clause, no clause written twice and m ≥ 2 clauses, the machine, started on the code of (k, φ), halts with the number of satisfying assignments of φ, in n + 1 bits, lowest bit first, after at most 2^{C·min{km/√(log m), k²·n·log log n/√(log n)}} steps. Here log is log₂ and the power of 2 is rounded down; nothing is added to it. The code is 1ᵏ 0 1ⁿ 0, then for each clause k positions of ⌊log₂ (2n)⌋ + 1 bits. 
