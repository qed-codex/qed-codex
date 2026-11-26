---
{
  "module": "src/Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/CechPairings/DoubleComplexMapMemTotal.lean",
  "declarations": [
    "CrystallineSemistableComparison.P.dc_map_col_surj"
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

## A cokernel annihilator for the total map of double complexes

[Theorem ALG.0638](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.P.dc_map_col_surj/)

Let $R$ be a commutative ring, let $K,L$ be double complexes of $R$-modules indexed by $p,q\ge0$, with commuting horizontal and vertical differentials, and let $\varphi:K\to L$ commute with both differentials. Fix $s\in R$ and $n\ge0$. Suppose multiplication by $s$ annihilates the cokernel of $$H^q(K^{p,\bullet})\to H^q(L^{p,\bullet})\qquad(p+q=n),$$ and the kernel of the same map whenever $p+q=n+1$. Then multiplication by $s^{2n+3}$ annihilates the cokernel of $$H^n(\operatorname{Tot}K)\to H^n(\operatorname{Tot}L).$$
