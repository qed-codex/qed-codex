---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/PowerSumTraces/EigSummands.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.C.eigSummands"
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

## A finite decomposition of an eigenspace

[Theorem REP.0431](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.C.eigSummands/)

Let $H$ be a complex Hilbert space, $(V_i)_{i\in I}$ pairwise orthogonal closed complex subspaces, and $W=\overline{\sum_{i\in I}V_i}$. Let $A:H\to H$ be bounded and self-adjoint, with $A(V_i)\subseteq V_i$ for every $i$. For $x\in\mathbb R$, put $E_x(U)=U\cap\ker(A-x)$. If $E_x(W)$ is finite-dimensional, there is a finite set $S\subseteq I$ such that $$i\in S\iff E_x(V_i)\ne0,\qquad E_x(W)=\bigoplus_{i\in S}E_x(V_i).$$ For every bounded complex-linear operator $T$ on $H$, $$\operatorname{tr}(P_{E_x(W)}TP_{E_x(W)})=\sum_{i\in S}\operatorname{tr}(P_{E_x(V_i)}TP_{E_x(V_i)}),$$ where $P_U$ is orthogonal projection onto $U$.
