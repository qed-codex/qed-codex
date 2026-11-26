---
{
  "module": "proof/consequences/GraphProblems/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: the interface statements, as propositions

The statements that one file needs from another are written here as definitions `St… : Prop`, in the
manner of `proof/consequences/CountKSat/Interfaces.lean`. Nothing is proved and nothing is assumed:
this file has
no theorem. One file proves `theorem … : St…`; a file that needs the statement takes it as a
hypothesis. 

### `Shaped`

 Every clause of ψ has at most w literals and variables below N. 

 ### Reading the input (proof/consequences/GraphProblems/Read.lean) 

 ### What the formulas say (proof/consequences/GraphProblems/Sets.lean, Color.lean) 

### `StDecide`

 The decision problems from the numbers: subsets of independent sets and of cliques, and
supersets of vertex covers and of dominating sets, are again such sets. 

 ### The machine that counts with a prescribed number of true variables (proof/consequences/GraphProblems/Sized.lean) 

### `StSized`

 For every width w and every δ > 0 a machine cut into polynomial-time steps returns `cntS n s ψ`
on (n in unary, s, ψ), for s ≤ n and ψ of width at most w with variables below n, within c·2^{δn}
steps and
with states of size polynomial in n and the number of clauses. 

 ### The tree for Dominating Set (proof/consequences/GraphProblems/DomTree.lean) 

### `ShortensD`

 `stepD w` (with `rootD`) shortens the clauses of Dominating Set to width w. The tree of depth 2n
has at most 2^{εn} leaves. At a leaf no clause has more than w literals, there are at most 3n
clauses, and
their variables are below n. The numbers `cntS` of the leaves add up to that of `domF`. The stack of
the walk never holds more than 2n + 1 nodes; each holds at most n open clauses of at most n
variables below n, and at most
2n closed clauses of at most w literals with variables below n. 

### `StShortens`

 For every ε > 0 some width w ≥ 1 works. 

 ### Certificates (proof/consequences/GraphProblems/Cert.lean) 

### `StCertForm`

 The formulas of the problems are computed in polynomial time from (n in unary, matrix). 

### `StCertBlock`

 The formula of a vector of block sizes is computed in polynomial time from ((n in unary, s, ψ),
y). 
