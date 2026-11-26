---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/BlockDeterminants/AbsNe.lean",
  "declarations": [
    "UpperTheory.TP.absNe"
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

## Nonvanishing from a dominant integration region

[Theorem ANT.1687](https://andrewodesky.com/rh/lean/UpperTheory.TP.absNe/)

Let $(A,\mu_A),(B,\mu_B),(C,\mu_C)$ be measurable spaces with measures that are countable sums of finite measures (the $s$-finite condition). Let $H\subset B$, $K\subset C$ be measurable with $0<\mu_B(H)<\infty$ and $\mu_C(K)<\infty$. Take functions $f:A\times B\times C\to\mathbb C$, $m:A\times C\to\mathbb C$, $s,c_0:C\to\mathbb C$, and $w:C\to[0,\infty]$, and constants $\kappa\ne0$, $r>0$. Assume $f$ is integrable for the product measure and $$f(x,b,c)=0\ (b\notin H),\quad f(x,b,c)=s(c)m(x,c)\ (b\in H),\quad \int_A m(x,c)\,d\mu_A(x)=\kappa c_0(c).$$ Assume also $$s(c)=1,\ c_0(c)=r\quad(c\in K),\qquad |c_0(c)|\le r,\quad |s(c)|\le w(c)\quad(c\in C),$$ where the last inequality uses the extended nonnegative norm. If $$\int_{C\setminus K}w\,d\mu_C<\mu_C(K),$$ then $\int_{A\times B\times C}f\,d(\mu_A\times\mu_B\times\mu_C)\ne0$.
