---
{
  "module": "proof/rates/GeneralPieces/Tied/BoundDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Tied/BoundDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Tied/BoundDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Part (c), first sentence, of the theorem on the general recursion, and the bound in m, for named programs, from pieces as the appendix defines them: definitions and statements only

`AppRunningTime.ThmRunningTime` and `AppRunningTime.BoundInM` say "there is a program" and "there is
a machine". The statements of this file name the programs. `ThmRunningTimeCm` is part (c), first
sentence, for the recursion on the
schedule of display (40), for EVERY x₀ of the theorem; `BoundInM` is the bound in m for the top
level in m (`AM`, `eM`) on that recursion, with the least x₀ of the theorem, on programs for the
pieces of Appendix B.
What they pin down. `BoundInM` names the algorithm (`solveG` on the schedule of display (40), `AM`),
not the argument of case (ii) of the lemma on groupings with explicit cost: it leaves the constant c
free.
The argument of case (ii) is what `GeneralPieces.StCaseII` and
`GeneralPieces.StSolveG2` (whose `ChainG2` has no counting condition) are about. `ThmRunningTimeCm`
speaks of every x₀ ≥ 18 with 2^x₀ ≥ c + 5.
Nothing is proved in this file; the two operations on programs that it names, `GeneralPieces.trimV`
("we may and do assume c^row, c^col ≤ 2λ") and `GeneralPieces.atZero` (the form that the recursion
reads), are defined in the imported file
`proof/rates/GeneralPieces/DefGenPieces/Progs.lean`, which holds definitions only. 

### `IsPiecesB`

 (P, A, val) are the pieces of the proof of the theorem on pieces with ρ = 1/√2, with the
constant c: the body of `AppRunningTime.ThmHalfPieces`, word for word. 

### `recOf`

 The programs that the recursion runs on, for pieces (P, val) with the constant c. 

### `ThmRunningTimeCm`

 Part (c), first sentence, for the named programs: for all pieces with parameters (ρ, c) and
every x₀ ≥ 18 with 2^x₀ ≥ c + 5, `PartCm` holds of the top level in m on the recursion on these
pieces. 

### `BoundInM`

 The bound in m for the named programs: for some programs (P, val) for the pieces of Appendix B,
with a constant c, the top level in m on the recursion for `recOf P val c` with x₀ = `x₀Of c` is
polynomial-time, counts
the satisfying assignments once the pad has 2^eM units, has eM = O(km/√(log m)), and one machine
computes it on every input and so counts within C·2^{C·km/√(log₂(m+2))} steps. 
