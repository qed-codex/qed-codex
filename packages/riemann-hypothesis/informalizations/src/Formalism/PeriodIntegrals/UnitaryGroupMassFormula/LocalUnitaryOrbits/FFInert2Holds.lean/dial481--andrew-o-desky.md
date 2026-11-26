---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalUnitaryOrbits/FFInert2Holds.lean",
  "declarations": [
    "PI.OmLocU.CntFF.fFInert2_holds"
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

## Counting frames with prescribed Hermitian Gram matrix

[Theorem ALG.1054](https://andrewodesky.com/rh/lean/PI.OmLocU.CntFF.fFInert2_holds/)

Let $k$ be a finite field with $q$ elements, and let $K/k$ have degree two. Let $\sigma\ne1$ be a $k$-automorphism of $K$ with $\sigma^2=1$. Fix integers $0\le a\le M$, a nonsingular $\sigma$-Hermitian matrix $J\in M_M(K)$, and a nonsingular $\sigma$-Hermitian matrix $T\in M_a(K)$. Then $$\#\{(x_0,\ldots,x_{a-1})\in(K^M)^a:\ h_J(x_i,x_j)=T_{ij}\text{ for all }i,j\} =\prod_{j=0}^{a-1}\left(q^{2(M-j)-1}-(-1)^{M-j}q^{M-j-1}\right),$$ where $h_J(x,y)=\sum_{u,v}\sigma(x_u)J_{uv}y_v$.
