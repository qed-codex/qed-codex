---
{
  "module": "proof/rates/ClauseBound/Inst/HalfSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfSpec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: auxiliary lemmas

Lemmas on the pieces of Appendix B, with ρ = 1/√2, as programs with a pad. The pieces are numbered
0, …, 4h, and the piece number i is the piece A_s, s = i − 2h, made from the operators
on the polynomial ring. The lemmas: a sum over i = 0, …, 4h of a function of i − 2h is the sum over
s = −2h, …, 2h; the number of all partitions of 0, …, 4h; |s| ≤ 2h; and a pad of length 2^{cλ}
is long enough for all tables when the constants are large enough at the length λ.
They are in the namespace `ClauseBound.Inst.Half.Spec`. 

### `sum_range_shift`

 A sum over i = 0, …, 4h of a function of i − 2h is the sum over −2h, …, 2h. 

### `deltaF_eq`

 The number of all partitions of 0, …, 4h. 

### `abs_sOf_le`

 |s| ≤ 2h. 

### `padLen_le`

 A pad of length 2^{cλ} is long enough for all tables. 
