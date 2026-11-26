---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RestrictCrystallineDeRhamFiniteExt.lean",
  "declarations": [
    "GlobalTheory.Per.TiedRestrict.restrict_crys_deRham"
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

## Crystalline and de Rham representations under finite restriction

[Theorem PHT.1327](https://andrewodesky.com/rh/lean/GlobalTheory.Per.TiedRestrict.restrict_crys_deRham/)

Let $l$ be a prime, and fix the local period datum, integral period-ring datum and compatible identifications with the crystalline and de Rham rings in ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $K\subset K'$ and $L$ be finite extensions of $\mathbb Q_l$ inside the chosen algebraic closure. Let $V$ be a finite-dimensional $L$-vector space, with its compatible $\mathbb Q_l$-vector-space structure, and let $\rho:G_K\to\mathrm{GL}_L(V)$ be a representation. Then $$\rho\text{ crystalline}\quad\Longrightarrow\quad\rho|_{G_{K'}}\text{ crystalline},$$ $$\rho\text{ de Rham}\quad\Longleftrightarrow\quad\rho|_{G_{K'}}\text{ de Rham}.$$ The period conditions are interpreted using the fixed datum at the respective fields.
