---
{
  "module": "proof/consequences/Sat3Graph/Ask.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Ask.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Ask.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7 for deciding: one question to the procedure for 3-SAT

Proof of `StAskSized` of proof/consequences/Sat3Graph/Defs.lean. On (n in unary, s, ψ) the machine
`askSized gates D` puts Γ beside ψ, splits every long clause and asks D.
* The 3-CNF has N = (variables of Γ) + (new variables) variables. Γ has at most (a+1)·(n+1)
  variables (`SizeCircuit.numVars_le`). The clauses of Γ have at most 3 literals and need no new
  variable; those of ψ need at most (w − 3)·|ψ| ≤ B·(n+1). So N ≤ (a+1+B)·(n+1): a 3-CNF on O(n)
  variables.
* The 3-CNF is satisfiable exactly if ψ ∧ Γ is (`splitN_spec`), that is if the number of satisfying
  assignments of ψ ∧ Γ is not 0, and this number is that of the satisfying assignments of ψ with
  exactly s true variables (`SizeCircuit.stGammaCount`, a statement on numbers; `askSized gates D`
  runs no machine but D). 

### `withGamma_replicate`

 What `withGamma` hands over on (n in unary, s, ψ). 

### `stAskSized`

 **`StAskSized`.** Let gates test the size with at most a·(n+1) gates, and let D decide 3-SAT
with an exponent δ₃ ≥ 0 such that δ₃·(a + 1 + B) ≤ δ. On (n in unary, s, ψ), for s ≤ n and ψ of
width at most w on x₀ … xₙ₋₁ with (w − 3)·|ψ| ≤ B·(n+1), `askSized gates D` says, within c'·2^{δn}
steps and on states of size at most c'·(n+2)^{c'}, whether ψ has a satisfying assignment with
exactly s true variables. 
