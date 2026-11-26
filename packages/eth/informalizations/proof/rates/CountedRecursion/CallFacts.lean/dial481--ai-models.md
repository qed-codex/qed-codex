---
{
  "module": "proof/rates/CountedRecursion/CallFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What is known at a call

«Case (ii) of Lemma 8 applies to the network with the smaller total (with B₁ in the role of B).» A
call that the specification permits (`spec.Child`) goes to the context that the solver makes from
the number y of a pattern and the first grouping x that the test of Lemma 8 accepts. `at_call`
collects what follows, for the use of `childIsGoodFrom` and `procedureCostFrom`:
the parts of the callee's context (ℓ, L, B' and the parent); the network of the pattern is a network
with the parameters P = g³λ and B₁; the input that the procedure writes from the parent belongs to
it; x has at most 2g/K nodes in every group and Y_{γ,γ'} ≤ L; 1 ≤ L ≤ gP. 

### `callNet`

 The network with the smaller total of the pattern number y, for the instance (a, f) of the level
ℓ + 1. 

### `callL`

 The L of Lemma 8 for it: ⌈(U + 2ζgP)/K²⌉ with ζ = 2^{−ℓ−5}, P = g³λ. 

### `callParent`

 The parent in the context of the callee. 

### `AtCall`

 What is known of the callee a' of the instance (a, f) of the level ℓ + 1, for the pattern number
y and the grouping number x. 

### `at_call`

 **A permitted call**: the callee belongs to a pattern y and to the first grouping x that the
test of Lemma 8 accepts on the network with the smaller total, and all of `AtCall` holds. 
