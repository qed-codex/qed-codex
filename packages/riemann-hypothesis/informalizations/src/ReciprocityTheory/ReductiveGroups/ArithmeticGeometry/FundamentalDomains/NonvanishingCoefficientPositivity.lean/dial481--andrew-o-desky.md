---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/NonvanishingCoefficientPositivity.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FD.nonvanishing_coefficient_positivity"
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

## A nonzero rank-two Fourier coefficient has positive definite frequency

[Theorem AGR.0697](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.nonvanishing_coefficient_positivity/)

Let $E$ be a CM number field and fix the arithmetic flag datum described below, of rank $r$ and signature $(p,r-p)$ at its CM type $\Psi$. Let $u_1,u_2\in\Lambda$ be linearly independent and span a totally isotropic plane for its Hermitian form $h$. Let $\lambda=(\lambda_{\tau j})\in\mathbb Z^{\Psi\times r}$ and let $P$ be a bounded holomorphic automorphic section of weight $\lambda$, cuspidal in the convention below. Assume $\chi_\lambda(\gamma)=1$ for every $\gamma\in\Gamma$ congruent to the identity modulo $g\Lambda$ on $\Lambda$.

For a family $A=(A_\tau)_{\tau\in\Psi}$ of complex $2\times2$ matrices, define its Fourier coefficient by the convention below. If it is nonzero at some frame in the flag domain, then every $A_\tau$ is positive definite.
