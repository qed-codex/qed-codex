---
{
  "module": "proof/sparsification/StepSparsify/CertWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CertWalk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/CertWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates of polynomial time for the sparsification of Appendix D, Step 5

This file proves `StCertNoTaut` of proof/sparsification/StepSparsify/Defs.lean.
`stCertNoTaut`: `noTaut` is a filter whose test runs through a clause and looks up a literal in it;
each of these has a certificate. 

### `stCertWalkSG`

 The walk that adds up is polynomial-time jointly in k, s, the pad, the root and whatever the
value function depends on, if the thresholds serve and k, 2^k and s are given in unary. 

### `stCertNoTaut`

 Deleting the clauses that contain a variable together with its negation is polynomial-time. 
