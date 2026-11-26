---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StandardSlopeBound/GramMatrixDuality.lean",
  "declarations": [
    "PI.SlopeSteps.gram_matrix_duality"
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

## Reciprocal Gram determinants for two integral Weyl lattices

[Theorem REP.1332](https://andrewodesky.com/rh/lean/PI.SlopeSteps.gram_matrix_duality/)

Let $N\ge0$ be an integer and let $\nu=(\nu_1,\ldots,\nu_N)$ be a weakly decreasing list of nonnegative integers. Use ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in square $N\times N$ variables $z_{ab}$, and put $$W_\nu=\Delta_\nu(\mathbb Z),\qquad D_\nu=\nabla_\nu(\mathbb Z),\qquad H_\nu=v_\nu\in\mathbb Q[z_{ab}].$$ Regard the integer polynomial modules as submodules of $\mathbb Q[z_{ab}]$ by coefficient inclusion.

For polynomials over $\mathbb Q$, use $\langle f,g\rangle_F=[f,g]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)). Given integer bases $e_1,\ldots,e_r$ of $W_\nu$ and $e'_1,\ldots,e'_{r'}$ of $D_\nu$, set $$G_{ij}=\frac{\langle e_i,e_j\rangle_F}{\langle H_\nu,H_\nu\rangle_F},\qquad G'_{ij}=\frac{\langle e'_i,e'_j\rangle_F}{\langle H_\nu,H_\nu\rangle_F}.$$ Then $r=r'$ and $\det G\det G'=1$.
