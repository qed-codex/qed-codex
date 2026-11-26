---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/Assembly.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.ConeMassOfFibre.full"
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

## The Hausdorff mass of a cone from generic fibre cardinality

[Theorem AG.0465](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ConeMassOfFibre.full/)

Let $n,m,\delta\ge0$, let $H\in\operatorname{GL}_n(\mathbb C)$, and let $J\subset\mathbb C[X_1,\ldots,X_n]$ be a homogeneous prime ideal with $X_j\notin J$ for some $j$. Put $$C=\{y\in\mathbb C^n:q(H^ty)=0\text{ for every }q\in J\}.$$ For $\pi\in M_{m,n}(\mathbb C)$ and $w\in\mathbb C^m$, let $N(\pi,w)$ be the cardinality of $\{y\in C:\pi y=w\}$, with value $+\infty$ for an infinite fibre. Suppose that for Lebesgue-almost every $\pi$, for Lebesgue-almost every $w$, one has $N(\pi,w)=\delta$. Then $$\mathcal H^{2m}(C\cap B(0,1))=\delta\,\mathcal H^{2m}(\{y\in B(0,1):y_j=0\text{ for }j>m\}).$$
