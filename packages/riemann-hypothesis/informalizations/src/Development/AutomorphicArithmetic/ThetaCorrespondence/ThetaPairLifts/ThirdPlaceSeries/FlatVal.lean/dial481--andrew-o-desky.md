---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatVal.lean",
  "declarations": [
    "GlobalTheory.CovTop.FlatVal.flat_val_alt"
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

## CM contribution to degrees on covers

[Theorem ARAK.0111](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.FlatVal.flat_val_alt/)

Use the theta-family conditions 1–14, the threshold-rule convention and the compatible-point conditions of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). For a point in such a family, let $1\le j<m$ be a nonterminal lift stage, with moduli signature $(p,q)$ and associated moduli variety $X$. Put $L=x^\varepsilon$, $f=[E:\mathbb Q]/2$, $r=k+m-1$, and $Z_0=frL$. The good-cover data and conditions are those of the good-cover hypothesis in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)), with $$e=\lfloor3L/\log3\rfloor_+,\qquad o=391Z_0^2.$$

Assume the uniform flat-section existence and common-degree assertion of ([Existence and common degree of flat CM sections](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt/)). Use the flat CM sections and arithmetic degrees defined there. Here $\Omega$ is the period defined in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)), $d$ is the auxiliary quadratic discriminant parameter, and $\mathrm{rd}_E$ is the root discriminant. Define $$c_1(\tau)=-\frac1{\#\pi_0(X)}\sum_{Z\in\pi_0(X)}\widehat{\deg}(s_{Z,\tau}),$$ with division by zero equal to zero if the component set is empty, as in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). Then, uniformly in that same sense, all flat sections exist and $$\left|c_1(\tau)+\frac{p-q}{2}\log\Omega\right|\le3qL,\qquad\sum_{\ell\in B}\log\ell\le40L.$$ The set $B$ consists exactly of the rational prime divisors of $2d\,|\operatorname{disc}E|\operatorname{lcm}(M,A)$, where $M$ and $A$ are the refined level integers (here $A=1$). In addition, the refined level integer $M$ satisfies $$M/p^{v_p(M)}\ge3\qquad\text{for every rational prime }p,$$ and the complex-comparison package holds.
