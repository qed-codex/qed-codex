---
{
  "module": "Nc/Price/Cover.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Cover.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Cover.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Certificates

For the proof of Theorem thm:duality (`Paper/Gauges.lean`), in a commutative monoid with a covering relation, with an
element C and a finite family of elements A β: certificates, their products and sums.


### `mon`

 A product of the members of a family. 

### `Cert`

 A certificate of level k and weight at most W for t: t·C^k is covered by products
C^u·∏A^v with u + Σv = k, and the numbers η^(Σv) add up to at most W. 
