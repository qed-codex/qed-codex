---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/ExportBoundOfAdmissible.lean",
  "declarations": [
    "Formalism.MainNotions.TwistedPlaces.point_bound"
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

## Total logarithmic prime cost of the local errors

[Theorem GC.0170](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.point_bound/)

Let an arithmetic datum with its full parameter choice carry a table satisfying ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)) with constant $C>0$. Assume its stated polynomial parameter bounds and the large-scale conditions below. For every finite set $\mathcal P$ of rational primes, $$6+\mathcal N+\log h_E+\log H+\sum_{\ell\in\mathcal P}\log\ell\,\Lambda_\ell\le2000(C+1)^3fm bL^2.$$ The notation, including the error function $\Lambda_\ell$ and cyclotomic torsion budget $\mathcal N$, is as in ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)) and ([Weighted projection defects from local congruence bounds](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.etaSum_le/)). The estimate is independent of $\mathcal P$.
