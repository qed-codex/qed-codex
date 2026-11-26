---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/LeafTruncPf.lean",
  "declarations": [
    "LateralTheory.E.LeafGhostRelCut.LeafTrunc_of"
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

## Factorization through a complex concentrated in degree zero

[Theorem ALG.0511](https://andrewodesky.com/rh/lean/LateralTheory.E.LeafGhostRelCut.LeafTrunc_of/)

Let $\mathcal A$ be an abelian category with a derived category, and let $$K_0\xrightarrow{f}K_1\xrightarrow{g}K_2,\qquad L\xrightarrow{\ell}K_2$$ be morphisms in $D(\mathcal A)$. Suppose $H^m(K_0)=0$ for $m>2$, $H^2(f)=0$, $H^1(g)=0$, and $H^m(K_2)=0$ for $m<0$. Suppose also that $H^m(L)=0$ for $m\ne0$ and $H^0(\ell)$ is an isomorphism. Then there is $h:K_0\to L$ such that $$\ell\circ h=g\circ f.$$
