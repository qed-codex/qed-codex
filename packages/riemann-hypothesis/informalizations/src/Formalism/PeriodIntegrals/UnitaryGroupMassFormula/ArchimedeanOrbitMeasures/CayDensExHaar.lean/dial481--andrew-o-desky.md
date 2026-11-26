---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/CayDensExHaar.lean",
  "declarations": [
    "HcHDC.cayDensU"
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

## A continuous Haar density in Cayley coordinates

[Theorem REP.0631](https://andrewodesky.com/rh/lean/HcHDC.cayDensU/)

Let $G=U(P,Q)$, let $\mathfrak g=\{X:X^*J+JX=0\}$ for $J=\operatorname{diag}(1_P,-1_Q)$, and fix Haar measures $m$ on $G$ and $\lambda$ on the additive group $\mathfrak g$. Define $$C(D)=\{g\in G:g(2I-X)=2I+X\text{ for some }X\in D\},$$ and let $c(g)=2(g+I)^{-1}(g-I)$ if this matrix belongs to $\mathfrak g$, with $c(g)=0$ otherwise. There exist a measurable neighborhood $D$ of $0$ in $\mathfrak g$ and a measurable $f:\mathfrak g\to[0,\infty]$, continuous at $0$, such that $$0<f(0)<\infty,\qquad c_*\bigl(m|_{C(D)}\bigr)=f\,(\lambda|_D).$$
