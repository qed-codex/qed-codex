---
{
  "module": "src/Formalism/FlagUnipotentLattices/MinkowskiFactorialBounds/BlockMinorSumCounterexample.lean",
  "declarations": [
    "Formalism.HermitianLatticeCounting.P.block_minor_sum_explicit",
    "Formalism.HermitianLatticeCounting.P.iterated_sum_bound_holds"
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

## An explicit sum bound for integral block-end expressions

[Theorem ANT.0269](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticeCounting.P.block_minor_sum_explicit/)

Let $E$ be a totally complex number field, $f$ its number of infinite places, and $r\ge0$. For a composition $c=(s_1,\ldots,s_t)$ of $r+1$ into positive integers and $a=(a_1,\ldots,a_t)\in E^t$, put $$D_j(c,a)=\prod_{h=1}^j(-1)^{s_h(s_h-1)/2}a_h^{s_h},\qquad W(c,a)=\prod_{j=1}^t\prod_{v\mid\infty}(1+|D_j(c,a)|_v^2)^2.$$ For every finite set $S$ of such pairs $(c,a)$ with all $D_j(c,a)$ nonzero algebraic integers, $$\sum_{(c,a)\in S}\frac1{W(c,a)}\le 2^r\exp\left(\frac{r+1}{e}\right)16^{f(r+1)}.$$

## Coefficient bounds for iterated operator expansions

[Theorem ALG.0607](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticeCounting.P.iterated_sum_bound_holds/)

Let $V$ be a complex vector space, $P$ an abelian group, $j:P\to V$ a function, and $D_a\in\operatorname{End}_{\mathbb C}(V)$ for $a$ in a set $\Lambda$. Give each $a$ a weight $w(a)\in\mathbb N$. Let $N_1,N_\infty:P\to\mathbb N$ be subadditive and vanish at zero. Fix $\lambda\in P$, $\Gamma\ge0$, and integers $c_0,q_0\ge0$.

Suppose that, whenever $N_1(\mu-\lambda)+c_0\le q_0$, each $D_a j(\mu)$ has a finite expansion $$D_a j(\mu)=\sum_\nu b_\nu j(\mu+\nu),\qquad \sum_\nu|b_\nu|\le\Gamma^{w(a)},$$ with $N_1(\nu)\le w(a)$ and $N_\infty(\nu)\le1$ on its support. For every finite ordered list $a_1,\ldots,a_h$, put $W=\sum_iw(a_i)$. If $N_1(\mu-\lambda)+W+c_0\le q_0$, then $$D_{a_1}\cdots D_{a_h}j(\mu)=\sum_\nu b_\nu j(\mu+\nu)$$ for finitely supported coefficients with $$\sum_\nu|b_\nu|\le\Gamma^W,\qquad N_1(\nu)\le W,\qquad N_\infty(\nu)\le h$$ on their support.
