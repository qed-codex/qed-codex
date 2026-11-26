---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/WittLogarithm.lean",
  "declarations": [
    "_private.Formalism.PeriodIntegrals.OrbitalBoundsConclusion.WittLogarithm.0.inv_series_sub"
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

## Coefficients of a compositional inverse remain in the subring

[Theorem ALG.0732](https://andrewodesky.com/rh/lean/_private.Formalism.PeriodIntegrals.OrbitalBoundsConclusion.WittLogarithm.0.inv_series_sub/)

Let $K$ be a field, let $R\subseteq K$ be a subring, and let $l,e\in K[[T]]$ satisfy $$l\in R[[T]],\qquad l(0)=e(0)=0,\qquad[T]l=1,\qquad l(e(T))=T.$$ Then $e\in R[[T]]$.
