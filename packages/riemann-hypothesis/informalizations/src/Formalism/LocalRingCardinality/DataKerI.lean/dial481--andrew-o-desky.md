---
{
  "module": "src/Formalism/LocalRingCardinality/DataKerI.lean",
  "declarations": [
    "Formalism.BasicNotions.KM.Gxz",
    "Formalism.BasicNotions.KM.applyAt0",
    "Formalism.BasicNotions.KM.nablaX",
    "Formalism.BasicNotions.KerEnt",
    "Formalism.BasicNotions.ThAtServed",
    "Formalism.BasicNotions.rhoMat"
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

## Rational kernel entries and derivative minors

[Definition / hypothesis PHT.D183](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)

Hypothesis (rational kernel entries). Use ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)), ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)), ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)), and ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)). Write $K$ for the coefficient field, $\jmath:K\hookrightarrow\mathbb C$ for its complex embedding, $w$ for a coefficient prime of residue characteristic $p_w$, $z$ for a source, $\mu$ for a twist, and $C^{z,\mu}$ for the twisted chain. A triple $(z,\mu,w)$ is level-free if $p_w\ne T_z$, $p_w\notin\{g_0,g_1\}$ and $p_w\notin Q_\mu$. Put $\overline{\mathbb Q}=\{x\in\mathbb C:x\text{ algebraic over }\mathbb Q\}$, and extend any embedding of this field to all complex numbers by value zero on transcendental numbers.

For every $w$, choose embeddings $\lambda_w:\overline{\mathbb Q}\hookrightarrow\mathbb C_{p_w}$ and $j_w:K\hookrightarrow\mathbb C_{p_w}$ such that $j_w(x)=\lambda_w(\jmath(x))$ and $$x\in\mathcal O_{K,w}\quad\Longleftrightarrow\quad|j_w(x)|\le1.$$ For every $z,\mu,i,c\in C_i^{z,\mu}$ choose a $K$-vector space $V_{z,\mu,i,c}$ with an injective $\jmath$-semilinear map $e_{z,\mu,i,c}:V_{z,\mu,i,c}\to(Y_i^{z,\mu}\to\mathbb C)$. No finite-dimensionality condition on these vector spaces is included. For every adjacent class pair choose a formal power series $\Theta^w_{z,\mu,i,c,c'}$ over $\mathbb C_{p_w}$ in variables $Z_{a,r,s}$ with $r<N_i,s<N_{i+1}$. The index $a$ ranges over $\{0,1\}\times A$; its embedding $\tau_a$ is the selected embedding corresponding to $(((-1)^{a_1},1),a_2)$ in the Galois group of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)).

For all natural $j,l$, define the row weights from the arrays of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)) by $$q^z_{\tau,l}=\begin{cases}U^z_{\tau,l},&l<k,\\-E^z_{\tau,h}+\dfrac{t+2-2(b+1)}2,&l=k+h(t+1)+b,\ 0\le h<m,\ 0\le b\le t,\\0,&l\ge k+m(t+1),\end{cases}$$ $$e_{j,\tau}=\begin{cases}E_{\tau,j-1},&1\le j\le m,\\0,&\text{otherwise},\end{cases}\qquad\nu^{\rm row}_{z,j,\tau,l}=q^z_{\tau,l}+e_{j,\tau}-\frac{N_{j-1}+N_j-1-2l}{2},$$ with $j-1$ truncated at zero. The selected-stage formula is also the one in ([Adjusted source lattices and explicit heights](https://andrewodesky.com/rh/lean/Formalism.MainNotions.FamP.nuDef/)). For each $z,i,a$ define a Young diagram by its cells $$\mathcal Y_{z,i,a}=\{(r,s):r<N_i,\ s<\lceil\nu^{\rm row}_{z,i+1,\tau_a,0}\rceil_+,\ s<\nu^{\rm row}_{z,i+1,\tau_a,r'}\text{ for every }r'\le r\}.$$ Let $J$ choose, for every $a$ and every column of this diagram of height $h$, a strictly increasing map $\{0,\ldots,h-1\}\to\{0,\ldots,n-1\}$. Set $$\nabla_{n,J}(X)=\prod_{a,\text{ columns}}\det(X_{a,r,J(s)})_{r,s<h},$$ $$G_{n,n',I}(X,Z)=\prod_{a,\text{ columns}}\det\left(\sum_{b<n}X_{a,r,b}Z_{a,b,I(s)}\right)_{r,s<h}.$$ For a formal series $\Theta(Z)$ let $D_\Theta$ act on polynomials in $(X,Z)$ by $$D_\Theta(X^\alpha Z^\beta)=X^\alpha\beta!\,[Z^\beta]\Theta.$$

Choose $j_w$-semilinear maps $S^w_{z,\mu,i,c}$ from $V_{z,\mu,i,c}$ to the linear dual of $\mathbb C_{p_w}[X_{a,r,b}:r\ge0,b<N_i]$, and $T^w_{z,\mu,i,c'}$ from $V_{z,\mu,i+1,c'}$ to functions on the column choices $I$ of size $N_{i+1}$. For level-free triples and $i<m$, every value $T^w(v')(I)$ has the same absolute value as $j_w(b)$ for some $b\in K$.

For level-free triples and $i<m$, the localized integral source lattice consists exactly of the class functions $\phi$ belonging to the specified rational coefficient-function space for which every class has a vector $v_c$ with $e(v_c)=\phi_c$ and $$|S^w(v_c)(\nabla_{N_i,J})|\le1\qquad\text{for every }J.$$ The analogous target lattice consists exactly of the class functions in its rational coefficient-function space for which every class has a vector $v'_{c'}$ realizing that function and $|T^w(v'_{c'})(I)|\le1$ for every $I$. The integral lattices and their complex realizations here are those of ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)).

