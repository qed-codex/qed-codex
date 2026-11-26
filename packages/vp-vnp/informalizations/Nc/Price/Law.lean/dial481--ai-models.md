---
{
  "module": "Nc/Price/Law.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Law.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Law.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Covers of wires as identities between functions of bits

For the proof of Theorem thm:laws (`Paper/Laws.lean`): a cover of a product of wires by products of wires is an identity
between functions of bits (`WireId`); powers and products of products of wires; their values at a spectral point.


### `WireId`

 An identity that rewrites wires. Parties V; old wires e with ends a e, b e and n e bits; new wires ν
with ends c ν, d ν. For all copies X p (of the bits of the old wires at p, for every party p):
[for every old wire the two copies agree] = Σ_i Σ_(bits g of all new wires) ∏_p tab i p (X p) (g at p);
in the term i the new wire ν has len i ν bits. 

### `enc`

 Strings of k bits as numbers. 

### `exists_wireId`

 A sum of restrictions of wires is an identity between functions of bits. 

### `wcls`

 Wires with the ends p, q, as a homomorphism from numbers to classes of tensors. 

### `F_wires_two`

 The price of wires of n e bits. 
