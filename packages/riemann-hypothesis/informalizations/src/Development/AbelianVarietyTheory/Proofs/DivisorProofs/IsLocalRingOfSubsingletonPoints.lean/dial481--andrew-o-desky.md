---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsLocalRingOfSubsingletonPoints.lean",
  "declarations": [
    "GlobalTheory.ConnConstSplit.exists_isSum_conn_const"
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

## Splitting a p-divisible group into connected and constant parts

[Theorem PHT.1384](https://andrewodesky.com/rh/lean/GlobalTheory.ConnConstSplit.exists_isSum_conn_const/)

Let $p$ be prime and let $C$ be an algebraically closed field of characteristic zero. Let $v:C\to\mathbb R_{\ge0}$ be a valuation and let $\mathcal O$ be an integral local ring with an injective structure map $\mathcal O\to C$ identifying $\mathcal O$ with the valuation ring of $v$. Assume $p$ is not a unit of $\mathcal O$ and $\mathcal O$ is complete for the ideal $(p)$.

Every $p$-divisible group $G/\mathcal O$ admits a direct-sum decomposition $$G\simeq G_1\oplus G_2$$ by morphisms of $p$-divisible groups, where the coordinate ring of $G_1[p^n]$ is local for every $n$, and the coordinate ring of $G_2[p^n]$ is isomorphic as an $\mathcal O$-algebra to $$\prod_{j=1}^{p^{n h_2}}\mathcal O,\qquad h_2=\operatorname{ht}(G_2).$$
