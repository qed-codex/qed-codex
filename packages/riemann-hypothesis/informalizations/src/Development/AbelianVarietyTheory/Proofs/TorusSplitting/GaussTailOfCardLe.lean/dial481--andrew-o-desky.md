---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TorusSplitting/GaussTailOfCardLe.lean",
  "declarations": [
    "GlobalTheory.gaussTail_of_card_le"
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

## A Gaussian tail bound from polynomial counting

[Theorem ALG.0882](https://andrewodesky.com/rh/lean/GlobalTheory.gaussTail_of_card_le/)

Let $I$ be a set, $h:I\to\mathbb R$, $g\ge0$ an integer, and $R_0>0$ with $R_0^2\ge16(2g+1)$. Suppose $h(i)\ge R_0$ for every $i$, and, for every $R\ge R_0$ and finite $S\subseteq I$ with $h(i)\le R$ on $S$, $$\#S\le(3R/R_0)^{2g}.$$ Then the family $\bigl(e^{-h(i)^2/16}\bigr)_{i\in I}$ is summable and $$\sum_{i\in I}e^{-h(i)^2/16}\le2\cdot9^g e^{-R_0^2/16}.$$
