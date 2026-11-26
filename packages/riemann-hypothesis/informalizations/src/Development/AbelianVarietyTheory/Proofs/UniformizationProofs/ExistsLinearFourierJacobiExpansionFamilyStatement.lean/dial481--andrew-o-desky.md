---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsLinearFourierJacobiExpansionFamilyStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_linear_fourierJacobi_expansion_family"
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

## A linear injective family of Fourier–Jacobi coefficient maps

[Theorem AV.0923](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_linear_fourierJacobi_expansion_family/)

Assume the two abelian-scheme law packages listed below. Let $R$ be a complete discrete valuation domain of characteristic zero. Fix its polarized degeneration and compatible uniformization data: a polarized abelian variety $(A,L)$ over $K=\operatorname{Frac}R$, a semiabelian model $G/R$, an abelian quotient $(B,M)$, a character lattice $X$, period points $c_\alpha\in B(R)$, rigidified cubical symmetric line bundles, and the prescribed compatible identifications on every infinitesimal thickening.

For every field extension $F/K$ and every $k\ge1$, there are $F$-linear maps $$e_\alpha:H^0(A_F,L_F^{\otimes k})\longrightarrow H^0(B_F,M_{k,\alpha})\qquad(\alpha\in X)$$ such that $(e_\alpha(s))_\alpha$ is the uniformization's Fourier–Jacobi expansion of $s$, every expansion of $s$ has these coefficients, and $$\bigl(\forall\alpha,\ e_\alpha(s)=0\bigr)\Longrightarrow s=0.$$ An index $\alpha$ occurs with a nonzero coefficient in some expansion if and only if $e_\alpha\ne0$.
