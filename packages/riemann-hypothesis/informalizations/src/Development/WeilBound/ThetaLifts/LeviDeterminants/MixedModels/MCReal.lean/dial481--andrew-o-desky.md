---
{
  "module": "src/Development/WeilBound/ThetaLifts/LeviDeterminants/MixedModels/MCReal.lean",
  "declarations": [
    "PositivityTheory.Mix.real_estimates_holds"
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

## Symplectic covariance on real Schwartz spaces

[Theorem REP.1590](https://andrewodesky.com/rh/lean/PositivityTheory.Mix.real_estimates_holds/)

Let $X$ be a finite-dimensional normed real vector space and $\beta:X\times X\to\mathbb R$ a symmetric bilinear form such that $\beta(x,y)=0$ for every $y$ implies $x=0$. Let $S:X\oplus X\to X\oplus X$ be an invertible real-linear map preserving $$\omega((a,b),(a',b'))=\beta(a,b')-\beta(a',b).$$ For $w=(a,b)$ define an operator on $\mathcal S(X)$ by $$(R_wf)(x)=\exp\!\left(-2\pi i\left(\beta(x,b)+\tfrac12\beta(a,b)\right)\right)f(x+a).$$ There is a continuous complex-linear isomorphism $T:\mathcal S(X)\to\mathcal S(X)$, with continuous inverse, satisfying $$TR_w=R_{Sw}T\qquad(w\in X\oplus X).$$
