---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/IsSSRepOfFiniteIndex.lean",
  "declarations": [
    "GlobalTheory.FiniteIndexSemisimple.isSSRep_of_finiteIndex"
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

## Semisimplicity descends from a subgroup of finite index

[Theorem REP.0920](https://andrewodesky.com/rh/lean/GlobalTheory.FiniteIndexSemisimple.isSSRep_of_finiteIndex/)

Let $k$ be a field of characteristic zero, $\Gamma$ a group, $n\ge0$, and $\rho:\Gamma\to\operatorname{GL}_n(k)$ a representation. If $N\subseteq\Gamma$ is a subgroup of finite index and $\rho|_N$ is semisimple, then $\rho$ is semisimple.
