---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BranchNormalisationHolds.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.BranchNorm.curveCoordinateGraph",
    "GlobalTheory.CompanionTheory.BranchNorm.normalCurveBranchOrder",
    "GlobalTheory.CompanionTheory.BranchNorm.placeHasBranch"
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

## Coordinate graphs on a punctured algebraic curve germ

[Theorem AG.0591](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.BranchNorm.curveCoordinateGraph/)

Let $I\subseteq\mathbb C[X_1,\ldots,X_n]$ be an ideal and $q\in\mathbb C^n$. Suppose $I$ is radical after localization at $q$, and the local ring of its zero set at $q$ has Krull dimension one. There is $\epsilon>0$ such that every $$x\in V(I)\cap B(q,\epsilon),\qquad x\ne q,$$ has the following description. There are an open neighborhood $W\subseteq\mathbb C^n$ of $x$, an index $i$, an open set $U\subseteq\mathbb C$, and a holomorphic map $g:U\to\mathbb C^n$ with $g_i(t)=t$, such that $$z\in V(I)\quad\Longleftrightarrow\quad z_i\in U\ \text{and}\ g(z_i)=z\qquad(z\in W).$$

## Algebraic and analytic orders on a normalized curve

[Theorem AG.1292](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.BranchNorm.normalCurveBranchOrder/)

Let $J\subseteq\mathbb C[X_1,\ldots,X_n]$ be prime with $\dim\mathbb C[X]/J=1$. Let $\widetilde X\subseteq\mathbb C^{n+m}$ be an affine normal integral model whose coordinate projection to $V(J)$ is finite and birational. More explicitly, its prime ideal $\widetilde J$ contracts to $J$, its coordinate ring is integrally closed, and each extra coordinate is integral over $\mathbb C[X]/J$ and is a fraction of elements of that ring. Let $w\in\widetilde X$, $r>0$, and let $\phi:B(0,r)\to\widetilde X$ be injective and holomorphic, with $\phi(0)=w$.

For every polynomial $g\in\mathbb C[X_1,\ldots,X_n,Y_1,\ldots,Y_m]$, $$\operatorname{ord}_{\mathcal O_{\widetilde X,w}}(g)=\operatorname{ord}_{t=0}g(\phi(t)).$$ The polynomial is mapped to the local ring on the left; the right side is the analytic vanishing order, allowing $\infty$.

## Places of the local normalization are analytic branches

[Theorem AG.1293](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.BranchNorm.placeHasBranch/)

Let $I\subseteq\mathbb C[X_1,\ldots,X_n]$, $q\in\mathbb C^n$, $\mathfrak m_q=\ker\operatorname{ev}_q$, and $$A=\mathbb C[X]_{\mathfrak m_q}/I\mathbb C[X]_{\mathfrak m_q}.$$ Assume that $I$ is radical at $q$ and $\dim A=1$. Let $\widetilde A$ be the integral closure of $A$ in its total quotient ring. Suppose that finitely many injective holomorphic maps $c_b:B(0,r_b)\to V(I)$ have $r_b>0$, $c_b(0)=q$, cover $V(I)$ in a neighborhood of $q$, and have pairwise intersections contained in $\{q\}$.

For every maximal ideal $P$ of $\widetilde A$ there is an index $b$ such that, for every polynomial $f$, $$\operatorname{ord}_{\widetilde A_P}(f)=\operatorname{ord}_{t=0}f(c_b(t)).$$ On the left, $f$ is mapped through $\mathbb C[X]\to A\to\widetilde A\to\widetilde A_P$; on the right is analytic vanishing order, with value $\infty$ for the zero germ.
