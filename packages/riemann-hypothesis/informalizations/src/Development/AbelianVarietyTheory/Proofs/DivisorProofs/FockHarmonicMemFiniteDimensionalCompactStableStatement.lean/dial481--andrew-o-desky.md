---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockHarmonicMemFiniteDimensionalCompactStableStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockHarmonic_mem_finiteDimensional_compactStable"
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

## A harmonic polynomial lies in a finite subspace stable under both compact Lie algebras

[Theorem THETA.0379](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockHarmonic_mem_finiteDimensional_compactStable/)

Let $p,q,r,s\ge0$, put $I=\{1,\ldots,p\}\sqcup\{1,\ldots,q\}$ and $J=\{1,\ldots,r\}\sqcup\{1,\ldots,s\}$, and consider $\mathcal P=\mathbb C[x_{ab}:a\in I,b\in J]$ with the two oscillator actions $A_1,A_2$ defined below. Let $h\in\mathcal P$ satisfy $$\bigl(A_1(Z)\bigr)_{-2}h=0$$ for every matrix $Z$ on $I$ whose two diagonal blocks vanish. Then there is a finite-dimensional subspace $H_0\subseteq\mathcal P$ containing $h$, consisting entirely of polynomials satisfying the same condition, invariant under $A_1(Z)$ for all block diagonal matrices $Z$ on $I$ and under $A_2(Y)$ for all block diagonal matrices $Y$ on $J$.
