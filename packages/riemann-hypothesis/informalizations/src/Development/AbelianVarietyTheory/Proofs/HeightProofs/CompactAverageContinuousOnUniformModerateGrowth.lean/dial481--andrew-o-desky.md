---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/CompactAverageContinuousOnUniformModerateGrowth.lean",
  "declarations": [
    "GlobalTheory.KAvgGrowth.continuousOn_and_umg_kAvg"
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

## Compact averaging preserves uniform moderate growth

[Theorem REP.0634](https://andrewodesky.com/rh/lean/GlobalTheory.KAvgGrowth.continuousOn_and_umg_kAvg/)

Let $J$ be a diagonal matrix with entries $\pm1$, let $G=\{g\in M_n(\mathbb C):g^*Jg=J\}$, and let $K$ be its standard maximal compact subgroup, with probability Haar measure $dk$. Let $f:M_n(\mathbb C)\to\mathbb C$ be continuous on $G$ and of uniform moderate growth there. For every continuous $e:K\to\mathbb C$, the function $$f_e(g)=\int_K e(k)f(gk)\,dk$$ is continuous on $G$ and of uniform moderate growth on $G$.
