---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CoefficientRingIntegersCompactAdicPropertiesStatement.lean",
  "declarations": [
    "GlobalTheory.T.coefficient_ring_integers_compact_adic_properties"
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

## Compactness and adic completeness of a coefficient ring

[Theorem PHT.0190](https://andrewodesky.com/rh/lean/GlobalTheory.T.coefficient_ring_integers_compact_adic_properties/)

Let $\ell$ be prime and $L/\mathbb Q_\ell$ a finite extension with its finite-dimensional vector-space topology, assumed to make $L$ a topological ring. Let $O$ be a commutative discrete valuation domain with fraction field $L$, embedded as an open subring of $L$. Then its image consists exactly of the elements integral over $\mathbb Z_\ell$, and this image is compact. For every $n\ge0$, $$O/\ell^nO\text{ is finite},$$ and $O$ is complete and separated for the ideal $\ell O$.
