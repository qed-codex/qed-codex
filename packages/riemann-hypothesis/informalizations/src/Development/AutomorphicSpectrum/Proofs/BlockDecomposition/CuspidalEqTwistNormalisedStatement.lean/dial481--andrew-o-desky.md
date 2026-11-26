---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CuspidalEqTwistNormalisedStatement.lean",
  "declarations": [
    "GlobalTheory.T.cuspidal_eq_twist_normalised"
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

## Cuspidal forms as twists of normalized forms

[Theorem REP.1692](https://andrewodesky.com/rh/lean/GlobalTheory.T.cuspidal_eq_twist_normalised/)

Let $E$ be a totally complex number field, $a\ge0$, and $\pi$ a cuspidal automorphic representation realized as a subspace of smooth automorphic forms on $\operatorname{GL}_a(\mathbb A_E)$. There are a cuspidal subrepresentation $\pi_0$ and a Hecke character $\chi$ of $E$ such that $$\pi=\pi_0\otimes\chi.$$ The representation $\pi_0$ is normalized in the following precise sense: every form $\phi$ in its space satisfies $$\phi(z(t)g)=\phi(g)$$ for every $t\in\mathbb R$ and $g\in\operatorname{GL}_a(\mathbb A_E)$, where $z(t)$ is the scalar $e^tI_a$ at every infinite place and the identity at every finite place.
