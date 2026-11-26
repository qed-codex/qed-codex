---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PotentialTheory/PshShift.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.M.pshShift"
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

## Making a smooth function plurisubharmonic by adding a potential

[Theorem AG.0254](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.pshShift/)

Let $X$ be a compact Hausdorff space equipped with a finite holomorphic atlas of complex dimension $e\ge0$. Suppose a neighborhood $U_x$ of each $x\in X$ and a smooth real function $\Omega_x$ on $U_x$ are given. Assume the differences $\Omega_x-\Omega_y$ are locally real parts of holomorphic functions on overlaps, and the Levi form of each $\Omega_x$ is positive on every nonzero complex tangent vector. For every smooth $w:X\to\mathbb R$, there exists $C\in\mathbb R$ such that $$w|_{U_x}+C\Omega_x\text{ is plurisubharmonic on }U_x\qquad(x\in X).$$
