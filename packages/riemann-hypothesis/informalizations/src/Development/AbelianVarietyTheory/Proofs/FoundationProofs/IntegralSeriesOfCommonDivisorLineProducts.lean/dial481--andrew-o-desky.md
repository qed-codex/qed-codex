---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/IntegralSeriesOfCommonDivisorLineProducts.lean",
  "declarations": [
    "GlobalTheory.EvenTheta.intSer_of_common_divisor"
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

## Integrality of a common divisor of separated series products

[Theorem PHT.0424](https://andrewodesky.com/rh/lean/GlobalTheory.EvenTheta.intSer_of_common_divisor/)

Let $p$ be prime and let $e,\Psi,A,B\in\mathbb C_p[[T]]$ have bounded coefficient sequences. Let $m,n\ge0$, $y_1,\ldots,y_m,y'_1,\ldots,y'_n\in\mathbb C_p$, and suppose $$\Psi(0)=1,\qquad \Psi A=\left(\prod_{i=1}^m(e-y_iT^2)\right)^2,\qquad \Psi B=\prod_{j=1}^n(e-y'_jT^2),$$ with $y_i\ne y'_j$ for every $i,j$. Then every coefficient of $\Psi$ has $p$-adic absolute value at most $1$.
