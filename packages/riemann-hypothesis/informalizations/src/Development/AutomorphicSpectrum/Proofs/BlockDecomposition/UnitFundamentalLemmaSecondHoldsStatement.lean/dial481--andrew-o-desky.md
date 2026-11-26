---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitFundamentalLemmaSecondHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.unit_fundamental_lemma_second_holds"
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

## Vanishing of the unit orbital integral outside the norm image

[Theorem REP.1232](https://andrewodesky.com/rh/lean/GlobalTheory.T.unit_fundamental_lemma_second_holds/)

Assume two universal local matrix statements: a matrix conjugate into $\mathrm{GL}_n(\mathcal O_F)$ is unit-integral (its characteristic polynomial has integral coefficients and unit constant term), and twisted conjugacy into that group makes its cyclic norm integral after the same change of basis; and every unit-integral matrix over the base has a cyclic norm preimage whose matrix and inverse are integral polynomials in the original matrix.

Let $E/k$ be a finite unramified Galois extension of nonarchimedean local fields, with generator $\sigma$ of its Galois group, and let $n\ge0$. Give both general linear groups their Borel measurable structures and Haar measures with $\mathrm{GL}_n(\mathcal O_E)$ and $\mathrm{GL}_n(\mathcal O_k)$ of volume one. Let $\gamma\in\mathrm{GL}_n(k)$ be regular semisimple, and choose any Haar measure on its centralizer. If there is no $\delta\in\mathrm{GL}_n(E)$ for which the cyclic product $\delta\sigma(\delta)\cdots\sigma^{[E:k]-1}(\delta)$ is conjugate over $E$ to $\gamma$, then the orbital integral of $\mathbf1_{\mathrm{GL}_n(\mathcal O_k)}$ at $\gamma$ is zero.
