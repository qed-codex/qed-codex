---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DepthZeroSupercuspidalCuspidalModule.lean",
  "declarations": [
    "GlobalTheory.DepthZeroCusp.depthZeroCuspidal"
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

## Cuspidality of the finite representation at depth zero

[Theorem REP.0196](https://andrewodesky.com/rh/lean/GlobalTheory.DepthZeroCusp.depthZeroCuspidal/)

Let $p$ be prime and $n\ge1$. Let $\pi$ be an irreducible supercuspidal complex representation of $\operatorname{GL}_n(\mathbb Q_p)$. Put $$K=\operatorname{GL}_n(\mathbb Z_p),\qquad K_1=\ker(K\to\operatorname{GL}_n(\mathbb F_p)).$$ If $V^{K_1}\ne0$, the induced representation of $K/K_1=\operatorname{GL}_n(\mathbb F_p)$ on $V^{K_1}$ is cuspidal.
