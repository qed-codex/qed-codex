---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DegenerationProofs/PrincipallyPolarizedAbelianVarietyPotentialSemiAStatement.lean",
  "declarations": [
    "GlobalTheory.T.principallyPolarizedAbelianVariety_potentialSemiAbelianModel"
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

## Potential semiabelian models of principally polarized abelian varieties

[Theorem AV.1658](https://andrewodesky.com/rh/lean/GlobalTheory.T.principallyPolarizedAbelianVariety_potentialSemiAbelianModel/)

Let $V$ be a complete discrete valuation ring with finite residue field, and let $K=\operatorname{Frac}V$ have characteristic zero. Let $A/K$ be an abelian variety supplied with a rigidified symmetric ample line bundle defining a principal polarization. There exist a complete discrete valuation ring $W$, its fraction field $L$, compatible maps $V\to W$ and $K\to L$, and a semiabelian scheme $G/W$ such that $W$ is finite as a $V$-module, $V\to W$ is local, and $$G\times_{\operatorname{Spec}W}\operatorname{Spec}L \simeq A\times_{\operatorname{Spec}K}\operatorname{Spec}L$$ as group schemes.
