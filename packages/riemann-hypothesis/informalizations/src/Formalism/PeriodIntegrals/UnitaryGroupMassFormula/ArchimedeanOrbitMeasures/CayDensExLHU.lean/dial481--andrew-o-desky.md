---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/CayDensExLHU.lean",
  "declarations": [
    "HcInf.local_haar_unique"
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

## Local proportionality to Haar measure

[Theorem ALG.0812](https://andrewodesky.com/rh/lean/HcInf.local_haar_unique/)

Let $G$ be a locally compact, second-countable Hausdorff topological group, $m$ a left Haar measure and $\beta$ a Borel measure. Let $W$ be an open neighborhood of $1$. Suppose $$\beta(hS)=\beta(S)$$ whenever $h\in G$, $S$ is Borel, and $S,hS\subseteq W$. Assume $\beta(K)<\infty$ for every compact $K\subseteq W$ and $\beta(W)>0$. There are $0<t<\infty$ and a neighborhood $W'\subseteq W$ of $1$ such that $$\beta|_{W'}=t\,m|_{W'}.$$
