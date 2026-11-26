---
{
  "module": "src/Formalism/LocalToGlobal/GenusGluing/GenusApproximation/LocalAdelicEquivHolds.lean",
  "declarations": [
    "Formalism.L2.GenusGluing.Gen.genusToPoint_holds"
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

## Realizing a lattice in the standard genus by a finite adelic isometry

[Theorem ANT.1074](https://andrewodesky.com/rh/lean/Formalism.L2.GenusGluing.Gen.genusToPoint_holds/)

Let $E/F$ be a CM extension of number fields, with its complex conjugation, unramified at every finite place. On $E^n$ let $$h(x,y)=\sum_{i=1}^n\bar x_i y_i,\qquad L_0=\mathcal O_E^n.$$ Let $N\subseteq E^n$ be a full finitely generated $\mathcal O_E$-lattice. Suppose that for every maximal ideal $\mathfrak p$ of $\mathcal O_E$, there is an $E$-linear isometry carrying $(L_0)_{(\mathfrak p,\bar{\mathfrak p})}$ onto $N_{(\mathfrak p,\bar{\mathfrak p})}$. Then there is $g\in U(h)(\mathbb A_{F,f})$ with $$N=E^n\cap g\widehat L_0.$$
