---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/SphericalTwistOfBlockTypeVector.lean",
  "declarations": [
    "GlobalTheory.BlockSph.sph_of_isBlockVec"
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

## A spherical twist forced by a block-type vector

[Theorem REP.1001](https://andrewodesky.com/rh/lean/GlobalTheory.BlockSph.sph_of_isBlockVec/)

Assume the three universal local representation packages below. Let $k$ be a nonarchimedean local field with valuation ring $O$ and maximal ideal $\mathfrak m$. Let $\chi:k^\times\to\mathbb C^\times$ have open kernel and be trivial on $1+\mathfrak m$. Let $\pi,\pi_1,\pi_2$ be irreducible smooth complex representations of $\operatorname{GL}_{r+t}(k)$, $\operatorname{GL}_r(k)$, and $\operatorname{GL}_t(k)$, respectively. Assume $$\pi\simeq\pi_1\times\pi_2,$$ where $\times$ is the specified normalized parabolic induction, and that no character $\chi\nu$ with $\nu$ unramified occurs in the cuspidal support of $\pi_1$.

Suppose $0\ne v\in\pi$ and, for every $h\in\operatorname{GL}_{r+t}(O)$ with block decomposition of sizes $(r,t)$ satisfying $$h_{21}\equiv0\pmod{\mathfrak m},\qquad h_{11}\equiv I_r\pmod{\mathfrak m},$$ one has $\pi(h)v=\chi(\det h_{22})v$. Then $$\pi_2\otimes(\chi^{-1}\circ\det)$$ has a nonzero $\operatorname{GL}_t(O)$-fixed vector.
