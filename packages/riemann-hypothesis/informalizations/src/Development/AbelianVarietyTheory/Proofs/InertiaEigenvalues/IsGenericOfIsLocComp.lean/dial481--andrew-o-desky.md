---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsGenericOfIsLocComp.lean",
  "declarations": [
    "GlobalTheory.CuspRep.Generic.isGeneric_of_isLocComp"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Genericity of finite local cuspidal components

[Theorem REP.1416](https://andrewodesky.com/rh/lean/GlobalTheory.CuspRep.Generic.isGeneric_of_isLocComp/)

Let $E$ be a totally complex number field, $a\ge0$, and $P$ an irreducible cuspidal automorphic subrepresentation for $\operatorname{GL}_a(\mathbb A_E)$ in the source's cuspidal model. Let $w$ be a nonzero prime of $\mathcal O_E$, and let $\sigma$ be a smooth irreducible complex representation of $\operatorname{GL}_a(E_w)$. If $\sigma$ is a local component of $P$ at $w$, then $\sigma$ is generic: it admits a nonzero Whittaker functional for a nondegenerate character of the standard maximal unipotent subgroup.
