---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockAdjoints.lean",
  "declarations": [
    "GlobalTheory.FockAdj.inner_pderiv"
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

## Differentiation and multiplication are adjoint in the Fock pairing

[Theorem REP.0324](https://andrewodesky.com/rh/lean/GlobalTheory.FockAdj.inner_pderiv/)

Let $I$ be a set with decidable equality, $H$ a complex inner product space, and $\iota:\mathbb C[X_i:i\in I]\to H$ a complex-linear map. Inner products are conjugate-linear in the first argument and linear in the second.

For a finitely supported multiindex $\alpha:I\to\mathbb N$, let $\operatorname{supp}(\alpha)=\{i:\alpha(i)\ne0\}$ and put $$X^\alpha=\prod_{i\in\operatorname{supp}(\alpha)}X_i^{\alpha(i)},\qquad \alpha!=\prod_{i\in\operatorname{supp}(\alpha)}\alpha(i)!,$$ with empty products equal to $1$. Suppose that for all such $\alpha,\beta$, $$\langle\iota(X^\alpha),\iota(X^\beta)\rangle=\begin{cases}\alpha!,&\alpha=\beta,\\0,&\alpha\ne\beta.\end{cases}$$

Then for every $i\in I$ and polynomials $P,Q$, $$\left\langle\iota\!\left(\frac{\partial P}{\partial X_i}\right),\iota(Q)\right\rangle=\langle\iota(P),\iota(X_iQ)\rangle.$$ Equivalently, $$\langle\iota(X_iP),\iota(Q)\rangle=\left\langle\iota(P),\iota\!\left(\frac{\partial Q}{\partial X_i}\right)\right\rangle.$$
