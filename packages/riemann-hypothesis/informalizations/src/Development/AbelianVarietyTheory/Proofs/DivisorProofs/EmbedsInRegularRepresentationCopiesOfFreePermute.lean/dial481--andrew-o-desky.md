---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EmbedsInRegularRepresentationCopiesOfFreePermute.lean",
  "declarations": [
    "GlobalTheory.BadCount.embReg_of_free_permuted_summands"
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

## Regular representations from freely permuted summands

[Theorem REP.1580](https://andrewodesky.com/rh/lean/GlobalTheory.BadCount.embReg_of_free_permuted_summands/)

Let $K$ be a field, $\Gamma$ a finite group, and $\rho$ a representation of $\Gamma$ on a finite-dimensional $K$-vector space $V$. Let $H\le\Gamma$ act freely on a finite set $X$, meaning that $hx=x$ implies $h=1$. Suppose $$V=\bigoplus_{x\in X}A_x,\qquad \rho(h)A_x\subseteq A_{hx}\quad(h\in H,x\in X).$$ There are $n\ge0$ and an injective $H$-equivariant $K$-linear map $$j:V\longrightarrow K[H]^n,\qquad n|H|=\dim_KV,$$ where $H$ acts by left multiplication on each group-algebra factor.
