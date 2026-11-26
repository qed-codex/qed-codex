---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean",
  "declarations": [
    "UpperTheory.Top.shape_closed_link_n_of_green"
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

## Existence of families with tied counting data for a supplied property of field data

[Theorem ANT.1.1767](https://andrewodesky.com/rh/lean/UpperTheory.Top.shape_closed_link_n_of_green/)

Assume the polynomial parametrization in ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)), for every prime $p$, every integer $d\ge1$ and every choice of the map $\tau$ and of the generators $\gamma_e$.

Let $\mathcal A$ be a class of families, and let a selection $\sigma$ on $\mathcal A$, functions $c_T$ and $c_{30}$, auxiliary records and a real number $c_I$ be data of the kinds listed in ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)) that satisfy the forty conditions of that entry. The selection may have thresholds, as explained in the conventions.

Let $\lambda>1$, and let $G$ be a property of field data that satisfies the supply condition with exponent $\lambda$. Suppose that every family in the class $\mathcal E(G,\lambda)$ satisfies the kernel bound eventually. Then there are real numbers $E_D$, $E_P$ and $\varepsilon_1>0$ such that, for every $0<\varepsilon<\varepsilon_1$, there are a family $\mathcal F$ in $\mathcal E(G,\lambda)$ with parameter $\varepsilon$ and real numbers $K,C_*,e_K,C_L,x_0$ for which $\mathcal F$ has tied counting data at $x$, with constants $E_D,E_P,K,C_*,e_K,C_L$, at every occupied scale $x\ge x_0$ of $\mathcal F$.
