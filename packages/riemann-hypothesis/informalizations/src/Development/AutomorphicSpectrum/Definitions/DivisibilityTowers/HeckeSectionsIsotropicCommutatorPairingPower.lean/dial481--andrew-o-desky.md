---
{
  "module": "src/Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Top.RootTower.MeanSlope",
    "GlobalTheory.CompanionTheory.Ar.Top.RootTower.T1",
    "GlobalTheory.CompanionTheory.Ar.Top.RootTower.T2",
    "GlobalTheory.CompanionTheory.Ar.Top.RootTower.ThmB"
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

## Root towers, their volumes and their slopes

[Definition / hypothesis ARAK.D260](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.RootModel/)

This page defines root models and root towers, the two real functionals that each root model carries, and the six conditions on a tower that are named *proportionality*, *equal volumes*, the *limit condition*, the *monomial expansion*, the *intersection lower bound* and the *mean slope lower bound*. It uses the coordinate systems, arithmetic varieties, Hermitian line data, geometric degrees $d_n$, logarithmic intersection integrals $\mathcal I_P$ and intersection systems of ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)).

Throughout, $\Psi$ is a finite set, $N\ge0$ is an integer, and $$d=|\Psi|\,\frac{N(N-1)}2 .$$

**Weights and polynomials.** A *weight* is a real array $u=(u_{\tau,i})$ with $\tau\in\Psi$ and $0\le i<N$; it is *rational* if all its entries are rational. Put $$\|u\|_1=\sum_{\tau,i}|u_{\tau,i}|,\qquad \|u\|_\infty=\max_{\tau,i}|u_{\tau,i}|,\qquad \operatorname{spr}(u)=\sum_{\tau}\Bigl(\max_i u_{\tau,i}-\min_i u_{\tau,i}\Bigr).$$ Let $\mathcal R=\mathbb R[X_{\tau,i}:\tau\in\Psi,\ 0\le i<N]$ and $\mathcal R_0=\mathcal R[X_0]$, with one further variable $X_0$. For a weight $u$ and a real number $s$ put $$\ell_u=-\sum_{\tau,i}u_{\tau,i}X_{\tau,i}\in\mathcal R,\qquad \ell_{u,s}=\ell_u+sX_0\in\mathcal R_0 .$$ The *flag degree* is the linear functional $\mathcal D:\mathcal R\to\mathbb R$ given by $$\mathcal D(F)=(-1)^d\sum_{w\in(S_N)^\Psi}\Bigl(\prod_{\tau}\operatorname{sgn}w_\tau\Bigr)\,\bigl[\textstyle\prod_{\tau,i}X_{\tau,i}^{\,N-1-w_\tau(i)}\bigr]F,$$ where $[m]F$ is the coefficient of the monomial $m$ in $F$ and $S_N$ is the group of permutations of $\{0,\dots,N-1\}$. Put $D(u)=\mathcal D(\ell_u^{\,d})$. For an integer $j$ and $\tau\in\Psi$, two further linear functionals on $\mathcal R$ are $$\operatorname{Sh}_{j,\tau}(F)=\mathcal D\Bigl(\sum_{0\le i<j}\frac{\partial F}{\partial X_{\tau,i}}\Bigr),\qquad \operatorname{Tot}_\tau(F)=\mathcal D\Bigl(\sum_{0\le i<N}\frac{\partial F}{\partial X_{\tau,i}}\Bigr).$$

**Root models.** A *root model* for $(\Psi,N)$ consists of the following data.

- A coordinate system with finite block set $K$ and finite coordinate sets $I_k$, a field $\Omega$ and a tuple $y\in\Omega^{J}$, $J=\coprod_kI_k$, whose homogeneous coordinate ideal $P=P_y$ is an arithmetic variety of dimension $d+1$. Every element of $\Omega$ is a quotient $g(y)/h(y)$ of two integral polynomials that are multihomogeneous of the same multidegree, with $h(y)\ne0$.
- For every real $t$ and every pair $(\tau,i)$, a smooth Hermitian line datum $L_{\tau,i}(t)$ whose multidegree does not depend on $t$; a smooth Hermitian line datum $A$; and integers $k_A\ge1$ and $\delta\ge1$. The metric functions of all these line data are invariant under complex conjugation of the coordinates.

The variable $X_{\tau,i}$ stands for the line $L_{\tau,i}(t)$ and $X_0$ for $A$. A monomial $m$ of $\mathcal R_0$ of degree $n$ thus determines a list of $n$ line data at time $t$: each variable is repeated as often as its exponent, in an order that depends only on $m$. Write $m_0$ for the exponent of $X_0$ in $m$.

