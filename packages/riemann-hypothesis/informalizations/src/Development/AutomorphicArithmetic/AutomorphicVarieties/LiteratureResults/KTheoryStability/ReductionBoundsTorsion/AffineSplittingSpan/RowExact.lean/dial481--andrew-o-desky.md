---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/AffineSplittingSpan/RowExact.lean",
  "declarations": [
    "PositivityTheory.KB.SplitAffineSpectral.NormTraceLemmas.row_exact"
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

## Exactness of an invariant homogeneous cochain row

[Theorem ALG.0728](https://andrewodesky.com/rh/lean/PositivityTheory.KB.SplitAffineSpectral.NormTraceLemmas.row_exact/)

Let $P,Q$ be groups and $\pi:P\to Q$ a homomorphism. Let $a,b\ge0$ and let $F:Q^{a+2}\times P^{b+1}\to\mathbb R$ satisfy $$F(\pi(g)x_0,\ldots,\pi(g)x_{a+1};gy_0,\ldots,gy_b)=F(x;y)\qquad(g\in P).$$ For a function $H$ on tuples of $Q$ and $P$, let $dH$ be the alternating sum obtained by deleting one $Q$-coordinate. If $dF=0$, there exists a function $G:Q^{a+1}\times P^{b+1}\to\mathbb R$ with the same simultaneous invariance such that $F=dG$.
