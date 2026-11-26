---
{
  "module": "proof/consequences/FromPrinted/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 7 on the machines of proof/threesat/Printed/: sets of size s and colorings, with the machines named

«Add the clause {¬x_u, ¬x_v} for each edge uv; Corollary 6 then counts the independent sets of size
s. The cliques of size s are the independent sets of size s of the complement graph, and the vertex
covers of size s are the complements of the independent sets of size n − s.»
The counts come from `FromPrinted.SplitCount.stEngineCounts`; the bounds on states and steps use
`size_square` and `steps_double` of proof/consequences/Consequences/Sets.lean.
* `SIZED_counts`: for every width w and δ > 0 some `SIZED w ℓ τ` has polynomial-time steps and
  counts the satisfying assignments with exactly s true variables: `SizeCircuit.stSizedFromEngines`
  for the family `FromPrinted.SplitCount.ENGINEsplit` and the circuits `SizeCircuit.sizeGates`
  (`SizeCircuit.stSizeGates`).
* `stSetsCounted`: that machine at width 2 after the three readers; for cliques and vertex covers by
  `Complement.stCounts`.
* `stColoringsCounted`: `Eight.ViaGrouping.COLOR_counts_of` for the family `ENGINEsplit`. 

### `SIZED_counts`

 For every width w and δ > 0 there are ℓ, τ such that `SIZED w ℓ τ` has polynomial-time steps and
returns, on (n in unary, s, ψ) for s ≤ n and ψ of width at most w on x₀ … xₙ₋₁, the number of
satisfying assignments of ψ with exactly s true variables, within c·2^{δn} steps, on states of size
at most c·(n + number of clauses + 2)^c. 

### `stSetsCounted`

 **Independent sets, cliques, vertex covers of size s, with the machines named.** For every δ > 0
there are ℓ, τ, c such that `SIZED 2 ℓ τ`, put after the reader of the formula for independent sets,
after `readClique` and after `readCover`, has polynomial-time steps and returns the three numbers
within c·2^{δn} steps, on states of size at most c·(n+2)^c. 

### `stColoringsCounted`

 **Proper colorings with k colors, with the machine named.** For every k ≥ 3 and δ > 0 there are
ℓ, τ, c such that the reader `readC k` followed by `ENGINEsplit (max k 2) ℓ τ` has polynomial-time
steps and returns, on the code of a graph G on n vertices, the number of proper colorings of G with
k colors in n·k + 1 bits, within c·2^{δn} steps, on states of size at most c·(n+2)^c. 
