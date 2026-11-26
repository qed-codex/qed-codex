---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaFunctionOrthogonalSumApproxFiniteSumsStatement.lean",
  "declarations": [
    "GlobalTheory.T.theta_function_orthogonal_sum_approx_finite_sums"
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

## Uniform approximation of a theta function by sums of products

[Theorem THETA.0858](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_function_orthogonal_sum_approx_finite_sums/)

Fix the source's full arithmetic theta datum, with CM extension $E/F$, a chosen CM type $\Phi$, and an element $\xi_0\in E$. Let $\psi:\mathbb A_F\to\mathbb C^\times$ be a continuous nontrivial unitary additive character trivial on $F$, with infinite component $$\psi_\infty(x)=\exp\left(-2\pi i\sum_{\tau\in\Phi}x_\tau\right).$$ Let $S,A,B,T$ be Hermitian $E$-spaces in this datum, with chosen orthogonal isometric embeddings identifying $S=A\perp B$. Define $\mathcal W(S,T)$ and $\beta_{S,T}$ in the conventions. Under the decomposition, write $w=(w_A,w_B)$.

Let $f:\mathcal W(S,T)\to\mathbb C$ be a theta function in the sense of the conventions. For every $\varepsilon>0$ there are finitely many continuous functions $P_i:\mathcal W(A,T)\to\mathbb C$ and theta functions $g_i:\mathcal W(B,T)\to\mathbb C$ such that $$P_i(a+u)=\psi(-\beta_{A,T}(a,u))P_i(u)\qquad(a\in M_{\dim T\times\dim A}(E)),$$ and $$\left|f(w)-\sum_iP_i(w_A)g_i(w_B)\right|\le\varepsilon\qquad(w\in\mathcal W(S,T)).$$
