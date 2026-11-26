---
{
  "module": "src/Development/EtaleCohomology/TateTwists/EtaleTateTwistGeneratorRestrictionAndRootChangeH.lean",
  "declarations": [
    "LateralTheory.EtaleFoundations.GenIsoSurjRootPf.prim_root_loc"
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

## Primitive roots of unity are locally unit powers of each other

[Theorem AG.0737](https://andrewodesky.com/rh/lean/LateralTheory.EtaleFoundations.GenIsoSurjRootPf.prim_root_loc/)

Let $q\ge1$ and let $U$ be a scheme. Suppose $q$ is invertible on $U$, and let $\zeta,\xi\in\Gamma(U,\mathcal O_U)$ both satisfy the $q$th cyclotomic polynomial. There is an etale covering family $g_i:U_i\to U$ and, for each $i$, an element $a_i\in(\mathbb Z/q\mathbb Z)^\times$ such that $$g_i^*\xi=(g_i^*\zeta)^{\widetilde a_i},$$ where $0\le\widetilde a_i<q$ represents $a_i$.
