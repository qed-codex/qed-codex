---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalMassFormulaStatement.lean",
  "declarations": [
    "GlobalTheory.T.local_mass_formula"
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

## Local density estimates for an anisotropic binary Hermitian form

[Theorem ANT.0998](https://andrewodesky.com/rh/lean/GlobalTheory.T.local_mass_formula/)

Let $E/F$ be a CM extension of number fields, let $J\in M_2(E)$ be a nonsingular anisotropic Hermitian form, and choose an $F$-basis $b_1,\ldots,b_d$ of $E$. Assume a full system of the measures specified below is given. For finite $v$, put $q_v=|\mathcal O_F/\mathfrak p_v|$, $E_v=F_v\otimes_FE$ and $\Lambda_v=\sum_j\mathcal O_{F_v}b_j$.

There is $C\in\mathbb R$ such that outside a finite set of places, writing $d_v(s)=m_{v,s}(\Lambda_v^2)_{\mathbb R}$, $$m_{v,s}(\Lambda_v^2)=0\quad(s\notin\mathcal O_{F_v},\ s\ne0),$$ $$|d_v(s)-1|\le C/q_v\quad(0\ne s\in\mathcal O_{F_v}),\qquad |d_v(s)-1|\le C/q_v^2\quad(|s|_v=1).$$
