---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/PolynomialDerivatives/MapDomainFlpFlp.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.LC.fockBasic"
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

## A polynomial transform intertwining multiplication with creation operators

[Theorem REP.0447](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.LC.fockBasic/)

Let $m,n\ge0$ and $c>0$, and put $\mathcal P=\mathbb C[x_{ai},y_{ai}:1\le a\le m,\ 1\le i\le n]$. Define commuting operators $$C_{ai}^x=-\partial_{x_{ai}}+2cy_{ai},\qquad C_{ai}^y=-\partial_{y_{ai}}+2cx_{ai}.$$ Define $\mathcal F_c$ linearly on monomials by $$\mathcal F_c(x^\alpha y^\beta)=\left(\prod_{a,i}(C_{ai}^x)^{\alpha_{ai}}(C_{ai}^y)^{\beta_{ai}}\right)1.$$ Then $\mathcal F_c:\mathcal P\to\mathcal P$ is a complex-linear bijection, and for every $P\in\mathcal P$, $$\mathcal F_c(x_{ai}P)=C_{ai}^x\mathcal F_c(P),\qquad\mathcal F_c(y_{ai}P)=C_{ai}^y\mathcal F_c(P).$$
