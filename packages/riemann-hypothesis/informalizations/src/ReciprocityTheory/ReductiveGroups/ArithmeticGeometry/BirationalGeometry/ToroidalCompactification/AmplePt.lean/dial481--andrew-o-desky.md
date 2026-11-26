---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/AmplePt.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.relAmple_pull"
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

## Relative ampleness after base change

[Theorem AG.1356](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.relAmple_pull/)

Let $S',S$ be schemes, $f:S'\to S$, and let $A\to S$, $A'\to S'$ be group objects in the corresponding categories of schemes over these bases. Suppose the square with maps $\varphi:A'\to A$ and $f$ is cartesian. Let $L$ and $L'$ be line bundles on $A$ and $A'$ and let $w:L'\simeq\varphi^*L$ be an isomorphism satisfying the compatibility on pulled-back local generators specified below. Let $U\subseteq S$ be affine open with $f(S')\subseteq U$.

If $L$ is relatively ample over $S$, then $L'$ is relatively ample over $S'$.
