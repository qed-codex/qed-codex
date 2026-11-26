---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsSelfdualMeasureHermitianAdelesStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_selfdual_measure_hermitian_adeles"
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

## A self-dual measure on adelic Hermitian matrices

[Theorem THETA.0405](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_selfdual_measure_hermitian_adeles/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $\psi:\mathbb A_F/F\to\mathbb C^\times$ be a continuous nontrivial unitary additive character. For every $n\ge0$ there is an additive Haar measure $\nu$ on the Hermitian matrices $$\mathcal H_n=\{S\in\operatorname{Mat}_n(\mathbb A_F\otimes_FE):S^*=S\}$$ that is self-dual for the pairing $$\chi(S,T)=\psi\!\left(\tfrac12\operatorname{Tr}_{(\mathbb A_F\otimes_FE)/\mathbb A_F}\operatorname{tr}(ST)\right).$$
