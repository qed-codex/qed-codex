---
{
  "module": "proof/variables/VariableBound/Search/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 2 of Appendix D as a program: the search for the checks

«Algorithm: start with the empty list; while X(𝓛) > 0, replace 𝓛 by the list (𝓛, Γ_u), u ∈ Ω, with
the smallest Υ; then output F(𝓛).» A check is a list of numbers of clauses, a list of checks a list
of such
lists. The program is generic in the function `evX` that returns X(𝓛) and in the list `fam` of the
candidates Γ_u; proof/variables/VariableBound/Count puts in the sums over the networks of Step 3 and
the family of Lemma 13.
«The number Υ is a rational with polynomially many bits, so the comparisons are exact»: all
candidates of one round have the same number of checks, so their Υ have a common denominator, and
the program compares the
numerators, which are integers (`upsNum`). The loop runs r̄ rounds and does nothing once X(𝓛) = 0.
The list is cut off by the pad after every round, so that the program is polynomial-time in the pad
with no side
condition; the cut-off does nothing if the pad is long enough.
This file has definitions only. The statements are propositions;
proof/variables/VariableBound/Search proves them. 

### `chksD`

 A list of checks, given by numbers of clauses, as a list of sets of clauses. 

### `loadSum`

 Σ_E 2^load(E). 

### `upsNum`

 The numerator of Υ(𝓛) over the denominator 3^r·2^(β−1)·2^t̄·(15n̄)^(r̄−r), for a list 𝓛 of r ≤
r̄ checks with X(𝓛) = x. 

### `argminD`

 The first member of the list with the smallest key; the default [] on the empty list. 

### `roundD`

 One round: nothing if X(𝓛) = 0; otherwise the candidate with the smallest Υ is appended. 

### `searchD`

 The search: r̄ rounds from the empty list. 

### `StructD`

 The conditions of Step 2 of Appendix D on a list of checks, here given by numbers: r ≤ r̄
checks, each an increasing list of at most s̄ = 16m/n̄ numbers below m, and load(E) ≤ t̄ + 2 for
every clause E. 

### `StSearchD`

 The search is right. X has at most 2^n elements; β, r̄, t̄ are the parameters of «Setting and
parameters» in Appendix D, for m clauses and n̄ ≥ 1; the candidates are increasing lists of numbers
below m, the list of candidates is not empty, and
they have (a), (b), (c) of Lemma 13 for v = n̄; `evX` returns X(𝓛) on every list that satisfies
`StructD`; the word of every such list fits under the pad. Then the list found satisfies `StructD`
and X = 0. 

### `StCertSearchD`

 The search is polynomial-time in the pad, jointly in everything it reads, if `evX` is; m, n̄, β,
r̄, t̄ are given in unary. 
