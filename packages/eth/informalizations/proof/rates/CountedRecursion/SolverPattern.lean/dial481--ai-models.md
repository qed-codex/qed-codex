---
{
  "module": "proof/rates/CountedRecursion/SolverPattern.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverPattern.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverPattern.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One pattern (a pattern is one function ι : ℛ → 𝓘 of the proof of Theorem A(b), numbered by y < |𝓘|^{|ℛ|})

«Case (ii) of Lemma 8 applies to the network with the smaller total»: `patternValue c` is the
procedure of that lemma up to the call (`groupingCall`), and its call is passed on as a call of the
solver.
* `patternValue_within`: the rule of substitution (`QueryMachines.StSubstWithin`) for this machine:
  the call costs two operations more.
* `K_succ_mul`, `two_le_K`, `rK_ready`, `rG_ready`, `nPatterns_ready`, `tables_lt`: the numbers of a
  level, and what the solver holds when the loop begins.
* `pattern_input`: what the solver hands to the procedure is the input that belongs to ζ = 2^{−ℓ−5},
  K_ℓ and the network of the pattern; the label length that the procedure computes is the L of the
  lemma, and L ≤ 3gP.
The context of the call written out (`child_eq`) and the run for one pattern (`pattern_run`) are in
SolverCall.lean. 

### `patternValue_within`

 The call of the procedure of the lemma is passed on as a call of the solver, at two operations
more. 

 ### The numbers of a level 

### `K_succ_mul`

 K_{ℓ+1} = g_ℓ². 

### `two_le_K`

 K_ℓ ≥ 2. 

### `rK_ready`

 The K that the solver holds. 

### `rG_ready`

 The g that the solver holds. 

### `nPatterns_ready`

 The number of patterns: |𝓘|^{|ℛ|}. 

### `tables_lt`

 The tables of a well-formed instance of the level ℓ + 1, read back from the oracle: |W_w| < 2^B
on the g² nodes. 

### `lof_le`

 L ≤ 3gP, crudely. 

### `total_le_gP`

 U ≤ gP, by (i) of Definition 2. 

 ### What is handed to the procedure of the lemma 

### `pattern_input`

 The network of the pattern y is a network with P = g³λ and B₁; the solver hands over the input
that belongs to it, with ζ = 1/2^{ℓ+5} and K_ℓ; the label length computed from it is the L of the
lemma; and L ≤ 3gP. 
