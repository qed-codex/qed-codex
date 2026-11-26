---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/SmoothOfMemLowKSub.lean",
  "declarations": [
    "GlobalTheory.StepBoundOneRep.stepBound_of_eigen"
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

## Bounds for Lie derivatives on finite generated steps

[Theorem REP.1344](https://andrewodesky.com/rh/lean/GlobalTheory.StepBoundOneRep.stepBound_of_eigen/)

Let $n\ge0$, $\epsilon\in\{+1,-1\}^n$, $G=U(\operatorname{diag}\epsilon)$ and $\mathfrak g=\operatorname{Lie}(G)$. Let $H$ be a complex Hilbert space carrying a unitary representation $\sigma$ of $G$. Let $\lambda\in\mathbb R^n$, $b\in\mathbb R$, and let $H_\lambda\subseteq H$ be the sum of the finite-dimensional irreducible compact subrepresentations of highest weight $\lambda+\rho_n-\rho_c$, with the root conventions in ([Scalar invariant differential operators on lowest-type coefficients](https://andrewodesky.com/rh/lean/GlobalTheory.T.gelfandInvariants_scalar_on_lowestKType_coefficients/)), and assume this sum is itself an irreducible compact subrepresentation of that weight. Assume $|\lambda_i|\le b^2$ for every $i$. Suppose every coefficient $f(g)=\langle y,\sigma(g)s\rangle$, for $s\in H_\lambda$ and $y\in H$, is smooth and satisfies $D_mf=c_m(\lambda)f$ for every $m\ge0$, with the operators $D_m$ defined in ([Scalar invariant differential operators on lowest-type coefficients](https://andrewodesky.com/rh/lean/GlobalTheory.T.gelfandInvariants_scalar_on_lowestKType_coefficients/)) and eigenvalues defined in the conventions.

For $P\ge0$, let $H_P$ be the complex span of $$d\sigma(X_1)\cdots d\sigma(X_j)s\qquad(j\le P,\ X_i\in\mathfrak g,\ s\in H_\lambda),$$ where $d\sigma(X)v$ is the derivative at zero of $t\mapsto\sigma(\exp(tX))v$. Put $$C_P=\sqrt n\,b^2+\tfrac32 n^{3/2}+3P.$$ Then $H_P$ is finite dimensional, every vector of $H_P$ has those derivatives in all directions in $\mathfrak g$, and, for every real Hilbert–Schmidt orthonormal family $(F_i)_{i=1}^{n^2}$ in $\mathfrak g$, $$\sum_i\|d\sigma(F_i)w\|^2\le C_P^2\|w\|^2\qquad(w\in H_P).$$ For every $X\in\mathfrak g$ and $w\in H_P$, $$\|d\sigma(X)w\|\le\sqrt{\operatorname{tr}(XX^*)}\,C_P\|w\|.$$
