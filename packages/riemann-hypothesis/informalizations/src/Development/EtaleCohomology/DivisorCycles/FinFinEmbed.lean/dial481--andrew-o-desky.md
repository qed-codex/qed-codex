---
{
  "module": "src/Development/EtaleCohomology/DivisorCycles/FinFinEmbed.lean",
  "declarations": [
    "LateralTheory.Fin.FinEmbed.intersectionNumber_baseChange"
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

## Splitting a semisimple representation into finitely many copies

[Theorem ALG.1226](https://andrewodesky.com/rh/lean/LateralTheory.Fin.FinEmbed.intersectionNumber_baseChange/)

Let $\Gamma$ be a group, $K$ a field, and $N,n\ge0$. Let $\rho:\Gamma\to\mathrm{GL}_N(K)$ and $r:\Gamma\to\mathrm{GL}_n(K)$ be semisimple representations. Suppose there are matrices $A\in\operatorname{Mat}_{N\times n}(K)$ and $B\in\operatorname{Mat}_{n\times N}(K)$ such that $BA=I_n$ and $\rho(g)A=Ar(g)$ for every $g$. Assume also that whenever $Z\in\operatorname{Mat}_N(K)$ satisfies $ZT=0$ for every matrix $T\in\operatorname{Mat}_{N\times n}(K)$ with $\rho(g)T=Tr(g)$ for every $g$, one has $Z=0$.

There are $k\ge0$ and matrices $T_j\in\operatorname{Mat}_{n\times N}(K)$, $T'_j\in\operatorname{Mat}_{N\times n}(K)$, for $1\le j\le k$, satisfying $$T_j\rho(g)=r(g)T_j,\qquad \rho(g)T'_j=T'_jr(g),\qquad \sum_{j=1}^kT'_jT_j=I_N.$$
