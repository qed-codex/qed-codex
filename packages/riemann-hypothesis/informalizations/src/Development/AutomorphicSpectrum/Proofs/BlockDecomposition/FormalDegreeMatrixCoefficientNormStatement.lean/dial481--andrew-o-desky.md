---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalDegreeMatrixCoefficientNormStatement.lean",
  "declarations": [
    "GlobalTheory.T.formal_degree_matrix_coefficient_norm"
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

## Hilbert–Schmidt convolution by an integrable coefficient

[Theorem REP.1572](https://andrewodesky.com/rh/lean/GlobalTheory.T.formal_degree_matrix_coefficient_norm/)

Let $G$ be a locally compact second-countable topological group with its Borel measurable structure, and let $\nu$ be a Haar measure invariant under both left and right translations. Let $\sigma,\rho$ be strongly continuous unitary representations on complex Hilbert spaces $A,B$. Assume $d>0$ and, for every $a,b,a',b'\in A$, the following integrand is integrable and $$\int_G\langle b,\sigma(g)a\rangle\overline{\langle b',\sigma(g)a'\rangle}\,d\nu(g)=\frac{\langle a',a\rangle\langle b,b'\rangle}{d}.$$ For every $v\in B$ for which $g\mapsto\overline{\langle v,\rho(g)v\rangle}$ is integrable, the bounded operator $$T_v a=\int_G\overline{\langle v,\rho(g)v\rangle}\,\sigma(g)a\,d\nu(g)$$ is Hilbert–Schmidt. Inner products are conjugate-linear in the first argument.
