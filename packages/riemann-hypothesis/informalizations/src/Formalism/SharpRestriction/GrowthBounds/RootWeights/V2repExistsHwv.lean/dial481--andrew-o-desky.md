---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/V2repExistsHwv.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.v2rep_exists_hwv"
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

## A highest-weight vector in a finite-dimensional stable subspace

[Theorem REP.0329](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.v2rep_exists_hwv/)

Let $K$ be a field of characteristic zero, $V$ a $K$-vector space, and $E_{ab}\in\operatorname{End}_K(V)$ for $1\le a,b\le n$, satisfying $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ For $\nu\in\mathbb Z^n$ put $V_\nu=\{v:E_{aa}v=\nu_av\text{ for all }a\}$. Let $Z\subseteq V$ be nonzero, finite-dimensional, stable under every $E_{ab}$, and contained in $\sum_{\nu\in\mathbb Z^n}V_\nu$. There exist $\mu\in\mathbb Z^n$ and $0\ne v\in Z$ such that $$E_{aa}v=\mu_av\quad(1\le a\le n),\qquad E_{ab}v=0\quad(a<b).$$
