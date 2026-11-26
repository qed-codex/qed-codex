---
{
  "module": "proof/networks/Eight/Level/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Polynomial-time steps for the networks and functions of one level

This file treats the pieces of Lemma 2 from the eight-square identity. A step of a step machine of
this development may be any polynomial-time function. Here: if the pieces of Lemma 2, «computable in
time poly(λ)», are computed in polynomial time
(`Eight.StKeeps`), then the row network and the column network of ι, given by procedures
(`levelNet`), have lengths of states and labels in unary and procedures with polynomial-time steps
(`stNetKeeps_of`); and some functions used by the algorithm of one
level (`levelAlg`) besides its calls (the count of functions ι, the choice of the network with the
smaller total, the final division by 2^{t|ℛ|}) are polynomial-time (namespace `Cert`). The
certificates of the plain functions come from proof/rates/ClauseBound/Alg/CertGridG.lean and
CertLevel.lean; the procedure for the
weights and its certificate come from the imported files. 

### `tOf_unary`

 t = ⌈λ/3⌉ in unary, for λ in unary. 

### `numPat8_polyT`

 The number (t + 1)^{|ℛ|} of functions ι is polynomial-time, for λ in unary. 

### `useRowP_polyT`

 The choice of the network with the smaller total is polynomial-time, for λ in unary. 

### `div_polyT`

 The final division by 2^{t|ℛ|} is polynomial-time, for λ in unary. 

### `factor_polyT`

 A value of a factor of the network of ι is polynomial-time, for λ in unary. 

### `stNetKeeps_of`

 The row network and the column network of ι, given by procedures, have lengths in unary and
procedures with polynomial-time steps, if the pieces are computed in polynomial time. 
