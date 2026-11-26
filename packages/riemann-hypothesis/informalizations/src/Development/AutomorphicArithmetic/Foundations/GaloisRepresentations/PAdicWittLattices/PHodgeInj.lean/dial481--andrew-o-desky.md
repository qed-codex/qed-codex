---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/PHodgeInj.lean",
  "declarations": [
    "UpperTheory.Gal.G3.pHodgeInj"
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

## Finite etale injectivity on Hodge cohomology

[Theorem AG.1218](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.pHodgeInj/)

Let $k$ be a field of characteristic zero, let $Z,W$ be $k$-schemes, and let $c:W\to Z$ be a finite, etale, surjective $k$-morphism. For all $a,b\ge0$, pullback is injective: $$c^*:H^b(Z,\Omega^a_{Z/k})\longrightarrow H^b(W,\Omega^a_{W/k}).$$
