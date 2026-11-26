---
{
  "module": "Zeta23/PairCeiling/CeilingLaw256.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/CeilingLaw256.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/CeilingLaw256.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/CeilingLaw256.lean — THEOREM 1′ instantiated at the N = 256 law of LawN256.lean, with NO hypothesis beyond
EnclOK: for every grid form factor S inside the kernel-checked enclosures — in particular the law's own — and every certificate (c₀, r),
r ∈ C¹[0,1] with r′ =: g differentiable off a countable set with integrable derivative h, that is valid against the law,
c₀ + Σ_{j=1}^{256} (S(j)/256)·r(j/256) ≤ p, one has
      c₀ + ∫₀¹ r(x)·x dx ≤ p + 0.82395317·|r(1)| + (1/(6·256²) + τ/512)·(|r′(1)| + ∫₀¹|r″|),   τ = 3·10⁻⁴⁰,
and 1/(6·256²) + τ/512 < 2.5431316·10⁻⁶.  With p = p₀ = 0.68182868746… (the law's simple-point fraction; validity configuration-by-
configuration averaged over the law's weights) and r(1) = 0 this is the bound 0.6818287 + 2.55·10⁻⁶·(|r′(1)| + V(r′)).
-/
```

### `lawN256_rows`

 **the row certificate of the N = 256 law, unpacked**: near-CUE rows with τ = 3·10⁻⁴⁰ and |D(1)| ≤ 0.82395317. 

### `ceiling_law256`

 **CEILING AT THE N = 256 LAW (Theorem 1′ instance, exact constants).** 

### `ceiling_law256_decimal`

 **the same with decimal constants**: v ≤ p + 0.82395317·|r(1)| + 2.5431316·10⁻⁶·|r′(1)| + 2.5431316·10⁻⁶·∫₀¹|r″|. 
