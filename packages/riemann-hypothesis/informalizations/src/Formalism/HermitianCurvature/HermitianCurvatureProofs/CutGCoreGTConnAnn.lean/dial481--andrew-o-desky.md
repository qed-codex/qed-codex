---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTConnAnn.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.annulus_condition_holds"
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

## A circle-valued phase with prescribed logarithmic derivatives

[Theorem AG.0782](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.annulus_condition_holds/)

Let $T\ge0$ and $\Omega=\{z\in\mathbb C:|z|^2>T\}$. Let $\alpha:\mathbb C\to\mathbb C$ be smooth on $\Omega$. Assume $$\operatorname{Re}(\partial_{\bar z}\alpha)=0\quad\text{on }\Omega,$$ and, for every $R>0$ with $R^2>T$, $$\operatorname{Im}\oint_{|z|=R}\alpha(z)\,dz\in\pi\mathbb Z.$$ There exists $u:\mathbb C\to\mathbb C$, smooth on $\Omega$, such that throughout $\Omega$, $$|u|=1,\qquad \overline u\,\partial_z u=\alpha,\qquad \overline u\,\partial_{\bar z}u=-\overline\alpha.$$
