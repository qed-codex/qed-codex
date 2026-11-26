---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/FourierJacobiPeriodGivesBesselPeriodOfLiftStatement.lean",
  "declarations": [
    "GlobalTheory.T.fourierJacobi_period_gives_bessel_period_of_lift"
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

## A nonzero Fourier–Jacobi period gives a nonzero Bessel period

[Theorem THETA.1313](https://andrewodesky.com/rh/lean/GlobalTheory.T.fourierJacobi_period_gives_bessel_period_of_lift/)

Fix the source's ambient arithmetic datum for unitary theta periods, over a CM extension $E/F$, and an additive character $\psi$ of $\mathbb A_F$. Fix its complete Bessel–Fourier–Jacobi transition datum of index $\rho\ge0$: Hermitian spaces with decompositions into a hyperbolic plane $\mathbb H$ and the indicated complements $$V=\mathbb H^\rho\oplus V_0,\qquad V_0=A\oplus L,\qquad W=\mathbb H^\rho\oplus W_0,$$ a Hermitian line $L$ with nonisotropic vector $\zeta$, compatible Weil actions $\omega$ for $(V,W)$ and $\omega_0$ for $(V_0,W_0)$ with unitary characters $(\chi_V,\chi_W)$ of $\mathbb A_E^\times$, and the chosen measures and fundamental domains defining the theta lifts and periods. Let $\mathcal S$ be a set of theta test functions, $\Gamma_0$ an additive subgroup of the smaller Schrödinger space, and $K$ a compact open subgroup of the finite adelic group of $W$. Assume the source's full local test-function conditions for this transition.

Let $L'$ be another Hermitian line with nonisotropic vector $\zeta'$, and choose a matrix $\tau:L'\to L$ with $$\tau\zeta'=-\zeta,\qquad (\zeta,\zeta)_L=\xi\bar\xi\,(\zeta',\zeta')_{L'},$$ where $\xi$ is the fixed scalar in the ambient datum. Let $\chi_A,\chi_z,\chi'$ be unitary characters of $\mathbb A_E^\times$ with $\chi_V=\chi_A\chi_z$. Choose Weil actions $\omega_A$ for $(A,W_0)$ with characters $(\chi_A,\chi_W)$ and $\omega_z$ for $(W_0,L')$ with characters $(\chi',\chi_z)$, satisfying the prescribed Weil-datum conditions.

Let $\phi$ on $U(A)(\mathbb A_F)$ and $G$ on $U(W)(\mathbb A_F)$ be rapidly decreasing, with $G$ right $K$-invariant. Let $\Xi_1,\Xi_2$ be theta functions for $(A,W_0)$ and $(L,W_0)$, respectively, whose tensor-product function $w\mapsto\Xi_1(w_A)\Xi_2(w_L)$, using the projections from $V_0=A\oplus L$, satisfies the prescribed vacuum condition for $\Gamma_0$. Let $\kappa_\tau$ be the map between Schrödinger spaces obtained by composition with $\tau$ followed by the adjoint identification. If the prescribed Fourier–Jacobi period satisfies $$\mathcal J_{\psi,\zeta',\omega_z}\bigl(\Theta_{\omega_A}(\phi,\Xi_1),G;\overline{\Xi_2\circ\kappa_\tau}\bigr)\ne0,$$ then for some $\Phi\in\mathcal S$ the prescribed Bessel period satisfies $$\mathcal B_{\psi,\zeta}\bigl(\phi,\Theta_\omega(G,\Phi)\bigr)\ne0.$$
