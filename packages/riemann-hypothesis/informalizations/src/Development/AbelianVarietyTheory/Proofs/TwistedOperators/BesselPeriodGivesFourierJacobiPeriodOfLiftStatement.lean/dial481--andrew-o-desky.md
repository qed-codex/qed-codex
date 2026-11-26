---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselPeriodGivesFourierJacobiPeriodOfLiftStatement.lean",
  "declarations": [
    "GlobalTheory.T.bessel_period_gives_fourierJacobi_period_of_lift"
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

## A nonzero Fourier-Jacobi period from a Bessel period

[Theorem THETA.1199](https://andrewodesky.com/rh/lean/GlobalTheory.T.bessel_period_gives_fourierJacobi_period_of_lift/)

Fix the source's arithmetic CM and Hermitian-space datum and an adelic additive character $\psi$. Let $J$ be a Fourier--Jacobi datum with $\sigma+1$ hyperbolic planes and remaining space $W_0$, and let $B$ be a Bessel datum with $\sigma$ hyperbolic planes and remaining decomposition $A\perp L$, with its specified nonisotropic vector $\zeta$ in $L$. Fix a compatible theta-lifting step, measures and fundamental domains, a test-function space $\mathcal S$, a vacuum subgroup $\Gamma_0$, and a compact open finite-adelic subgroup $K$ satisfying the local test-space conditions.

Let $\chi_A,\chi_L$ be circle-valued splitting characters whose product is the step's character, and fix the compatible Weil actions for $(W_0,A)$ and $(W_0,L)$. Let $\phi$ and $G$ be rapidly decreasing functions on the adelic groups of $W_0$ and the Bessel ambient space, respectively, and suppose $G$ is right $K$-invariant. Let $\Xi,\Phi_0$ be theta functions for these two pairs, with $\Phi_0\ne0$, and suppose the contracted product of $\Xi$ and $\Phi_0$ is a $\Gamma_0$-vacuum vector. If the Bessel period of the theta lift of $\phi$ using $\Xi$, against $G$, is nonzero, then for some $\Phi\in\mathcal S$ the Fourier--Jacobi period of $\phi$, the theta lift of $G$ using $\Phi$, and $\Phi_0$, at $\zeta$, is nonzero.
