---
{
  "module": "src/Formalism/CharacterColumnKernels/IdempotentNormalForms/IdemNormalForm.lean",
  "declarations": [
    "Formalism.NG.burnside"
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

## Surjectivity of an irreducible action with scalar commutant

[Theorem REP.0784](https://andrewodesky.com/rh/lean/Formalism.NG.burnside/)

Let $k$ be a field, $A$ a unital $k$-algebra, and $V$ a finite-dimensional $k$-vector space with a compatible $A$-module structure. Suppose $V$ is a simple $A$-module and every $A$-linear endomorphism of $V$ is multiplication by a scalar in $k$. Then $$A\longrightarrow\operatorname{End}_k(V),\qquad a\longmapsto(v\mapsto av),$$ is surjective.
