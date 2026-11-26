---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/SiuInequalityIntegralHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.siu_inequality_integral_holds"
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

## A nonzero section from positive top intersection

[Theorem AG.1438](https://andrewodesky.com/rh/lean/GlobalTheory.T.siu_inequality_integral_holds/)

Let $K$ and $I_k$ be finite sets, let $\Omega$ be a field of characteristic zero, and let $y=(y_{ki})\in\Omega^{\coprod_k I_k}$. Define $$P=\ker\bigl(\mathbb Z[X_{ki}]\to\Omega[T_k:k\in K],\ X_{ki}\mapsto y_{ki}T_k\bigr),\qquad P_{\mathbb Q}=P\mathbb Q[X_{ki}].$$ Let $D\ge0$ and $\alpha\in\mathbb Z^K$. Assume $K\ne\varnothing$, $P$ is a relevant multihomogeneous prime ideal with $P\cap\mathbb Z=0$, and $$\dim(\mathbb Z[X_{ki}]/P)=D+1+|K|.$$ Assume every element of $\Omega$ is a quotient of evaluations at $y$ of integral polynomials of the same multidegree, with nonzero denominator. Let $\mathcal I$ be an intersection system over $\mathbb Q$ satisfying the point-degree normalization and rational-divisor recursion. Assume $\alpha$ has nonnegative $\mathcal I$-degree on every integral projective curve contained in the multiprojective variety of $P_{\mathbb Q}$, and $$\mathcal I(P_{\mathbb Q};\underbrace{\alpha,\ldots,\alpha}_{D})>0.$$ For a choice $c=(c_k)$ with every $y_{k,c_k}\ne0$, put $A_c=\mathbb Z[y_{ki}/y_{k,c_k}:k\in K,i\in I_k]$. There exist $k\ge1$ and $0\ne e\in\Omega$ such that $$e\prod_{\kappa\in K}y_{\kappa,c_\kappa}^{-(k\alpha_\kappa-1)}\in A_c\qquad\text{for every such }c.$$ Here relevance means that each coordinate block has at least one coordinate outside $P$.
