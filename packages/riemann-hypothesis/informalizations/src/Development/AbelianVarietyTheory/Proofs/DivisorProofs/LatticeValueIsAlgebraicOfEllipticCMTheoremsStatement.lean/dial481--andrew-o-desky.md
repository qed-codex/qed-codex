---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeValueIsAlgebraicOfEllipticCMTheoremsStatement.lean",
  "declarations": [
    "GlobalTheory.T.latticeValueIsAlgebraic_of_ellipticCM_theorems"
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

## Algebraicity of normalized CM lattice sums

[Theorem ANT.1672](https://andrewodesky.com/rh/lean/GlobalTheory.T.latticeValueIsAlgebraic_of_ellipticCM_theorems/)

Assume the source's four literature packages for rational ray-zeta values and their congruences, functional equations of paired partial zeta functions, generation and conjugates of the Hilbert class field by elliptic $j$-invariants, and Artin reciprocity on CM elliptic torsion. Let $K$ be a quadratic number field, $d\ge1$, $\delta\in K$ satisfy $\delta^2=-d$, and $\iota:K\to\mathbb C$ be an embedding. Let $\Lambda_0$ be an elliptic period datum with lattice $\iota(\mathcal O_K)$, and choose $\Omega_0\in\mathbb C$ with $$\Omega_0^{12}=g_2(\Lambda_0)^3-27g_3(\Lambda_0)^2.$$ Let $E$ be a CM number field over $K$, with maximal real subfield $F$, a finite CM type $(\phi_i)_{i\in I}$ all extending $\iota$, and $s\ge1$. Assume $E/F$ is unramified at all finite places. Choose a nonzero proper ideal $\mathfrak f\subset\mathcal O_F$ satisfying the conductor conditions in the final paragraph and a finite set $Q$ of split primes of $F$ prime to $\mathfrak f$. Put $\mathfrak c=\mathfrak f\prod_{q\in Q}q$. Let $y\in\mathbb A_{E,f}^\times$, and let $L=E\cap y\widehat{\mathcal O_{\mathfrak c}}$, where $\mathcal O_{\mathfrak c}=\mathcal O_F+\mathfrak c\mathcal O_E$. For $\kappa\in\mathbb N^I$, suppose $S$ is entire and, for $\Re z>1-s$, $$S(z)=\sum_{x\in(L\setminus\{0\})/\mathcal O_F^\times}\prod_{i\in I}\phi_i(x)^{-(2s+\kappa_i)}\overline{\phi_i(x)}^{\kappa_i}|\phi_i(x)|^{-2z},$$ with convergence as an unordered sum. Then $$\frac{C\,S(0)}{\Omega_0^{\,2s|I|+2\sum_i\kappa_i}}\in\overline{\mathbb Q},\qquad C=|\operatorname{disc}F|^{(2s-1)/2}\prod_i\Gamma(2s+\kappa_i)\left(\frac{2\pi}{\sqrt d}\right)^{\sum_i\kappa_i}.$$ The conductor conditions require every prime of $\mathfrak f$ to split in $E$, have exponent at most two, and lie over an odd rational prime $\ell\nmid\operatorname{disc}E$ such that every prime of $E$ over $\ell$ has norm $\ell$.
