---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/SkewAnalyticGroup/Analytic.lean",
  "declarations": [
    "QnRdSkewW.skew_reduction_analytic"
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

## Integration by parts along a measure-preserving matrix flow

[Theorem REP.0695](https://andrewodesky.com/rh/lean/QnRdSkewW.skew_reduction_analytic/)

Let $G\subset M_n(\mathbb C)$ be closed, $X\in M_n(\mathbb C)$, and assume $g\exp(tX)\in G$ for every $g\in G$, $t\in\mathbb R$. Let $\mu$ be a Borel measure on the matrix space, concentrated on $G$, finite on compact sets, and invariant under $g\mapsto g\exp(tX)$ for every real $t$. Suppose $f_1,f_2:M_n(\mathbb C)\to\mathbb C$ are locally restrictions to $G$ of smooth functions on the matrix space, and each vanishes on $G$ outside some compact subset of the matrix space. Writing $$D_Xf(g)=\left.\frac d{dt}f(g\exp(tX))\right|_{t=0},$$ one has $$\int D_Xf_1(g)\,\overline{f_2(g)}\,d\mu(g) =-\int f_1(g)\,\overline{D_Xf_2(g)}\,d\mu(g).$$
