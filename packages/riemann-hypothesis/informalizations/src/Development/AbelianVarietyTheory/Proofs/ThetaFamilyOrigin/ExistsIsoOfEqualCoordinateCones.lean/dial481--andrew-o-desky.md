---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaFamilyOrigin/ExistsIsoOfEqualCoordinateCones.lean",
  "declarations": [
    "GlobalTheory.ZH.IsoCone.exists_hom",
    "GlobalTheory.ZH.IsoCone.exists_iso"
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

## A morphism from inclusion of projective coordinate cones

[Theorem AG.0237](https://andrewodesky.com/rh/lean/GlobalTheory.ZH.IsoCone.exists_hom/)

Let $K$ be algebraically closed, $p:X\to\operatorname{Spec}K$ and $p':Y\to\operatorname{Spec}K$ schemes, with $Y$ reduced and locally of finite type over $K$. Let $L,L'$ be line bundles on $X,Y$, and let $(s_j),(s'_j)$ be families of global sections indexed by the same finite set $J$. Suppose each family satisfies the affine-chart conditions below.

For a local $K$-algebra $R$ and an $R$-point $x$ of $X$, let $\mathcal C_s(x)\subseteq R^J$ be the tuples obtained by evaluating the $s_j$ in a single chosen local trivialization of $L$ valid on all of $x$, and multiplying them by a common unit of $R$. Define $$C_s(X)=\bigcup_{x\in X(K)}\mathcal C_s(x)\subseteq K^J,$$ and similarly for $Y$. If $C_{s'}(Y)\subseteq C_s(X)$, there is a $K$-morphism $g:Y\to X$ such that $$\mathcal C_{s'}(y)\subseteq\mathcal C_s(g\circ y)$$ for every commutative local ring $R$, every morphism $y:\operatorname{Spec}R\to Y$, and the induced scalar structure.

## Equal coordinate cones determine a proper integral variety

[Theorem AG.0275](https://andrewodesky.com/rh/lean/GlobalTheory.ZH.IsoCone.exists_iso/)

Let $K$ be algebraically closed, $X,X'$ proper integral $K$-schemes, $H,H'$ line bundles, $J$ a finite set, and $(s_j)_{j\in J}$, $(s'_j)_{j\in J}$ global sections. Suppose the nonvanishing loci of the sections cover each scheme, are affine, and their rings of functions are generated over $K$ by the ratios $s_j/s_i$, respectively $s'_j/s'_i$.

For a local commutative ring $R$, a morphism $y:\operatorname{Spec}R\to X$ and $v\in R^J$, say $v$ is a coordinate vector of $y$ if some bundle chart contains its image and $v$ is the vector of section values in that chart multiplied by one unit of $R$. Define coordinate vectors on $X'$ in the same way. Suppose the sets of coordinate vectors of $K$-points of $X$ and $X'$ agree. There is a $K$-isomorphism $\phi:X\simeq X'$ such that every coordinate vector of every $y:\operatorname{Spec}R\to X$, for every local commutative ring $R$, is also a coordinate vector of $\phi\circ y$.
