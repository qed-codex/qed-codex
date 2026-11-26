---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeTateCokernelSharp.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.HT.hodge_tate_cokernel_sharp"
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

## Annihilator of the Hodge–Tate cokernel

[Theorem PHT.1686](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.hodge_tate_cokernel_sharp/)

Let $p,C,v,O,G$ and $\alpha_G$ be as in the setup of ([Hodge–Tate maps, orthogonality and a cokernel bound](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate/)). For every $\kappa\in O$ satisfying $$v(\kappa)^{p-1}\le v(p),$$ one has $\kappa\,\omega_{G^\vee}\subset\operatorname{im}\alpha_G$.
