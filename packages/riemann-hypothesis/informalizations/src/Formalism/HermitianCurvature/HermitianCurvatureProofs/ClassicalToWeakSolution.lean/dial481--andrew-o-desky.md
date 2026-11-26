---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/ClassicalToWeakSolution.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.classical_to_weak_solution"
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

## A classical homogeneous solution is a weak solution

[Theorem ALG.0187](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.classical_to_weak_solution/)

Let $U\subseteq\mathbb R^d$ be open, $N\ge0$, and $$P=\sum_{k=0}^m\ \sum_{w\in\{1,\ldots,d\}^k}a_w(x)\partial_w,\qquad m\le N,$$ be a scalar differential operator with smooth complex coefficients on $U$. Here $\partial_w=\partial_{w_1}\cdots\partial_{w_k}$. Suppose $u:\mathbb R^d\to\mathbb C$ is $C^N$ on $U$ and $Pu=0$ there. For every smooth compactly supported $\varphi:\mathbb R^d\to\mathbb C$ with support contained in $U$, $$\int_{\mathbb R^d}u(x)P^t\varphi(x)\,dx=0,\qquad P^t\varphi=\sum_{k=0}^m\ \sum_w(-1)^k\partial_w(a_w\varphi).$$
