---
{
  "module": "proof/networks/Eight/SecLevel_EStar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_EStar.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_EStar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Hence e* = 0», with ρ = 11/12

Proves e* = 0 with ρ = 11/12, following the last paragraph of the proof of Proposition 3 sentence by
sentence, up to the conclusion e* = 0. The first sentence of Proposition 3 with ρ = 11/12 is a
hypothesis `hP3` of every theorem
here. e* (`Paper.eStar`), `Paper.Achievable` and the two general facts
`Paper.achievable_of_eStar_lt` and `Paper.eStar_le` do not depend on Lemma 2. 

### `eStar_le_of`

 «Let e > e*; then (K, e) is achievable for infinitely many K. Let e'' > ρe. For all large K we
have (ρ + 2/K)e + 2/K ≤ e'', so (9K¹⁶, e'') is achievable for infinitely many K, and therefore e* ≤
e''.» Same as in the paper;
«large» is K ≥ (2e + 2)/(e'' − ρe). 

### `eStar_le_rho_mul_of`

 «Letting e'' → ρe and e → e* gives e* ≤ ρe*.» Here: for every η > 0, take e = e* + η/2 and e'' =
ρe + η/2, which is at most ρe* + η. 

### `eStar_eq_zero_of`

 **Proposition 3**, second sentence, with ρ = 11/12: e* = 0. «Since 0 ≤ e* ≤ 1/2 and ρ < 1, e* = 0.»
Same as in the paper (e* ≤ 1/2 is not needed). 
