---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/TameParahoricRepSplitsAsProduct.lean",
  "declarations": [
    "GlobalTheory.TameIwahori.exists_prinSeries"
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

## Principal-series support from a compact Iwahori eigenvector

[Theorem REP.0519](https://andrewodesky.com/rh/lean/GlobalTheory.TameIwahori.exists_prinSeries/)

Assume the representation-theoretic inputs in the conventions. Let $k$ be a nonarchimedean local field, $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_n(k)$, and $\theta_1,\ldots,\theta_n:k^\times\to\mathbb C^\times$ smooth characters. Suppose $0\ne v\in\pi$ is fixed by the inverse image of the upper unitriangular subgroup under $\operatorname{GL}_n(\mathcal O_k)\to\operatorname{GL}_n(\kappa_k)$ and satisfies $$\pi(\operatorname{diag}(u_1,\ldots,u_n))v=\prod_i\theta_i(u_i)\,v\qquad(u_i\in\mathcal O_k^\times).$$ There are characters $\psi_1,\ldots,\psi_n:k^\times\to\mathbb C^\times$ such that $\psi_i|_{\mathcal O_k^\times}=\theta_i|_{\mathcal O_k^\times}$, every $\psi_i$ occurs in the cuspidal support of $\pi$, and $\pi$ is a subquotient of the normalized principal series induced from $\psi_1\otimes\cdots\otimes\psi_n$.
