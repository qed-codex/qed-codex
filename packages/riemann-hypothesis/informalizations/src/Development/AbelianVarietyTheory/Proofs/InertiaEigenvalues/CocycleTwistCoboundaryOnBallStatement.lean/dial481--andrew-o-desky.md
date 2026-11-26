---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CocycleTwistCoboundaryOnBallStatement.lean",
  "declarations": [
    "GlobalTheory.T.cocycle_twist_coboundary_on_ball"
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

## An explicit annihilator for torsion integral cyclotomic cocycles

[Theorem PHT.0764](https://andrewodesky.com/rh/lean/GlobalTheory.Cyc.FrameTorsion.torsion_killed/)

Let $\ell$ be prime, let $K\subset\overline{\mathbb Q}_\ell$ be finite over $\mathbb Q_\ell$, and let $K_0$ be its maximal unramified subfield. Put $$K_m=K_0(\mu_{\ell^m}),\quad K_\infty=\bigcup_mK_m,\quad G_m=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K_m),\quad H_\infty=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K_\infty).$$ Let $m\ge1$, with $m\ge2$ if $\ell=2$, and choose a norm-preserving extension of the natural Galois action to $\mathbb C_\ell$. Write $\chi$ for the cyclotomic character. Let $U:G_{\mathbb Q_\ell}\to M_r(\mathbb C_\ell)$ and $g\in G_m$ satisfy the frame conditions below.

For $i\in\mathbb Z$, define $\sigma*_iy=\chi(\sigma)^iU(\sigma)\sigma(y)$ on $\mathbb C_\ell^r$, and let $B=\mathcal O_{\mathbb C_\ell}^r$. Let $J\subset\mathbb Z$ be finite. Suppose there are linearly independent $e_1,\ldots,e_r\in\mathbb C_\ell^r$ and weights $u_a\in J$ with $\sigma*_{u_a}e_a=e_a$ for $\sigma\in G_m$.

Let $c:G_{\mathbb Q_\ell}\to\mathbb C_\ell^r$ restrict to a continuous $B$-valued cocycle on $G_m$ for $*_i$. If $\ell^kc$ is a coboundary with a primitive in $B$ for some $k\ge0$, then so is $\ell^{b_i}c$, where $$b_i=1+\max\left(1,\sum_{u\in J\setminus\{i\}}\bigl(m+v_\ell(u-i)\bigr)\right).$$
