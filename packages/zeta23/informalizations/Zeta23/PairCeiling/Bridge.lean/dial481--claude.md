---
{
  "module": "Zeta23/PairCeiling/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Bridge.lean — from the GRID certificate (NumericCert: bounds on Dleft/Dright/Egrid/D1/E1 for the form factor S) to the
INTERVAL hypotheses of the stability lemma (Stability/Grid: Dfun/Efun of the atom masses s j := S j / N on [0,1]).
 §1 dictionary: Csum s m = T S m / N; Dfun s N (m/N) = Dright S N m; on the open cell (m/N,(m+1)/N), Dfun = Csum s m − t²/2 lies between
    Dleft S N (m+1) and Dright S N m (D decreases between atoms); Efun s N (m/N) = Egrid S N m.
 §2 sup bridges: grid one-sided bounds ⇒ |Dfun| ≤ B₁ on [0,1]; and |Egrid j| + |D^±_i|/N ≤ B₂ (all i, j) ⇒ |Efun| ≤ B₂ on [0,1]
    (Efun x − Efun(m/N) = ∫_{m/N}^x Dfun, |x − m/N| ≤ 1/N).
 §3 the package for a certificate: EnclOK ⇒ the four hypotheses the ceiling-stability theorem consumes.
-/
```

 ## §1. Dictionary between the atom masses s = S/N and the form factor S 

### `massOf`

 the atom masses of a configuration with form factor S. 

### `Dfun_grid_eq_Dright`

 D at a grid point is the right value. 

### `Dfun_cell_bounds`

 on the open cell (m/N, (m+1)/N), D lies between Dleft (m+1) and Dright m. 

 ## §2. The sup bridges 

### `abs_Dfun_le_of_grid`

 **sup|D| from the grid**: one-sided grid bounds give |D| ≤ B₁ on all of [0,1]. 

### `Efun_grid_eq_Egrid`

 E at a grid point is Egrid. 

### `abs_Efun_le_of_grid`

 **sup|E| from the grid**: the combined grid bounds give |E| ≤ B₂ on all of [0,1]. 

 ## §3. The package consumed by the ceiling-stability theorem 

### `package_of_check`

 **from a checked certificate to the interval hypotheses**: for every form factor S inside the enclosures, the atom masses
s := S/N satisfy |D(1)| ≤ bD1, |E(1)| ≤ bE1, |D| ≤ b1 on [0,1], |E| ≤ b2 on [0,1]. 
