---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/AwSpec.lean",
  "declarations": [
    "LateralTheory.Fix.EtaleChapterDTwo.s26"
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

## Tensoring a quasi-isomorphism of nonnegative etale complexes

[Theorem AG.1008](https://andrewodesky.com/rh/lean/LateralTheory.Fix.EtaleChapterDTwo.s26/)

Let $R$ be a commutative ring and let $I,I',J$ be cochain complexes of sheaves of $R$-modules on the big étale site of schemes. Assume all three vanish in degrees below $0$, and for every degree $n$ and scheme $U$, the $R$-module $J^n(U)$ is flat. If $f:I\to I'$ is a quasi-isomorphism, the induced map $$\operatorname{Tot}(I\otimes_RJ)\longrightarrow\operatorname{Tot}(I'\otimes_RJ)$$ is a quasi-isomorphism.
