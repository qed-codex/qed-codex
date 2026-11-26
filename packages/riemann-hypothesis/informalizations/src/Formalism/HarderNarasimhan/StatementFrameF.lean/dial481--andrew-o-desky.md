---
{
  "module": "src/Formalism/HarderNarasimhan/StatementFrameF.lean",
  "declarations": [
    "Formalism.HN.FrameLA1",
    "Formalism.HN.TheoremF"
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

## Slope inequality for a family of maps

[Theorem ARAK.1120](https://andrewodesky.com/rh/lean/Formalism.HN.theoremF/)

Moment estimates for linear maps give a bound for the difference between source and target slopes.

Let $K$ be a totally complex number field equipped with a field involution, an automorphism whose square is the identity. Write $\mathcal O_K$ for its ring of integers, $n=[K:\mathbb Q]$, $\Delta_K=\operatorname{disc}K$, and $\Sigma_\infty(K)$ for its set of infinite places. For each $w\in\Sigma_\infty(K)$ choose a representing embedding $\sigma_w:K\to\mathbb C$, and put $t=|\Sigma_\infty(K)|$. No compatibility between the involution and these embeddings is assumed; the coordinate and slope formulas below are independent of the involution.

Let $I$ be a nonempty finite set. For each $i\in I$, let $N_i\subseteq V_i$ be a finitely generated $\mathcal O_K$-module spanning a finite-dimensional $K$-space $V_i$. Let $C\subseteq W$ be another such module spanning $W$. Choose bases $b_i,b_C$ of $V_i,W$, and write $$d_i=\dim_KV_i,\qquad r=\dim_KW,\qquad R=\sum_{i\in I}d_i>0.$$ At each infinite place $w$, choose invertible complex matrices $X_i(w),X_C(w)$ of sizes $d_i,r$.

To define the slopes, let $b,X$ denote the chosen basis and matrices for any one of the spaces $V_i,W$. For a vector $x$ in this space, let $[x]_b$ be its coordinate column, and let $\sigma_w$ act entrywise. Define $$f_w(x)=X(w)^{-1}\sigma_w([x]_b),\qquad \rho(x)=\bigl(\Re f_w(x),\Im f_w(x)\bigr)_{w\in\Sigma_\infty(K)}.$$ The target of $\rho$ has its Euclidean inner product. For a finitely generated $\mathcal O_K$-submodule $A$ of this space, write $\Lambda_A=\rho(A)$ and $m(A)=\operatorname{rk}_{\mathbb Z}\Lambda_A$. Write $\operatorname{covol}_{\mathbb R}\Lambda$ for the volume of a fundamental parallelepiped of a Euclidean lattice $\Lambda$ in its real span, assigning covolume $1$ to the zero lattice. Put $$\nu(\Lambda)=-\frac{\log\operatorname{covol}_{\mathbb R}\Lambda}{\operatorname{rk}_{\mathbb Z}\Lambda},\qquad \mu_0(A)=\nu(\Lambda_A).$$ Throughout, division by zero, $\log0$, and empty real suprema and infima have value zero. A submodule $B\subseteq A$ is saturated if $$\Lambda_B=\Lambda_A\cap\operatorname{span}_{\mathbb R}\Lambda_B.$$ Let $p_B$ be the orthogonal projection onto $(\operatorname{span}_{\mathbb R}\Lambda_B)^\perp$. Define $$\mu_{0,\max}(A)=\sup_{0\ne B\subseteq A}\mu_0(B),\qquad \mu_{0,\min}(A)=\inf_{\substack{B\subsetneq A\\B\text{ saturated}}}\nu(p_B\Lambda_A),$$ where $B$ ranges over $\mathcal O_K$-submodules. Thus quotients carry the norm given by orthogonal projection. Put $$c_K=-\log2+\frac{\log|\Delta_K|}{n},\qquad \mu(A)=2\mu_0(A)+c_K,\qquad \mu_{\max}(A)=2\mu_{0,\max}(A)+c_K,\qquad \mu_{\min}(A)=2\mu_{0,\min}(A)+c_K.$$

Let $B_i:V_i\to W$ be $K$-linear maps with $B_iN_i\subseteq C$, and let $h_i\in\mathbb R$. Write $[B_i]_w$ for the matrix of $B_i$ in $b_i,b_C$ after applying $\sigma_w$ entrywise. With $\|\cdot\|_{\mathrm{op}}$ denoting the operator norm for Euclidean norms, define $$h(B_i)=\frac1t\sum_{w\in\Sigma_\infty(K)}\log\bigl\|X_C(w)^{-1}[B_i]_wX_i(w)\bigr\|_{\mathrm{op}}^2,$$ and assume $h(B_i)\le h_i$ whenever $B_i\ne0$. Let $s,U,S\in\mathbb R$ satisfy $$sR\le\sum_i d_i(\mu(N_i)-h_i),\qquad U\ge0,\qquad \mu_{\max}(N_i)-h_i\le s+U\quad(i\in I),$$ $$s-\mu_{\min}(C)\le S,\qquad S\ge0.$$

Fix $v\in\Sigma_\infty(K)$, an integer $r_1\ge0$, invertible complex matrices $Y_i,Y_C$ of sizes $d_i,r$, and complex-linear maps $\widetilde B_i:\mathbb C^{d_i}\to\mathbb C^{r+r_1}$. In the standard coordinates, suppose their first $r$ rows equal $Y_C^{-1}[B_i]_vY_i$. Put $D=r+r_1$. For a complex-linear map $T$ between Euclidean spaces, write $T^*$ for its adjoint and $\|T\|_{\mathrm{HS}}^2=\operatorname{tr}(T^*T)$ for its squared Hilbert--Schmidt norm. Write $I_{d_i}$ for the identity on $\mathbb C^{d_i}$. For positive real weights $\gamma_i$, set $$Q=\sum_i\gamma_i\widetilde B_i\widetilde B_i^*.$$ Let $\delta,e,\eta\in\mathbb R$ satisfy $$0\le\delta<1,\qquad(1-\delta)D\le r,\qquad0\le e\le\tfrac14,\qquad\eta\ge0,$$ $$\sum_i\|\gamma_i\widetilde B_i^*\widetilde B_i-I_{d_i}\|_{\mathrm{HS}}^2\le eR,\qquad \operatorname{tr}(Q^2)\le(1+\eta)\frac{(\operatorname{tr}Q)^2}{D}.$$ Then $$s-\mu(C)\le\log|I|+\frac{4U\log(1+S/U)+(\eta+4\sqrt e)S}{1-\delta}.$$ In particular, the term $U\log(1+S/U)$ has value zero when $U=0$ under the division convention above.
