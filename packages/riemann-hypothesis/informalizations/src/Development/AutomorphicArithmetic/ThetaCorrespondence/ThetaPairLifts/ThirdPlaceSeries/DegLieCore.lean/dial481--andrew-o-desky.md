---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DegLieCore.lean",
  "declarations": [
    "GlobalTheory.DefCoreLie.degLie_core_alt"
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

## Terminal determinant degree from Lie frames

[Theorem ARAK.0042](https://andrewodesky.com/rh/lean/GlobalTheory.DefCoreLie.degLie_core_alt/)

At the terminal stage, the determinant degree computed from integral and archimedean Lie frames is independent of the component, the chosen frame data and the CM-type direction. Its value is $$\deg_{\mathrm{Lie},\tau}=-\left(\frac{p-q}{2}\log\Omega+q\bigl(\log d-\log\operatorname{rd}_E\bigr)\right).$$

Fix the arithmetic theta datum, size data, integral and rational realizations, initial divisor data and a point with its auxiliary choices as in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). Assume its point compatibility and recursive-realization identifications from ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). Let $j=m$ be the terminal stage. Assume the Gram-norm hypothesis of ([Weight, size and lattice conditions at a unitary lift stage](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.GramAt/)), the weight and host conditions below, and that the coefficient field $K$ is algebraically closed in the function field of every component of the stage moduli variety. The displayed identity holds for every component $Z$, every point and frame datum on $Z$ described below, and every $\tau\in\Psi$.
