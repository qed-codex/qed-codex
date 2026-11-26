---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRightInvOfSpan.lean",
  "declarations": [
    "GlobalTheory.HSShort.htMul"
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

## Additivity of the height of multihomogeneous forms

[Theorem ARAK.0688](https://andrewodesky.com/rh/lean/GlobalTheory.HSShort.htMul/)

Let $F$ be a number field, $B,N,n\ge0$, $w\in M_{N,n}(F)$, and $A_\sigma\in M_N(\mathbb C)$ for every embedding $\sigma:F\to\mathbb C$. Assume $N>0$, the columns of $w$ span $F^N$, every $A_\sigma$ is invertible, and there is $\Lambda\ge1$ with $\|A_\sigma^{-1}\sigma(w_{\bullet k})\|_2\le\Lambda$ for every $k,\sigma$. For nonzero multihomogeneous $G,G'\in F[X_{bj}]$ of any respective block multidegrees, $$h(GG')=h(G)+h(G').$$ For every $0\ne c\in F$, $h(c)=0$.
