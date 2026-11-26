---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SliceReducedAwayZariski.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Heights.BranchOrder.localOrder"
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

## Divisor multiplicity from local branches

[Theorem AG.0056](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Heights.BranchOrder.localOrder/)

Let $J\subseteq\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim(\mathbb C[x]/J)=d+1$, and let $\ell(x)=\sum_j u_jx_j\notin J$. Let $W$ be a minimal prime of $J+(\ell)$ and $p\in V(W)$.

For $b=1,\ldots,m$, suppose $\gamma_b:B_{d+1}(0,r_b)\to V(J)$ is holomorphic and injective, $r_b>0$, and $\gamma_b(0)=p$. Assume their images cover $V(J)$ near $p$; near $p$, $V(W)$ lies in every $\gamma_b(B_{d+1}(0,r_b)\cap\{t_1=0\})$; and images of distinct branches intersect only in $\{\ell=0\}$. Suppose, for integers $a_b\ge0$, $$\ell(\gamma_b(t))=t_1^{a_b}H_b(t),$$ where $H_b$ is holomorphic and nowhere zero on its ball. Then $$\operatorname{length}_{\mathbb C[x]_W}\bigl((\mathbb C[x]/(J+(\ell)))_W\bigr)=\sum_{b=1}^m a_b.$$ Here $B_{d+1}(0,r)$ is the open Euclidean ball in $\mathbb C^{d+1}$.
