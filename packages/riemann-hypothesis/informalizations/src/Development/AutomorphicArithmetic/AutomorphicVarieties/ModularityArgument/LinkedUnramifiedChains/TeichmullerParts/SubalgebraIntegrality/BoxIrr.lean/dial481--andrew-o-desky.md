---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/TeichmullerParts/SubalgebraIntegrality/BoxIrr.lean",
  "declarations": [
    "UpperTheory.V.Z.J.D.boxIrr"
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

## Tensor products preserve irreducibility with scalar endomorphisms

[Theorem REP.0492](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.D.boxIrr/)

Let $G,H$ be groups and let $\rho:G\to\operatorname{GL}_{\mathbb C}(V)$, $\tau:H\to\operatorname{GL}_{\mathbb C}(W)$ be complex representations. Suppose both are irreducible, every $G$-equivariant endomorphism of $V$ is a scalar, and every $H$-equivariant endomorphism of $W$ is a scalar. Then the representation of $G\times H$ on $V\otimes_{\mathbb C}W$ given by $$(g,h)(v\otimes w)=\rho(g)v\otimes\tau(h)w$$ is irreducible, and every equivariant endomorphism of this tensor product is a scalar.
