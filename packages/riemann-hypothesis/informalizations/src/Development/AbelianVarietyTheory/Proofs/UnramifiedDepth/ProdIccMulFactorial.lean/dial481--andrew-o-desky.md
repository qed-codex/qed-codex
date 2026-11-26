---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ProdIccMulFactorial.lean",
  "declarations": [
    "GlobalTheory.CayleyCapelli.cayleyId"
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

## The determinant differential operator on a determinant power

[Theorem ALG.0961](https://andrewodesky.com/rh/lean/GlobalTheory.CayleyCapelli.cayleyId/)

Let $K$ be a field of characteristic zero, let $n,s\ge0$, and let $X=(X_{ij})$ be an $n\times n$ matrix of independent variables. Then $$\det\!\left(\frac{\partial}{\partial X_{ij}}\right)\det(X)^{s+1}=\left(\prod_{j=0}^{n-1}(s+1+j)\right)\det(X)^s.$$