Let $I$ be an intersection system. The *arithmetic functional at time $t$* is the linear map $\mathcal A^{(t)}:\mathcal R_0\to\mathbb R$ with $$\mathcal A^{(t)}(m)=\frac{I_P\bigl(\text{the lines of }m\text{ at time }t\bigr)}{\delta\,k_A^{\,m_0}}\quad(\deg m=d+1),\qquad \mathcal A^{(t)}(m)=0\quad(\deg m\ne d+1).$$ The *limit functional* $\mathcal P:\mathcal R_0\to\mathbb R$ is the linear map with $\mathcal P(m)=\lim_{t\to0^+}\mathcal A^{(t)}(m)$ on monomials. The *geometric functional* is the linear map $\mathcal G:\mathcal R_0\to\mathbb R$ with $$\mathcal G(m)=\frac{\mathcal I_P\bigl(\text{the lines of }m\text{ at time }1;\,1\bigr)}{\delta\,k_A^{\,m_0}}\quad(\deg m=d),\qquad \mathcal G(m)=0\quad(\deg m\ne d),$$ where the last argument of $\mathcal I_P$ is the constant function $1$.

For a weight $u$ and a real $s$, the *real combination* $(u,s)$ gives the coefficient $-u_{\tau,i}$ to $L_{\tau,i}(t)$ and $s/k_A$ to $A$. Two positivity conditions refer to it.

- It is *nef on the fibres* if, for every prime number $p$ and every relevant multihomogeneous prime ideal $W\supseteq P$ with $W\cap\mathbb Z=(p)$ and $\dim(R/W)=1+|K|$, $$-\sum_{\tau,i}u_{\tau,i}\,d_1(W;a_{\tau,i})+\frac{s}{k_A}\,d_1(W;a_A)\ \ge 0,$$ where $R$ is the integral polynomial ring of the coordinate system and $a_{\tau,i}$, $a_A$ are the multidegrees of $L_{\tau,i}$ and $A$.
- It is *semipositive at time $t$* if the function $$\varphi_t=-\sum_{\tau,i}u_{\tau,i}\log h_{\tau,i}^{(t)}+\frac{s}{k_A}\log h_A$$ on $\mathbb C^J$, where $h^{(t)}_{\tau,i}$ and $h_A$ are the metric functions of $L_{\tau,i}(t)$ and $A$, has nonnegative Levi form $$\tfrac14\bigl(D^2\varphi_t(z)(w,w)+D^2\varphi_t(z)(iw,iw)\bigr)\ \ge 0$$ at every point $z$ of the complex cone $\mathcal C_P$ and every $w\in\mathbb C^J$ with $\sum_{x\in J}\frac{\partial f}{\partial z_x}(z)\,w_x=0$ for all $f\in P$. Here $D^2\varphi_t$ is the second real derivative.

**Root towers.** A *root tower* $T$ for $(\Psi,N)$ consists of an integer $j$ with $1\le j<N$; a finite nonempty set $\mathcal C$ of *components*; a finite set $S_0$ of natural numbers containing $2$; a rational weight $\nu$; and a root model $M_{B,c}$ for every natural number $B$ and every $c\in\mathcal C$. Fix an intersection system $I$, and write $\mathcal A^{(t)}_{B,c}$, $\mathcal P_{B,c}$, $\mathcal G_{B,c}$ for the three functionals of $M_{B,c}$. Let $\varrho$ be the weight $\varrho_{\tau,i}=N-1-i$. Define $$v_c=\frac{\mathcal G_{2,c}(\ell_\varrho^{\,d})}{D(\varrho)},\qquad V=\sum_{c\in\mathcal C}v_c,\qquad P_{B,c}(F)=\mathcal P_{B,c}(F),\qquad P_B(F)=\sum_{c\in\mathcal C}P_{B,c}(F)\qquad(F\in\mathcal R),$$ $$\mu_{B,c}(u)=\frac{P_{B,c}(\ell_u^{\,d+1})}{(d+1)\,v_c\,D(u)} .$$ The number $v_c$ is the *volume* of the component $c$, and $\mu_{B,c}(u)$ is its *slope* at level $B$ in the direction $u$.

