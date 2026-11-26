---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/LineBundleTrivialIsoDescendFieldStatement.lean",
  "declarations": [
    "GlobalTheory.T.lineBundle_trivial_iso_descend_field"
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

## Triviality and isomorphism of line bundles descend over fields

[Theorem AG.1097](https://andrewodesky.com/rh/lean/GlobalTheory.T.lineBundle_trivial_iso_descend_field/)

Let $i:K_0\hookrightarrow K$ be a field embedding and $X_0/K_0$ a smooth proper geometrically connected scheme. Let $\phi:X\to X_0$ identify $X$ with its base change to $K$. If $M$ is a line bundle on $X_0$ and $\phi^*M$ has a nowhere-vanishing global section, then $M$ has one. If $M,N$ are line bundles on $X_0$ and $\phi^*M\simeq\phi^*N$, then $M\simeq N$.
