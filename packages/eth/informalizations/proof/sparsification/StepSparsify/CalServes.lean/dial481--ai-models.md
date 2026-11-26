---
{
  "module": "proof/sparsification/StepSparsify/CalServes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalServes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CalServes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Calabro's thresholds serve

This file proves `StServesCal` of proof/sparsification/StepSparsify/Defs.lean: first from
`StCertThCal`, the statement that Calabro's thresholds are polynomial-time (`stServesCal`), then
outright (`servesCal`), with the proof of that statement in
proof/sparsification/StepSparsify/CertThCal.lean. Throughout α = `alphaS k s` and τ = `tauOf s`.
The tree: Calabro's thresholds satisfy the four conditions `ThrC` with α in the role of τ
(`Cal.stThrCal`), k² ≤ α, and β₁ + … + β_{k−1} ≤ τ^(2k) (`stCalNumbers`); so the general theorem
`SparsificationLemma.stTreeG` applies with D = τ^(2k)·n.
Its bound on the number of leaves, a sum of binomial coefficients in D, is replaced by that of
`stCalLeaves`; the latter speaks of the tree that starts with the empty side list, which has as many
leaves (`SparsificationLemma.stSide`).
The hypothesis of `Serves.tree` that no clause of ψ contains a variable together with its negation
is not used.
The occurrences fit the code parameter by `stCalNumbers`.
The certificate is the twin of `thrList_polyT`, `polyT_pickKU`
(proof/sparsification/UniformInK/Cert/Sparsify.lean) and `polyT_stepCU`
(proof/sparsification/UniformInK/Cert/Walk.lean), with `StCertThCal` in the place of `thetaU_polyT`. 

### `length_leaves_rootC`

 The tree that starts with the n clauses xᵢ ∨ ¬xᵢ on the side list has as many leaves as the tree
that starts with the empty side list. 

### `thrListCal_polyT`

 The list of the pairs (j, h), each with Calabro's threshold θ (j - h), is polynomial-time
jointly in k and s, both given in unary. 

### `polyT_stepCCal`

 The two children of a node of the counting tree with Calabro's thresholds are polynomial-time
jointly in k, s and the node, if k, 2^k and s are given in unary. 

### `stServesCal`

 Calabro's thresholds serve, if they are polynomial-time. 

### `servesCal`

 Calabro's thresholds serve. 
