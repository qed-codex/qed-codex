---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleLocalPrimitiveRootAndRootsOfUnity.lean",
  "declarations": [
    "GlobalTheory.EtC.PrimLoc.prim_loc"
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

## Primitive roots and power roots after etale covers

[Theorem AG.0283](https://andrewodesky.com/rh/lean/GlobalTheory.EtC.PrimLoc.prim_loc/)

Let $q\ge1$ and $U$ be a scheme. The following assertions hold, with each occurrence of etale locally allowing its own covering of $U$.

1. If $q$ is invertible in $\Gamma(U,\mathcal O_U)$, a primitive $q$th root exists etale locally.
2. For primitive roots $\zeta,\xi\in\Gamma(U,\mathcal O_U)$, etale locally $\xi=\zeta^a$ for some $a\in(\mathbb Z/q\mathbb Z)^\times$.
3. For a primitive root $\zeta$ and any $x\in\Gamma(U,\mathcal O_U)$ with $x^q=1$, etale locally $x=\zeta^a$ for some integer $a\ge0$.
4. If $q$ is invertible, every unit of $\Gamma(U,\mathcal O_U)$ has a unit $q$th root etale locally.
