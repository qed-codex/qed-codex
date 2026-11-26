---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FontaineFormalismOfRegular.lean",
  "declarations": [
    "GlobalTheory.RegularRing.dcrisExact"
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

## Exactness of crystalline invariants for regular period data

[Theorem PHT.0740](https://andrewodesky.com/rh/lean/GlobalTheory.RegularRing.dcrisExact/)

Let $G$ be a group, let $Q\subseteq K_0\subseteq K$ be fields with $K_0,K$ finite-dimensional over $Q$, and let $L/Q$ be a finite field extension. Fix the period datum described below, with crystalline ring $B$ an integral domain. Suppose $$b\ne0,\quad b\,g(b')=g(b)\,b'\ (g\in G)\quad\Longrightarrow\quad b'=cb\text{ for some }c\in K_0.$$ For an $L$-representation $V$ with compatible $Q$-scalars, put $$D(V)=(V\otimes_QB)^G,$$ and call $V$ crystalline when $\dim_LD(V)=[K_0:Q]\dim_LV$. If $$0\longrightarrow V_0\longrightarrow V_1\longrightarrow V_2\longrightarrow0$$ is an equivariant exact sequence of finite-dimensional crystalline $L$-representations, then the induced sequence $$0\longrightarrow D(V_0)\longrightarrow D(V_1)\longrightarrow D(V_2)\longrightarrow0$$ is exact.
