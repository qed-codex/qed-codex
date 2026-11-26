---
{
  "module": "proof/variables/SparsifyThenCount/CertBoth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CertBoth.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CertBoth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The merged function is polynomial-time for every family of thresholds Θ that serves

`stCertBDG : StCertDG → StCertBDG`. The test `VariableBound.useMD`, which chooses between the two
branches, and the exponent `VariableBound.eBD` do not name the thresholds: they are those of
proof/variables/VariableBound. They are proved polynomial-time here (`useMD_polyT`, `eBD_polyT`),
from the test whether every variable occurs (`UniformInK.CertBoth.allOccU_polyT`) and the
certificates of the two exponents.
The certificates of the algorithm for the bound in m are those of
proof/rates/ClauseBound/Alg/CertTop.lean. 

### `useMD_polyT`

 The test that chooses the algorithm for the bound in m is polynomial-time, if the solver, `pick`
and `slU` are. 

### `eBD_polyT`

 The exponent function of the merged function is polynomial-time, if the solver, `pick` and `slU`
are. 

### `stCertBDG`

 For thresholds that serve, the merged function of (input, pad) and its exponent function of the
input are polynomial-time if the solver, `pick` and `slU` are; given that the algorithm for the
bound in n is (`StCertDG`). 
