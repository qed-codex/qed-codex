---
{
  "module": "src/Formalism/LocalToGlobal/CharacterGerms/RowTiePKeyJoint.lean",
  "declarations": [
    "Formalism.L2.FormalSeriesBounds.RowTiePKey.jointEig_holds"
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

## Joint eigenvector decomposition for commuting potent matrices

[Theorem ALG.0963](https://andrewodesky.com/rh/lean/Formalism.L2.FormalSeriesBounds.RowTiePKey.jointEig_holds/)

Let $K$ be an algebraically closed field of characteristic zero, $n\ge0$, and $q\ge2$. Let $\mathcal T\subseteq M_n(K)$ satisfy $$T^q=T\quad(T\in\mathcal T),\qquad ST=TS\quad(S,T\in\mathcal T).$$ Every $v\in K^n$ is a finite sum $v=\sum_{j=1}^m w_j$ such that, for every $j$ and every $T\in\mathcal T$, there is $c\in K$ with $Tw_j=cw_j$.
