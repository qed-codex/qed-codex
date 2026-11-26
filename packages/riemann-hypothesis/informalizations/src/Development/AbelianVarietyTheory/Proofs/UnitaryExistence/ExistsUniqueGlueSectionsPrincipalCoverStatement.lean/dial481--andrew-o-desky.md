---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/ExistsUniqueGlueSectionsPrincipalCoverStatement.lean",
  "declarations": [
    "GlobalTheory.T.existsUnique_glue_sections_principal_cover"
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

## Gluing sections over a finite principal cover

[Theorem AG.0398](https://andrewodesky.com/rh/lean/GlobalTheory.T.existsUnique_glue_sections_principal_cover/)

Fix the source's Hermitian moduli datum over a CM number field: its CM involution, signatures, lattice, level, and moduli scheme $X$. Let $S$ be a commutative ring and $x:\operatorname{Spec}S\to X$. Let $A_x$ be the universal abelian scheme pulled back to $\operatorname{Spec}S$, and write $\mathcal P_x$ for its prescribed polarization line bundle. Let $h_1,\ldots,h_n\in S$ generate the unit ideal, and let $$s_i\in\Gamma((A_x)_{D(h_i)},\mathcal P_x).$$ Assume that the two restrictions of $s_i,s_j$ to $D(h_ih_j)$ agree for every $i,j$. There is a unique $s\in\Gamma(A_x,\mathcal P_x)$ restricting to $s_i$ on every $(A_x)_{D(h_i)}$.
