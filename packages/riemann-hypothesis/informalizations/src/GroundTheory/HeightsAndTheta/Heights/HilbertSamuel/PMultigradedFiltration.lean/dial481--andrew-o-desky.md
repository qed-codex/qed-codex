---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PMultigradedFiltration.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.MultigradedFiltration.proof"
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

## A prime filtration of a finite multigraded module

[Theorem ALG.0523](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.MultigradedFiltration.proof/)

Let $F$ be a field, $K$ a finite set, and $I_k$ finite sets. Give $$A=F[X_{k,i}:k\in K,\ i\in I_k]$$ the $\mathbb Z^K$-grading $\deg X_{k,i}=e_k$. Let $M=\bigoplus_{c\in\mathbb Z^K}M_c$ be a finitely generated graded $A$-module. There are an integer $t\ge0$, a filtration by $A$-submodules $$0=N_0\subseteq N_1\subseteq\cdots\subseteq N_t=M,$$ homogeneous elements $x_j\in M_{c_j}$, and multihomogeneous prime ideals $\mathfrak q_j\subset A$, for $0\le j<t$, such that $$N_{j+1}=N_j+Ax_j,\qquad ax_j\in N_j\ \Longleftrightarrow\ a\in\mathfrak q_j\quad(a\in A).$$ For every prime $\mathfrak p$ minimal over $\operatorname{Ann}_A(M)$, $$\#\{j:\mathfrak q_j=\mathfrak p\}=\operatorname{length}_{A_{\mathfrak p}}M_{\mathfrak p}.$$
