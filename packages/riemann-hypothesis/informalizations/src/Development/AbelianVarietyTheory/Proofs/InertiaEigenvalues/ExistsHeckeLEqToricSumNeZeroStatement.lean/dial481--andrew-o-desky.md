---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHeckeLEqToricSumNeZeroStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_heckeL_eq_toricSum_ne_zero"
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

## A nonzero Hecke value represented by a toric lattice sum

[Theorem ANT.0816](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_heckeL_eq_toricSum_ne_zero/)

Fix the source's full CM arithmetic field datum with CM field $E$, maximal real subfield $F$ and distinguished element $\sqrt{-d}\in E$. Let $(\phi_i)_{i\in I}$ be a CM type with $\phi_i(\sqrt{-d})$ independent of $i$, let $s\ge1$ and $\kappa_i\ge1$, and let $\mathfrak f$ be a nonzero proper ideal of $\mathcal O_F$ satisfying the conductor conditions below. Let $\chi$ be a unitary Hecke character whose product of local restrictions above each place of $F$ is trivial on $F^\times$, with infinity exponents $\kappa_i+s$ in the ratio convention below and exact conductor exponent $v(\mathfrak f)$ at every prime of $E$ above $v$.

There exists an entire function $L(z,\chi)$ agreeing with the Hecke Euler product on $\operatorname{Re}z>1$, such that $L(s,\chi)\ne0$ and a complex number is the toric lattice sum below if and only if it equals $L(s,\chi)$.
