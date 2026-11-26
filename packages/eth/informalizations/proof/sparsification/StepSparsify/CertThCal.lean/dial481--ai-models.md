---
{
  "module": "proof/sparsification/StepSparsify/CertThCal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CertThCal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CertThCal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Calabro's thresholds are polynomial-time

Calabro's thresholds θ i are polynomial-time: `thetaC_polyT` shows that `Cal.thetaC a i` is
polynomial-time whenever Calabro's α (here `a`) is polynomial-time and i is given in unary.
The thresholds are defined by a recursion on sums of products. Here they are computed from closed
forms. By `SparsificationLemma.Cal.stBetaCat`, θ 0 = 2 and θ i = α·2·(8α)^(i−1)·Cat_(i−1) for i ≥ 1
(`thetaC_eq`),
and Cat_c = C(2c, c)/(c + 1).
The certificates for binomial coefficients and for ⌈log₂⌉ are those of
proof/rates/ClauseBound/ParityChecks/CertLib.lean; the one for powers with the exponent in unary is
`PolyT.pow_unary`. 

### `thetaC_eq`

 Calabro's thresholds in closed form: θ 0 = 2, and θ i = α·(2·(8α)^(i−1)·Cat_(i−1)) for i ≥ 1. 

### `catalan_polyT`

 The Catalan number Cat_c is polynomial-time, for c in unary. 

### `thetaC_polyT`

 The threshold θ i is polynomial-time whenever Calabro's α (here `a`) is polynomial-time and i is
given in unary. 

### `alphaS_polyT`

 Calabro's α for the width max(k, 3) and ε = 2^(−s) is polynomial-time jointly in k and s, if s
is given in unary. 

### `stCertThCal`

 Calabro's thresholds are polynomial-time, jointly in k, s and the index, all given in unary. 
