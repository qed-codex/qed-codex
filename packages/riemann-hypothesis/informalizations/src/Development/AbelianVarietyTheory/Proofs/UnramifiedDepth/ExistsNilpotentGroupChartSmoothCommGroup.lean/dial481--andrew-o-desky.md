---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsNilpotentGroupChartSmoothCommGroup.lean",
  "declarations": [
    "GlobalTheory.ChF.exists_nilChart"
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

## Formal coordinates on a smooth commutative group

[Theorem AG.1185](https://andrewodesky.com/rh/lean/GlobalTheory.ChF.exists_nilChart/)

Let $R$ be a commutative local ring and $G$ a commutative group scheme over $R$, smooth of relative dimension $g\ge0$. There exist a commutative $g$-dimensional formal group law $F$ over $R$ and maps $X_S:S^g\to G(S)$ for every commutative $R$-algebra $S$, with $X_S(0)=1$, having the following properties on tuples of nilpotent elements:

- $X_S$ is injective on these tuples, commutes with every $R$-algebra homomorphism, and satisfies $X_S(a)X_S(b)=X_S(F(a,b))$.
- If $\rho:S\to S'$ is a split surjective $R$-algebra homomorphism with nilpotent kernel, every $z\in\ker(G(S)\to G(S'))$ equals $X_S(a)$ for a tuple $a\in(\ker\rho)^g$.
