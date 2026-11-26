---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsSelfdualMeasureHermitianTuplesStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_selfdual_measure_hermitian_tuples"
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

## A self-dual measure on adelic Hermitian tuples

[Theorem THETA.0664](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_selfdual_measure_hermitian_tuples/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J\in M_M(E)$ be a nondegenerate $\sigma$-Hermitian matrix. Let $\psi:\mathbb A_F\to\mathbb C$ be a continuous, unit-modulus, nontrivial additive character that is trivial on $F$. For every $n\ge0$, the additive group $$W=(\mathbb A_F\otimes_F E)^{n\times M}$$ has a Haar measure $\mu$ self-dual for $$\langle X,Y\rangle_\psi=\psi\left(\sum_{a=1}^{n}\operatorname{Tr}_{\mathbb A_F\otimes_F E/\mathbb A_F}(h_J(X_a,Y_a))\right).$$
