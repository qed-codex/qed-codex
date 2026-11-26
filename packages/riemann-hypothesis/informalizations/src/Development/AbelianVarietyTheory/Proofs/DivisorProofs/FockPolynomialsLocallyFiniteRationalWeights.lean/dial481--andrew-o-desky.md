---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockPolynomialsLocallyFiniteRationalWeights.lean",
  "declarations": [
    "GlobalTheory.FockPolGK.pol_locFin_weights"
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

## Local finiteness and rational weights of Fock polynomials

[Theorem THETA.1498](https://andrewodesky.com/rh/lean/GlobalTheory.FockPolGK.pol_locFin_weights/)

For $p,q,r,s\ge0$, put $I=\{1,\ldots,p\}\sqcup\{1,\ldots,q\}$, $J=\{1,\ldots,r\}\sqcup\{1,\ldots,s\}$, and $\mathcal P=\mathbb C[x_{ac}:a\in I,c\in J]$. Equip $\mathcal P$ with the two polynomial oscillator Lie actions $\omega_1$ of $\mathfrak{gl}_{p+q}(\mathbb C)$ and $\omega_2$ of $\mathfrak{gl}_{r+s}(\mathbb C)$ defined in ([A harmonic polynomial lies in a finite subspace stable under both compact Lie algebras](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockHarmonic_mem_finiteDimensional_compactStable/)).

For each action $\omega_i$, every polynomial belongs to a finite-dimensional subspace stable under the block-diagonal Lie algebra: $\mathfrak{gl}_p\oplus\mathfrak{gl}_q$ for $i=1$, and $\mathfrak{gl}_r\oplus\mathfrak{gl}_s$ for $i=2$. Every polynomial also belongs to the sum of the rational weight spaces $$\mathcal P_{\mu}^{(i)}=\{v:\omega_i(E_{aa})v=\mu_a v\text{ for all }a\},\qquad \mu_a\in\mathbb Q.$$ Here $E_{aa}$ are the diagonal matrix units for the relevant Lie algebra.
