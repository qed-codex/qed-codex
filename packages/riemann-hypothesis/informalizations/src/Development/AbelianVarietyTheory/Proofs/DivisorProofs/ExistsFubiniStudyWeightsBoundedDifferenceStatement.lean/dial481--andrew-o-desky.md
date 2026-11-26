---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFubiniStudyWeightsBoundedDifferenceStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_fubiniStudyWeights_bounded_difference"
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

## Uniform boundedness of normalized section weights

[Theorem ARAK.1376](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_fubiniStudyWeights_bounded_difference/)

Let $k$ be an integral commutative ring finite over $\mathbb Z$, and let $p:X\to\operatorname{Spec}k$ be an integral projective scheme, flat over $\mathbb Z$, of dimension $D+1$. Fix Hermitian line bundles $\overline L,\overline A$ with chosen nonzero rational trivializations. Let $e\ge1$, and choose $D+1$ global sections $x_0,\ldots,x_D$ of $L^{\otimes e}$ with no common zero; regard them as rational functions using the chosen trivialization.

There is $B\ge0$ such that for every integer $n\ge1$ the functions $$u_n(\sigma,y)=\frac1{en}\log\left(\sum_{j=0}^D\|x_j(y)\|_\sigma^{2n}\right)$$ form a smooth real-valued family, compatible with complex conjugation, and satisfy $$|u_n(\sigma,y)|\le B$$ for every embedding $\sigma:k\to\mathbb C$ and every complex point $y$ above $\sigma$.
