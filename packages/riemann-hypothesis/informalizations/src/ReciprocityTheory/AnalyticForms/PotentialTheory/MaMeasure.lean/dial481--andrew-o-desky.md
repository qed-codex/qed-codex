---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PotentialTheory/MaMeasure.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.M.maMeasure_thm"
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

## Measure associated with positive mixed potentials

[Theorem AG.1141](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.maMeasure_thm/)

Let $X$ be a compact Hausdorff space with its Borel sigma-algebra and a finite holomorphic atlas of complex dimension $e$. For $1\le i\le e$, let $\Phi_i$ be smooth real local potentials: each is defined on an open cover, and differences on overlaps are locally real parts of holomorphic functions. Assume their Levi forms are nonnegative. Form a measure $\mu$ by a smooth partition of unity subordinate to the atlas, using in each chart the nonnegative mixed density $$e!(2/\pi)^e\operatorname{Re}D(H_1,\ldots,H_e),$$ where $H_i=(\partial^2\Phi_i/\partial z_a\partial\bar z_b)_{a,b}$ and $D$ is the polarized determinant, normalized by $D(H,\ldots,H)=\det H$. Then $\mu$ is finite. For every measurable $g:X\to\mathbb R$, integrability of $g$ against this density on every compact subset of every chart is equivalent to $g\in L^1(\mu)$; when these conditions hold, the partition-of-unity mixed integral equals $\int_Xg\,d\mu$.
