---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsFibreMeasuresLocalHermitianFormStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_fibreMeasures_localHermitianForm"
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

## Disintegration along a local Hermitian norm

[Theorem ANT.1423](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_fibreMeasures_localHermitianForm/)

Let $E/F$ be a CM extension of number fields with involution $\sigma$, let $M\ge1$, and let $J\in M_M(E)$ be nondegenerate and $\sigma$-Hermitian. At a nonzero prime $v$ of $\mathcal O_F$, put $V=(F_v\otimes_F E)^M$ and let $q:V\to F_v$ be the scalar-valued Hermitian form determined by $J$. Let $\mu$ and $\nu$ be any additive Haar measures on $V$ and $F_v$, respectively.

There are measures $\mu_c$ on $V$, indexed by $c\in F_v$, supported on $q^{-1}(c)$, such that for every measurable $\varphi:V\to[0,\infty]$, $$\int_V\varphi\,d\mu=\int_{F_v}\left(\int_V\varphi\,d\mu_c\right)d\nu(c).$$ For every continuous compactly supported real function $\varphi$, it is integrable for each $\mu_c$ with $c\ne0$, and $c\mapsto\int_V\varphi\,d\mu_c$ is continuous on $F_v^\times$.
