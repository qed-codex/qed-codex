---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/WeightCharacters/LadicWeightEmbeddingOverPlace.lean",
  "declarations": [
    "UpperTheory.Gal.Wt.famWt_holds",
    "UpperTheory.Gal.Wt.kaplFin_holds",
    "UpperTheory.Gal.Wt.kapl_holds",
    "UpperTheory.Gal.Wt.sepPoly_holds"
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

## Polynomial approximation on ultrametric balls

[Theorem ALG.1231](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Wt.kaplFin_holds/)

Let $k$ be a normed field whose distance is ultrametric, let $S\subset k$ be finite, and let $\delta,\varepsilon\in\mathbb R$ satisfy $\delta>0$ and $0<\varepsilon\le1$. Suppose $\|c\|\ge\delta$ for every $c\in S$. There is $P\in k[X]$ such that $$\|x\|\le\delta\ \Longrightarrow\ \|P(x)\|\le1,$$ $$c\in S,\quad\|x-c\|\le\|c\|/2\ \Longrightarrow\ \|P(x)\|\le\varepsilon,$$ $$\|x\|\le\delta\varepsilon\ \Longrightarrow\ \|P(x)-1\|\le\varepsilon.$$

## Polynomials separating disjoint ultrametric compact sets

[Theorem ALG.1366](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Wt.sepPoly_holds/)

Let $k$ be a normed field with ultrametric distance, let $I$ be a finite set, and let $Z_1,Z_2\subseteq k^I$ be disjoint compact sets. For every $\varepsilon>0$ there is $P\in k[X_i:i\in I]$ such that $$|P(z)-1|\le\varepsilon\quad(z\in Z_1),\qquad |P(z)|\le\varepsilon\quad(z\in Z_2).$$

## Polynomial approximation near zero in an ultrametric field

[Theorem PHT.1560](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Wt.kapl_holds/)

Let $k$ be a normed field with ultrametric distance, $Y\subseteq k$ compact, and $\delta,\varepsilon\in\mathbb R$ with $\delta>0$ and $0<\varepsilon\le1$. There is a polynomial $p\in k[T]$ such that $$|p(x)|\le1\quad(x\in Y),\qquad |p(x)|\le\varepsilon\quad(x\in Y,\ |x|\ge\delta),$$ $$|p(x)-1|\le\varepsilon\quad(x\in k,\ |x|\le\delta\varepsilon).$$

## Archimedean weights in a bounded automorphic family

[Theorem AGR.1710](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Wt.famWt_holds/)

Let $E$ be a CM number field, $G=U(a)(\mathbb A_{E^+})$ the source's definite unitary group, $\tau:E\hookrightarrow\mathbb C$, and $K\subseteq G$ any subgroup. Let $W$ be the source's finite-dimensional archimedean representation with prescribed dominant integral weights $W(\tau')$, let $\nu\in\mathbb Z^a$ be dominant, and let $d\in\mathbb N$. For $k\ge0$, put $t_k(z)=\operatorname{diag}(z,\ldots,z,1,\ldots,1)$, with $z$ in the first $\min(k,a)$ positions, and $s_k(\nu)=\sum_{i\le\min(k,a)}\nu_i$. Write $x_k(z)$ for any infinite-component element supported at $\tau$ with matrix $t_k(z)$ there.

Suppose $B(y_1,y_2):W\to\mathbb C^G$ is complex linear in its vector argument, for $y_1,y_2\in\operatorname{GL}_a(\mathbb C)$, and satisfies the following family conditions. Every value is an automorphic function fixed by $K$; all values together span a finite-dimensional space; and for every infinite-component element $x$, $$R_x B(y_1,y_2)v=B(g_\tau(x)y_1,g_\tau(x)y_2)(W(x)v),$$ where $R_x f(g)=f(gx)$ and $g_\tau(x)$ is its matrix at $\tau$. For upper-triangular $b$, $$B(y_1b,y_2)v=\left(\prod_i b_{ii}^{\nu_i}\right)B(y_1,y_2)v.$$ For all $k$, all choices of $x_k$, and all $y_1,y_2,v,g$, the circle function $$z\longmapsto[B(t_k(z)y_1,t_k(z)y_2)(W(x_k(z))v)](g)$$ is a finite linear combination of powers $z^m$ with $m\le s_k(\nu)+d$. With the first matrix argument fixed to $1$, the function $$z\longmapsto[B(1,t_k(z)y_2)(W(x_k(z))v)](g)$$ is a finite linear combination of powers $z^m$ with $m\ge-d$.

Let $U\subseteq\mathbb C^G$ be an automorphic representation containing all values of $B$, with at least one such value nonzero. There are dominant integral weights $\mu(\tau')$ at all complex embeddings such that $U$ has these weights and a nonzero $K$-fixed vector, $$\mu(\tau')=W(\tau')\quad\text{if }\tau'\text{ and }\tau\text{ define different complex places},\qquad |\mu_i(\tau)-\nu_i|\le2d\quad(1\le i\le a).$$
