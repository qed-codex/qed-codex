---
{
  "module": "src/Formalism/RealPlaceAnalysis/RealPlaceTaylor/IndefiniteUnitaryPreservesForm.lean",
  "declarations": [
    "Formalism.REAL.polar_decomposition_holds"
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

## Polar decomposition for an indefinite unitary group

[Theorem REP.1137](https://andrewodesky.com/rh/lean/Formalism.REAL.polar_decomposition_holds/)

Let $n\ge0$, choose $\varepsilon_i\in\{1,-1\}$, and put $J=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)$. Set $$G=\{g\in M_n(\mathbb C):g^*Jg=J\},\quad K=\{k\in U(n):kJ=Jk\},$$ $$\mathfrak p=\{X\in M_n(\mathbb C):X^*J+JX=0,\ XJ=-JX\}.$$ Every $g\in G$ has a unique decomposition $g=k\exp X$ with $k\in K$ and $X\in\mathfrak p$. There is a function $L:M_n(\mathbb C)\to M_n(\mathbb C)$, continuous on $G$, such that for every $g\in G$, $$L(g)\in\mathfrak p,\qquad g\exp(-L(g))\in K.$$
