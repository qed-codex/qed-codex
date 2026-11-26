---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/PrimeLogarithmTail/SumLogBlock.lean",
  "declarations": [
    "PI.TailWork.tail_odd"
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

## An explicit tail bound for the sum of log p over p squared

[Theorem ANT.0854](https://andrewodesky.com/rh/lean/PI.TailWork.tail_odd/)

Let $k\ge3$ be an integer and $Q$ a finite set of primes with $p\ge2k+1$ for every $p\in Q$. Then $$\sum_{p\in Q}\frac{\log p}{p^2}\le\frac{2.04}{2k+1}.$$
