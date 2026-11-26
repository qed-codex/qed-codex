---
{
  "module": "proof/rates/GeneralPieces/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix A, with case (ii) of Lemma 8: definitions and interface statements

Here the programs of the recursion are analysed as in the paper: groups of exactly g/K nodes,
Hoeffding's inequality for sampling without replacement, and every x₀ ≥ 18 with 2^x₀ ≥ c + 5.
Nothing is proved and nothing is assumed in this file:
`St… : Prop` are statements; one file proves each, and a file that needs one takes it as a
hypothesis. 

### `StCaseII`

 The existence claim in the proof of Lemma 8, case (ii): if K divides g, every node shares at
most P bits in all and at most P/g bits with any other node,
and 2ζ²g ≥ K·ln(2gK), then some grouping has exactly g/K nodes in every group and, for any two
different groups, the sum Y of c_ab over a in one and b in the other is < (U + 2ζgP)/K². Here U =
Σ_a Σ_{b ≠ a} c_ab. 

### `zetaOf`

 ζ of a step, 3/(2D). With it, the error term 3p²M/(D·K²) of the label length one level down
(`lamNextG`; M = d²·m·λ, so that p·M is the paper's P) is 2ζ·p·(pM)/K², the paper's 2ζgP/K². 

### `LevelOK2`

 What the proof needs of one step at the label length lam: the pieces are pieces there, K ≥ 2
divides p, the condition of case (ii) of Lemma 8 holds with ζ = `zetaOf s`,
the grid is square, and the total of every pattern is at most the program's bound: `ubarG`, or
2·`ebarG` for a pattern with `s.thin && colSide` true. 

### `StExpandG2`

 One level: if the step is in order (`LevelOK2`) and the pad is long enough, d^{|R|} times the
value of the instance is an integer plus the sum of the values of the instances one level down;
these are well
formed with label length `lamNextG` and bound `bNextG`, there are at most `nPat` of them, and the
integer is bounded. 

### `ChainG2`

 The schedule is a chain of steps p·d → K that ends at K₀ nodes, and every step is in order
(`LevelOK2`) at its label length. 

### `StSolveG2`

 All levels: if every step of the schedule is in order and the pad is long enough, `solveG`
returns the value of the instance. 

### `StChain2`

 Every step of the schedule is in order at every label length, for pieces whose numbers of bits
are at most 2λ and every x₀ of Theorem A. 

### `StRate2`

 Part (b) of Theorem A as an inequality for the exponent of the pad, for every x₀ ≥ 18 with 2^x₀
≥ c + 5; C₀ depends on c only. 

### `StSeq2`

 Parts (a) and (b) in the form that the top levels use, for every x₀ of Theorem A. (Here C₀ may
depend on P, ρ and x₀; `StRate2` gives one that depends on c only.) 
