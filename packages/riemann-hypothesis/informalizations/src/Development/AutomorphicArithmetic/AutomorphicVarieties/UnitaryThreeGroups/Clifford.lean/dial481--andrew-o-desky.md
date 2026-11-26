---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/Clifford.lean",
  "declarations": [
    "UpperTheory.V.U3.exists_selfTwist"
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

## A self-twist from reducibility on a normal subgroup

[Theorem REP.1261](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.exists_selfTwist/)

Let $\Gamma$ be a group, $\kappa$ an algebraically closed field of characteristic zero, $m\ge0$, and $\rho:\Gamma\to\operatorname{GL}_m(\kappa)$. Let $H\triangleleft\Gamma$ contain every commutator. Suppose $\rho$ is irreducible and $\rho|_H$ is reducible. There is a character $\varphi:\Gamma\to\kappa^\times$ such that $$\varphi\ne1,\qquad H\subseteq\ker\varphi,\qquad\varphi^m=1,\qquad \varphi\otimes\rho\simeq\rho.$$
