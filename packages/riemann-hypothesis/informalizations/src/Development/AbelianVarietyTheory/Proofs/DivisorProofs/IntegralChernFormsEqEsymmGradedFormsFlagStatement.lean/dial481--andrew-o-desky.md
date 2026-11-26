---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IntegralChernFormsEqEsymmGradedFormsFlagStatement.lean",
  "declarations": [
    "GlobalTheory.T.integral_chernForms_eq_esymm_gradedForms_flag"
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

## Replacing Chern forms by elementary symmetric graded forms in integrals

[Theorem AG.1529](https://andrewodesky.com/rh/lean/GlobalTheory.T.integral_chernForms_eq_esymm_gradedForms_flag/)

Let $F$ be a field with an embedding $\sigma:F\hookrightarrow\mathbb C$, and let $X/F$ be a smooth geometrically integral projective variety. Let $I$ be finite. For each $i\in I$, fix a rank-$m_i$ vector bundle $E_i$ on $X$ with a full flag and a smooth positive Hermitian metric compatible with its frame data. Write $c_{i,j}$ for its degree-$j$ Chern form and $x_{i,a}$, $1\le a\le m_i$, for the first Chern forms of its graded line bundles with induced metrics. Let $R\in\mathbb R[T_{i,j}:i\in I,j\ge0]$ and $Q\in\mathbb R[X_{i,a}:i\in I,1\le a\le m_i]$. Define $R^{\mathrm{root}}$ by substituting the elementary symmetric polynomial $e_j(X_{i,1},\ldots,X_{i,m_i})$ for $T_{i,j}$. Then, using wedge products and taking the top-degree part in the integral, $$\int_{X_\sigma(\mathbb C)}R(c_{i,j})\wedge Q(x_{i,a}) =\int_{X_\sigma(\mathbb C)}R^{\mathrm{root}}(x_{i,a})\wedge Q(x_{i,a}).$$
