---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CurveBranchLengthHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.curve_branch_length_holds"
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

## Local intersection length from orders on analytic branches

[Theorem AG.1648](https://andrewodesky.com/rh/lean/GlobalTheory.T.curve_branch_length_holds/)

Let $I\subseteq\mathbb C[X_1,\ldots,X_n]$, let $q,u\in\mathbb C^n$, and put $\ell_u(x)=\sum_i u_i x_i$ and $\mathfrak m_q=\ker(\operatorname{ev}_q)$. Assume that $I$ is radical at $q$. Let $c_b:B(0,r_b)\to V(I)$, $1\le b\le m$, be injective holomorphic maps with $r_b>0$ and $c_b(0)=q$, whose images cover $V(I)$ in some neighborhood of $q$. Suppose distinct images intersect only in $\{\ell_u=0\}$. For integers $o_b\ge0$, suppose $$\ell_u(c_b(t))=t^{o_b}H_b(t)\qquad(|t|<r_b),$$ where each $H_b$ is holomorphic and nowhere zero. For a module $M$, let $\lambda(M)$ be its module length when finite, and let $\lambda(M)=0$ when its length is infinite. Then $$\lambda_{\mathbb C[X]_{\mathfrak m_q}} \left(\mathbb C[X]_{\mathfrak m_q}/(I,\ell_u)\mathbb C[X]_{\mathfrak m_q}\right) =\sum_{b=1}^m o_b.$$ The same convention for infinite module length applies on the left.
