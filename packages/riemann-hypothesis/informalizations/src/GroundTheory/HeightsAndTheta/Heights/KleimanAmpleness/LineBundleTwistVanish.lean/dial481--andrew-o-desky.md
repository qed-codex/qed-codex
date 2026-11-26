---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/LineBundleTwistVanish.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Kleiman.SectionsOverLocalization.twistVanishAll_closed"
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

## Uniform higher-cohomology vanishing for powers of a generated line bundle

[Theorem AG.0358](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Kleiman.SectionsOverLocalization.twistVanishAll_closed/)

Let $S$ be a commutative Noetherian ring, $\Omega$ a field with an $S$-algebra structure, and $x_0,\ldots,x_N\in\Omega$. On the coordinate-chart system in the conventions, let $G,B$ be line bundles represented by invertible finitely generated fractional ideals. Suppose finitely many global sections $\eta_0,\ldots,\eta_r\in\Omega$ of $B$ generate $B$ on every chart. There is $c_0\in\mathbb Z$ such that $$H^i\bigl(G\otimes B^{\otimes b}\otimes\mathcal O(c)\bigr)=0\qquad(i\ge1,\ b\ge0,\ c\ge c_0).$$
