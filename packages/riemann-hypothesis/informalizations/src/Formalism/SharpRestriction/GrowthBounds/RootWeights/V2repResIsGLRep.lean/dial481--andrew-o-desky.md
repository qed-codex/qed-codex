---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/V2repResIsGLRep.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.v2rep_res_isGLRep"
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

## Integral weight spaces on a stable finite-dimensional subspace

[Theorem REP.0986](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.v2rep_res_isGLRep/)

Let $K$ be a field of characteristic zero, $V$ a $K$-vector space, $n\ge0$, and $E_{ab}\in\operatorname{End}_K(V)$ for $1\le a,b\le n$. Assume $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ For $\mu\in\mathbb Z^n$, put $$V_\mu=\{v\in V:E_{aa}v=\mu_av\text{ for every }a\}.$$ Let $W\subseteq V$ be finite-dimensional, stable under every $E_{ab}$, and contained in $\sum_{\mu\in\mathbb Z^n}V_\mu$. For the restricted operators on $W$, the same commutator relations hold, $$W=\sum_{\mu\in\mathbb Z^n}(W\cap V_\mu),$$ and every $w\in W$ belongs to a finite-dimensional subspace of $W$ stable under all restricted operators.
