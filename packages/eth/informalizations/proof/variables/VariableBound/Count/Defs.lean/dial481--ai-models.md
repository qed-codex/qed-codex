---
{
  "module": "proof/variables/VariableBound/Count/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One sparse formula counted as in Steps 1 to 4 of Appendix D: the program and its interface statements

ψ has m clauses of 1 to k literals on n variables, and every variable occurs in at most Δ clauses.
The program computes the parameters n̄, β, r̄, M, t̄ defined under «Setting and parameters» in
Appendix D. If m ≤ n̄, it outputs F of the empty list. Otherwise it lists the
family of Lemma 13 for v = n̄, finds the checks by the search of Step 2, in which X(𝓛) is computed
by the networks of Step 3 through a clique solver, and outputs F(𝓛).
This file has definitions only. The statements are propositions; proof/variables/VariableBound/Count
proves them. 

### `countD`

 The count of Steps 1 to 4 for ψ on n variables; under the hypotheses of `StCountD` it is the
number of satisfying assignments among the 2ⁿ assignments. 

### `FitsD`

 What the count of one formula needs of the length of the pad, written F here (not the count F(𝓛)
of Step 1): it must be at least the bounds below for the networks, the list of profiles and the list
of checks. None of the three depends on the formula. 

### `StCountD`

 Steps 1 to 4: the count is right. Hypotheses: the clique solver S is correct (`S.Correct ok`) at
the index i (`ok i`) and has K ≥ 2 there; every clause of ψ has 1 to k literals on the variables 0,
…, n − 1 (`WfL`); every variable occurs in
at most Δ clauses; m ≤ Δ·n; 2 ≤ Δ; n ≥ 29·⌈log₂(2Δ)⌉ + 19 (with the inequalities of «Setting and
parameters» in Appendix D this gives n ≥ 2·log(2Δ), r̄ ≤ 10n and M ≤ 14n); and the pad fits
(`FitsD`). 

### `StCertCountD`

 For every polynomial-time clique solver (`S.Poly`), the count of one sparse formula is
polynomial-time, jointly in its input: the width k, given in unary as the first component; then the
pad, the index, (n, Δ) in unary and the formula. 
