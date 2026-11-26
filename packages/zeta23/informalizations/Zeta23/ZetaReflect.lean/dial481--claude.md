---
{
  "module": "Zeta23/ZetaReflect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZetaReflect.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZetaReflect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZetaReflect.lean — the two reflection seam obligations of ZetaSeam.

Paper [subsec:weil], verbatim: "The multiset {(γ_ρ, m_ρ)} is invariant under
γ ↦ γ̄ (i.e. ρ ↦ 1 − ρ̄; multiplicities agree because conj ξ(conj s) = ξ(s) =
ξ(1−s))".  These are CLASSICAL facts about ζ, not paper inputs.

Contents:
  • riemannZeta_conj : ζ(s̄) = ζ(s)̄ for s ≠ 1 (Schwarz reflection: Dirichlet
    series on Re s > 1 + the identity theorem on ℂ∖{1});
  • analyticOrderAt_conj_conj : vanishing order is invariant under z ↦ z̄
    conjugation of a function (general lemma);
  • analyticOrderAt_zeta_one_sub : order transport through the functional
    equation ζ(1−s) = 2(2π)^{−s}Γ(s)cos(πs/2)·ζ(s) (prefactor nonvanishing in
    the strip);
  • zeta_reflect_zero, zeta_mult_reflect : the ZetaSeam field shapes.
-/
```

 ### 1. Schwarz reflection for ζ 

### `riemannZeta_conj`

 **Schwarz reflection for ζ**: ζ(s̄) = ζ(s)̄ away from the pole. 

 ### 2. Vanishing order under conjugation 

### `analyticOrderAt_conj_conj`

 The vanishing order of z ↦ conj (f (conj z)) at conj w equals that of f at w. 

### `analyticOrderAt_zeta_conj`

 Order of ζ is conjugation-symmetric away from the pole. 

 ### 3. Order transport through the functional equation 

### `Efac`

 The prefactor of [riemannZeta_one_sub]: E(s) = 2(2π)^{−s} Γ(s) cos(πs/2). 

### `analyticOrderAt_zeta_one_sub`

 Order transport through the functional equation: for w in the open strip,
ord_{1−w} ζ = ord_w ζ. 

 ### 4. The ZetaSeam reflection fields 

### `zeta_reflect_zero`

 H-symm (set): ρ ↦ 1 − ρ̄ maps nontrivial zeros to nontrivial zeros. 

### `zeta_mult_reflect`

 H-symm (multiplicity): m_{1−ρ̄} = m_ρ. 
