---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensFFAll.lean",
  "declarations": [
    "PI.VolStabS.fFCount_holds"
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

## A uniform finite-field Hermitian frame count

[Theorem ALG.0876](https://andrewodesky.com/rh/lean/PI.VolStabS.fFCount_holds/)

For every integer $M\ge0$ there is $C\in\mathbb R$ with the following property. Let $k$ be a finite field of odd characteristic, $q=\#k$, and let $K$ be either a quadratic field extension of $k$ with its nontrivial involution $\sigma$, or $k\times k$ with the factor-exchange involution. Let $J\in\operatorname{Mat}_M(K)$ and $T\in\operatorname{Mat}_a(K)$ be invertible $\sigma$-Hermitian matrices, with $a+2\le M$. Then $$\left|\frac{\#\{X\in\operatorname{Mat}_{M\times a}(K):\sigma(X)^{\mathsf T}JX=T\}} {q^{\,2Ma-a^2}}-1\right|\le Cq^{-2}.$$