*Proportionality.* The tower is *proportional* if $v_c>0$ for every $c$; $\mathcal G_{B,c}(F)=v_c\,\mathcal D(F)$ for all $B$, $c$ and all $F\in\mathcal R$; and $\mathcal G_{B,c}=\mathcal G_{B',c}$ on $\mathcal R_0$ for all $B,B'$ and $c$.

*Equal volumes.* The tower has *equal volumes* if $v_c=v_{c'}$ for all $c,c'\in\mathcal C$.

*Admissible directions.* A pair $(u,g)$ of a weight and a real number is *admissible* if $g>0$; each row of $u$ is strictly decreasing, $u_{\tau,0}>u_{\tau,1}>\dots>u_{\tau,N-1}$; $u_{\tau,j-1}-u_{\tau,j}\ge g$ for every $\tau$; and $|u_{\tau,a}-u_{\tau,b}|\ge g$ for every $\tau$ and all $a\ne b$ with $a$ in the smaller block, which is $\{0,\dots,j-1\}$ if $j\le N-j$ and $\{j,\dots,N-1\}$ otherwise. For such a pair put $$B_0(u,g)=4\,|\Psi|\,N^2\Bigl(1+\frac{\|u\|_\infty}{g}\Bigr).$$

*The limit condition.* For $s>0$ put $u_s=u-s\nu$ and $t(s)=\exp(-1/s^2)$. The tower satisfies the *limit condition* for $I$ if, for every admissible $(u,g)$, every natural number $B$ with $B_0(u,g)<B+1$ and every $c\in\mathcal C$, the following four statements hold in the root model $M_{B,c}$:

1. for all sufficiently small $s>0$, the real combination $(u_s,s)$ is nef on the fibres and semipositive at time $t(s)$;
2. $\mathcal A^{(t(s))}_{B,c}\bigl(\ell_{u_s,s}^{\,d+1}\bigr)\to P_{B,c}(\ell_u^{\,d+1})$ as $s\to0^+$;
3. $\mathcal G_{B,c}\bigl(\ell_{u_s,s}^{\,d}\bigr)\to v_c\,D(u)$ as $s\to0^+$, and $v_c\,D(u)>0$;
4. $\dfrac{\mathcal A^{(t(s))}_{B,c}\bigl(\ell_{u_s,s}^{\,d+1}\bigr)}{(d+1)\,\mathcal G_{B,c}\bigl(\ell_{u_s,s}^{\,d}\bigr)}\to\mu_{B,c}(u)$ as $s\to0^+$.

*The flag height.* For each $\tau\in\Psi$ take a generic $N\times N$ matrix $(x_{\tau,a,b})$ of indeterminates, and let $\Omega_{\rm fl}$ be the field of rational functions over $\mathbb Q$ in all these indeterminates. The *flag coordinate system* has one block $(\tau,r)$ for every $\tau\in\Psi$ and $0\le r\le N-2$; its coordinates are indexed by the subsets $A\subseteq\{0,\dots,N-1\}$ with $r+1$ elements, and the coordinate tuple is $$y_{(\tau,r),A}=\det\bigl(x_{\tau,a,b}\bigr)_{0\le a\le r,\ b\in A}\in\Omega_{\rm fl}.$$ Let $P_{\rm fl}$ be its homogeneous coordinate ideal. The *root line* $\Lambda_{\tau,i}$ is the Hermitian line datum whose multidegree is $1$ on the block $(\tau,i)$, $-1$ on the block $(\tau,i-1)$ and $0$ on all other blocks (a block that does not exist is omitted), with metric function $h(z)=\prod_{k}\bigl(\sum_{A}|z_{k,A}|^2\bigr)^{a_k/2}$, where $a_k$ is its degree on the block $k$. The *flag height* attached to $I$ is the linear map $H_I:\mathcal R\to\mathbb R$ with $$H_I(m)=(-1)^{d+1}\,I_{P_{\rm fl}}\bigl(\text{the root lines of }m\bigr)\quad(\deg m=d+1),\qquad H_I(m)=0\quad(\deg m\ne d+1),$$ where a monomial $m$ of $\mathcal R$ determines its list of root lines as above, with $\Lambda_{\tau,i}$ in the place of $X_{\tau,i}$.

*The monomial expansion.* The tower satisfies the *monomial expansion* for $I$ if there are a real number $C_1$ and a natural number $B_1$ such that for every natural number $B\ge B_1$ there are real numbers $\alpha_\tau,\beta_\tau$ $(\tau\in\Psi)$ with $$\Bigl|\,P_B(m)-V\Bigl(H_I(m)-\sum_{\tau}(\alpha_\tau-\beta_\tau)\operatorname{Sh}_{j,\tau}(m)-\sum_\tau\beta_\tau\operatorname{Tot}_\tau(m)\Bigr)\Bigr|\ \le\ C_1\,\frac{\log B}{B}$$ for every monomial $m$ of $\mathcal R$ of degree $d+1$.

*The two lower bounds.* Let $C$, $\rho$ and $\lambda$ be real numbers. For a natural number $B$ and a weight $u$ put $$\mathcal B(B,u)=\bigl(\log(B\rho)+|\lambda|\bigr)\,\|u\|_1+\min(j,N-j)\,\operatorname{spr}(u).$$ The tower satisfies the *intersection lower bound* for $I$ with constants $(C,\rho,\lambda)$ if $$-\,C\,(d+1)\,V\,D(u)\,\mathcal B(B,u)\ \le\ P_B(\ell_u^{\,d+1}),$$ and the *mean slope lower bound* for $I$ with constants $(C,\rho,\lambda)$ if $$-\,C\,\mathcal B(B,u)\ \le\ \frac1{|\mathcal C|}\sum_{c\in\mathcal C}\mu_{B,c}(u),$$ in each case for every admissible $(u,g)$ and every natural number $B$ with $B\ge128$, $B_0(u,g)<B+1$ and $|S_0|\le B$.
