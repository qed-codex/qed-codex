---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasGoodReductionOfManyRationalTorsionPointsStatement.lean",
  "declarations": [
    "GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points"
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

## Good reduction from infinitely many full rational torsion groups

[Theorem AV.1512](https://andrewodesky.com/rh/lean/GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points/)

Let $R$ be a henselian discrete valuation ring with algebraically closed residue field $\kappa$, let $K=\operatorname{Frac}R$, and let $A/K$ be an abelian variety of dimension $g\ge0$. Suppose the set $$\{m\in\mathbb Z_{\ge0}:m\ne0\text{ in }\kappa,\ \#A(K)[m]=m^{2g}\}$$ is infinite. Then $A$ extends to an abelian scheme over $R$.
