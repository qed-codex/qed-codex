---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/ClosedPhiHolds.lean",
  "declarations": [
    "UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_holds"
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

## Weil–Deligne power sums under joint approximation

[Theorem PHT.1706](https://andrewodesky.com/rh/lean/UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_holds/)

Let $E$ be a number field with algebraic closure $\Omega$, $\ell$ a prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and $a\ge1$. Fix compatible local period-ring data, a finite place $w$, a valuation ring of $\Omega$ over $w$, and the source's local comparison over a topological $\mathbb Z_\ell$-algebra, compatible with the induced Weil–Deligne construction. Let $r:G_E\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ be continuous and semisimple. Let $\mathcal C$ be a set of continuous representations of the same dimension, crystalline in these local data, all with prescribed jump multiset $J_\tau$ at each embedding induced by a finite local coefficient extension.

For $\sigma\in W_w$, let $p_j(\rho)=\sum_\lambda\lambda^j$, where the sum runs over the roots, with multiplicity, of the characteristic polynomial of $\sigma$ in the Weil–Deligne parameter of $\rho$. Take $S:\mathbb N\to\overline{\mathbb Q}_\ell$. Assume that for every $n\ge0$ and $\varepsilon>0$ there are a finite $T\subset\mathcal C$ and coefficients $c_\rho\in\overline{\mathbb Q}_\ell$ with $$\left|\operatorname{tr}r(g)-\sum_{\rho\in T}c_\rho\operatorname{tr}\rho(g)\right|_\ell\le\varepsilon\quad(g\in G_E),$$ $$\left|S(j)-\sum_{\rho\in T}c_\rho\iota^{-1}(p_j(\rho))\right|_\ell\le\varepsilon\quad(0\le j\le n).$$ Then $p_j(r)=\iota(S(j))$ for every $j\ge0$.
