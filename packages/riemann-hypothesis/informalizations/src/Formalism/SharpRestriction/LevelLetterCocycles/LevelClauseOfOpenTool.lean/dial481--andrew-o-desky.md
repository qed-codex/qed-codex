---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/LevelClauseOfOpenTool.lean",
  "declarations": [
    "Formalism.MainNotions.CrystallineLiftingInputs.power_series_dvr_factorisation"
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

## A valuation bound from power-series ideal membership

[Theorem PHT.0979](https://andrewodesky.com/rh/lean/Formalism.MainNotions.CrystallineLiftingInputs.power_series_dvr_factorisation/)

Let $O$ be a discrete valuation ring, $\ell$ a prime, $\varpi$ a uniformizer, and $e\ge1$ an integer such that $\ell$ and $\varpi^e$ are associated in $O$. Let $\varepsilon,u\in O[[X]]^\times$ and $b,y,t\ge0$ satisfy $b\ge1$ and $y\ge b/\ell$. If $$(\ell\varepsilon+uX^\ell)^y\in(\varpi^t,X^b)\subseteq O[[X]],$$ then $$\frac te\le y-\frac b\ell+2+\log_\ell y.$$
