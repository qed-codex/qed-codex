---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/GL3Theta.lean",
  "declarations": [
    "Formalism.MainNotions.GL3Theta.LiftObj"
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

## Geometric theta-lift data

[Definition / hypothesis THETA.D187](https://andrewodesky.com/rh/lean/Formalism.MainNotions.GL3Theta.LiftObj/)

Hypothesis (geometric theta-lift datum). Use ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), and ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)). Fix a source and one of its twisted chains $C$, with rank $N_i$, class set $C_i$, frame domain $Y_i$, determinant functions $d_i(y,\tau)$, determinant phases $\rho_i(c),\rho'_i(c')$, and uniformization operators $U^C_{i,c,c'}$. Write $D_{\det}$ for its determinant group and $U$ for the prescribed subgroup.

Choose characters $\mu_i:D_{\det}\to\mathbb C^\times$ for every natural $i$, full self-dual lattices $L_i^0\subset E^{N_i}$, full self-dual lattices $L_{i,c}\subset E^{N_i}$ for $c\in C_i$, and determinant labels $t_{i,c}\in D_{\det}$. Require $$x\in L_i^0\quad\Longleftrightarrow\quad x_k\text{ is integral over }\mathbb Z\text{ for every }k,\qquad [t_{i,c}]=\operatorname{relDet}(L_i^0,L_{i,c}).$$ Define characters $$r_i(t)=\mu_{i+1}(t)^{-1}\chi_D(t)^{-\lfloor N_{i+1}/2\rfloor},\qquad r'_i(t)=\mu_{i+1}(t)\chi_D(t)^{\lfloor N_i/2\rfloor}.$$ For $i<m$ require $\rho_i(c)=r_i(t_{i,c})$ and $\rho'_i(c')=r'_i(t_{i+1,c'})$.

Choose maps $f_i:Y_i\to\prod_{\tau\in\mathcal T}M_{N_i}(\mathbb C)$ for all natural $i$. For $i\le m$ each map is injective, its image consists exactly of tuples of invertible matrices, and $$d_i(y,\tau)=\det f_i(y)_\tau.$$ Choose $c^D_\tau\in\mathbb C$ and a number field $M\subset\mathbb C$ containing every $e_\tau(x)$ for $x\in E$. For each $\tau$ require $c^D_\tau\in M$ and $$\{a\in M:a e_\tau^{\rm coord}\in\operatorname{span}_{\mathcal O_M}\{(e_\nu(x))_\nu:x\in A_0\}\}=c^D_\tau\mathcal O_M.$$ Here $e_\tau^{\rm coord}$ is the coordinate unit vector. Finally choose a finite subset $S\subset\mathbb N$ and functions $$\Theta_{i,c,c'}:\mathbb C^{\mathcal T\times\{0,\ldots,N_{i+1}-1\}\times\{0,\ldots,N_i-1\}}\longrightarrow\mathbb C$$ for every $i,c,c'$. The datum itself imposes no analytic condition on these functions.

The polynomial uniformization law at $(i,\nu)$ is the following additional condition. Let $\mathcal P_i=\mathbb C[X_{\tau,a,b}:a,b<N_i]$ and $\mathrm{ev}_i(Q)(y)=Q(f_i(y))$. Fix a complex-linear map $R_i:(Y_i\to\mathbb C)\to\mathcal P_i$ with $R_i\mathrm{ev}_i=1$ whenever such a map exists, and an arbitrary fixed map otherwise. For a function $\Theta$, let $\mathcal J_\Theta:\mathcal P_i\to\mathcal P_{i+1}$ first substitute $$X_{\tau,a,b}\longmapsto\sum_{s<N_{i+1}}W_{\tau,s,b}Z_{\tau,s,a},$$ where $W_{\tau,s,b}=0$ for $b\ge N_{i+1}$, and then replace each $Z$-monomial $Z^\alpha$ by $(\prod_{\tau,s,a}(c^D_\tau)^{\alpha_{\tau sa}})\partial^\alpha\Theta(0)$. Set $U_\Theta=\mathrm{ev}_{i+1}\mathcal J_\Theta R_i$. Require $$U^C_{i,c,c'}(\mathrm{ev}_iQ)=U_{\Theta_{i,c,c'}}(\mathrm{ev}_iQ)$$ for every $c,c'$ and every polynomial $Q$ satisfying $$Q((X_\tau\beta_\tau)_\tau)=\left(\prod_{\tau,a}(\beta_\tau)_{aa}^{\nu_{\tau a}}\right)Q(X)$$ for all upper triangular matrices $\beta_\tau$ with nonzero diagonal. The full polynomial uniformization law requires this identity for every $Q\in\mathcal P_i$. The weight used for a source $z$ is $\nu_{\tau a}=\lfloor\nu^{\rm row}_{z,i+1,\tau,a}\rfloor_+$, the nonnegative natural floor of the row weight defined in ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)).
