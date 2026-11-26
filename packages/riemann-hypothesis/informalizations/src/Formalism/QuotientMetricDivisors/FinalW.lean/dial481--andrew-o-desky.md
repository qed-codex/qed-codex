---
{
  "module": "src/Formalism/QuotientMetricDivisors/FinalW.lean",
  "declarations": [
    "Formalism.DivisionValues.divIntoDualShift",
    "Formalism.DivisionValues.height_constant_bound",
    "Formalism.DivisionValues.shiftEx",
    "Formalism.DivisionValues.shiftMu"
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

## Averaged height bound from mixed Hermitian identities

[Theorem ARAK.1741](https://andrewodesky.com/rh/lean/Formalism.DivisionValues.height_constant_first/)

A mixed Hermitian identity bounds the height of a factored pairing.

Let $K$ be a number field with a ring involution, and let $\Sigma=\Sigma_\infty(K)$. All vector spaces, subspaces and linear maps below are defined over $K$. Metrics and operator norms are taken on their scalar extensions along a chosen embedding $\sigma_w:K\hookrightarrow\mathbb C$ for each $w\in\Sigma$; duals carry dual norms. Let $E_0,\ldots,E_r,U,H_0,W$ be finite-dimensional $K$-spaces. Choose a $K$-basis of $U$ and a matrix $G\in M_{\dim U}(K)$ such that $\sigma_w(G)$ is Hermitian positive definite for every $w$, and give $U_w$ the Hermitian metric with Gram matrix $\sigma_w(G)$. Give a surjection $q:U\to H_0$ and give $H_{0,w}$ the quotient metric. Give $E_{i,w},W_w$ Hermitian metrics, and give a $K$-linear isomorphism $\Phi:H_0\to W$ and a nonzero $K$-linear map $B:E_0\to W^\vee$. Put $$h(B)=\frac1{|\Sigma|}\sum_{w\in\Sigma}\log\|B_w\|^2.$$ Let $\mathcal I$ be finite and nonempty and let $J$ be finite. Give $K$-subspaces $A_p\subset H_0$ with $\sum_{p\in\mathcal I}A_p=H_0$. Assume that $\kappa_w>0$ and that the real numbers $\lambda_{j,p,w},\lambda^-_{j,p,w}$ satisfy $0<\lambda^-_{j,p,w}\le\lambda_{j,p,w}$ and $$\langle\Phi_wz,\Phi_wy\rangle_w =\kappa_w\prod_{j\in J}\lambda_{j,p,w}\,\langle z,y\rangle_{0,w} \qquad(z\in A_{p,w},\ y\in H_{0,w}).$$ Give $K$-linear maps $K_i:E_i\to E_{i+1}$ for $0\le i<r$, $T:E_r\to U^\vee$, and arbitrary real bounds $p_w,k_{i,w}$ with $$\|T_w\|\le p_w,\qquad \|K_{i,w}\|\le k_{i,w}.$$ Require, for every $z\in E_0$ and $u\in U$, $$(Bz)(\Phi qu)=\bigl(TK_{r-1}\cdots K_0z\bigr)(u).$$ The composition is the identity when $r=0$. Define $$R_w=\log(p_w^2)+\sum_{i=0}^{r-1}\log(k_{i,w}^2)-\log\kappa_w-\min_{p\in\mathcal I}\sum_{j\in J}\log\lambda^-_{j,p,w}.$$ Then $$\log\|B_w\|^2\le R_w,\qquad h(B)\le\frac1{|\Sigma|}\sum_w\left(\log(p_w^2)+\sum_i\log(k_{i,w}^2)\right) -\frac1{|\Sigma|}\sum_w\min_p\sum_j\log\lambda^-_{j,p,w}-\bar\kappa,$$ where $\bar\kappa=|\Sigma|^{-1}\sum_w\log\kappa_w$.

In the exponential specialization, let $A,l_j,q_{j,w}\in\mathbb R$ and $\alpha:J\to\{0,\ldots,r-1\}$, and suppose $$\|T_w\|^2\le e^A,\qquad \|K_{i,w}\|^2\le\exp\left(\sum_{\alpha(j)=i}q_{j,w}\right),\qquad \log\lambda_{j,p,w}\ge l_j.$$ Put $$H_w=A+\sum_jq_{j,w}-\log\kappa_w-\min_p\sum_j\log\lambda_{j,p,w}.$$ Then $$\log\|B_w\|^2\le H_w,\qquad h(B)\le\frac1{|\Sigma|}\sum_wH_w \le A+\sum_j\frac1{|\Sigma|}\sum_wq_{j,w}-\sum_jl_j-\bar\kappa.$$

## Lattice shifts from local period divisibility

[Theorem ARAK.0179](https://andrewodesky.com/rh/lean/Formalism.DivisionValues.shiftEx/)

Let $K$ be a number field with an involution. At a finite place $v$, normalize $v$ to be $1$ on a uniformizer and put $\ell_v=\log\operatorname{Norm}(\mathfrak p_v)/[K:\mathbb Q]$. Let $N\subset K^d$ be a full $\mathcal O_K$-lattice and let $\tau_v\in\mathbb Z$ have finite support. Put $$I_\tau=\prod_v\mathfrak p_v^{-\tau_v},\qquad N'=I_\tau N.$$ Then $N'$ is a full lattice, and locally $N'_v=a_vN_v$ for every $a_v\in K^\times$ with $v(a_v)=-\tau_v$. It is the unique submodule with these localizations. If $K$ is totally complex, $d>0$, and both lattices carry the same Hermitian metrics, specified by invertible frames at infinity, then $$\mu(N')=\mu(N)+2\sum_v\ell_v\tau_v.$$

There is also the following integrality assertion, which does not require $K$ to be totally complex. Let $R\subset K^D$ be an $\mathcal O_K$-submodule and $B:K^d\times K^D\to K$ bilinear. At every finite place supply a module $M_v\subset K^{n_v}$, matrices $\pi_v:K^{n_v}\to K^D$ and $\iota_v:K^D\to K^D$, a bilinear pairing $P_v:K^d\times K^{n_v}\to K$, and $\zeta_v\in K^\times$ with $v(\zeta_v)=0$. Assume $$P_v(z,F)=\zeta_v B(z,\iota_v\pi_vF),\qquad R_v=(\iota_v\pi_vM_v)_v.$$ Let $\sigma_v\in\mathbb R$ satisfy $$P_v(z,F)=0\quad\text{or}\quad v(P_v(z,F))\ge\sigma_v\qquad(z\in N,\ F\in M_v).$$ If $\tau_v\le\lceil\sigma_v\rceil$ for every $v$, then $B(N',R)\subset\mathcal O_K$, equivalently $B(N')\subset R^\vee$. The same integrality conclusion holds for any $N,N'$ with the stated local shift relation, without lattice or finite-support assumptions on them.
