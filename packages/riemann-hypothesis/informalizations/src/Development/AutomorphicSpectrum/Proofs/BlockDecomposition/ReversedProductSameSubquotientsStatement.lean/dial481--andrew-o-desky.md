---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ReversedProductSameSubquotientsStatement.lean",
  "declarations": [
    "GlobalTheory.T.reversed_product_same_subquotients"
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

## Irreducible subquotients survive reversal of an induced product

[Theorem REP.0663](https://andrewodesky.com/rh/lean/GlobalTheory.T.reversed_product_same_subquotients/)

Let $k$ be a nonarchimedean local field. Assume ([Admissibility of smooth irreducible general linear representations](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.SmGLBridge.irreducibleAdmissible/)) universally over nonarchimedean local fields, and assume that, for every $N$, every smooth irreducible complex representation $\pi$ of $\operatorname{GL}_N(k)$ satisfies $$\pi\circ(g\mapsto(g^{-1})^t)\simeq\pi^\vee.$$ Let $\pi_1,\ldots,\pi_h$ be smooth irreducible complex representations of $\operatorname{GL}_{n_i}(k)$, with $\sum_i n_i=N$. If a smooth irreducible complex representation $\sigma$ of $\operatorname{GL}_N(k)$ is a subquotient of $$\pi_1\times\cdots\times\pi_h,$$ then it is a subquotient of $$\pi_h\times\cdots\times\pi_1.$$
