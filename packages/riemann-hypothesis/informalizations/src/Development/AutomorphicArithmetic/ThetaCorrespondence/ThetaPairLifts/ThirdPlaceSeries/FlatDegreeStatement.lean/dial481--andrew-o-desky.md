---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean",
  "declarations": [
    "GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt"
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

## Existence and common degree of flat CM sections

[Theorem ARAK.0124](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt/)

Assume ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). For the families, compatible points and threshold rules of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)), flat CM sections exist on every component of every good cover at every nonterminal stage, eventually and uniformly in the sense specified below. Every such section, in every CM-type direction, has the same arithmetic degree $$\widehat{\deg}s=\frac{p-q}{2}\log\Omega+q\bigl(\log d-\log\operatorname{rd}_E\bigr).$$ Here $(p,q)$ is the stage signature, $d$ is the distinguished quadratic-discriminant parameter, $\operatorname{rd}_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]}$, and $\log\Omega$ is the real CM period in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). The good-cover data and conditions are those of the good-cover hypothesis in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)), with $$e=\lfloor3L/\log3\rfloor_+,\qquad o=391(frL)^2,$$ where $L=x^\varepsilon$, $f=[E:\mathbb Q]/2$ and $r=k+m-1$.
