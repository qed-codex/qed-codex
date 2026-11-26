---
{
  "module": "proof/rates/ClauseBound/TopN/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One evaluation, the parameters and the exponent of the networks are polynomial-time

Lemmas that one evaluation of a sparse formula (`evalV`, with the certificate `StCertAdm` of the
network of marks), the parameters (β, the number of layers, the bounds on shared bits and size,
⌊n^{1/17}⌋, the threshold τ, the label length `lamS`) and the exponent of the networks computed
under a bound (`needNetC`) are polynomial-time or given in unary. 

 ### One sparse formula, for any polynomial-time `val` 

### `evalV_polyT`

 One evaluation. 

 ### The parameters 

### `betaN_unary`

 β is given in unary if s is. 

### `layersN_unary`

 The number of layers is given in unary if s is. 

### `blockN_unary`

 2^β cut off at n + 1 is given in unary if n and s are. 

### `UbN_unary`

 The bound on the shared bits is given in unary. 

### `PbN_unary`

 The bound on the size is given in unary. 

### `root17_polyT`

 ⌊n^{1/17}⌋ in unary is polynomial-time in n in unary. 

### `tauOf_polyT`

 The threshold τ = 2^(4s+17) is polynomial-time in s in unary. 

 ### The exponent of the networks 

### `lamS_unary`

 The label length of the rebalanced instance is given in unary. 

### `needNetC_polyT`

 The exponent of the networks, computed under a bound. 
