---
{
  "module": "src/Formalism/RankGapBounds/RankGapProofs/CardLargePrimeFactorsLeOneHolds.lean",
  "declarations": [
    "Formalism.RankGapBounds.ChebyshevFactorialBounds.chebyshevThetaLe_holds"
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

## Sum of logarithms of primes up to an integer

[Theorem ANT.1737](https://andrewodesky.com/rh/lean/Formalism.MainNotions.J.sum_log_primes_le/)

For every integer $N\ge0$, $$\sum_{\substack{p\le N\\p\text{ prime}}}\log p\le N\log4.$$
