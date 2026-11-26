---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsConjDoubleBlockOfIsoSubspaces.lean",
  "declarations": [
    "GlobalTheory.DoubleBlock.exists_conj_double"
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

## Two disjoint isomorphic subrepresentations give a repeated block

[Theorem REP.0576](https://andrewodesky.com/rh/lean/GlobalTheory.DoubleBlock.exists_conj_double/)

Let $k$ be a field, let $\Gamma$ be a group, and let $\rho:\Gamma\to\operatorname{GL}_a(k)$ be semisimple. Suppose $W_1,W_2\subseteq k^a$ are invariant subspaces with $$W_1\ne0,\qquad W_1\cap W_2=0,\qquad W_1\simeq W_2\quad\text{as }\Gamma\text{-modules}.$$ There are integers $d>0$, $u\ge0$ with $2d+u=a$, representations $\sigma:\Gamma\to\operatorname{GL}_d(k)$ and $\upsilon:\Gamma\to\operatorname{GL}_u(k)$, and a change of basis $P\in\operatorname{GL}_a(k)$ such that $$P^{-1}\rho(g)P=\operatorname{diag}(\sigma(g),\sigma(g),\upsilon(g))\qquad(g\in\Gamma).$$
