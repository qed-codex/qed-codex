---
{
  "module": "src/Formalism/BranchSandwichDivisors/ChainDenominatorCoupled.lean",
  "declarations": [
    "Formalism.BranchingDeterminantCap.stepDiiiRecord"
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

## Terminal period height with a source-prime saving

[Theorem THETA.0182](https://andrewodesky.com/rh/s/q9-terminal-period-height.html)

Let $\Sigma$ be finite and $T\subset\Sigma$. Supply real arrays $a_\rho,b_\rho,n_\rho,\alpha_\rho,D_{0,\rho},D_{1,\rho},c_\rho,\xi_\rho$ and real parameters $h_P,\ell,e,a,\Lambda,L,m,f,k,N,S,\eta,b',C_T,C_e,C$. Assume $$h_P\le-\sum_\rho n_\rho\ell+\sum_\rho(2c_\rho+\xi_\rho)+e,$$ $$c_\rho\le(N-1)D_{1,\rho}\log(2a),\qquad\xi_\rho\le\frac{N(N-1)}2\log(2a),\qquad n_\rho=\alpha_\rho-D_{0,\rho},$$ $$\alpha_\rho=a_\rho-(N-k)/2\quad(\rho\in T),\qquad\alpha_\rho\ge S-(N-1)/2\quad(\rho\notin T),$$ $$D_{0,\rho}\le S+m\eta+\mathbf1_{\rho\in T}b_\rho,\qquad D_{1,\rho}\le3D_{0,\rho}+S+\eta,\qquad b_\rho\le2b'\quad(\rho\in T).$$ The remaining assumptions are $$0\le\ell\le C_TmL,\quad C_T\ge0,\quad L\le\Lambda,\quad\Lambda\ge0,\quad0\le\log(2a)\le2\Lambda,$$ $$1\le m\le N,\quad k,S,\eta,b'\ge0,\quad |\Sigma|\le f,\quad e\le C_efN^2\Lambda,\quad C_e\ge0,\quad2(16+C_T+C_e)\le C.$$ Then $$h_P\le-\sum_{t\in T}a_t\ell+C\{|T|b'N+f(m\eta+S)N+fN^2\}\Lambda.$$ The parameters $c_\rho$ and $\xi_\rho$ are logarithmic quantities; no positivity of their exponentials is an additional hypothesis. In the application $\ell=\log T_u$ for the auxiliary source prime $T_u$.
