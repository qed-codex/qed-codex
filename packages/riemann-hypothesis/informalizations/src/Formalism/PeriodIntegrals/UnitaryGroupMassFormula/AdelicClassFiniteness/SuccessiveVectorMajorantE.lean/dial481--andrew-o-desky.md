---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/AdelicClassFiniteness/SuccessiveVectorMajorantE.lean",
  "declarations": [
    "PIW.AdelClassFin.successive_vector_majorant"
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

## A positive definite majorant with the same determinant norm

[Theorem ALG.0205](https://andrewodesky.com/rh/lean/PIW.AdelClassFin.successive_vector_majorant/)

Let $J\in M_n(\mathbb C)$ be Hermitian with $\det J\ne0$, where $n\ge0$. There is a positive definite Hermitian matrix $H\in M_n(\mathbb C)$ such that $$\det H=|\det J|,\qquad |z^*Jz|\le z^*Hz\quad(z\in\mathbb C^n).$$
