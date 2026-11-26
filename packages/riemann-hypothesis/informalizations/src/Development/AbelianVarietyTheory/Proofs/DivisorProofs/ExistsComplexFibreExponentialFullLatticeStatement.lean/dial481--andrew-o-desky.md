---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsComplexFibreExponentialFullLatticeStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_complexFibreExponential_full_lattice"
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

## The full period lattice of a complex abelian fibre

[Theorem AV.0274](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_complexFibreExponential_full_lattice/)

Let $G\to X$ be a commutative abelian scheme, smooth of relative dimension $g\ge0$, and let $y:\operatorname{Spec}\mathbb C\to X$. There are a surjective holomorphic group homomorphism $$e:\mathbb C^g\longrightarrow G_y(\mathbb C)$$ whose derivative at zero identifies $\mathbb C^g$ with the tangent space at the identity, and a $\mathbb Z$-submodule $\Lambda\subseteq\mathbb C^g$ such that $$\Lambda\text{ is discrete},\qquad\operatorname{span}_{\mathbb R}\Lambda=\mathbb C^g,\qquad\ker e=\Lambda.$$
