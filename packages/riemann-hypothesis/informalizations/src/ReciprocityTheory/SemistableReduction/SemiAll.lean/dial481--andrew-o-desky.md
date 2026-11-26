---
{
  "module": "src/ReciprocityTheory/SemistableReduction/SemiAll.lean",
  "declarations": [
    "ReciprocityTheory.MultiplicativeHeights.Closed.semistable"
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

## A semistable majorant of a self-dual Hermitian lattice

[Theorem ARAK.0407](https://andrewodesky.com/rh/lean/ReciprocityTheory.MultiplicativeHeights.Closed.semistable/)

Let $K$ be a number field with an involution $c$ inducing complex conjugation under every embedding $\sigma:K\hookrightarrow\mathbb C$. Let $S\in\operatorname{Mat}_r(K)$ be $c$-Hermitian and let $L\subseteq K^r$ be a finitely generated $\mathcal O_K$-module spanning $K^r$, self-dual for $h_S(x,y)=c(x)^{\mathsf T}Sy$. There are positive definite Hermitian matrices $H_\sigma$ with $$H_\sigma\sigma(S)^{-1}H_\sigma=\sigma(S),\qquad H_{\bar\sigma}=\overline{H_\sigma},$$ such that $L$ has degree zero and every $\mathcal O_K$-submodule $B\subseteq L$ has degree at most zero for these metrics. Moreover, if $N\in\operatorname{Mat}_r(K)$ preserves $L$ and $$u^*\sigma(N)^*H_\sigma\sigma(N)u<u^*H_\sigma u\qquad(\sigma:K\hookrightarrow\mathbb C,\ u\ne0),$$ then $N=0$.
