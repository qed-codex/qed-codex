---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/StrictNormalCrossingsDescentEtaleCompletionStatement.lean",
  "declarations": [
    "GlobalTheory.T.strictNormalCrossings_descent_etale_completion"
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

## Descent of a coordinate normal-crossings equation

[Theorem AG.1322](https://andrewodesky.com/rh/lean/GlobalTheory.T.strictNormalCrossings_descent_etale_completion/)

Let $A$ be a commutative Noetherian local ring, let $k$ be a field, and let $m,e\ge0$. Set $$B=k[[t_1,\ldots,t_m,u_1,\ldots,u_e]].$$ Let $\varphi:A\to B$ be flat, with $\mathfrak m_A B=\mathfrak m_B$, and assume the induced map $A\to k$ makes $k$ a finite $A$-module. Let $D\subset A$ be an ideal satisfying $$DB=(t_1\cdots t_m).$$ Suppose the ideals $\varphi^{-1}((t_i))$ are pairwise distinct. There are $n\ge0$, elements $r_1,\ldots,r_n\in A$, and a subset $T\subset\{1,\ldots,n\}$ such that $$\mathfrak m_A=(r_1,\ldots,r_n),\qquad \dim A=n,\qquad D=\left(\prod_{i\in T}r_i\right).$$ Empty products mean $1$.
