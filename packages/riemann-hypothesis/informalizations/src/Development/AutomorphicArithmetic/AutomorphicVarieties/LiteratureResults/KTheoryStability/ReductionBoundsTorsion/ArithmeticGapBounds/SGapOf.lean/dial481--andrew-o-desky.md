---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/ArithmeticGapBounds/SGapOf.lean",
  "declarations": [
    "PositivityTheory.KB.sGap_of"
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

## A three-fifths contraction for an arithmetic Hecke average

[Theorem AGR.0184](https://andrewodesky.com/rh/lean/PositivityTheory.KB.sGap_of/)

Let $L$ be a totally complex number field, $N\ge3$, and $\pi\in\mathcal O_L$ a prime element with $|\mathcal O_L/(\pi)|\ge25$. Put $$G=\prod_{w\mid\infty}\operatorname{GL}_N(\mathbb C),\qquad G^1=\prod_{w\mid\infty}\operatorname{SL}_N(\mathbb C),\qquad\Gamma=\operatorname{GL}_N(\mathcal O_L).$$ Let $\mathcal F\subset G^1$ be a measurable fundamental domain for the diagonal image of $\operatorname{SL}_N(\mathcal O_L)$, of finite measure for a left and right Haar measure $\mu$. Let $f:G\to\mathbb R$ be continuous, left $\Gamma$-invariant, invariant under the full center $\prod_w\mathbb C^\times$, square-integrable on $\mathcal F$, and of mean zero there.

Put $q=\operatorname{diag}(\pi,1,\ldots,1)\in\operatorname{GL}_N(L)$, $H=\Gamma\cap q^{-1}\Gamma q$, and $$Tf(x)=[\Gamma:H]^{-1}\sum_{\gamma\in H\backslash\Gamma}f(q\gamma x),$$ using the diagonal archimedean embeddings in this formula. Then $Tf$ has all the same stated properties as $f$ and $$\int_{\mathcal F}|Tf|^2\,d\mu\le\left(\frac35\right)^2\int_{\mathcal F}|f|^2\,d\mu.$$
