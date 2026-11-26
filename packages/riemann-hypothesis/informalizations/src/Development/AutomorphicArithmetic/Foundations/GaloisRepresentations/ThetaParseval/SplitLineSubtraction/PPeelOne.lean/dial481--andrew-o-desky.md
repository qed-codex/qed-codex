---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/PPeelOne.lean",
  "declarations": [
    "UpperTheory.Gal.TP.Sub.peelOne_holds"
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

## Removing a character from a semisimple characteristic-polynomial identity

[Theorem REP.1028](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TP.Sub.peelOne_holds/)

Let $\Gamma$ be a group and $k$ an algebraically closed field of characteristic zero. Let $r$ and $r'$ be semisimple representations of dimensions $m+1$ and $m'$, and let $a_1,\ldots,a_{t+1}$ and $a'_1,\ldots,a'_{t'}$ be one-dimensional $k$-characters of $\Gamma$, with $a_i\ne a'_j$ for every $i,j$. If, for every $g\in\Gamma$, $$\det(T-r(g))\prod_{j=1}^{t'}(T-a'_j(g))=\det(T-r'(g))\prod_{i=1}^{t+1}(T-a_i(g)),$$ there is a semisimple representation $s$ of dimension $m$ with $r\simeq s\oplus a_{t+1}$ and $$\det(T-s(g))\prod_{j=1}^{t'}(T-a'_j(g))=\det(T-r'(g))\prod_{i=1}^{t}(T-a_i(g))\qquad(g\in\Gamma).$$
