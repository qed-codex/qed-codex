---
{
  "module": "src/Formalism/QuotientMetricDivisors/HermitianTwistDivisors/SecondStepGluing.lean",
  "declarations": [
    "Formalism.DivisionValues.lattice_gluing"
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

## Gluing lattices from localizations

[Theorem ARAK.0130](https://andrewodesky.com/rh/lean/Formalism.DivisionValues.lattice_gluing/)

Let $K$ be a number field and $L_0\subset K^D$ a full $\mathcal O_K$-lattice. For every nonzero prime ideal $\mathfrak p$ choose a full lattice $L(\mathfrak p)\subset K^D$, and assume $L(\mathfrak p)_\mathfrak p=(L_0)_\mathfrak p$ except at finitely many primes. Then $$L=\bigcap_\mathfrak p L(\mathfrak p)_\mathfrak p\subset K^D$$ is a full $\mathcal O_K$-lattice and satisfies $L_\mathfrak p=L(\mathfrak p)_\mathfrak p$ at every prime. The subscript denotes localization inside $K^D$.
