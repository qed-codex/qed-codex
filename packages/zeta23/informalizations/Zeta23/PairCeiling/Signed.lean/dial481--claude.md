---
{
  "module": "Zeta23/PairCeiling/Signed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Signed.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Signed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Signed.lean — the SIGNED-edge form of the ceiling: when the certificate has r(1) ≥ 0 and the law's edge
discrepancy D(1) ≥ 0 (an open-band law's free closed-band atom makes D(1) = Σ_j s_j − 1/2 positive), the edge term −r(1)·D(1) of the
signed second integration by parts (Stability.abel_ibp_second) is ≤ 0 and is DROPPED, rather than bounded by |r(1)|·|D(1)|:
      c₀ + ∫₀¹ r(x)·x dx ≤ p + |r′(1)|·|E(1)| + M·∫₀¹|r″|.
For near-CUE laws (NearCUE.lean) and the N = 256 law (LawN256.lean, with a kernel-checked certificate that D(1) ≥ 0) this yields
      v ≤ p + (1/(6N²) + τ/(2N))·(|r′(1)| + ∫₀¹|r″|),        N = 256:  v ≤ p + 2.5431316·10⁻⁶·(|r′(1)| + ∫₀¹|r″|).
-/
```

### `ceiling_signed`

 **signed ceiling**: r(1) ≥ 0 and D(1) ≥ 0 kill the edge term. 

### `ceiling_nearCUE_signed`

 **signed ceiling for a near-CUE law.** 

 ## the sign certificate D(1) ≥ 0 from the enclosures 

### `edgeNonneg`

 integer check: 2·Σlo ≥ K·N, i.e. T_N/N ≥ 1/2. 

### `LawN256_edge`

 the N = 256 law's edge discrepancy is nonnegative (kernel evaluation). 

### `ceiling_law256_signed`

 **SIGNED CEILING AT THE N = 256 LAW**: for certificates with r(1) ≥ 0 the edge term vanishes —
      c₀ + ∫₀¹ r(x)·x dx ≤ p + 2.5431316·10⁻⁶·|r′(1)| + 2.5431316·10⁻⁶·∫₀¹|r″|. 
