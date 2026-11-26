---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalCompactificationSmoothSncBoundary.lean",
  "declarations": [
    "GlobalTheory.UChartSmooth.smooth_and_snc"
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

## Smoothness and normal crossings from toroidal local charts

[Theorem AG.0089](https://andrewodesky.com/rh/lean/GlobalTheory.UChartSmooth.smooth_and_snc/)

Let $E$ be a CM number field and fix unitary moduli data, with the host and polarized-lattice conventions of ([An indefinite polarized CM lattice splits by signature](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitianLatticeSignatureSplit_of_indefinite/)) and signature $(p,q)$, $p+q\ge1$, level, coefficient field $k$, open moduli scheme $X/k$, and expected dimension $d_X$. Let $\phi$ be the invariant function on balanced forms specifying a polarized fan, with no self-intersections, in every module rank at most $\min(p,q)$.

Choose schemes and maps $$X\xrightarrow{j}S\xrightarrow{\pi}Z\xrightarrow{z}\operatorname{Spec}k,\qquad i=\pi j,$$ a line-bundle datum $L_Z$, integers $N,d\ge0$, an ideal sheaf $J$ on $Z$, and an effective Cartier datum $B$ on $S$, with $j$ an open immersion. Assume the source's compactification and normalized-blowup package for these data, its boundary separation package, and its monomial local-chart package at every point of $S\setminus j(X)$.

Then $S\to\operatorname{Spec}k$ is smooth of relative dimension $d_X$, and the reduced closed boundary $S\setminus j(X)$ is a simple normal-crossing subscheme.
