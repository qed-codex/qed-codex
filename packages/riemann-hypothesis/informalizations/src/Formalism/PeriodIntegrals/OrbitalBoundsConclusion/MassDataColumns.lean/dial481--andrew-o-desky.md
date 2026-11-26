---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/MassDataColumns.lean",
  "declarations": [
    "PIW.MassDataColumns.haar_ratio_eq_relIndex"
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

## Haar volume ratios equal subgroup indices

[Theorem ALG.0291](https://andrewodesky.com/rh/lean/PIW.MassDataColumns.haar_ratio_eq_relIndex/)

Let $G$ be a topological group with its Borel measurable structure and a left Haar measure $\mu$. Let $K'\subseteq K\subseteq G$ be subgroups, with $K'$ open in $G$ and $K$ compact. Then $$\frac{\mu(K)}{\mu(K')}=[K:K'].$$ The measures in this formula are their finite real values.
