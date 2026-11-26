---
{
  "module": "src/Formalism/PadicSubsetSums/StableGradedCounts/CardLtAddCardGtAddCardEq.lean",
  "declarations": [
    "Formalism.IrreducibleCountingLemmas.Z.good_cuspidal_multiplicity_one"
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

## A squarefree polynomial family with no common small factor degree

[Theorem ALG.0581](https://andrewodesky.com/rh/lean/Formalism.IrreducibleCountingLemmas.Z.good_cuspidal_multiplicity_one/)

Let $k$ be a field, let $P$ be a nonempty set, and let $r\ge1$. Let $f_v\in k[T]$ for $v\in P$, let $I$ be a finite set, let $n_i,d_i\ge1$, and let $h_{v,i}\in k[T]$. Suppose $$\deg f_v=r,\qquad f_v\text{ is squarefree},\qquad f_v=\prod_{i\in I}h_{v,i}^{d_i},\qquad\deg h_{v,i}=n_i$$ for every $v$ and $i$. Assume there is no integer $a\ge1$ with $2a\le r$ such that, for every $v\in P$, some divisor of $f_v$ in $k[T]$ has degree $a$. Then $|I|=1$, and $d_i=1$ and $n_i=r$ for every $i\in I$.
