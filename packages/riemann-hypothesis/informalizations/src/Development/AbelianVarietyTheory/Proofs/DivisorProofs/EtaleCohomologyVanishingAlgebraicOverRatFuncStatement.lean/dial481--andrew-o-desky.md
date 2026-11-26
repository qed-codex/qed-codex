---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyVanishingAlgebraicOverRatFuncStatement.lean",
  "declarations": [
    "GlobalTheory.T.etale_cohomology_vanishing_algebraic_over_ratFunc"
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

## Etale cohomology over algebraic extensions of a rational function field

[Theorem AG.1142](https://andrewodesky.com/rh/lean/GlobalTheory.T.etale_cohomology_vanishing_algebraic_over_ratFunc/)

Let $k$ be algebraically closed and let $K$ be a field algebraic over $k(t)$. Let $q\ge1$ be an integer invertible in $K$. For every integer twist $i$ and every integer $n\ge2$, $$H^n_{\mathrm{\acute et}}(\operatorname{Spec}K,\mathbb Z/q\mathbb Z(i))=0.$$ The coefficient sheaves use the cyclotomic-generator definition in ([Vanishing of integral etale cohomology at the characteristic prime](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.jCharVan/)).
