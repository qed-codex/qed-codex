---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/NefShiftOfGeneratedAtCharZeroPoints.lean",
  "declarations": [
    "GlobalTheory.NefOfGen.nef_of_gen"
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

## Nefness after a constant change of metric

[Theorem ARAK.1587](https://andrewodesky.com/rh/lean/GlobalTheory.NefOfGen.nef_of_gen/)

Assume the source's arithmetic intersection calculus package. Let $k$ be an integral ring finite over $\mathbb Z$, and let $p:X\to\operatorname{Spec}k$ be an integral projective scheme, flat over $\mathbb Z$, of dimension $D+1$, $D\ge0$. Let $\overline M$ be a smooth Hermitian line bundle. Suppose its metric is semipositive and its degree on every integral curve over a finite field is nonnegative. Suppose some $M^{\otimes m}$, $m\ge1$, has a finite family of sections $s_1,\ldots,s_N$ such that at every point of $X$ with characteristic-zero residue field at least one $s_i$ is nonzero.

There is $t\ge0$ such that replacing every archimedean norm by $e^{-t}\|\cdot\|$ makes $\overline M$ nef: it retains semipositive metrics and nonnegative vertical degrees and has nonnegative arithmetic degree on every horizontal integral curve.
