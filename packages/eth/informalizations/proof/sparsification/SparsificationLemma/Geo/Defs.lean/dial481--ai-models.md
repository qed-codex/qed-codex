---
{
  "module": "proof/sparsification/SparsificationLemma/Geo/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Geo/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification theorem for the geometric thresholds: definitions and statements

The thresholds are `UniformInK.thetaU τ`: θ 0 = 1 and θ i = 4·τ^(2i−1); the numbers β are
`UniformInK.betaSU τ`: β 0 = 0 and β i = 4·τ^(2i−2). They satisfy `SparsificationLemma.ThrC` if 1 ≤
k and 8k ≤ τ.
Two forms of one theorem: for any τ that is large enough for ε (`StThmTau`); and for τ = 2^(4s+17),
with 2^(−s) in the role of ε, which is what the end theorem for all widths k uses (`StThmS`).
For a rational ε ∈ (0,1], τ = ⌈(8k/ε)³⌉ is large enough for k and ε (`tauE`, `StTauE`).
This file has definitions only. The statements are propositions; they are proved in other files. 

### `StThrGeo`

 The thresholds `thetaU τ` with the numbers `betaSU τ` satisfy the four conditions, if 1 ≤ k and
8k ≤ τ. 

### `StDegGeo`

 2·(θ 0 + … + θ (k−1)) + 2 ≤ τ^(2k), if 1 ≤ k and 8 ≤ τ. 

### `outTau`

 The outputs for the parameter τ. Paths are cut after τ^(2k)·n steps; no path is longer
(`StThmTau`). 

### `StThmTau`

 The theorem for any τ ≥ 8k with (k/τ)·log₂(e·τ·τ^(2k)) ≤ ε. The procedure stops on every path;
the outputs are k-CNFs on the same variables, none with a clause written twice; there are at most
2^(εn) of them;
every assignment that satisfies φ satisfies exactly one of them, and every other assignment none; a
variable occurs in at most τ^(2k) clauses of an output. 

### `tauE`

 The parameter for width k and a rational ε: τ = ⌈(8k/ε)³⌉. 

### `StTauE`

 τ = ⌈(8k/ε)³⌉ is large enough for k and ε, and at most (9k/ε)³. 

### `StThmS`

 The theorem for τ = 2^(4s+17) and s ≥ `s0U k` (then k² ≤ 2^s), with 2^(−s) in the role of ε: at
most 2^(n/2^s) outputs, so at most 2^(⌊n/2^s⌋+1); at most 2^(2k(4s+17)) occurrences of a variable. 
