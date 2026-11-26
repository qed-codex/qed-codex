---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/UnipotentCoordinatesMeasurePreserving.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.unipotent_dual_lattice_covolume"
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

## Covolume of a lattice defined by a conjugation congruence

[Theorem ANT.0909](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.unipotent_dual_lattice_covolume/)

Let $E$ be a CM field, $F=E^+$, and suppose their absolute different ideals satisfy $$\mathfrak D_{E/\mathbb Q}=\mathfrak D_{F/\mathbb Q}\mathcal O_E.$$ Put $d=[F:\mathbb Q]$ and $R_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]}$. For an integer $g>0$, $\nu\in\mathbb Z$, and $s\ge0$, let $$L=\{x\in g\mathfrak D_{E/\mathbb Q}^{\nu}:x-(-1)^s\bar x\in g^2\mathfrak D_{E/\mathbb Q}^{\nu}\}.$$ Embed $E$ in $\mathbb C^d$ using one embedding from each conjugate pair. With its standard real Euclidean measure, $$\operatorname{covol}(L)=R_E^{2\nu d}(R_E/2)^d g^{3d}.$$
