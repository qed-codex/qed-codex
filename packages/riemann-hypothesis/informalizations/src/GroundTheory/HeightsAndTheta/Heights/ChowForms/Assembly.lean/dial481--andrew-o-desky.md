---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ChowForms/Assembly.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.ChowFormBirational.full",
    "GroundTheory.Heights₂.Heights.LengthQuotientDet.full"
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

## Generic-point ratios from derivatives of a Chow form

[Theorem AG.1380](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ChowFormBirational.full/)

Let $F$ be a field of characteristic zero, $n,k\ge0$, and $P\subset F[X_1,\ldots,X_n]$ a relevant homogeneous prime. Put $K=\operatorname{Frac}(F[X]/P)$ and let $\eta_j\in K$ be the image of $X_j$. Let $g\in F[U_{ij}:0\le i\le k,1\le j\le n]$ be a Chow form for $P$ with $k+1$ hyperplane blocks. Choose $c_1,\ldots,c_n\in K$ with $\sum_j c_j\eta_j=1$.

Let $\mathcal I$ be the incidence ideal of tuples of $k+1$ hyperplanes meeting $V(P)$, and let $\mathcal S$ be the substitution $$U_{ij}\longmapsto U_{ij}-\left(\sum_lU_{il}\eta_l\right)c_j.$$ Write $h_j=\mathcal S(\partial g/\partial U_{0j})$. There is $t=(t_j)\in F^n$ such that $$\sum_jt_j\frac{\partial g}{\partial U_{0j}}\notin\mathcal I,$$ and for every $m$, $$h_m\left(\sum_lt_l\eta_l\right)=\left(\sum_lt_lh_l\right)\eta_m\quad\text{in }K[U_{ij}].$$

## Cokernel length over a discrete valuation ring

[Theorem ALG.1417](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.LengthQuotientDet.full/)

Let $O$ be a commutative discrete valuation domain, $M$ a finite free $O$-module, and $\varphi:M\to M$ an $O$-linear endomorphism with $\det\varphi\ne0$. With $v_O$ the valuation normalized by $v_O(\varpi)=1$ for a uniformizer $\varpi$, $$\operatorname{length}_O(M/\varphi M)=v_O(\det\varphi).$$
