---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/TransferenceMinima.lean",
  "declarations": [
    "transference_successive_minima"
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

## Transference for successive Euclidean minima

[Theorem ARAK.0412](https://andrewodesky.com/rh/lean/transference_successive_minima/)

Let $\Lambda\subset\mathbb R^N$ be a discrete additive subgroup spanning $\mathbb R^N$. Set $$\Lambda^*=\{y\in\mathbb R^N:\langle x,y\rangle\in\mathbb Z\text{ for all }x\in\Lambda\}.$$ For $1\le i\le N$, let $\lambda_i(\Lambda)$ be the infimum of the nonnegative $t$ for which $\Lambda$ contains $i$ real-linearly independent vectors of norm at most $t$. Then $$\lambda_i(\Lambda)\lambda_{N+1-i}(\Lambda^*)\le N.$$
