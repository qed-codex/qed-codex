---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRationalPowerSeriesOfAdelicIntegralPositiveRad.lean",
  "declarations": [
    "GlobalTheory.RatCrit.isRat_of_adelic"
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

## A rationality criterion for power series over a function field

[Theorem AG.0908](https://andrewodesky.com/rh/lean/GlobalTheory.RatCrit.isRat_of_adelic/)

Let $k$ be an algebraically closed field of characteristic zero and $F/k$ a function field in one variable, finite over $k(t)$ for some transcendental $t$. Let $v$ run over all normalized discrete valuations of $F$ trivial on $k^\times$, with valuation rings $O_v$. Let $\phi\in F[[X]]$. Suppose there are $u_v\in F^\times$ and $e_v,\psi_v\in O_v[[X]]$ such that $$\{v:v(u_v)\ne0\}\text{ is finite},\qquad\sum_v v(u_v)>0,$$ $$e_v(0)\ne0\quad\text{for every }v,\qquad e_v(0)\in O_v^\times\quad\text{for all but finitely many }v,$$ and, after viewing their coefficients in $F$, $$e_v(u_vX)\phi(X)=\psi_v(u_vX)\qquad\text{for every }v.$$ Then there are $P,Q\in F[X]$ with $Q\ne0$ and $Q\phi=P$.
