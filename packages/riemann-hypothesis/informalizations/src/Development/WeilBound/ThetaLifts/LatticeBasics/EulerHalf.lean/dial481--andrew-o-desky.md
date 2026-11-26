---
{
  "module": "src/Development/WeilBound/ThetaLifts/LatticeBasics/EulerHalf.lean",
  "declarations": [
    "GlobalTheory.ThK.Dbl.dProd"
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

## A nonvanishing doubling Euler product on a right half-plane

[Theorem ANT.1614](https://andrewodesky.com/rh/lean/GlobalTheory.ThK.Dbl.dProd/)

Let $F\subseteq E$ be number fields, $n\ge0$, and $T$ a finite set of finite places of $F$. For each finite place $v$ set $q_v=|\mathcal O_F/\mathfrak p_v|$ and let $\epsilon_v=1$ if an $F$-algebra embedding $E\hookrightarrow F_v$ exists, and $\epsilon_v=-1$ otherwise. Define $$D_v(s)=\prod_{i=0}^{n-1}\left(1-\epsilon_v^{\,n-i-1}q_v^{-(2s+i+1)}\right)^{-1}.$$ There is a holomorphic function $d$ on $\Re s>0$, nonzero at every point of this half-plane, such that $$d(s)=\prod_{v\notin T}D_v(s)\qquad(\Re s>0),$$ where the product converges as a product indexed by finite places.
