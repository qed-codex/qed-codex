---
{
  "module": "src/CompanionTheory/AutomorphicTheory/PieriRules/InfinitesimalCharacterDiscreteSeries.lean",
  "declarations": [
    "CompanionTheory.PieriExpansion.rank_one_pieri"
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

## Rank one factorization of a Bessel coefficient integral

[Theorem REP.1456](https://andrewodesky.com/rh/lean/CompanionTheory.PieriExpansion.rank_one_pieri/)

Let $k,r\ge0$, $d=2r+k+1$, and let $H_{k,r}$ be the Hermitian form with $r$ hyperbolic planes and a middle block $\operatorname{diag}(1_k,-1)$. Let $\epsilon\in\{+,-\}^d$, $\lambda_1>\cdots>\lambda_d$ with $\lambda_i-(d-1)/2\in\mathbb Z$, and let $\sigma$ on a complex inner product space $H$ satisfy the discrete-series package of ([Decay of matrix coefficients on the lowest compact type](https://andrewodesky.com/rh/lean/CompanionTheory.FamilyDerivativeExpansion.DecS.decay_low_range/)) for $(\epsilon,\lambda)$ after its unitary Cayley identification with $H_{k,r}$. Suppose some $h\in\mathbb R$ satisfies the opposite-sign weight gap $|\lambda_i-\lambda_j|\ge h$ when $\epsilon_i\ne\epsilon_j$ and the following bounds. Put $$a=\frac{h}{8\sqrt{2(r+1)}},\quad A_G=4(k+r)(r+1),\quad A_S=(2r+k)\bigl(r(r-1)+2r(k+1)+r^2\bigr),\quad M=2(r^2+r+1).$$ Require $k\ge1$, $h\ge120d^3$, $$2M(A_S+A_G)+A_G+3\le a,\qquad9(r+1)d^2+3A_G+3\le a.$$

Let $z$ lie in the middle block with negative Hermitian norm, let $u\in\mathbb R^k$, and let $\pi$ on a finite-dimensional complex Hilbert space $W$ satisfy the source's compact-type package of parameter $u$ on the subgroup $U(k)$ fixing $z$ and the hyperbolic basis. Write $N_r$ for the unipotent subgroup associated to the isotropic flag and $\psi_z(n)=\exp(2i\operatorname{Im}\ell_z(n))$, where $\ell_z(n)$ is the sum of successive upper flag entries and the last flag coordinate of $nz$ (the empty sum is zero). Let $\mu_W,\mu_N$ be nonzero sigma-finite measures on the ambient matrix space, supported on these respective subgroups and invariant under their left translations.

There exists a map $L:H\to W$ such that for every pair of smooth vectors $w,v$, the operator-valued integrand below is integrable and $$\int_{U(k)\times N_r}\langle v,\sigma(hn)w\rangle\overline{\psi_z(n)}\,\pi(h)^{-1}\,d\mu_W(h)d\mu_N(n) =\bigl[x\mapsto\langle Lv,x\rangle Lw\bigr].$$
