---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLimitCocycleOfCompatibleModPowStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_limit_cocycle_of_compatible_mod_pow"
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

## Lifting compatible finite-level cocycles to a lattice cocycle

[Theorem GC.0369](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_limit_cocycle_of_compatible_mod_pow/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite, and $L/\mathbb Q_\ell$ a finite extension with its finite-dimensional vector-space topology. Let $O$ be a discrete valuation domain with fraction field $L$, open in $L$. Let $V$ be a finite-dimensional continuous $L$-representation of $G_K$, $\Lambda$ a stable $O$-lattice, and $\varpi\in O$ irreducible. Suppose each $\varpi^n\Lambda$ is stable and maps $w_n:G_K\to\Lambda$ satisfy:

- their reductions to $\Lambda/\varpi^n\Lambda$ are continuous cocycles;
- $w_{n+1}(g)-w_n(g)\in\varpi^n\Lambda$ for all $n,g$.

There is a continuous cocycle $d:G_K\to\Lambda$ with $$d(g)-w_n(g)\in\varpi^n\Lambda\qquad(n\ge0,\ g\in G_K).$$
