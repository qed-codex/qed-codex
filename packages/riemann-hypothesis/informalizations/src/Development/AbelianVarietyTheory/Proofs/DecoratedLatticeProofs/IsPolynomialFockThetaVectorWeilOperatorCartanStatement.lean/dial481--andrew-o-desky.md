---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IsPolynomialFockThetaVectorWeilOperatorCartanStatement.lean",
  "declarations": [
    "GlobalTheory.T.isPolynomialFockThetaVector_weilOperator_cartan"
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

## Transport of polynomial Fock vectors

[Theorem THETA.1679](https://andrewodesky.com/rh/lean/GlobalTheory.T.isPolynomialFockThetaVector_weilOperator_cartan/)

Fix the full arithmetic datum in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)) with CM extension $E/F$, unitary spaces $S,T$, an adelic additive character $\psi$, splitting characters $\chi_S,\chi_T$, and a compatible Weil datum $\omega$ for $(S,T)$. Fix compatible archimedean coordinates $\theta$ and matrix families $s_S,s'_S,s_T$ at those coordinates. Let $g\in U(S)(\mathbb A_F)$ satisfy $$s'_S(\tau)g_\tau=g_\tau s_S(\tau)\qquad\text{at every prescribed archimedean embedding }\tau.$$ If $f$ is a theta function satisfying the covariance, finite-level and archimedean regularity conditions in ([The polynomial pairing of adelic Fock vectors](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockVectors_inner_eq_fockInnerProduct_mul_norm/)) and there is $N\ge0$ such that every length-$N$ word in the oscillator annihilation operators for $(s_S,s_T)$ kills $f$, then $\omega(g,1)f$ is a permitted theta function satisfying the same finite-word-annihilation condition for $(s'_S,s_T)$. Each word may use arbitrary matrix directions at arbitrary prescribed archimedean places.