Choose nonzero scalars $u^w_{z,\mu,i,c,c'}\in\mathbb C_{p_w}$ for every natural $i$ and adjacent pair. For level-free triples and $i<m$, whenever $$e(v')=K^{z,\mu}_{i,c,c'}e(v),$$ require, for every $I$, $$T^w(v')(I)=u^w_{z,\mu,i,c,c'}\,S^w(v)\bigl(D_{\Theta^w_{z,\mu,i,c,c'}}G_{N_i,N_{i+1},I}\bigr).$$ Here $K^{z,\mu}_{i,c,c'}$ is the class-to-class transition of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)). All polynomials with integer coefficients in these formulas are mapped into $\mathbb C_{p_w}$ by the integer coefficient map.

## Local frames for kernel-entry series

[Definition / hypothesis PHT.D191](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThAtServed/)

Hypothesis (local frames for kernel entries). Use ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)), ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)), and ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)). Fix an eligible source and coefficient prime $(z,w)$ as defined in ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)). The embedding of $\overline{\mathbb Q}$ used by its local comparison is $\lambda_w$ of ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)).

Choose, for every natural stage $j$, every local component and tuple of submodules $a$, and every local factor $v$, a square matrix $g_{j,a,v}$ over its unramified local field $Q_{j,v}$, of the size prescribed at that stage. For $j\le m$ and genuine lattice tuples, require $\det g_{j,a,v}$ to be a unit in $Q_{j,v}$ and require that tuple's $v$th lattice to be the column span of $g_{j,a,v}$ over the specified local DVR.

Identify each selected embedding $\tau$ with its local factor and Frobenius coordinate $(v,r)$. Let $\rho_j(g)_\tau$ be the matrix obtained from $g_{j,v}$ by applying the $r$th power of the specified local Frobenius, then the local-factor embedding into the local comparison coefficient field, and finally its embedding into $\mathbb C_{p_w}$.

For $j<m$ and every adjacent pair $a,a'$ of genuine local component-lattice tuples, there are scalars $c_\tau$ with $|c_\tau|=1$ such that the formal series $$\Theta^w_{z,\mu_w,j,c(j,a),c(j+1,a')}$$ is obtained from the formal local comparison series for $(j,a,a')$ by the following linear substitution into the signed embedding variables $Z_{x,s,t}$ of ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)). For a variable $X_{\tau,b,a}$ of the local comparison series, use $$X_{\tau,b,a}\longmapsto\sum_{\substack{x,s,t\\\tau_x=\tau}}c_\tau\,M_{\tau,b,t}\,N_{\tau,s,a}\,Z_{x,s,t},$$ where $$(M_\tau,N_\tau)=\begin{cases}(\rho_{j+1}(g_{j+1,a'})_\tau,\rho_j(g_{j,a})_\tau^{-1}),&r\text{ even},\\(\rho_{j+1}(g_{j+1,a'})_\tau^{-\mathsf T},\rho_j(g_{j,a})_\tau^{\mathsf T}),&r\text{ odd}.\end{cases}$$ Rows and columns are identified by the prescribed equality of the local ranks with $N_j,N_{j+1}$. The class map $c(j,a)$, coefficient fields, Frobenius maps, embeddings, local comparison series and chosen twist $\mu_w$ are the ones specified in ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)).
