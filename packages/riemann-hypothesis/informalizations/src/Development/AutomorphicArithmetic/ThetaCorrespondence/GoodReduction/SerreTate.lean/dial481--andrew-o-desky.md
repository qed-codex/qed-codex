---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/SerreTate.lean",
  "declarations": [
    "UpperTheory.Lit.neronOggShafarevich"
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

## Good reduction and unramified torsion

[Theorem AV.1653](https://andrewodesky.com/rh/lean/UpperTheory.Lit.neronOggShafarevich/)

Let $R$ be a discrete valuation ring with perfect residue field $\kappa$, let $K=\operatorname{Frac}R$, and let $\Omega$ be a separable closure of $K$. Fix a valuation ring $V\subseteq\Omega$ whose inverse image in $K$ is $R$, and let $I_V\subseteq\operatorname{Gal}(\Omega/K)$ be its inertia group. For an abelian variety $A/K$, the following four conditions are equivalent:

1. $A$ extends to an abelian scheme over $R$.
2. For every integer $m\ge0$ whose image in $\kappa$ is nonzero, $I_V$ acts trivially on $A[m](\Omega)$.
3. The set of integers $m\ge0$ whose image in $\kappa$ is nonzero and for which $I_V$ acts trivially on $A[m](\Omega)$ is infinite.
4. For some prime $\ell$ whose image in $\kappa$ is nonzero, $I_V$ acts trivially on the $\ell$-adic Tate module $T_\ell A$.
