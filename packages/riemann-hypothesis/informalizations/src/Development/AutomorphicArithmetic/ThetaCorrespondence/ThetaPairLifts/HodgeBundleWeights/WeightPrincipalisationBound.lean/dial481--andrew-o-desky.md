---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeightPrincipalisationBound.lean",
  "declarations": [
    "GlobalTheory.DegVal.birOn_of_weight_gaps_large"
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

## Cusp ratios generate the generic flag field

[Theorem AV.0038](https://andrewodesky.com/rh/lean/GlobalTheory.DegVal.birOn_of_weight_gaps_large/)

Under the global hypotheses below, the ratios of cusp sections of a sufficiently separated weight generate the entire generic flag field of every component.

Fix an arithmetic datum and an enhanced geometric and adelic realization satisfying the comparison-law hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Let $j\in\mathbb N$ have signature $(p,q)$ with $p,q\ge1$. Fix $e\in\mathbb N$ and $o\in\mathbb R$, and let $X/K$ satisfy the good-cover hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) with parameters $e,o$. Write $$r_j=p+q,\quad \Psi=\{\tau:E\hookrightarrow\mathbb C:\tau(r)=r_0\},\quad d=|\Psi|\binom{r_j}{2}.$$ If an integral weight $\lambda$ satisfies $$\lambda_{\tau,a}-\lambda_{\tau,a+1}\ge(d+3)^2+2r_j\qquad(\tau\in\Psi,\ 0\le a<r_j-1),$$ then for every irreducible component $Z$ of $X$ the generic evaluation map on $S_Z(\lambda,0)$ is nonzero, and $$K\left(\frac{\operatorname{ev}_Z(f)}{\operatorname{ev}_Z(g)}:f,g\in S_Z(\lambda,0)\right)=\Omega_Z.$$ The generic flag field $\Omega_Z$ and the cusp space are defined in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Fractions with zero denominator have value zero, the convention in the source's field operations.
