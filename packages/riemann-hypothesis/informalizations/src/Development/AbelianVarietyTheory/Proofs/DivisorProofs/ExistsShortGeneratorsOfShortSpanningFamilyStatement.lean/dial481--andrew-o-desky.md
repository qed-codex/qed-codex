---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsShortGeneratorsOfShortSpanningFamilyStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_short_generators_of_short_spanning_family"
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

## Short integral generators from a short spanning family

[Theorem ARAK.1592](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_short_generators_of_short_spanning_family/)

Let $K$ be a number field of degree $d$, and let $V$ be a finite-dimensional $K$-vector space with its compatible $\mathcal O_K$-module structure. For every embedding $\sigma:K\hookrightarrow\mathbb C$, let $N_\sigma:V\to\mathbb R_{\ge0}$ satisfy $$N_\sigma(ax)=|\sigma(a)|N_\sigma(x),\qquad N_\sigma(x+y)\le N_\sigma(x)+N_\sigma(y).$$ Let $L\subseteq V$ be a finitely generated $\mathcal O_K$-submodule and $S\subseteq L$ a set with $\operatorname{span}_KS=V$ and $N_\sigma(y)\le A$ for every $y\in S$ and every $\sigma$, where $A\in\mathbb R$. Put $r=\dim_K\operatorname{span}_KL$ and $\Delta_K=\operatorname{disc}K$.

There exist $n\le2dr$, vectors $w_1,\ldots,w_n\in V$, and $B\ge1$ such that $$L=\sum_{i=1}^n\mathbb Zw_i,\qquad N_\sigma(w_i)\le B,\qquad B\le\max\{1,d^4r|\Delta_K|^{1/d}A\}.$$
