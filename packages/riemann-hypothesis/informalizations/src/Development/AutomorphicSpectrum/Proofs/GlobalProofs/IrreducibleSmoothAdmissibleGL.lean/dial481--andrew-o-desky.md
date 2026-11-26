---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/IrreducibleSmoothAdmissibleGL.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible"
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

## Admissibility of smooth irreducible general linear representations

[Theorem REP.1662](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible/)

Let $k$ be a nonarchimedean local field, $n\ge0$, and $\pi$ a smooth irreducible representation of $\mathrm{GL}_n(k)$ on a complex vector space $V$. Then $\pi$ is admissible: for every compact open subgroup $K\subseteq\mathrm{GL}_n(k)$, $$\dim_{\mathbb C}V^K<\infty.$$
