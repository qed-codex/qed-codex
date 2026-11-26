---
{
  "module": "src/CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/CoefWeightedLocHolds.lean",
  "declarations": [
    "Formalism.L2.SG.Closed.BM.BesselNVGap_holds",
    "Formalism.L2.SG.Closed.BM.CoefWeightedLoc_holds",
    "Formalism.L2.SG.Closed.BM.WlocExists_holds"
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

## A normalized Bessel function with weighted integrability and reproducing convolutions

[Theorem REP.1643](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.WlocExists_holds/)

Assume ([Nonvanishing of a Bessel integral of translated lowest-type vectors](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.BesselNVGap_holds/)) and ([Weighted integrability of a lowest compact-type coefficient](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.CoefWeightedLoc_holds/)). Fix $(k,r,z,c,u,v,b)$ satisfying the real-place numerical conditions of ([Nonvanishing of a Bessel integral of translated lowest-type vectors](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.BesselNVGap_holds/)), and put $n=2r+k+1$. This includes positive even $k$, the permitted nondegenerate Bessel parameters $z$, nonzero character coefficients $c$, integral strictly decreasing Harish–Chandra parameters $u,\lambda=(v,-b)$, their interlacing and half-integral differences, and the specified large adjacent gaps in $b$. Write $G=U(H_{k,r})$ for the package's real unitary group, $U_z$ for its compact Bessel subgroup, $N$ for its unipotent subgroup, $S_z=U_zN$ for the subgroup used in its quotient measure and height, and $\psi_{z,c}$ for its unipotent character.

Let $\sigma$ be a discrete-series representation satisfying the conditions of ([Nonvanishing of a Bessel integral of translated lowest-type vectors](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.BesselNVGap_holds/)) on a complex Hilbert space $H$ with this parameter, let $\pi$ be its prescribed finite-dimensional unitary Bessel type on $V$, and let $w$ be a unit lowest vector of $\sigma$. Choose Haar measures $\mu_G,\mu_S$ on $G,S_z$ and a quotient measure $\nu$ satisfying $$\int_G f(g)\,d\mu_G(g)=\int\!\int_{S_z}f(sx)\,d\mu_S(s)\,d\nu(x)$$ for nonnegative measurable $f$. Set $$d_\sigma=\frac{\|w\|^4}{\int_G|\langle w,\sigma(g)w\rangle|^2d\mu_G(g)},\quad e(g)=d_\sigma\overline{\langle w,\sigma(g)w\rangle},\quad a=4n^2\sqrt{2(r+1)}.$$ Let $h_z(x)=\inf_{s\in S_z}\|sx\|_{\mathrm{op}}$. There is a function $W$ into $V$, continuous on $G$, with $$W(hmg)=\psi_{z,c}(m)\pi(h)W(g)\quad(h\in U_z,\ m\in N,\ g\in G),$$ $$\int\|W(x)\|\,d\nu(x)<\infty,\qquad\int\|W(x)\|^2d\nu(x)=1,\qquad\int\|W(x)\|h_z(x)^a d\nu(x)<\infty.$$ For every $x\in G$, $g\mapsto e(g)W(xg)$ is integrable and $$\int_G e(g)W(xg)\,d\mu_G(g)=W(x).$$ There are also a compact $\Omega\subseteq G$ containing $1$, a measurable scalar function $\alpha$ supported in $\Omega$, and $A\in\mathbb R$ with $|\alpha|\le A$, such that $g\mapsto\alpha(g)W(xg)$ is integrable and $\int_G\alpha(g)W(xg)\,d\mu_G(g)=W(x)$ for every $x\in G$.

## Weighted integrability of a lowest compact-type coefficient

[Theorem REP.1563](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.CoefWeightedLoc_holds/)

Let $k,r\ge0$, $N=2r+k+1$, $a=\max\{k-1,0\}$, $v_0,\ldots,v_{a-1}\in\mathbb R$ and $b_0,\ldots,b_{2r+1}\in\mathbb R$. For $0\le i<N$, define $$\lambda_i=\begin{cases}v_i&i<a,\\-b_{i-a}&i\ge a.\end{cases}$$ Give the first $a$ positions positive sign and the remaining positions alternating signs starting with positive. Assume $\lambda$ is strictly decreasing with $\lambda_i-(N-1)/2\in\mathbb Z$. Suppose there is an odd integer $t\ge0$ with $$N+5\le t,\qquad1801\le N+t,$$ $$b_{j+1}-b_j>2\bigl(N+(2r+2)t\bigr)^3+t+3\qquad(0\le j<2r+1).$$ Let $\sigma$ satisfy the discrete-series conditions of ([Discrete series with a prescribed minimal compact type](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.G2.discrete_series_exists_large_gap/)) with this signature and parameter, and let $w$ be a unit vector in its lowest compact-type subspace. On the corresponding unitary group, with its fixed Haar measure $dg$, $$\int |\langle w,\sigma(g)w\rangle|\,\|g\|_{\mathrm{op}}^{4N^2\sqrt{2(r+1)}}\,dg<\infty.$$ The matrix operator norm is taken for the usual Euclidean norm on $\mathbb C^N$.

## Nonvanishing of a Bessel integral of translated lowest-type vectors

[Theorem REP.1570](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.BM.BesselNVGap_holds/)

Let $k\ge2$ be even, $r\ge0$, and $N=2r+k+1$. Give $\mathbb C^N$ a Hermitian form $H$ with hyperbolic pairs $(e_a,f_a)$, $0\le a<r$, and middle block $W$ of form $\operatorname{diag}(1_k,-1)$. Put $G=U(H)$, choose $z\in W$ with $H(z,z)<0$, and choose $c_a\in\mathbb C^\times$. Let $u\in\mathbb R^k$, $v\in\mathbb R^{k-1}$ and $b\in\mathbb R^{2r+2}$, and put $\lambda=(v_0,\ldots,v_{k-2},-b_0,\ldots,-b_{2r+1})$. Assume $u$ and $\lambda$ are strictly decreasing and, in their respective ranks $d$, have entries in $(d-1)/2+\mathbb Z$. Suppose $$u_i>v_i>u_{i+1}\ (0\le i<k-1),\qquad u_{k-1}>-b_0,\qquad u_i-\lambda_j\in\mathbb Z+\tfrac12.$$ Assume there is an odd integer $t$ with $N+5\le t$, $1801\le N+t$, and $$b_{j+1}-b_j>2(N+(2r+2)t)^3+t+3\quad(0\le j<2r+1).$$ Let $\epsilon$ have its first $k-1$ signs positive, followed by alternating signs beginning with positive. Let $\sigma$ on a complex Hilbert space satisfy the discrete-series conditions at $(\epsilon,\lambda)$ specified in the conventions below after a unitary Cayley identification with $H$, and let $w$ be a unit vector in a lowest compact-type subspace under such an identification.

Let $H_z\simeq U(k)$ fix $z$ and all $e_a,f_a$, and let $\pi$ satisfy the finite-dimensional compact-type conditions of parameter $u$ on this group specified in the conventions below. Let $N_r$ be the unitary unipotent subgroup for the ordered isotropic flag $\langle e_0,\ldots,e_{r-1}\rangle$, acting trivially on its successive quotients and on $\langle e_a\rangle^\perp/\langle e_a\rangle$. Define $$\psi_{z,c}(n)=\exp\!\left(i\Re\left(\sum_{a<r-1}c_a n_{e_a,e_{a+1}}+c_{r-1}(nz)_{e_{r-1}}\right)\right),$$ with empty sum and character $1$ when $r=0$. Let $\mu_H,\mu_N$ be nonzero sigma-finite Borel measures on the matrix space supported on $H_z,N_r$, respectively, and invariant under all left translations from those subgroups. There exist $x,x_0\in G$ such that the operator-valued integral $$\int_{H_z\times N_r}\langle\sigma(x_0)w,\sigma(hn)\sigma(x)w\rangle\,\overline{\psi_{z,c}(n)}\,\pi(h)^{-1}\,d(\mu_H\times\mu_N)(h,n)$$ is nonzero.
