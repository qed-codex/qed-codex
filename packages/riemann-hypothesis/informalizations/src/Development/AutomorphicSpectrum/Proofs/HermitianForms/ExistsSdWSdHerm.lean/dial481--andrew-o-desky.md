---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/HermitianForms/ExistsSdWSdHerm.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.SdFin.exists_of_bilin"
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

## A self-dual measure for a nondegenerate local bilinear form

[Theorem ANT.0348](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SdFin.exists_of_bilin/)

Let $F$ be a number field, $v$ a finite place, and $F_v$ its completion. Let $\psi:F_v\to\mathbb C^\times$ be a continuous nontrivial additive character with $|\psi(t)|=1$. Let $V$ be a finite-dimensional $F_v$-vector space with a Hausdorff topology making addition and scalar multiplication continuous, equipped with its Borel measurable structure. Let $\beta:V\times V\to F_v$ be symmetric bilinear and nondegenerate. There is an additive Haar measure $\mu$ on $V$ which is self-dual for $\chi(x,y)=\psi(\beta(x,y))$.
