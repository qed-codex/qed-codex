---
{
  "module": "src/Formalism/LocalToGlobal/Divisibility/ConstantGeTwentyEight.lean",
  "declarations": [
    "Formalism.L2.DIV.height_chain_atR"
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
