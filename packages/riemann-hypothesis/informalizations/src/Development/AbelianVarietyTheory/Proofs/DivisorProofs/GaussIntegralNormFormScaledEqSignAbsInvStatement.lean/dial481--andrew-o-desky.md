---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaussIntegralNormFormScaledEqSignAbsInvStatement.lean",
  "declarations": [
    "GlobalTheory.T.gaussIntegral_normForm_scaled_eq_sign_abs_inv"
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

## Scaling of a local norm-form Gauss integral

[Theorem THETA.0613](https://andrewodesky.com/rh/lean/GlobalTheory.T.gaussIntegral_normForm_scaled_eq_sign_abs_inv/)

Let $F$ be a nonarchimedean local field of characteristic zero and $E/F$ a quadratic field extension with its $F$-module topology. Fix an $F$-linear conjugation $c$ and $\delta\in E^\times$ with $c(\delta)=-\delta$ and basis $(1,\delta)$ of $E/F$. Let $\psi:F\to\mathbb C$ be a continuous nontrivial additive character with $|\psi(x)|=1$, and let $\mu$ be an additive Haar measure on the Borel sets of $E$.

There is $g\in\mathbb C$ such that, for every $t\in F^\times$ and every compact set $K\subseteq E$, there is a compact open additive subgroup $L\subseteq E$ containing $K$ for which $$\int_L\psi\bigl(tN_{E/F}(z)\bigr)\,d\mu(z)=g\,\eta_{E/F}(t)|t|_F^{-1}.$$
