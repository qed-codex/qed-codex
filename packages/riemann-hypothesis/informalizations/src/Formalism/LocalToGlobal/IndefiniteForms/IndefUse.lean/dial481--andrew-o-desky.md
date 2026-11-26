---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteForms/IndefUse.lean",
  "declarations": [
    "Formalism.L2.Indef.IndefSide.boundsMu"
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

## Base target slope from determinant and local index bounds

[Theorem ARAK.0173](https://andrewodesky.com/rh/lean/Formalism.L2.Indef.IndefSide.boundsMu/)

Let $K$ be a totally complex number field with involution $a\mapsto\bar a$. Fix a subfield $K_0\subset K$ and an infinite place $v_0$. Require $$\sigma(\bar a)=\overline{\sigma(a)}\quad(a\in K_0,\ \sigma:K\hookrightarrow\mathbb C),\qquad v_0(\bar a)=\overline{v_0(a)}\quad(a\in K).$$ Assume the five universal assertions stated in the conventions, including ([Gluing lattices from localizations](https://andrewodesky.com/rh/lean/Formalism.DivisionValues.lattice_gluing/)).

Let $T$ be a set with a distinguished element $t_0$, and let $J$ and $P$ be finite sets. For each $t\in T$, choose an ambient space $K^{n_t}$, a matrix $H_t\in M_{n_t}(K_0)$ positive definite at every infinite place, a full lattice $M_t\subset K^{n_t}$, and a surjection $P_t:K^{n_t}\to K^{d_t}$. Put $Q_t=P_tM_t$. Choose quotient frames $X_{Q,t,v}$, subspaces $Q_{t,p}\subset K^{d_t}$, and, for each $j\in J$, row spaces $K^{z_{j,t}}$, form matrices $H_{j,t}$, frames $X_{Z,j,t,v}$, full lattices $L_{j,t}$ and subspaces $Z_{j,t,p}$. Require all $Q_t$ to be full lattices, the $Q_{t_0,p}$ to form a direct-sum decomposition of $K^{d_{t_0}}$, and the $Z_{j,t_0,p}$ to form a direct-sum decomposition of $K^{z_{j,t_0}}$ for each $j$.

Choose an integer $D>0$, target frames $X_{E,v}$ on $K^D$, auxiliary spaces $K^{w_j}$ with frames $X_{W,j,v}$ and full lattices $M_j$, subspaces $E_p\subset K^D$ and $W_{j,p}\subset K^{w_j}$, and isomorphisms $$\iota_t:K^{d_t}\longrightarrow K^D,\qquad \theta_{j,t}:K^{z_{j,t}}\longrightarrow K^{w_j}.$$ All frames are invertible, $d_{t_0}>0$, and $$\iota_{t_0}(Q_{t_0,p})=E_p,\qquad \theta_{j,t_0}(Z_{j,t_0,p})=W_{j,p},\qquad \dim_K W_{j,p}=\dim_K E_p.$$ For a frame $X_{A,v}$ define $\langle x,y\rangle_{A,v}=\overline{X_{A,v}^{-1}v(x)}^{\,t}X_{A,v}^{-1}v(y)$. Choose positive real numbers $\kappa_v$ and $\lambda_{j,t,p,v}$. For every $t,v$ with $t=t_0$ or $v=v_0$, require $$\langle\iota_tx,\iota_ty\rangle_{E,v}=\kappa_v\prod_j\lambda_{j,t,p,v}\langle x,y\rangle_{Q_t,v}\quad(x\in\iota_t^{-1}E_p,\ y\in K^{d_t}),$$ $$\langle\theta_{j,t}x,\theta_{j,t}y\rangle_{W_j,v}=\lambda_{j,t,p,v}\langle x,y\rangle_{Z_{j,t},v}\quad(x\in\theta_{j,t}^{-1}W_{j,p},\ y\in K^{z_{j,t}}).$$ The quotient and row forms satisfy $$X_{Q,t,v}^{-*}X_{Q,t,v}^{-1}=\bigl(v(P_t)v(H_t)^{-1}v(P_t)^*\bigr)^{-1},$$ $$X_{Z,j,t,v_0}^{-*}X_{Z,j,t,v_0}^{-1}=v_0(H_{j,t}).$$ For the base type, also require $H_{j,t_0}\in M_{z_{j,t_0}}(K_0)$ and $X_{Z,j,t_0,v}^{-*}X_{Z,j,t_0,v}^{-1}=v(H_{j,t_0})$ for every $v$. Here $A^{-*}=(A^{-1})^*$.

Choose a type $t_y$ at every nonzero prime ideal $\mathfrak p_y$ of $\mathcal O_K$, invariant under conjugation, with finite exceptional set $\mathcal T=\{y:t_y\ne t_0\}$. Define $$R_0=\bigcap_y(\iota_{t_y}Q_{t_y})_{\mathfrak p_y}\subset K^D,$$ and give it the metrics $\|X_{E,v}^{-1}v(x)\|_2$. Its linear dual lattice is $R_0^\vee=\{f\in(K^D)^*:f(R_0)\subseteq\mathcal O_K\}$, with the dual metrics.

Write $d_K=[K:\mathbb Q]$, $s_K=|\Sigma_\infty(K)|$, and $$\overline{\log\kappa}=s_K^{-1}\sum_v\log\kappa_v,\quad \ell_y=\frac{\log\operatorname{Norm}(\mathfrak p_y)}{d_K},\quad e_y=y(p_y),\quad r_y=\frac{p_y}{\sqrt{e_y}},$$ where $p_y$ is the residue characteristic and $y(a)$ is the additive prime-ideal valuation, assigned zero at $a=0$. For lattices $A,B$ in the same space set $$i_y(A,B)=\operatorname{length}_{\mathcal O_K}\frac{A_y}{A_y\cap B_y}-\operatorname{length}_{\mathcal O_K}\frac{B_y}{A_y\cap B_y},$$ with ordinary localization at $\mathfrak p_y$ and with each length converted to a natural number, assigning infinite length zero. For a nonsingular Hermitian form $h_H(x,z)=\bar x^{\,t}Hz$ put $$L^\#=\{z:h_H(L,z)\subseteq\mathcal O_K\},\qquad \mathfrak j_y(H,L)=i_y(L,L^\#).$$ Thus the Hermitian index has the sign $\mathfrak j_y(H,L)=-y(\det(h_H(b_a,b_b))_{a,b})$ for a basis after simultaneous localization at $\mathfrak p_y$ and $\overline{\mathfrak p_y}$. Put $$I_{j,y}=i_y(M_j,\theta_{j,t_y}L_{j,t_y}),\qquad A_{j,y}=I_{j,y}+i_{\bar y}(M_j,\theta_{j,t_y}L_{j,t_y})+\mathfrak j_y(H_{j,t_y},L_{j,t_y}).$$

Supply real numbers $l_{3,j},E_{1,j}$, real functions $F_j(y),J_j(t,y)$, and errors $\epsilon_{y,j}$. Require $$\frac{\operatorname{lcv}(M_j)}D\le l_{3,j},\qquad A_{j,y}=F_j(y)=0\quad(y\notin\mathcal T),$$ $$\sum_j\bigl(I_{j,y}+i_{\bar y}(M_j,\theta_{j,t_y}L_{j,t_y})\bigr)\le D\left\{\sum_j(2e_yF_j(y)+e_y\epsilon_{y,j})+\frac{2e_y}{p_y^2}\right\}\quad(y\in\mathcal T),$$ $$\epsilon_{y,j}\ge0\quad(y\in\mathcal T),\qquad \sum_{y\in\mathcal T}\ell_ye_y\bigl(\epsilon_{y,j}+J_j(t_y,y)\bigr)\le E_{1,j}.$$

For every $t,y$ choose a $K$-basis $b_{t,y}$ of $K^{d_t}$ spanning $Q_t$ after extension to $S_y^{-1}\mathcal O_K$, where $S_y=\mathcal O_K\setminus(\mathfrak p_y\cup\overline{\mathfrak p_y})$. Define $$\Gamma_t=(P_tH_t^{-1}P_t^*)^{-1},\qquad G_y=\det(\overline{b_{t_y,y,a}}^{\,t}\Gamma_{t_y}b_{t_y,y,b})_{a,b}.$$ Let $\mathcal S$ be finite with $\mathcal T\subseteq\mathcal S$, and choose real $G,E_3,E_{2,j},\gamma_y,\eta_{y,j}$ such that $$y(G_y)=0\ (y\notin\mathcal S),\qquad y(G_y)\le D\gamma_y\ (y\in\mathcal S),\qquad \sum_{y\in\mathcal S}\ell_y\gamma_y\le G,$$ $$\mathfrak j_y(H_{j,t_y},L_{j,t_y})\le e_yJ_j(t_y,y)D+\eta_{y,j}\quad(y\in\mathcal T),\qquad \sum_{y\in\mathcal T}\frac{\ell_y\eta_{y,j}}D\le E_{2,j},$$ $$\sum_{y\in\mathcal S}\ell_y\frac2{r_y^2}\le E_3.$$ Then $$\mu(R_0^\vee)\le\overline{\log\kappa}+\sum_jl_{3,j}+2\sum_j\sum_{y\in\mathcal T}\ell_ye_yF_j(y)+G+\sum_j(E_{1,j}+E_{2,j})+E_3.$$
