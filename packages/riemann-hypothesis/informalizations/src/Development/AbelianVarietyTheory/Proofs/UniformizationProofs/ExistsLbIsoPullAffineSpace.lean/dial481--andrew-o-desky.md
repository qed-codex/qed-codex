---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsLbIsoPullAffineSpace.lean",
  "declarations": [
    "GlobalTheory.exists_lbIso_pull_affineSpace"
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

## Line bundles on a product with affine space

[Theorem AG.0610](https://andrewodesky.com/rh/lean/GlobalTheory.exists_lbIso_pull_affineSpace/)

Let $K$ be a field and $X$ an integral locally noetherian $K$-scheme whose local rings are unique factorization domains. For every $g\ge0$ and every line bundle $L$ on $\mathbb A_K^g\times_KX$, there is a line bundle $L_0$ on $X$ with $$L\simeq\operatorname{pr}_X^*L_0.$$
