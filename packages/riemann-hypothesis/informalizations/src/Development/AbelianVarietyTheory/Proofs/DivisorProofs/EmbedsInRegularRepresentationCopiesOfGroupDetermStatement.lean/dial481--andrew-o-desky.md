---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EmbedsInRegularRepresentationCopiesOfGroupDetermStatement.lean",
  "declarations": [
    "GlobalTheory.T.embedsInRegularRepresentationCopies_of_groupDeterminant"
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

## Embedding into copies of a regular representation

[Theorem ALG.0345](https://andrewodesky.com/rh/lean/GlobalTheory.T.embedsInRegularRepresentationCopies_of_groupDeterminant/)

Let $K$ be a field, $\Gamma$ a finite group, $R$ a commutative $K$-algebra, and $a:\Gamma\to\operatorname{End}_{K\text{-alg}}(R)$ an action. Let $H\le\Gamma$ and $u\in R$. Assume the determinant of the matrix $$\bigl(a(hg)u\bigr)_{h,g\in H}$$ is a non-zero-divisor in $R$. Let $V,V_1,V_2\subseteq R$ be $K$-linear subspaces, with $V_2$ finite-dimensional, and let $\rho$ be a representation of $\Gamma$ on $V$ satisfying $\rho(g)v=a(g)v$ in $R$. Suppose, for every $h\in H$, $$V\,a(h)u\subseteq V_1,\qquad a(h)V_1\subseteq V_1,\qquad V_1\,a(h)u\subseteq V_2.$$ There is $n\ge0$ and an injective $H$-equivariant $K$-linear map $$V\hookrightarrow K[H]^n,\qquad n|H|\le\dim_KV_2,$$ where $H$ acts by left multiplication on each copy of its group algebra.
