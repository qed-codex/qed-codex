---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterDerived.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.metricChange"
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

## Variation of an arithmetic intersection under a metric change

[Theorem ARAK.1569](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.metricChange/)

Let $K$ be a nonempty finite set and $I_k$ finite coordinate-index sets and put $R=\mathbb Z[X_{k,i}:k\in K,i\in I_k]$. Let $P\subset R$ be a relevant multihomogeneous horizontal prime defining an arithmetic variety $X\subset\prod_k\mathbb P^{|I_k|-1}_{\mathbb Z}$ of dimension $n+1$, $n\ge0$. Let $\overline L_1,\ldots,\overline L_n,\overline A$ be coordinate line bundles with smooth positive homogeneous metric functions. Let $u$ be a smooth real function on nonzero complex coordinate blocks, invariant under independent nonzero complex rescaling of each block.

Let $I_X$ be any arithmetic intersection family satisfying permutation symmetry, tensor-product additivity and arithmetic divisor recursion. Write $\overline{\mathcal O}(u)$ for the trivial line bundle whose metric function is $e^{-u}$. Then $$I_X(\overline L_1,\ldots,\overline L_n,\overline A\otimes\overline{\mathcal O}(u))=I_X(\overline L_1,\ldots,\overline L_n,\overline A)-\int_{X(\mathbb C)}u\,c_1(\overline L_1)\cdots c_1(\overline L_n).$$ Here the integral is the intersection integral of ([A logarithmic intersection integral on an analytic resolution](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.resBridge/)), obtained by summing the mixed complex-Hessian densities over finite projection sheets.
