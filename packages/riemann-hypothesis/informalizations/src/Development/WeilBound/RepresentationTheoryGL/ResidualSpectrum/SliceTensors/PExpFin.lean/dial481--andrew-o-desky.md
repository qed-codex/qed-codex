---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/PExpFin.lean",
  "declarations": [
    "PositivityTheory.Rg.Rs.PExpFin.exists_kl"
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

## A polynomial recurrence for a finite-dimensional space of torus translates

[Theorem AGR.0356](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Rs.PExpFin.exists_kl/)

Let $E$ be a totally complex number field, $N,r\ge0$, and $s\in\mathbb R$. For $t\in\mathbb R$ let $a_r(t)\in\operatorname{GL}_N(\mathbb A_E)$ have finite component $1$ and, at every infinite place, diagonal entries $e^t$ in positions $i<r$ and $1$ in the other positions, with $0\le i<N$. Let $F:\operatorname{GL}_N(\mathbb A_E)\to\mathbb C$. If $$\operatorname{span}_{\mathbb C}\{g\mapsto F(a_r(t)g):t\in\mathbb R\}$$ is finite-dimensional, there is a monic $p(X)=\sum_{j=0}^d c_jX^j\in\mathbb C[X]$ such that $$\sum_{j=0}^dc_jF(a_r(sj)g)=0\qquad\bigl(g\in\operatorname{GL}_N(\mathbb A_E)\bigr).$$
