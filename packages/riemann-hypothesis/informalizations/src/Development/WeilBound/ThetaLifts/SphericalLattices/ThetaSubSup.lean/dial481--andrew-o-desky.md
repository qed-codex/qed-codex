---
{
  "module": "src/Development/WeilBound/ThetaLifts/SphericalLattices/ThetaSubSup.lean",
  "declarations": [
    "PositivityTheory.Sph.maxAt_of"
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

## Uniqueness of a maximal proper submodule of a local theta quotient

[Theorem REP.1558](https://andrewodesky.com/rh/lean/PositivityTheory.Sph.maxAt_of/)

Fix number fields $E/F$, an $F$-automorphism $\sigma$ of $E$, spaces $X,W$ of ranks $n,d$, a global oscillator model and action $\omega$, an adelic additive character $\psi$, and a finite place $v$ of $F$. Assume a compatible local Weil and Heisenberg realization exists on the local Schwartz–Bruhat space $\mathcal S$. Let $A\subseteq\mathcal S$ be the span of $\omega_v(g,1)\phi-\phi$ for $g\in U(X)(F_v)$ and $\phi\in\mathcal S$.

Suppose either every $U(W)(F_v)$-stable subspace between $A$ and $\mathcal S$ equals $A$ or $\mathcal S$, or the following condition holds for every compatible local realization. There is $s\in\mathcal S$ whose $U(W)(F_v)$-translates span $\mathcal S/A$; for each $\phi\in\mathcal S$ there are finitely many $k_i\in U(W)(F_v)$, scalars $c_i,c\in\mathbb C$, with $$c_i\omega_v(1,k_i)s=s\quad\text{for every }i,\qquad \sum_i c_i\omega_v(1,k_i)\phi-cs\in A.$$ Then any two maximal proper $U(W)(F_v)$-stable subspaces of $\mathcal S$ containing $A$ are equal.
