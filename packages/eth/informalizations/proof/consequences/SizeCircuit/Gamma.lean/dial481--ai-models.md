---
{
  "module": "proof/consequences/SizeCircuit/Gamma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Gamma.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Gamma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the 3-CNF Γ

Proofs of `StGamma` and `StGammaCount` of proof/consequences/SizeCircuit/Defs.lean. The paper: «a
new variable for each gate, clauses of at most 3 literals that force it to equal the value of the
gate, and a clause that makes the output true give a 3-CNF Γ with O(n) variables and O(n) clauses.
Each S of size s extends to exactly one satisfying assignment of Γ, and no other S to any.»

Both follow from `stUniqueExtension` (General.lean): the clauses of the gates have exactly one
extension of every S, and in it the variable of the output has the value of the circuit, which is 1
exactly if |S| = s. The count: an assignment that satisfies ψ ∧ Γ is sent to its part on x₀ … xₙ₋₁;
this is one to one and onto the assignments that satisfy ψ and make exactly s variables true. 

 ### The shape of the formula 

### `var_gateClauses`

 The variables of the four clauses of a gate are the two wires that it reads and its own wire. 

### `shaped_zipIdx`

 The clauses of the gates of K, numbered from j on, have at most 3 literals and variables below n +
j + (number of gates), if the gates read earlier wires only. 

### `length_zipIdx`

 Four clauses for every gate. 

### `length_formulaOf`

 Four clauses for every gate and one for the output. 

### `shaped_formulaOf`

 The formula of a non-empty circuit whose gates read earlier wires only is a 3-CNF on the
variables of the wires. 

### `holds_formulaOf`

 The formula holds exactly if the clauses of the gates hold and the variable of the output is 1. 

 ### Words and sets 

### `count_ofFn`

 The number of ones of the word of x is the number of places where x is 1. 

 ### Γ 

### `stGamma`

 **`StGamma`.** «give a 3-CNF Γ with O(n) variables and O(n) clauses. Each S of size s extends to
exactly one satisfying assignment of Γ, and no other S to any.» For every family of circuits that
tests the size with at most a·(n+1) gates, and n ≥ 1: Γ is a 3-CNF on n + (number of gates) ≤
(a+1)·(n+1) variables with at most 4a·(n+1) + 1 clauses; an assignment x of x₀ … xₙ₋₁ with exactly s
ones has exactly one extension that satisfies Γ, and every other x has none. 

### `holds_restrict`

 A formula on x₀ … xₙ₋₁ holds under an assignment on more variables exactly if it holds under its
part on x₀ … xₙ₋₁. 

### `stGammaCount`

 **`StGammaCount`.** A formula ψ on x₀ … xₙ₋₁ together with Γ has as many satisfying assignments
as ψ has satisfying assignments with exactly s true variables. For every n, also n = 0. 
