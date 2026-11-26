---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/FiniteEtaleModels/PNormExt.lean",
  "declarations": [
    "UpperTheory.Gal.FiniteEtaleModels.normExt_holds"
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

## Extension of a lift across a dense open subscheme

[Theorem AG.1542](https://andrewodesky.com/rh/lean/UpperTheory.Gal.FiniteEtaleModels.normExt_holds/)

Let $U,S,Y,B$ be schemes, $i:U\hookrightarrow S$ a dominant open immersion, and $f:S\to B$, $g:Y\to B$, $y:U\to Y$ morphisms with $g\circ y=f\circ i$. Assume $S$ is locally Noetherian, every local ring $\mathcal O_{S,s}$ is an integrally closed domain, and $g$ is finite. Then there is $y':S\to Y$ such that $$y'\circ i=y,\qquad g\circ y'=f.$$
