---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PotentialTheory/DegreeInt.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.M.degreeFormulaInt"
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

## Degree formula for integrable mixed potential densities

[Theorem AG.0927](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.degreeFormulaInt/)

Let $X,Y$ be compact Hausdorff spaces with finite holomorphic atlases of complex dimension $e\ge0$, and let $h:Y\to X$ be holomorphic. Suppose $S\subseteq X$ and $h^{-1}S\subseteq Y$ are analytic subsets with empty interior. Let $d\ge0$. Require every fibre above $X\setminus S$ to have $d$ points and the differential of $h$ to have nonzero determinant at every point of $Y\setminus h^{-1}S$.

For $i=1,\ldots,e$, let $\Phi_i$ be smooth real local potentials on $X$ whose differences on overlaps are locally real parts of holomorphic functions. Write $\mu_\Phi=dd^c\Phi_1\wedge\cdots\wedge dd^c\Phi_e$. If $g:X\to\mathbb R$ is integrable against the local mixed densities on every compact subset of every chart, then $g\circ h$ has the same integrability property for the pulled-back potentials, and $$\int_Y(g\circ h)\,d\mu_{h^*\Phi}=d\int_Xg\,d\mu_\Phi.$$
