---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/GridDownArrowThetaFunctionFockDenseOfLevelStatement.lean",
  "declarations": [
    "GlobalTheory.T.gridDownArrow_thetaFunction_fock_dense_of_level"
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

## Fock approximations preserving a finite translation level

[Theorem THETA.0933](https://andrewodesky.com/rh/lean/GlobalTheory.T.gridDownArrow_thetaFunction_fock_dense_of_level/)

Fix the source's global arithmetic datum, a finite parameter group, parameter sets, character family and number-field realization. Let $(V_{ij})$ be a compatible grid, meaning a family of Hermitian spaces indexed by pairs of integers, with the prescribed Weil actions, theta arrows, levels, models and measures. Assume the realization's base conditions and all grid compatibility conditions described below. Fix a family parameter $t$ and $0\le i\le m$, $0\le j<m$, and put $V=V_{ij}$, $W=V_{i,j+1}$.

Let $U$ be an open additive subgroup of the oscillator space for $(V,W)$, and let $\Phi$ be a theta test function invariant under finite Heisenberg translations from $U$. Let $\mu$ and $\mathcal F$ give the rational oscillator lattice a measurable fundamental domain of volume one. For every $d\ge0$ and $\varepsilon>0$, there are finitely many theta test functions $f_l$ annihilated by every archimedean annihilation operator and polynomials $P_l$ in the Fock variables of ([Approximation of theta functions by polynomial Fock vectors](https://andrewodesky.com/rh/lean/GlobalTheory.FockApprox.theta_approx_fock/)) such that $$\Psi=\sum_lP_l(\text{creation operators})f_l$$ is invariant under the same finite translations and $$\sum_{|a|\le d}\|D_a(\Psi-\Phi)\|_{L^2(\mathcal F,\mu)}<\varepsilon.$$
