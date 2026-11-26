---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/GlobAut.lean",
  "declarations": [
    "Formalism.MainNotions.S.AutInst"
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

## Cusp projection and multiplicity data

[Definition / hypothesis AGR.D002](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.AutInst/)

Fix the arithmetic unitary-group datum described in the conventions. Let $G$ be the adelic unitary group of its CM extension $E/F$, let $G_\infty=\prod_{v\mid\infty}U(p_v,q_v)$ and $G_f$ be its archimedean and finite factors, and choose a sigma-finite measure $\mu_f$ on $G_f$ and any subset $\mathcal F\subset G(\mathbb A_F)$. Let $\mu_A$ be the product of fixed Haar measures on the groups $U(p_v,q_v)$ and $\mu_f$, and put $\mathscr H=L^2(G(\mathbb A_F),\mu_A|_{\mathcal F})$. Choose bounded complex-linear operators $R(g)$ on $\mathscr H$ for $g\in G(\mathbb A_F)$, complex inner-product spaces $H_v,H_\infty$, bounded complex-linear operators $\sigma_v(g)$ on $H_v$ for every $g\in M_n(\mathbb C)$, vectors $w_v\in H_v$, bounded complex-linear operators $\sigma_\infty(g)$ on $H_\infty$ for $g\in G_\infty$, a function $e:G_f\to\mathbb C$, and a bounded complex-linear operator $R_e$ on $\mathscr H$.

Let $d_v$ be the reciprocal matrix-coefficient integral $$d_v=\frac{\|w_v\|^4}{\int_{U(p_v,q_v)}|\langle w_v,\sigma_v(g)w_v\rangle|^2\,dg},\qquad\phi(g_\infty)=\left(\prod_vd_v\right)\overline{\prod_v\langle w_v,\sigma_v(g_v)w_v\rangle}.$$ Let $D_{\mathrm{mult}}$ be the natural-number dimension of the image of the map $A\mapsto R_e\circ A$ on the space of bounded intertwiners from $H_\infty$ to $\mathscr H$, with intertwining taken for $\sigma_\infty$ and the archimedean action $R$. This dimension is zero if the image is infinite-dimensional. Fix two propositions $A_1,A_2$. The *cusp-projection condition* is the conjunction of the following assertions:

1. If $A_1$ holds, then $\phi$ is integrable on $G_\infty$.
2. If $A_2$ holds and a bounded operator $T$ realizes right convolution by $(g_\infty,g_f)\mapsto\phi(g_\infty)e(g_f)$, then $T$ is an orthogonal projection, its range is finite dimensional, and $$\dim_{\mathbb C}\operatorname{im}T=D_{\mathrm{mult}}.$$ Item 2 also requires the following vanishing property. For every vector $f_0$ in the range of $T$, define its extension by $\widetilde f_0(g)=f_0(\gamma_g g)$ if some $\gamma_g\in G(F)$ has $\gamma_g g\in\mathcal F$, using the fixed choice of such an element, and by $\widetilde f_0(g)=f_0(g)$ otherwise.

For each nonzero totally isotropic $E$-subspace $W\subset E^n$, extend $W$ and $E^n$ by scalars to each adelic factor. Write $V$ for the resulting ambient space and $W^\perp$ for the orthogonal complement of the extended $W$ under the extended Hermitian form. Let $N_W\subseteq G$ consist of the elements whose matrices satisfy, at every factor, $$(g-1)W=0,\qquad(g-1)W^\perp\subseteq W,\qquad(g-1)V\subseteq W^\perp,$$ using the matrix $P_vg_vP_v^{-1}$ at an infinite place $v$. For every finite nonzero measure $\xi$ on $G$ with $\xi(G\setminus N_W)=0$ such that $$\int_G H(mn_0)\,d\xi(m)=\int_G H(m)\,d\xi(m)\qquad(n_0\in N_W)$$ for every function $H:G\to\mathbb C$ satisfying $H(\gamma y)=H(y)$ for all $\gamma\in G(F)\cap N_W$ and $y\in G$, one has $$\int_G\widetilde f_0(mx)\,d\xi(m)=0\qquad\text{for }\mu_A\text{-almost every }x.$$

The convolution kernel is required to be integrable against $\mu_A$, and convolution means equality of all weak matrix coefficients: $$\langle x,Ty\rangle=\int_G\phi(g_\infty)e(g_f)\langle x,R(g)y\rangle\,d\mu_A(g)\qquad(x,y\in\mathscr H).$$
