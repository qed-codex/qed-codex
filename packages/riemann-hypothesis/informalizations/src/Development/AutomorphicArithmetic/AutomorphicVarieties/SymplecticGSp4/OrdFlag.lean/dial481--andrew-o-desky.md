---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/OrdFlag.lean",
  "declarations": [
    "UpperTheory.V.GradeZeroInterpolatingElement.ordFlag"
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

## A triangular flag from spectral projector relations

[Theorem ALG.1323](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.ordFlag/)

Let $H$ be a group, $I\subset H$ a subgroup, $K$ a field, $\rho:H\to M_4(K)$ a multiplicative homomorphism, $s_0\in H$, and $\psi_0,\ldots,\psi_3:H\to K$ functions. Put $c_i=\psi_i(s_0)$ and $$P_i=\prod_{j\ne i}(\rho(s_0)-c_j1).$$ Assume the $c_i$ are pairwise distinct and $$\det(T1-\rho(s_0))=\prod_{i=0}^3(T-c_i),\qquad P_j\rho(g)P_i=0\quad(i<j,\ g\in H),$$ $$P_i(\rho(s)-\psi_i(s)1)P_i=0\quad(s\in I).$$ There are $u\in\mathrm{GL}_4(K)$ and characters $\kappa_i:H\to K^\times$ such that $u\rho(g)u^{-1}$ is upper triangular with diagonal entries $\kappa_i(g)$, and $$\kappa_i(s)=\psi_i(s)\quad(s\in I),$$ $$\left(\prod_{j\ne i}(c_i-c_j)\right)\kappa_i(g)=\operatorname{tr}(P_i\rho(g))\quad(g\in H).$$
