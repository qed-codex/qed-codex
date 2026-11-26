---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsEverywhereNormDivOfEtaProdEqOne.lean",
  "declarations": [
    "GlobalTheory.QuadSymbol.exists_everywhereNorm_div_of_etaProd_eq_one"
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

## A global scalar realizing prescribed local norm classes

[Theorem ANT.1353](https://andrewodesky.com/rh/lean/GlobalTheory.QuadSymbol.exists_everywhereNorm_div_of_etaProd_eq_one/)

Let $L/K$ be a quadratic extension of number fields. For every finite place $v$ choose $x_v\in K_v^{\times}$, and for every infinite place $w$ choose $y_w\in K_w^{\times}$. Let $N_v$ and $N_w$ be the norm subgroups of $(K_v\otimes_K L)^{\times}$ and $(K_w\otimes_K L)^{\times}$. Define $\eta_v(t)=1$ on $N_v$ and $-1$ off $N_v$, and similarly at infinity.

Suppose $x_v\in N_v$ for all but finitely many $v$ and $$\prod_{v\text{ finite}}\eta_v(x_v)\prod_{w\mid\infty}\eta_w(y_w)=1.$$ There is $t\in K^{\times}$ such that $$x_v/t\in N_v\quad\text{for every finite }v,\qquad y_w/t\in N_w\quad\text{for every infinite }w.$$
