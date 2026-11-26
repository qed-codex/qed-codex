---
{
  "module": "src/Development/EtaleCohomology/TateTwists/EtaleKInjectiveExtensionAlongQuasiIsoFromSingle.lean",
  "declarations": [
    "LateralTheory.EtaleFoundations.TwResExt.ext_hom_pf"
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

## Extension to a K-injective complex along a quasi-isomorphism

[Theorem AG.1087](https://andrewodesky.com/rh/lean/LateralTheory.EtaleFoundations.TwResExt.ext_hom_pf/)

Let $R$ be a commutative ring and $F$ a sheaf of $R$-modules on the big étale site of schemes. Let $T,I$ be cochain complexes of such sheaves, with $I$ K-injective and $I^n=0$ for $n<0$. Suppose $\varepsilon:F[0]\to T$ is a quasi-isomorphism. Every cochain map $a:F[0]\to I$ extends to a map $m:T\to I$ with $m\varepsilon=a$. If $m,m':T\to I$ satisfy $m\varepsilon=m'\varepsilon$, then $m,m'$ are chain homotopic.
