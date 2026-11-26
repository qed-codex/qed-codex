---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SatakeParameterSphericalProductSpehQuotients.lean",
  "declarations": [
    "GlobalTheory.SatInd.exists_sat_multiProd"
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

## Satake parameters of a spherical induced vector

[Theorem REP.1404](https://andrewodesky.com/rh/lean/GlobalTheory.SatInd.exists_sat_multiProd/)

Let $E$ be a number field, $w$ a nonzero prime of $\mathcal O_E$, and $E_w$ its completion. Fix $c,n\ge0$ and block sizes $N_1,\ldots,N_c\ge0$ with $\sum_aN_a=n$. For each $a$, let $\pi_a$ be a smooth irreducible complex representation of $\mathrm{GL}_{N_a}(E_w)$. Form their normalized parabolic induction $$I=\pi_1\times\cdots\times\pi_c.$$ If $0\ne f\in I$ is fixed by $\mathrm{GL}_n(\mathcal O_{E_w})$, then there are Satake multisets $S_a\subset\mathbb C^\times$ for the $\pi_a$ such that $f$ is a spherical Hecke eigenvector in $I$ with Satake multiset $$S_1\sqcup\cdots\sqcup S_c.$$
