---
{
  "module": "src/Development/WeilBound/ThetaLifts/FrameEstimates/OneVar.lean",
  "declarations": [
    "PositivityTheory.ThKEst.oneVar_of"
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

## A uniform bound for a scaled lattice sum

[Theorem ANT.1633](https://andrewodesky.com/rh/lean/PositivityTheory.ThKEst.oneVar_of/)

Let $V$ be a finite-dimensional real normed vector space, $d=\dim_{\mathbb R}V$, and $\Lambda\subseteq V$ a discrete $\mathbb Z$-submodule. If $N\in\mathbb N$ satisfies $d<N$, there is $C\ge0$ such that for every $t\in\mathbb R$, $$\sum_{x\in\Lambda}(1+e^{-t}\|x\|)^{-N}\le C\exp\bigl(d\max(0,t)\bigr).$$
