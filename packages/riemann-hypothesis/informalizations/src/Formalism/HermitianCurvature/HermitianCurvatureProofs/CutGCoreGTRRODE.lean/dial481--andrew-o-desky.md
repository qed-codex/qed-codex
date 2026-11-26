---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTRRODE.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.rotation_ode_holds"
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

## Integral weights of a periodic matrix homomorphism

[Theorem REP.0892](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.rotation_ode_holds/)

Let $I$ be a finite set and $M:\mathbb R\to\operatorname{Mat}_I(\mathbb C)$ satisfy $$M(0)=1,\qquad M(\phi+\psi)=M(\phi)M(\psi),\qquad M(2\pi)=1.$$ Suppose every entry is differentiable at $0$, with derivative $B_{ij}$, and $B_{ij}=0$ whenever $i\ne j$. There are integers $n_i$ such that $$M(\phi)_{ij}=\begin{cases}e^{in_i\phi}&i=j,\\0&i\ne j\end{cases}\qquad(\phi\in\mathbb R).$$
