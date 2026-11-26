---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/GramDetNeZeroLocalBasisCofiniteStatement.lean",
  "declarations": [
    "GlobalTheory.T.gram_det_ne_zero_local_basis_cofinite"
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

## Nonzero Gram determinant and bases away from finitely many primes

[Theorem AV.0600](https://andrewodesky.com/rh/lean/GlobalTheory.T.gram_det_ne_zero_local_basis_cofinite/)

Fix the CM lattice datum described below, of $\mathcal O_E$-rank $p+q$, with underlying module $\Lambda$ and alternating pairing $B$. Choose a finite set $I$ of cardinality $p+q$ and an $\mathcal O_E$-linearly independent family $(e_i)_{i\in I}$ in $\Lambda$. Let $(b_k)$ be the integral basis of $E$ used in the datum and $(b_k^\vee)$ its trace-dual basis over $\mathbb Q$, and set $$s(x,y)=\sum_kB(b_kx,y)b_k^\vee,\qquad G=(s(e_i,e_j))_{i,j\in I}.$$ Then $\det G\ne0$. Moreover, for all but finitely many rational primes $\ell$, there is an integer $n\ge0$, not divisible by $\ell$, such that $$n\Lambda\subseteq\sum_{i\in I}\mathcal O_Ee_i.$$
