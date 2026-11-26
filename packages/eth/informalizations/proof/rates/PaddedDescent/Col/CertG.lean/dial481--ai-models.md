---
{
  "module": "proof/rates/PaddedDescent/Col/CertG.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/CertG.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/CertG.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Certificates (`PolyT`) for the test `goodG` and the rebalancing `rebalG`, jointly in the pad, K,
g and the label length β (data, in unary) and the context.
They follow the certificates of `goodB` and `rebalF` in `PaddedDescent/F/CertNet.lean`. 

### `goodG2`

 The test `goodG` is polynomial-time, jointly in K and g (in unary), the label length and the
colouring. 

### `rebalG_polyT`

 `rebalG` is polynomial-time, jointly in the pad, in K, g and the label length (in unary), and in
the context. 

### `certRebalG`

 The statement `StCertRebalG` holds: `rebalG` is polynomial-time, by `CertNet.rebalG_polyT`. 
