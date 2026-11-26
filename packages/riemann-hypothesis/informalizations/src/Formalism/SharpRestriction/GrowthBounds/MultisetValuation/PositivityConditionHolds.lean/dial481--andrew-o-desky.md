---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PositivityConditionHolds.lean",
  "declarations": [
    "Formalism.MainNotions.FormalGroupSystem.Pf.sx_dwork"
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

## Dwork integrality criterion

[Theorem PHT.0107](https://andrewodesky.com/rh/lean/Formalism.MainNotions.FormalGroupSystem.Pf.sx_dwork/)

Let $p$ be an odd prime, $W=W(\overline{\mathbb F}_p)$ its Witt-vector ring, $K=\operatorname{Frac}W$, and $\sigma$ the Witt Frobenius on $K$. For $\Psi\in K[[X_1,\ldots,X_n]]$ with zero constant term, $$\exp\Psi\in W[[X_1,\ldots,X_n]]\quad\Longleftrightarrow\quad\Psi^\sigma(X_1^p,\ldots,X_n^p)-p\Psi(X_1,\ldots,X_n)\in pW[[X_1,\ldots,X_n]].$$ The superscript means applying $\sigma$ to the coefficients.
