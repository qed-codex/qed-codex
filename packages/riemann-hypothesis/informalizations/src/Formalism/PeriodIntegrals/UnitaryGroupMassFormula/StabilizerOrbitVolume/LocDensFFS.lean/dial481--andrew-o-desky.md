---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerOrbitVolume/LocDensFFS.lean",
  "declarations": [
    "PI.VolStabSW.fFSplit_holds"
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

## Exact Gram-matrix count over a split quadratic algebra

[Theorem ALG.0746](https://andrewodesky.com/rh/lean/PI.VolStabSW.fFSplit_holds/)

Let $k$ be a finite field of order $q$, let $0\le a\le M$, and put $K=k\times k$ with involution $\overline{(x,y)}=(y,x)$. Let $J\in M_M(K)$ and $T\in M_a(K)$ be Hermitian matrices with unit determinants. The number of ordered tuples $x_1,\ldots,x_a\in K^M$ satisfying $$\overline{x_i}^{t}Jx_j=T_{ij}\qquad(1\le i,j\le a)$$ is $$q^{a(M-a)}\prod_{i=0}^{a-1}(q^M-q^i).$$
