---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SmoothOfAlgClosedUnif.lean",
  "declarations": [
    "GlobalTheory.FlagBundle.tower"
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

## A projective variety completing a rational frame family to full flags

[Theorem AG.1500](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.tower/)

Use the rational frame systems and refinements of ([Rational frame systems and flag refinements](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.Fr/)). Let $F$ be a field, let $Z/F$ be smooth, geometrically integral and projective of dimension $d$, and identify its function field with $\Omega/F$. Fix a finite index set $I$, natural numbers $m_i,k_i$ with $k_i\le m_i$, and a rational frame system $S$ of type $k$ on $Z$.

There are a smooth geometrically integral projective variety $Y/F$, an $F$-embedding $\phi:\Omega\hookrightarrow F(Y)$, a morphism $f:Y\to Z$ inducing $\phi$, and a frame system $S'$ of type $m$ on $Y$ such that $(\phi,f)$ is a full-flag refinement from $S$ to $S'$ and $$\dim Y=d+\sum_{i\in I}\binom{m_i-k_i}{2}.$$
