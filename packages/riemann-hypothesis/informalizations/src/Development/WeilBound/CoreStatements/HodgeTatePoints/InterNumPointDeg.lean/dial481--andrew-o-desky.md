---
{
  "module": "src/Development/WeilBound/CoreStatements/HodgeTatePoints/InterNumPointDeg.lean",
  "declarations": [
    "PositivityTheory.HtPt.Kra.finiteSections"
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

## Finiteness, graded generation, and generic base change for sections

[Theorem AG.1190](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Kra.finiteSections/)

Let $S$ be a commutative Noetherian ring, $\Omega$ an $S$-algebra that is a field, $N\ge0$, and $0\ne x\in\Omega^{N+1}$. For every nonempty subset $I\subset\{i:x_i\ne0\}$, let $R_I\subset\Omega$ consist of ratios $f(x)/m(x)$, where $m$ is a monomial in the variables indexed by $I$ and $f,m\in S[X_0,\ldots,X_N]$ are homogeneous of the same degree. For $c\in\mathbb Z$, let $T_I(c)$ be the $R_I$-span of the same ratios with $\deg f=\deg m+c$.

Suppose a line-bundle system is given by finitely generated invertible fractional ideals $L_I\subset\Omega$ of $R_I$ such that, whenever $I\subset J$, one has $L_I\subset L_J$ and $$y\in L_J\ \Longleftrightarrow\ \exists a\in R_I:\ a\text{ is a unit in }R_J\text{ and }ay\in L_I.$$ Set $H=\bigcap_I L_I$ and $H(c)=\bigcap_I L_IT_I(c)$, with products denoting the spans of products. Then $H$ is a finite $S$-module. For every $c_1\in\mathbb Z$, there are finitely many integers $d_j\ge c_1$ and $s_j\in H(d_j)$ such that for every $c\ge c_1$, $$H(c)\subset\operatorname{span}_S\{f(x)s_j:f\in S[X_0,\ldots,X_N]\text{ homogeneous of degree }e\ge0,\ e+d_j=c\}.$$ For every field $F$ that is a fraction ring of $S$, with compatible maps $S\to F\to\Omega$, let $R_{I,F}$ be the same chart rings with coefficients in $F$. Then $$\operatorname{span}_F H=\bigcap_I\operatorname{span}_{R_{I,F}}L_I.$$
