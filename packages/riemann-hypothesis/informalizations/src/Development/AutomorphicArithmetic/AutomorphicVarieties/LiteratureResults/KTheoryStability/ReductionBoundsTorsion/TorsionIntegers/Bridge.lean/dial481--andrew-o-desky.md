---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/TorsionIntegers/Bridge.lean",
  "declarations": [
    "PositivityTheory.KB.bOdd_zk"
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

## Rank bound for selected odd homology classes

[Theorem GC.0137](https://andrewodesky.com/rh/lean/PositivityTheory.KB.bOdd_zk/)

Let $L$ be a totally complex number field and $r_2$ its number of complex places. Let $k\ge0$ be even, $k+1<r_2$, $b\ge1$, and $n\ge2(k+1)+4$. For $x\in H_{k+1}(\mathrm{GL}_n(\mathcal O_L),\mathbb Z)$ define $z_0(x)=x$ and recursively $$z_{t+1}(x)=(\operatorname{diag}_b)_*z_t(x)-b^{t+2}(\operatorname{stab})_*z_t(x).$$ Here $\operatorname{diag}_b$ repeats a matrix in $b$ diagonal blocks, and $\operatorname{stab}$ embeds it as the first block with an identity complement; both maps go from rank $b^tn$ to rank $b^{t+1}n$. Then $$\operatorname{rank}_{\mathbb Z}\left\langle z_k(x):x\in H_{k+1}(\mathrm{GL}_n(\mathcal O_L),\mathbb Z)\right\rangle\le r_2.$$
