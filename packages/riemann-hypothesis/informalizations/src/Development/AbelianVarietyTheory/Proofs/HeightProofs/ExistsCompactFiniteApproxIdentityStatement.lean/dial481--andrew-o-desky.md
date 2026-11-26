---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsCompactFiniteApproxIdentityStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_compactFinite_approxIdentity"
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

## Uniform approximation to evaluation by compact-finite kernels

[Theorem REP.0830](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_compactFinite_approxIdentity/)

Let $n\ge0$, choose signs $\varepsilon_1,\ldots,\varepsilon_n\in\{\pm1\}$, and set $$J=\operatorname{diag}(\varepsilon_i),\qquad K=\{k\in U(n):kJ=Jk\}.$$ Let $dk$ be Haar probability measure on $K$. Let $X$ be a topological space and let $F:X\times K\to\mathbb C$ be continuous. For every compact $C\subseteq X$ and $\delta>0$, there is a continuous $e:K\to\mathbb C$ such that the span of all its left and right translates is finite-dimensional and $$\left|F(x,1)-\int_K e(k)F(x,k)\,dk\right|<\delta\qquad(x\in C).$$
