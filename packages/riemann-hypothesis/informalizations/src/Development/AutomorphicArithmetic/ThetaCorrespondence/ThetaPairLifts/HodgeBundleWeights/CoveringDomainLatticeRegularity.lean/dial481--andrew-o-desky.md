---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringDomainLatticeRegularity.lean",
  "declarations": [
    "GlobalTheory.CovTop.GoodDom.weight_lattice_span_on_domain"
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

## Integral cusp rules span the coefficient-field cusp space

[Theorem AV.0033](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.GoodDom.weight_lattice_span_on_domain/)

Assume Hypothesis (global Hodge-bundle inputs) in ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). For any arithmetic datum, take a geometric and adelic realization as data, and let $j\in\mathbb N$ be an index with signature $(p,q)$ satisfying $$p,q\ge1,\qquad 2<\left\lfloor\frac{[E:\mathbb Q]}2\right\rfloor.$$ For any $e\in\mathbb N$ and $o\in\mathbb R$, let $X/K$ satisfy the good-cover hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) with parameters $e,o$. Let $\lambda_{\tau,a}\in\mathbb Z$, indexed by $\tau\in\Psi=\{\tau:E\hookrightarrow\mathbb C:\tau(r)=r_0\}$ and $0\le a<p+q$, satisfy $$\lambda_{\tau,a}\ge\lambda_{\tau,b}\quad(a\le b),\qquad \lambda_{\tau,p-1}-\lambda_{\tau,p}\ge1.$$ Then the valuation-integral submodule $\Lambda(\lambda,0)$ spans the entire cusp-rule space over the coefficient field: $$\operatorname{span}_K\Lambda(\lambda,0)=S(\lambda,0).$$ The cusp space and integral submodule have the definitions in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)).
