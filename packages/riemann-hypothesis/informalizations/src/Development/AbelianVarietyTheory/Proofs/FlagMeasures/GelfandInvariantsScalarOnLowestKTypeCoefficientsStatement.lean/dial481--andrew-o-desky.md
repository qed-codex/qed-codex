---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/GelfandInvariantsScalarOnLowestKTypeCoefficientsStatement.lean",
  "declarations": [
    "GlobalTheory.T.gelfandInvariants_scalar_on_lowestKType_coefficients"
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

## Scalar invariant differential operators on lowest-type coefficients

[Theorem REP.0654](https://andrewodesky.com/rh/lean/GlobalTheory.T.gelfandInvariants_scalar_on_lowestKType_coefficients/)

Let $n\ge0$, choose signs $\varepsilon_i\in\{\pm1\}$ and $\lambda\in\mathbb R^n$, and put $G=U(\operatorname{diag}\varepsilon)$ and $K=G\cap U(n)$. Let $\pi$ be a strongly continuous unitary representation of $G$ on a complex Hilbert space $H$. Let $\rho_c,\rho_n$ be the half-sums of the positive roots $e_i-e_j$ with $i<j$ and respectively equal and unequal signs, and put $\kappa=\lambda+\rho_n-\rho_c$.

Let $S$ be the sum of all irreducible finite-dimensional $K$-submodules of highest weight $\kappa$. Assume $S$ itself is such an irreducible $K$-submodule. There are scalars $c_m\in\mathbb C$ for $m\ge0$ such that, for every $s\in S$ and $u\in H$, the matrix coefficient $f_{u,s}(g)=\langle u,\pi(g)s\rangle$ is smooth on $G$ and $$D_m f_{u,s}(g)=c_m f_{u,s}(g)\qquad(g\in G,\ m\ge0).$$
