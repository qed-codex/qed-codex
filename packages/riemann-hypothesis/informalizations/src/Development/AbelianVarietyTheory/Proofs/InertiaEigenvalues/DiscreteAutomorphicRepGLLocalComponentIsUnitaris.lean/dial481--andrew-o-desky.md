---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DiscreteAutomorphicRepGLLocalComponentIsUnitaris.lean",
  "declarations": [
    "GlobalTheory.DiscreteUnit.isUnitarisable_of_isLocCompGL"
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

## Unitarizability of local components of discrete automorphic representations

[Theorem REP.1655](https://andrewodesky.com/rh/lean/GlobalTheory.DiscreteUnit.isUnitarisable_of_isLocCompGL/)

Let $E$ be a totally complex number field and $N\ge0$. Let $V$ be a nonzero irreducible right-translation-invariant complex subspace of smooth automorphic functions on $\mathrm{GL}_N(\mathbb A_E)$, all invariant under the real split central subgroup and square-integrable modulo $\mathrm{GL}_N(E)$ and that subgroup. Let $w$ be a finite place of $E$, and let $\sigma$ be a smooth irreducible complex representation of $\mathrm{GL}_N(E_w)$. Suppose there is a nonzero complex-linear map from $\sigma$ to $V$ intertwining $\mathrm{GL}_N(E_w)$ with its natural action at $w$. Then the space of $\sigma$ admits a positive-definite Hermitian form $B$ satisfying $$B(\sigma(g)v,\sigma(g)u)=B(v,u)\qquad(g\in\mathrm{GL}_N(E_w)).$$
