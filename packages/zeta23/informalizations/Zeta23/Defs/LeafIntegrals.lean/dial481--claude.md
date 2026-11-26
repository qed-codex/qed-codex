---
{
  "module": "Zeta23/Defs/LeafIntegrals.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Defs/LeafIntegrals.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Defs/LeafIntegrals.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


Zeta23/Defs/LeafIntegrals.lean — self-contained elementary integral bounds used as drop-ins by
§5's lem:ends (Zeta23/PrimeSideA/EndsE1.lean). Imports only Mathlib.


### `integral_left`

 ∫_T^{2T} ((1+(τ−T))²)⁻¹ dτ = 1 − 1/(1+T) ≤ 1 

### `integral_right`

 ∫_T^{2T} ((1+(2T−τ))²)⁻¹ dτ = 1 − 1/(1+T) ≤ 1 

### `Ig_core`

 the (Ig) core: ∫_{[T,2T]} (1 + min(τ−T, 2T−τ))⁻² dτ ≤ 2. 

 ## (W3) core: ∫ ψ(r)² (2+|r|)² dr ≤ 18 L² + 18 (c/w)² for any even 0 ≤ ψ ≤ L with ψ(r) ≤ c/(w r²) 

### `W3_core`

 Abstract form of lem:ends' leaf (W3): for ψ : ℝ → ℝ with ψ(|r|) = ψ(r), 0 ≤ ψ ≤ L,
ψ(r) ≤ c/(w r²) (r ≠ 0) and ψ² integrable:  ψ²(2+|r|)² is integrable and
∫ ψ(r)²(2+|r|)² dr ≤ 18L² + 18(c/w)²  (majorant 9L² on |r| ≤ 1, 9(c/w)²/r² on |r| ≥ 1). 
