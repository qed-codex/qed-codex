---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/CpSeriesCoeffNormBoundedRingLaws.lean",
  "declarations": [
    "GlobalTheory.MomOne.sup_norm_laws"
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

## Norm bounds for bounded p-adic power series

[Theorem PHT.0630](https://andrewodesky.com/rh/lean/GlobalTheory.MomOne.sup_norm_laws/)

Let $p$ be prime and write $C_p$ for the completed algebraic closure of $\mathbb Q_p$. For $f=\sum_{n\ge0}f_nX^n\in C_p[[X]]$, write $\|f\|\le A$ to mean $|f_n|\le A$ for every $n$, and call $f$ bounded if this holds for some real $A$. The following assertions hold for $f,g,h,v\in C_p[[X]]$, real bounds $A,B$, and nonnegative integer indices and exponents $i,j,k$.

1. If $\|f\|\le A$ and $\|g\|\le B$, then $\|f+g\|\le\max(A,B)$ and $\|fg\|\le AB$.
2. If $\|f\|\le A$, $\|h\|\le1$, and $h_0=0$, then $\|f\circ h\|\le A$.
3. If $\|f\|\le1$, $|f_0|=1$, and $fg=1$, then $\|g\|\le1$.
4. If $f,g$ are bounded and $\|fg\|\le B$, then $|f_i||g_j|\le B$ for all $i,j\ge0$.
5. If $f,g$ are bounded, $fg=1$, and $f_0=1$, then $\|f\|\le1$ and $\|g\|\le1$.
6. If $\|v\|\le1$, $|v_0|=1$, and $\|X^k v f\|\le B$ for $k\ge0$, then $\|f\|\le B$.
