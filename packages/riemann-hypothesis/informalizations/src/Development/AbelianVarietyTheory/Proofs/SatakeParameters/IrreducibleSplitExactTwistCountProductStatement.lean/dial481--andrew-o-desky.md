---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/IrreducibleSplitExactTwistCountProductStatement.lean",
  "declarations": [
    "GlobalTheory.T.irreducible_split_exact_twistCount_product"
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

## Separating one unramified character line in cuspidal support

[Theorem REP.0743](https://andrewodesky.com/rh/lean/GlobalTheory.T.irreducible_split_exact_twistCount_product/)

Assume the three representation-theoretic packages specified below. Let $k$ be a nonarchimedean local field and let $r,t\ge0$. Let $\chi:k^\times\to\mathbb C^\times$ be smooth and let $\pi$ be a smooth irreducible complex representation of $\operatorname{GL}_{r+t}(k)$. Fix a cuspidal-support list $\sigma_1,\ldots,\sigma_s$, where $\sigma_i$ is a representation of $\operatorname{GL}_{d_i}(k)$. Suppose exactly $t$ indices satisfy $$d_i=1,\qquad\sigma_i\simeq\chi\,\operatorname{unr}(\alpha)\quad\text{for some }\alpha\in\mathbb C^\times.$$ There are smooth irreducible representations $\pi_1$ of $\operatorname{GL}_r(k)$ and $\pi_2$ of $\operatorname{GL}_t(k)$ such that $$\pi\simeq\pi_1\times\pi_2,$$ and no $\chi\operatorname{unr}(\alpha)$ occurs in the cuspidal support of $\pi_1$.
