---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/MemPrimesOverOfMem.lean",
  "declarations": [
    "Formalism.MainNotions.TwistedPlaces.etaSum_le"
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

## Weighted projection defects from local congruence bounds

[Theorem GC.0168](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.etaSum_le/)

Let an arithmetic datum with its full parameter choice carry a table satisfying ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)) with constant $C$. Assume $g_0,g_1\ne2$ and that the nonnegative sequence $V$ in ([Fixed-data congruence-defect bound](https://andrewodesky.com/rh/s/defect.html)) is summable. Let $\mathcal P$ be the finite set of residue primes of the twisted coefficient places in the specified support. For every $1\le j\le m$, $$\eta_j\le d_j\left\{6+\mathcal N+\log h_E+\log H+\sum_{\ell\in\mathcal P}\log\ell\,\Lambda_\ell+\sum_{n=0}^{\infty}V(n)\right\}.$$ Here $\eta_j$ is the weighted projection defect, $d_j$ the selected dimension, $H$ the positive finite group order, $h_E$ the class number, and $\Lambda_\ell$ the error function defined in ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). The number $\mathcal N$ is the source's nonnegative cyclotomic torsion budget.
