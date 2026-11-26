---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FiniteSemisimple.lean",
  "declarations": [
    "GlobalTheory.PsChar.exists_ssRep"
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

## Semisimple representations realizing pseudcharacters

[Theorem AGR.1510](https://andrewodesky.com/rh/lean/GlobalTheory.PsChar.exists_ssRep/)

Let $\Gamma$ be a group, $k$ an algebraically closed field of characteristic zero, and $d\ge0$. For $T:\Gamma\to k$, define multilinear trace expressions recursively by $$A_0(T)=1,$$ $$A_{n+1}(T;g_0,\ldots,g_n)=T(g_0)A_n(T;g_1,\ldots,g_n)-\sum_{i=1}^n A_n(T;g_1,\ldots,g_0g_i,\ldots,g_n).$$ Suppose $T(1)=d$, $T(xy)=T(yx)$ for every $x,y\in\Gamma$, and $A_{d+1}(T;g_0,\ldots,g_d)=0$ for every tuple. There is a semisimple representation $\rho:\Gamma\to\mathrm{GL}_d(k)$ with $$\operatorname{tr}\rho(g)=T(g)\qquad(g\in\Gamma).$$
