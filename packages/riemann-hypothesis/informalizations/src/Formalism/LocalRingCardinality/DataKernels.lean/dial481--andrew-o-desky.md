---
{
  "module": "src/Formalism/LocalRingCardinality/DataKernels.lean",
  "declarations": [
    "Formalism.BasicNotions.ColumnChain",
    "Formalism.BasicNotions.ColumnsAtT",
    "Formalism.BasicNotions.PeriodMap"
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

## Column chains and period pairings

[Definition / hypothesis THETA.D127](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)

Hypothesis (column chains and period pairings). Use the ranks $k,m,t,f$, $N_j=k+j(t+1)$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) and rational arrays $(U_{\tau,i},V_{\tau,i},b_{\tau,j},e_{\tau,j})$ of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)), with a finite embedding index set $\mathcal T$. A column chain consists of the following choices, made for every integer $i\ge0$.

Choose a finite class set $C_i$, a finite group $G_{i,c}$ for each $c\in C_i$, and a set $Y_i$. There is a positive integer $D_G$ such that $|G_{i,c}|\mid D_G$ for $i\le m$. Choose nonzero complex numbers $d_{i,y,\tau}$ for $y\in Y_i$, $\tau\in\mathcal T$, phase functions $\rho_i:C_i\to\mathbb C$ and $\rho'_i:C_{i+1}\to\mathbb C$, and complex-linear maps $$u_{i,c,c'}:\mathbb C^{Y_i}\longrightarrow\mathbb C^{Y_{i+1}}.$$ For $i<m$, require $|\rho_i(c)|=|\rho'_i(c')|=1$. Choose integer functions $s^\sharp_{i,\tau},s^\div_{i,\tau}$ satisfying, for $i<m$, $$s^\sharp_{i,\tau}=e_{\tau,i}-N_{i+1}/2,\qquad s^\div_{i,\tau}=e_{\tau,i}-N_i/2.$$ The row $e_{\tau,i}$ is indexed from zero in these formulas.

These choices define a map $K_i:\mathbb C^{C_i\times Y_i}\to\mathbb C^{C_{i+1}\times Y_{i+1}}$ by $$\begin{aligned} (K_i\phi)_{c'}(y')={}&\sum_{c\in C_i}\frac{\rho_i(c)\rho'_i(c')}{|G_{i,c}|} \left(\prod_\tau d_{i+1,y',\tau}^{s^\div_{i,\tau}}\right)^{-1}\\ &\qquad\cdot u_{i,c,c'}\left(y\mapsto\prod_\tau d_{i,y,\tau}^{s^\sharp_{i,\tau}}\phi_c(y)\right)(y'). \end{aligned}$$ Write $K^{(m)}=K_{m-1}\cdots K_0$.

The prime-level data consist of a prime $T$, a finite set $\mathcal V_T$ with $|\mathcal V_T|=f$, a finite field $\mathbb F_v$ of cardinality $T$ for each $v\in\mathcal V_T$, and a nontrivial additive character $\psi_v:\mathbb F_v\to\mathbb C^\times$. For every $v$, choose a multiplicative homomorphism $$r_v:\mathbb F_v^\times\longrightarrow\operatorname{End}_{\mathbb C}(\mathbb C^{C_0\times Y_0}),$$ and a finite-dimensional subspace $U^0\subseteq\mathbb C^{C_0\times Y_0}$ stable under every $r_v(a)$. Choose a positive integer $d^*$, a positive real $D^*$ and a real $\Gamma>1$. Put $$U^{\rm ram}=U^0\cap\bigcap_{v\in\mathcal V_T}\ker\left(\sum_{a\in\mathbb F_v^\times}r_v(a)\right),\quad T^*=\left(\frac{D^*}{d^*}\right)^{1/(fk)}\Gamma^{-2/(fk)}.$$

The period data consist of complex vector spaces $P_T,Z_T,R_T$, complex-linear maps $$\operatorname{ev}:\mathbb C^{C_m\times Y_m}\to Z_T,\qquad l:Z_T\to R_T,$$ and a complex-bilinear pairing $q:R_T\times P_T\to\mathbb C$. The column-period pairing is $$\mathcal P(\phi,F)=q\bigl(l(\operatorname{ev}(K^{(m)}\phi)),F\bigr).$$ A member consists of one such column chain, prime-level datum and period datum.
