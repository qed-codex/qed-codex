---
{
  "module": "Zeta23/PairCeiling/LawN256.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/LawN256.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/LawN256.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/LawN256.lean — GENERATED (70-digit interval arithmetic; scale K = 2^140): enclosures lo_j ≤ K·S(j) ≤ hi_j, j = 1..256, of the grid
form factor S(j) = (Σ_c w_c |Σ_i m_{c,i} e^{2πi j x_{c,i}/256}|²)/256 of the finitely supported 256-periodic LAW of marked configurations — exact rational weights
w_c ≥ 0 summing to 1, rational positions x_{c,i} ∈ [0,256), marks m_{c,i} ∈ {1,2} with Σ_i m_{c,i} = 256 — recorded in the certificate file
cert_N256_blk_b128m.json (sha256 cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8) (the optimal law of an exact-rational linear programme over 256-periodic marked configurations; the certificate file is available from the authors);
and the row
certificate (RowCert.lean) they satisfy: |256·S(j) − j| ≤ τ := 3/10^40 for 0 < j < 256 and |D(1)| ≤ 82395317/10^8.  The law's simple-point
fraction is p₀ = 1 − a_N = 10909258999421303588095230195816054408197/16000000000000000000000000000000000000000 exactly (= 0.68182868746…).
DISPLAYED HYPOTHESIS downstream: EnclOK (that the true S lies in these enclosures) — verified outside Lean by interval arithmetic;
everything downstream of the enclosures is kernel-checked (LawN256_check by decide +kernel).
-/
```

### `LawN256`

 the row-certificate data for the N = 256 law. 

### `LawN256_check`

 the integer row checker accepts (kernel evaluation). 
