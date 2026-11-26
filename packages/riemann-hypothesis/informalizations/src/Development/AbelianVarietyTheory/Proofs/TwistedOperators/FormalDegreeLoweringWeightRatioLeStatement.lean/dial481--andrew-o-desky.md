---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/FormalDegreeLoweringWeightRatioLeStatement.lean",
  "declarations": [
    "GlobalTheory.T.formalDegree_loweringWeight_ratio_le"
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

## Formal-degree comparison after lowering one parameter

[Theorem REP.1388](https://andrewodesky.com/rh/lean/GlobalTheory.T.formalDegree_loweringWeight_ratio_le/)

Fix $n\ge3$, signatures $\varepsilon$ of size $n+1$ and $\varepsilon'$ of size $n$, and an identification deleting a positive-sign coordinate from $\varepsilon$. Let $\lambda,\mu$ be Harish–Chandra parameters for these signatures, with a common real bound $B$ on their absolute values. Assume the following parameter-pair conditions: adjacent entries in each decreasing list differ by at least $2$; opposite-sign entries have gaps at least $1000(n+1)^3$; the smaller signature has at least one negative coordinate and at least as many positive as negative coordinates; and the signed lists for $(\lambda,\mu)$ and for $(\lambda-e_s,\mu)$ satisfy the prescribed interlacing rule for every coordinate $s$.

Let $\pi,\sigma$ be the discrete-series models with parameters $\lambda,\mu$ in complex inner-product spaces. Then $\sigma$ has a formal degree, and $\pi$ has a formal degree $d$ such that for every $s$ and every discrete-series model $\rho$ with parameter $\lambda-e_s$, there is a formal degree $d_s$ with $$d\le2^n d_s.$$ All formal degrees use the fixed Haar measures on the respective unitary groups.
