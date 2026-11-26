---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/BlowupProjections/BlowupProjStatement.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement"
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

## Projective resolution with normal-crossing coordinates

[Definition / hypothesis AG.D070](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement/)

This hypothesis requires the following statement for every field $K$ of characteristic zero and every pair of integers $M,D\ge0$.

Let $i:X\hookrightarrow\mathbb P^M_K$ be a closed immersion with $X$ reduced. Let $U\subseteq X$ be a dense open subscheme smooth over $K$ of pure relative dimension $D$. There exist an integer $r\ge0$, a $K$-scheme $X'$, a closed immersion $$j:X'\hookrightarrow\mathbb P^M_K\times_K\mathbb P^r_K,$$ and a $K$-morphism $f:X'\to X$ such that $i\circ f=\operatorname{pr}_1\circ j$ and all the following hold.

- The scheme $X'$ is smooth over $K$ of pure relative dimension $D$.
- The restriction $f^{-1}(U)\to U$ is an isomorphism, and $f^{-1}(U)$ is dense in $X'$.
- There is a finite affine open cover $(V_\alpha)$ of $X'$. On each $V_\alpha$, there are regular functions $z_{\alpha,0},\ldots,z_{\alpha,D-1}$ whose Kähler differentials form a basis of $\Omega^1_{\mathcal O_{X'}(V_\alpha)/K}$ over $\mathcal O_{X'}(V_\alpha)$, and an integer $0\le k_\alpha\le D$, such that $$V_\alpha\cap\bigl(X'\setminus f^{-1}(U)\bigr) =\bigcup_{0\le h<k_\alpha}\{y\in V_\alpha:z_{\alpha,h}(y)=0\}.$$
