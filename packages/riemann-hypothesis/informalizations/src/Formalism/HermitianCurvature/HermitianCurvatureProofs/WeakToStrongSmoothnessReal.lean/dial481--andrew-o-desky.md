---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/WeakToStrongSmoothnessReal.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.weak_to_strong_smoothness"
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

## Differentiability detected by a norming family

[Theorem ALG.0994](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.weak_to_strong_smoothness/)

Let $X$ be a finite-dimensional real normed space, $V$ a complex Banach space, and $E$ a complex normed space. Let $(\lambda_i:V\to E)_{i\in I}$ be bounded complex-linear maps satisfying $$\bigl(\|\lambda_i(v)\|\le c\text{ for every }i\bigr)\Longrightarrow\|v\|\le c\qquad(v\in V,\ c\in\mathbb R).$$ Let $\Omega\subseteq X$ be open, $\Phi:X\to V$, $m\ge0$, and $b:X\to\mathbb R$ continuous on $\Omega$. Suppose each $\lambda_i\circ\Phi$ is $C^{m+1}$ on $\Omega$ and $$\|D^q(\lambda_i\circ\Phi)(x)\|\le b(x)\qquad(i\in I,\ 0\le q\le m+1,\ x\in\Omega).$$ Then $\Phi$ is $C^m$ on $\Omega$ and $$\|D^q\Phi(x)\|\le b(x)\qquad(0\le q\le m,\ x\in\Omega).$$
