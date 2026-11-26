---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsOther.lean",
  "declarations": [
    "Formalism.L2.SG.RowsOther.kppDiag_of_pairs"
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

## A degenerate kernel bound from pair sums

[Theorem ALG.0146](https://andrewodesky.com/rh/lean/Formalism.L2.SG.RowsOther.kppDiag_of_pairs/)

Assume the universal Gram and summation package described below. Let $H,H_1$ be complex inner product spaces, with $H_1$ complete, let $I$ be finite, and let $T,R$ be sets. Supply families $a_t\in H$, $v_t\in H_1$, maps $r:T\to R$, $i:R\to I$, a matrix $B\in M_I(\mathbb C)$, $\gamma>0$, a function $G:T\to\mathbb R$, a predicate $J$ on $T$, and a function $s:T^2\to\mathbb N$. Assume $\sum_t\|a_t\|<\infty$ and $\sum_t\|v_t\|<\infty$. Put $$Z=\{t:G(t)=0,\ \neg J(t)\},\quad Q(Z)=\{(t,t')\in Z^2:r(t)=r(t')\},\quad V_j=\sum_{\substack{t\in Z\\i(r(t))=j}}v_t.$$ Let $P_g,d\in\mathbb R$, with $P_g\ge0$, and $k,f\in\mathbb N$. Suppose $$\left\|\sum_{t\in Z}a_t\right\|^2=\operatorname{Re}\sum_{j,j'\in I}B_{jj'}\langle V_j,V_{j'}\rangle,\qquad P_g\gamma I-B\text{ is positive semidefinite},$$ $$\langle v_t,v_{t'}\rangle=0\quad\text{if }i(r(t))=i(r(t'))\text{ and }r(t)\ne r(t'),$$ and $s(t,t')\ge1$ whenever $r(t)=r(t')$ and $G(t),G(t')\ne0$. If $$P_g\gamma\sum_{(t,t')\in Q(Z)}|\langle v_t,v_{t'}\rangle|\le d\exp(-kf\log k),$$ then $$\left\|\sum_{t\in Z}a_t\right\|^2\le d\exp(-kf\log k).$$
