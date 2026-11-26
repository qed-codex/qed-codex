---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TraceLimits/SlopeTestRemainingChoices.lean",
  "declarations": [
    "UpperTheory.Gal.Lim.joint"
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

## Joint approximation of traces and auxiliary sequences

[Theorem ALG.1622](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Lim.joint/)

Let $k$ be an ultrametric normed field, $\Gamma$ a group, $a\ge0$, and $r,\rho_i:\Gamma\to\operatorname{GL}_a(k)$ with $i\in I$. Fix sets $J,J'$, maps $\theta:J\to k$, $\theta':J'\to k$, $\eta_i:J\to k$, $\eta'_i:J'\to k$, and $A\subseteq I$. Set $\Theta=\theta\sqcup\theta'$ and $H_i=\eta_i\sqcup\eta'_i$, as points of $k^{J\sqcup J'}$. Assume that for every $\varepsilon>0$ there are a finite set $B\subseteq\{H_i:i\in A\}$ and scalars $c_h\in k$ such that $$\left|P(\Theta)-\sum_{h\in B}c_hP(h)\right|\le\varepsilon\qquad(P\in\mathbb Z[X_j:j\in J\sqcup J']).$$ Assume also that, for every finite $F\subseteq I$, coefficients $d_i\in k$, and $\delta\in\mathbb R$, the inequalities $$\left|P(\theta)-\sum_{i\in F}d_iP(\eta_i)\right|\le\delta\quad(P\in\mathbb Z[X_j:j\in J])$$ imply $|\operatorname{tr}r(g)-\sum_{i\in F}d_i\operatorname{tr}\rho_i(g)|\le\delta$ for every $g\in\Gamma$.

Let $S:\mathbb N\to k$, let $s(\rho,j)\in k$ be assigned to every $a$-dimensional representation $\rho$ and $j\ge0$, and choose $p:\mathbb N\to J'$ and $u:\mathbb N\to k$ with $$S(j)=u(j)\theta'(p(j)),\qquad s(\rho_i,j)=u(j)\eta'_i(p(j))\quad(i\in A).$$ Then for every $n\ge0$ and $\varepsilon>0$ there are a finite $T\subseteq\{\rho_i:i\in A\}$ and coefficients $b_\rho\in k$ such that simultaneously $$\left|\operatorname{tr}r(g)-\sum_{\rho\in T}b_\rho\operatorname{tr}\rho(g)\right|\le\varepsilon\quad(g\in\Gamma),\qquad\left|S(j)-\sum_{\rho\in T}b_\rho s(\rho,j)\right|\le\varepsilon\quad(0\le j\le n).$$
