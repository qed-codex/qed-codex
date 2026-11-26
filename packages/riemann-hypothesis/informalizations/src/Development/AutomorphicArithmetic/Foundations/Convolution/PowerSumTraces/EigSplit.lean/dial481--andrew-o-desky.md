---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/PowerSumTraces/EigSplit.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.C.eigSplit"
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

## A finite spectral approximation to a compressed trace

[Theorem REP.0410](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.C.eigSplit/)

Let $H$ be a complex Hilbert space, $W\subseteq H$ a closed subspace, and $A:H\to H$ a bounded positive operator preserving $W$. Write $P_W$ for orthogonal projection and assume $AP_W$ is compact. For every $\eta>0$ the set $$S=\{x\in\mathbb R:x>\eta,\ E_x\ne0\},\qquad E_x=W\cap\ker(A-x),$$ is finite, and each $E_x$ for $x\in S$ is finite dimensional. For every continuous $\phi:\mathbb R\to\mathbb R$, $c\ge0$, and bounded operator $T$ satisfying $|\phi(x)|\le c$ on $[0,\eta]$ and $P_WTP_W$ trace class, $$\left|\operatorname{tr}_W\bigl(\phi(A)P_WT\bigr)-\sum_{x\in S}\phi(x)\operatorname{tr}_{E_x}(T)\right|\le c\,\|P_WTP_W\|_1.$$
