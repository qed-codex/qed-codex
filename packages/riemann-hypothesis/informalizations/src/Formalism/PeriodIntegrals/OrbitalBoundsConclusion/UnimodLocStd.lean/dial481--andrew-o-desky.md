---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnimodLocStd.lean",
  "declarations": [
    "unimodular_local_standard"
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

## A unitary change making a CM lattice index prime to a chosen prime

[Theorem ANT.1079](https://andrewodesky.com/rh/lean/unimodular_local_standard/)

Let $a,b,c,d,\lambda,I,L,L_0,H,\Lambda$ satisfy the conditions in ([Self-dual lattices from an imaginary quadratic period pair](https://andrewodesky.com/rh/lean/PI.ULS.CmOK/)).

For every prime $\ell$ there is a complex-linear isometry $\delta$ of $H$ with no nonzero fixed vector such that the relative indices of $L_0$ and $\delta\Lambda$ in both directions are finite and $$\ell\nmid[\delta\Lambda:L_0\cap\delta\Lambda].$$
