---
{
  "module": "Zeta23/PairCeiling/Ceiling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Ceiling.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Ceiling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Ceiling.lean — the CEILING THEOREM in certificate language:
if a pair (c₀, r) satisfies the certificate inequality at ONE configuration whose form-factor measure has masses s_j at j/N
and whose fraction of simple points is p₁ — i.e. c₀ + Σ_j s_j r(j/N) ≤ p₁ — then its VALUE v = c₀ + ∫₀¹ r(k)k dk obeys
      v ≤ p₁ + |r(1)|·|D(1)| + |r′(1)|·|E(1)| + (sup|E|)·∫₀¹|r″|,
and the parametrised corollary with numeric bounds.  (The configuration-specific numbers for an instance come from
NumericCert.lean + Bridge.lean, or from RowCert.lean + NearCUE.lean; the N = 256 law is assembled in CeilingLaw256.lean.)
-/
```

### `ceiling_of_valid_at`

 **CEILING (abstract form).** Validity of the certificate at the configuration (masses s at j/N, simple fraction p₁)
bounds the certificate's value by p₁ plus the stability error. 

### `ceiling_numeric`

 **CEILING (parametrised corollary).** With numeric bounds |D(1)| ≤ d₁, |E(1)| ≤ e₁, sup|E| ≤ M for the configuration
and |r(1)| ≤ a, |r′(1)| ≤ b, ∫₀¹|r″| ≤ c for the certificate:  v ≤ p₁ + d₁·a + e₁·b + M·c. 
