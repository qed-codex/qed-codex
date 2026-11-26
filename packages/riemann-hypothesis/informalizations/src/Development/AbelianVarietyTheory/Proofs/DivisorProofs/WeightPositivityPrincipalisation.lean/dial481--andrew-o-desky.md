---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/WeightPositivityPrincipalisation.lean",
  "declarations": [
    "GlobalTheory.CentreCusp.exists_cusp_genVal_ne_zero'"
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

## A cusp section with nonzero generic value on every component

[Theorem AV.0046](https://andrewodesky.com/rh/lean/GlobalTheory.CentreCusp.exists_cusp_genVal_ne_zero'/)

Sufficiently separated integral weights have a cusp section with nonzero generic value on every component, under the following hypotheses.

Fix an arithmetic datum and an enhanced geometric and adelic realization satisfying the comparison-law hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Let $j\in\mathbb N$ have signature $(p,q)$ with $p,q\ge1$. For every $e\in\mathbb N$, $o\in\mathbb R$ and cover $X/K$ satisfying the good-cover hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) with parameters $e,o$, put $$r_j=p+q,\qquad d=|\Psi|\binom{r_j}{2},\qquad \Psi=\{\tau:E\hookrightarrow\mathbb C:\tau(r)=r_0\}.$$ Let $\lambda_{\tau,a}\in\mathbb Z$ for $\tau\in\Psi$ and $0\le a<r_j$, and suppose $$\lambda_{\tau,a}-\lambda_{\tau,a+1}\ge(d+3)^2+2r_j\qquad(\tau\in\Psi,\ 0\le a<r_j-1).$$ For every irreducible component $Z$ of $X$, there exists $$f\in S_Z(\lambda,0)\qquad\text{with}\qquad \operatorname{ev}_Z(f)\ne0.$$ Here $S_Z(\lambda,0)$ is the space of cusp rules supported on $Z$, and $\operatorname{ev}_Z$ evaluates such a rule at the generic eigenframe over $\Omega_Z$; both are defined in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)).
