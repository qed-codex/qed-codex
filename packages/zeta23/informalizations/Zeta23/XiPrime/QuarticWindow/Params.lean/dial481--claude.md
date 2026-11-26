---
{
  "module": "Zeta23/XiPrime/QuarticWindow/Params.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Params.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Params.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/QuarticWindow/Params.lean — the window-realizing parameter family `P.atV v T`
(mirror of Zeta23/ThmD/ParamsD.lean for the profile-v windows of Zeta23/XiPrime/Defs.lean).

`P.phiV v T u = √(max 0 (v(u/L))) · φ(u)` and `P.atV v T := ⟨x ↦ φ_v(L/2 − w·x), λ, w⟩` are those of
Zeta23/XiPrime/Defs.lean §4.  Here: λ, w — hence L, X, λ₁, d, τ_k, h, 𝓔_T, toSetting — of `P.atV v T` are P's
DEFINITIONALLY (rfl lemmas), and the window of `P.atV v T` AT HEIGHT T is φ_v (`atV_phi`, needs v even and
w ≠ 0), so its abstract local data / taper constants / prime-side traces are the AdmWindow data of φ_v.
-/
```

### `phiV_eq`

 φ_v in closed form on the tree's taper: φ_v(u) = √(max 0 (v(u/L)))·Taper.phi ϱ L w u (rfl). 

### `phiV_even`

 φ_v is even when v is. 

### `atV_phi`

 **the window of `P.atV v T` at height T is φ_v** (v even, w ≠ 0). 

### `atV_localFun`

 the abstract local data of `P.atV v T` at height T are the AdmWindow data of φ_v. 

### `atV_trGtilde`

 the prime-side traces of `P.atV v T` at height T are the abstract-layer traces of the φ_v data. 

 ### eventual side conditions shared by the QuarticWindow files 

### `tendsto_L_of_valid`

 L_T → ∞ (valid parameters). 

### `eventually_w8`

 eventually 8w ≤ L_T. 
