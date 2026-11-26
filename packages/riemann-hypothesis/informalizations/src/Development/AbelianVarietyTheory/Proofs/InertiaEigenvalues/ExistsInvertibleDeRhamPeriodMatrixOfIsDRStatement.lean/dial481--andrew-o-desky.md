---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsInvertibleDeRhamPeriodMatrixOfIsDRStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_invertible_deRhamPeriodMatrix_of_isDR"
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

## An invertible de Rham period matrix

[Theorem PHT.1612](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_invertible_deRhamPeriodMatrix_of_isDR/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ a finite extension, and $V$ a $\mathbb Q_\ell$-vector space with a basis $b$ indexed by a finite set $I$. Fix the local period-ring, integral and comparison data in ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Write $B_{\mathrm{dR}}$ for their de Rham ring and $g_B$ for the action of $g\in G_K$ on it. If $\rho:G_K\to\operatorname{GL}(V)$ is de Rham for these data, there is $Q\in\operatorname{GL}_I(B_{\mathrm{dR}})$ such that $$[\rho(g)]_b\,g_B(Q)=Q\qquad(g\in G_K),$$ where the entries of $[\rho(g)]_b$ are embedded from $\mathbb Q_\ell$ in $B_{\mathrm{dR}}$.
