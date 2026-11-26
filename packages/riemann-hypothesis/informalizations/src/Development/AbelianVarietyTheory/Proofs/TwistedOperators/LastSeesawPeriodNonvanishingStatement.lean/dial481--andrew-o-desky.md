---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LastSeesawPeriodNonvanishingStatement.lean",
  "declarations": [
    "GlobalTheory.T.lastSeesaw_periodNonvanishing"
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

## Nonvanishing at the final seesaw step

[Theorem THETA.1181](https://andrewodesky.com/rh/lean/GlobalTheory.T.lastSeesaw_periodNonvanishing/)

Fix the source's global theta datum $D$ and its rank-zero Jacobi datum $\mathcal J$, comprising spaces $W,W_0$ with the prescribed zero-hyperbolic-rank decomposition and quotient measures. Let $X=T\perp L$ be an orthogonal decomposition of Hermitian spaces with $\dim L=1$, and let $-L$ have the negative form. Let $\psi$ be an adelic additive character. For spaces $S,U$ and an additive subgroup $\Lambda$ of their adelic tensor space, write $\mathcal V_\psi(S,U;\Lambda)$ for theta functions, with Heisenberg action as in ([Detection of a functional by translates of one vacuum vector](https://andrewodesky.com/rh/lean/GlobalTheory.T.tame_functional_vacuum_irreducibility/)), fixed by the following lattice translations: translations by $2\Lambda$ and the specified halves selected by integral conjugate idempotents.

Take lattices $\Gamma,\Gamma_L,\Gamma_X$ in the tensor spaces for $(W,T),(W_0,-L),(W_0,X)$ satisfying the final-lattice compatibility package. Fix any $\zeta\in E^{\dim(-L)}$, splitting characters $\chi_S,\chi_T,\chi_z$, and Weil actions for $(W,T),(W_0,X),(W_0,-L)$ with character pairs $$(\chi_S,\chi_T),\quad(\chi_S,\chi_T\chi_z^{-1}),\quad(\chi_S^{-1},\chi_z),$$ respectively, satisfying the source's Weil-datum conditions. Choose a Haar measure and rational fundamental domain $\mathcal F_T$ on $U(T)$. Let $\varphi$ on $U(W_0)$ and $u$ on $U(T)$ be rapidly decreasing in the source's height sense, and let $\Xi\in\mathcal V_\psi(W_0,X;\Gamma_X)$. Write $\Theta_{S\to U}(v;f)$ for the theta lift obtained by integrating $(\omega(g,h)f)(0)v(g)$ over the fixed rational quotient of $U(S)$. If $$\int_{\mathcal F_T}\Theta_{W_0\to X}(\varphi;\Xi)(h,1)u(h)\,dh\ne0,$$ then there exist $\Phi\in\mathcal V_\psi(W,T;\Gamma)$ and $\Phi_0\in\mathcal V_\psi(W_0,-L;\Gamma_L)$ such that the rank-zero Fourier–Jacobi period attached to $\mathcal J,\psi,\zeta$ satisfies $$\mathcal P_{\mathcal J,\psi,\zeta}\bigl(\varphi,\Theta_{T\to W}(u;\Phi),\Phi_0\bigr)\ne0.$$
