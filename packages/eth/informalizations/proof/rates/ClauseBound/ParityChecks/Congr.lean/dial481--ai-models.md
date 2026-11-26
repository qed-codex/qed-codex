---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Congr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Congr.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Congr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Integers determined by their residues modulo a power of 2

An integer of absolute value below 2^{β−1} is determined by its residue modulo 2^β, an integer in
[0, 2^n] by its residue modulo 2^{n+1}, and exact division by 2^r carries a congruence over. 

### `bal_eq`

 A number of absolute value below 2^{β−1} is the balanced representative of any number congruent
to it modulo 2^β. 

### `emod_eq`

 A number in [0, 2^n] is the remainder modulo 2^{n+1} of any number congruent to it. 

### `div_congr`

 If a ≡ 2^r·b modulo 2^{β+r}, then a/2^r ≡ b modulo 2^β (the division is exact). 
