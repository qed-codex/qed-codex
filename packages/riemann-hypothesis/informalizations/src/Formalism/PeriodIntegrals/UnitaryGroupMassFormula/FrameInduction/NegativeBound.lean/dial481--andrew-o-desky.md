---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/FrameInduction/NegativeBound.lean",
  "declarations": [
    "PI.FrameInd.negative_bound"
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

## Dimension of a nonpositive Hermitian subspace

[Theorem ALG.1065](https://andrewodesky.com/rh/lean/PI.FrameInd.negative_bound/)

Let $k,r\ge0$, put $d=2r+k+1$, and equip $\mathbb C^d$ with the Hermitian form $h(x,y)=\overline{x}^{\,t}Hy$, where rows and columns are numbered $0,\ldots,d-1$ and $$H_{ij}=\begin{cases} 1,&i<r,\ i+j=2r+k,\\ 1,&j<r,\ i+j=2r+k,\\ 1,&i=j,\ r\le i<r+k,\\ -1,&i=j=r+k,\\ 0,&\text{otherwise}. \end{cases}$$ Every complex linear subspace $S$ satisfying $\operatorname{Re}h(x,x)\le0$ for all $x\in S$ has $$\dim_{\mathbb C}S\le r+1.$$
