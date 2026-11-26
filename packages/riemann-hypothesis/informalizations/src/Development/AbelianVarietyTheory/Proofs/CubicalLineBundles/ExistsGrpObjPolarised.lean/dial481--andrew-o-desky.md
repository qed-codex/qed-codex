---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/ExistsGrpObjPolarised.lean",
  "declarations": [
    "GlobalTheory.WeierstrassCurve.exists_polAV"
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

## A polarized elliptic model with its canonical tangent vector

[Theorem AV.0769](https://andrewodesky.com/rh/lean/GlobalTheory.WeierstrassCurve.exists_polAV/)

Let $R$ be a commutative ring and let $W$ be a Weierstrass equation over $R$ whose discriminant is a unit. There are an abelian scheme $A/R$ smooth of relative dimension one, a symmetric rigidified relatively ample line bundle $L$ on $A$ with trivial translation kernel, and an $R$-isomorphism $$\psi:A\xrightarrow{\sim}W$$ taking the identity section to the point at infinity.

There is a tangent vector $v\in\operatorname{Lie}(A/R)$ that is an $R$-basis of this rank-one module and whose image under $\psi$ is the dual-number point with projective coordinates $$[\epsilon:-1:0]\in W\bigl(R[\epsilon]/(\epsilon^2)\bigr).$$
