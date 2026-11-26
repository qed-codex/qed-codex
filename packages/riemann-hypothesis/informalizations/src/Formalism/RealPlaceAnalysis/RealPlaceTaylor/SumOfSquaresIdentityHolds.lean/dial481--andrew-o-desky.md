---
{
  "module": "src/Formalism/RealPlaceAnalysis/RealPlaceTaylor/SumOfSquaresIdentityHolds.lean",
  "declarations": [
    "Formalism.REAL.sumOfSquaresIdentity_holds"
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

## A sum of squares from signed adjoint relations

[Theorem REP.1160](https://andrewodesky.com/rh/lean/Formalism.REAL.sumOfSquaresIdentity_holds/)

Let $V$ be a complex inner product space, $n\ge0$, and $\varepsilon:\{1,\ldots,n\}\to\{+,-\}$. Let $E_{ab}\in\operatorname{End}_{\mathbb C}(V)$ satisfy $$\langle E_{ab}x,y\rangle=s_{ab}\langle x,E_{ba}y\rangle,\qquad s_{ab}=\begin{cases}1&\varepsilon(a)=\varepsilon(b),\\-1&\varepsilon(a)\ne\varepsilon(b).\end{cases}$$ Set $C=\sum_{a,b}E_{ab}E_{ba}$ and $C_K=\sum_{\varepsilon(a)=\varepsilon(b)}E_{ab}E_{ba}$. Then, for every $w\in V$, $$\sum_{a,b}\|E_{ab}w\|^2=\langle w,(2C_K-C)w\rangle.$$
