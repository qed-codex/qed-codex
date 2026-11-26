---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/RestrictedTensorProductIrreducibleCountableDimen.lean",
  "declarations": [
    "GlobalTheory.rtens_irreducible"
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

## Irreducibility of a restricted tensor product

[Theorem REP.0531](https://andrewodesky.com/rh/lean/GlobalTheory.rtens_irreducible/)

Let $I$ be an index set, $N_i\ne0$ complex vector spaces of dimension at most countable, and $s_i\in N_i$ with $\{i:s_i=0\}$ finite. For each $i$, let $S_i\subseteq\operatorname{End}_{\mathbb C}(N_i)$ have no common invariant subspaces other than $0,N_i$. Let $$T=\bigotimes_{i\in I}'(N_i,s_i)$$ be the algebraic restricted tensor product. Suppose linear operators $A_{i,a}\in\operatorname{End}_{\mathbb C}(T)$ are given for every $a\in\operatorname{End}_{\mathbb C}(N_i)$ and, for $a\in S_i$, satisfy $$A_{i,a}\left(\bigotimes_jx_j\right)=\bigotimes_jy_j,\qquad y_i=ax_i,\quad y_j=x_j\ (j\ne i),$$ whenever $x_j=s_j$ outside a finite set. Then the only subspaces invariant under every $A_{i,a}$ with $a\in S_i$ are $0,T$.
