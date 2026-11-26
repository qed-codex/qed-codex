---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/WeilRepresentationContinuityStatement.lean",
  "declarations": [
    "GlobalTheory.T.weil_representation_continuity"
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

## Joint continuity of the adelic Weil action on Schwartz functions

[Theorem THETA.0931](https://andrewodesky.com/rh/lean/GlobalTheory.T.weil_representation_continuity/)

Fix the source's global arithmetic datum over a CM extension $E/F$, a Hermitian space $V$ from its space package, and $n\ge0$. Let $\psi:\mathbb A_F\to\mathbb C^\times$ be a continuous nontrivial unitary additive character trivial on $F$. Let $\chi:\mathbb A_E^\times\to U(1)$ be a continuous Hecke character, with $\chi|_{\mathbb A_F^\times}=\eta^{\dim V}$ for every nontrivial continuous quadratic-extension character $\eta$ trivial on $F^\times$ and on adelic norms; assume such an $\eta$ exists. Choose a compatible family of archimedean embeddings, and an additive Haar measure $\mu$ on $\operatorname{Mat}_{\dim V,n}(\mathbb A_E)$ with a measurable rational fundamental domain of measure one.

Suppose $\omega$ is a representation of the split rank-$n$ unitary group on the corresponding adelic Schwartz space, satisfying the Schrödinger formulas below. For every Schwartz function $\Phi$, the map $$(g,x)\longmapsto(\omega(g)\Phi)(x)$$ is jointly continuous.
