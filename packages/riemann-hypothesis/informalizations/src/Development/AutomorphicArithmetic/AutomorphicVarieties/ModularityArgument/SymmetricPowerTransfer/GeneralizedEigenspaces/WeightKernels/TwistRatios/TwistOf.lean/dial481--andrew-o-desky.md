---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/WeightKernels/TwistRatios/TwistOf.lean",
  "declarations": [
    "UpperTheory.V.Z.Sym.Ga.twistOf"
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

## A character twist from equal traces on an open set

[Theorem REP.0614](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Sym.Ga.twistOf/)

Let $\ell$ be prime, $\Gamma$ a compact totally disconnected topological group, and $$\rho,\rho':\Gamma\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$$ group homomorphisms. Suppose the restriction of $\rho$ to every open subgroup of $\Gamma$ is irreducible. If there is a nonempty open set $U\subseteq\Gamma$ such that $$\operatorname{tr}\rho'(g)=\operatorname{tr}\rho(g)\qquad(g\in U),$$ then there is a character $\xi:\Gamma\to\overline{\mathbb Q}_\ell^\times$ with open kernel and an isomorphism $$\rho'\simeq\rho\otimes\xi.$$ No continuity assumption on the two initial homomorphisms is imposed.
