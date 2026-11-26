---
{
  "module": "proof/rates/ClauseBound/ParityChecks/CertTopOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertTopOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertTopOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The function `AO` and its exponent function `eO` are polynomial-time

`stCertO : StCertCountOL → StCertO`. The file parallels proof/rates/ClauseBound/TopN/Cert.lean: the
walk, the decoder, exhaustive counting, the output word and the exponent of the networks under a
bound have their
certificates there and in proof/consequences/CountKSatRate/; the count of one sparse formula has its
certificate as a hypothesis. This file shows that the bounds for the networks of three layers are
given in unary, that the exponent for
everything but the networks is polynomial-time, and that so are the five tests of `planAtO`, by
which it chooses between the networks and trying all assignments. 

 ### Logarithms 

### `log_two_eq`

 ⌊log₂ n⌋ is the number of binary digits of n, less one. 

 ### The parameters of the networks of three layers 

### `UbOL_unary`

 The bound on the shared bits is given in unary. 

### `PbOL_unary`

 The bound on the size is given in unary. 

### `restO_aux`

 The formula of the exponent for everything but the networks, for any polynomial-time numbers. 

### `restO_polyT`

 The exponent for everything but the networks is polynomial-time. 

### `ite_five`

 A case distinction on five tests, for tests that are not looked into. 

 ### The function and its exponent 

### `planAtO_polyT`

 The plan, jointly in n and s in unary and the index. 

### `stCertO`

 The function of (input, pad) and the exponent function of the input are polynomial-time. 
