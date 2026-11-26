---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/ConvexCones/PsdConeFinitelyManyOrbitsStatement.lean",
  "declarations": [
    "GlobalTheory.T.psd_cone_finitely_many_orbits"
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

## Finitely many generators for strict Voronoi cells

[Theorem ALG.1331](https://andrewodesky.com/rh/lean/GlobalTheory.T.psd_cone_finitely_many_orbits/)

Let $\mathcal O$ be a characteristic-zero Dedekind domain finite as a $\mathbb Z$-module, let $a\mapsto\bar a$ be a map $\mathcal O\to\mathcal O$, and let $g\ge0$. A bilinear form on an $\mathcal O$-module is balanced if it is symmetric and $B(ax,y)=B(x,\bar a y)$. For a finite projective $\mathcal O$-module $X$, let $\mathcal C_X$ be the real-valued forms pulled back from positive-definite balanced forms on projective quotients of $X$.

Assume the following reduction-cover condition for every finite projective $\mathcal O$-module $Y$: there are finitely many finite lists of symmetric positive-semidefinite integer-valued forms on $Y$, such that every $B\in\mathcal C_Y$, after pullback by an $\mathcal O$-linear automorphism, is a nonnegative real combination of one list.

For a nonnegative form $B$ on $X$, define $$\varphi_g(B)=\frac{2^g}{|X/2X|}\sum_{u\in X/2X}\inf_{x\in u}B(x,x).$$ There is a finite set $S$ of integer-valued bilinear forms on $X$ such that every $B\in\mathcal C_X$ admits an $\mathcal O$-linear automorphism $e$, a finite list $\gamma_1,\ldots,\gamma_m\in S$, and $c_i\ge0$ with $$B(ex,ey)=\sum_ic_i\gamma_i(x,y),$$ where the list has all these properties:

1. Every $\gamma_i$ is balanced and nonnegative.
2. $\varphi_g(\sum_i t_i\gamma_i)=\sum_it_i\varphi_g(\gamma_i)$ for all $t_i\ge0$.
3. There are an integer $N>0$ and a $\mathbb Z$-linear functional $\ell$ on the group of integer-valued bilinear forms on $X$ with $\ell(\gamma_i)=N\varphi_g(\gamma_i)$, and $N\varphi_g(\beta)\le\ell(\beta)$ for every balanced nonnegative integer-valued form $\beta$. If equality holds, then for some integer $k>0$ one has $k\beta=\sum_i b_i\gamma_i$ with integers $b_i\ge0$.
