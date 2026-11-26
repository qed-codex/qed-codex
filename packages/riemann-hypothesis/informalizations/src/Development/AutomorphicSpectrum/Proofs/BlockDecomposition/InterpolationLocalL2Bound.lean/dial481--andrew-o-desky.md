---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/InterpolationLocalL2Bound.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.InterpLoc.interpolation_local_L2_bound"
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

## Pointwise bounds from an L2 norm on one compact set

[Theorem REP.1248](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.InterpLoc.interpolation_local_L2_bound/)

Let $X$ be a set, $Y$ a locally compact Hausdorff space with its Borel measurable structure, and $\nu$ a measure positive on every nonempty open set and finite on compact sets. Let $F:X\times Y\to\mathbb C$ have continuous functions $F(x,\cdot)$ whose complex linear span is finite-dimensional. There is a compact $\Omega\subseteq Y$ such that for every $y_0\in Y$ there is $C_{y_0}\ge0$ with $$|F(x,y_0)|^2\le C_{y_0}\int_\Omega |F(x,y)|^2\,d\nu(y)\qquad(x\in X).$$
