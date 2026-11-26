---
{
  "module": "Ov/Duality/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Gauges as infima of weights

For an abstract commutative monoid with a covering relation: a function that is defined as the infimum of the weights of
certificates is a gauge, if certificates can be multiplied and added along covers. Used for Theorem thm:duality
(`Paper/Gauges.lean`) and Proposition prop:extend (`Paper/Extension.lean`).


### `isPre_sInf`

 Let S t be sets of numbers ≥ 0, the weights of the certificates for t. Their infimum is a gauge
if certificates can be multiplied and put together along covers, 1 has a certificate of weight
1, and none of a weight below 1. 

### `Cover.mul_mul`

 Covers can be multiplied. 
