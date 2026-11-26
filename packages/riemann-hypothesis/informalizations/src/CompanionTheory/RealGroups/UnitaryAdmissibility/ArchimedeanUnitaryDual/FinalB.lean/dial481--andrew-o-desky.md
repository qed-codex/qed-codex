---
{
  "module": "src/CompanionTheory/RealGroups/UnitaryAdmissibility/ArchimedeanUnitaryDual/FinalB.lean",
  "declarations": [
    "CompanionTheory.Rg.Fl.B.flathTensorProduct"
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

## Restricted tensor factorization on a unitary group

[Theorem REP.0078](https://andrewodesky.com/rh/lean/CompanionTheory.Rg.Fl.B.flathTensorProduct/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J$ be a nonsingular $n\times n$ Hermitian matrix over $E$, with $n\ge0$. Put $G=U(J)$ and let $\pi$ be a strongly continuous, topologically irreducible unitary representation of $G(\mathbb A_F)$ on a complex Hilbert space $H$. There are irreducible unitary representations $(\pi_v,H_v)$ of $G(F_v)$, vectors $\xi_v\in H_v$, and a map $B:\prod_vH_v\to H$ with the following properties. The vectors $\xi_v$ have norm one at all but finitely many places, and for each $g\in G(\mathbb A_F)$, $\pi_v(g_v)\xi_v=\xi_v$ at all but finitely many places. If $y_v=\xi_v$ and $y'_v=\xi_v$ outside finite sets, then $$\langle B(y'),B(y)\rangle=\prod_v\langle y'_v,y_v\rangle,\qquad \pi(g)B(y)=B((\pi_v(g_v)y_v)_v).$$ The linear span of these $B(y)$ is dense in $H$.
