---
{
  "module": "src/CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/MultiplicityOneUnitaryBranchingOfGapHyp.lean",
  "declarations": [
    "CompanionTheory.Lime.BM.uniqGap_holds"
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

## Multiplicity one for smooth Bessel maps with a weight gap

[Theorem REP.1670](https://andrewodesky.com/rh/lean/CompanionTheory.Lime.BM.uniqGap_holds/)

Let $k\ge1$, $r\ge0$, and $N=2r+k+1$. Give $\mathbb C^N$ the Hermitian form consisting of $r$ hyperbolic planes and a middle block $\operatorname{diag}(1_k,-1)$, and write $G$ for its unitary group. Let $\epsilon\in\{+,-\}^N$ and $\lambda\in\mathbb R^N$ satisfy $$\lambda_1>\cdots>\lambda_N,\qquad \lambda_i-(N-1)/2\in\mathbb Z,$$ $$|\lambda_i-\lambda_j|\ge h\quad(\epsilon_i\ne\epsilon_j),\qquad h\ge120N^3.$$ Let $\sigma$ satisfy the discrete-series conditions of ([Discrete series with a prescribed minimal compact type](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.G2.discrete_series_exists_large_gap/)) for $(\epsilon,\lambda)$, including a unitary Cayley identification with the displayed form and the specified minimal compact type. Choose $z$ in the middle block with negative Hermitian norm, nonzero parameters $c_1,\ldots,c_r\in\mathbb C$, and $u\in\mathbb R^k$. Let $\pi$ satisfy the source's finite-dimensional unitary compact-type package of parameter $u$ on the $U(k)$ acting on the orthogonal complement of $z$ in that block.

Let $N_r$ be the prescribed unipotent subgroup associated to the $r$ hyperbolic planes and $\psi_{z,c}$ its prescribed Bessel character. Suppose $B_1,B_2$ are complex-linear on $\sigma^\infty$, equivariant in the form $$B_i(\sigma(hn)v)=\psi_{z,c}(n)\pi(h)B_i(v)\qquad(h\in U(k),\ n\in N_r),$$ and each is bounded by a finite sum of norms of Lie derivatives of $v$. There are $a,b\in\mathbb C$, not both zero, such that $$aB_1(v)+bB_2(v)=0\qquad(v\in\sigma^\infty).$$
