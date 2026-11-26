---
{
  "module": "src/Formalism/LocalToGlobal/HermitianColumns/TiedCh.lean",
  "declarations": [
    "Formalism.L2.Herm.HermColsCh"
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

## Hermitian column levels and local modifications

[Definition / hypothesis ARAK.D163](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)) and ([Integral level lattices and their class representatives](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ColLevel/)). Write $K$ for the coefficient field, $E/F$ for the CM extension and $E_0\subset E$ for the fixed quadratic subfield. At source $u$ the distinguished rational prime is $T=T_u$, the class lattice in $X_i$ is $L_{i,c}$, and its Hermitian dual is $L_{i,c}^\#$. Hats denote finite adelic completions. Coordinates always use the fixed Hermitian frames.

Hypothesis (Hermitian levels and classes). At every source choose the initial data of ([Integral level lattices and their class representatives](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ColLevel/)). For every $i\ge0$ choose a finite set $\mathcal B_{u,i}$ and a branch map $b_{u,i}$ from its prescribed class set. The terminal set $\mathcal B_{u,m}$ has exactly one element.

For $1\le i\le m$ and $\beta\in\mathcal B_{u,i}$ choose a finitely generated full integral lattice $\Lambda_{i,\beta}\subset X_i$ in coordinates, with $$T\Lambda_{i,\beta}^\#\subset\Lambda_{i,\beta},\qquad[\Lambda_{i,\beta}^\#:\Lambda_{i,\beta}]=T^{2f}.$$ Choose local subgroups $U_{i,\beta,v}$ of the unitary stabilizers of these completed lattices. They equal the full stabilizer when $v\nmid g_0g_1T$. At $v\mid g_a$ they contain every stabilizer element $x$ with $(x-1)\Lambda_v\subset g_a\Lambda_v$. At $v\mid T$ they are exactly the stabilizer elements with $(x-1)(\Lambda^\#)_v\subset\Lambda_v$. Choose an adelic subgroup $U_{i,\beta}$ consisting exactly of unitary finite adelic matrices whose local components lie in these groups.

Choose $y_c\in U(X_i)(\mathbb A_f)$ for classes in branch $\beta$, giving a bijection onto $$U(X_i)(F)\backslash U(X_i)(\mathbb A_f)/U_{i,\beta}.$$ Require $\widehat{\operatorname{crd}(L_{i,c})}=y_c\widehat\Lambda_{i,\beta}$. Choose injective homomorphisms from the prescribed class stabilizers to $U(X_i)(F)$, with image $U(X_i)(F)\cap y_cU_{i,\beta}y_c^{-1}$. Identify the prescribed finite-prime labels $v$ bijectively with all finite $F$-places dividing $T$, and identify each prescribed finite field $k_v$ with $\mathcal O_F/v$ by a ring isomorphism.

Hypothesis (prime-$T$ lattices and residues). Choose $\pi_u\in\mathcal O_E\cap E_0$ with $$\pi_u\bar\pi_u=T_u,\qquad\pi_u\equiv1\pmod{Q_Sqd(g_0g_1)^2}.$$ For each finite-prime label choose a maximal ideal $P_v\subset\mathcal O_E$ containing $\pi_u$, contracting to its designated $F$-prime, and a surjective ring map $r_v:\mathcal O_E\to k_v$ with kernel $P_v$. On $\mathcal O_F$ it is the quotient map under the chosen $k_v\simeq\mathcal O_F/v$. If $\ell_w=T_u$ and $\jmath(y)=\tau_{w,v}(x)$ for $x\in\mathcal O_E$, $y\in K$, require $$\operatorname{val}_w(y)>0\iff x\in\begin{cases}P_v,&\epsilon_w=\mathrm{true},\\\bar P_v,&\epsilon_w=\mathrm{false},\end{cases}$$ where $\tau_{w,v}$ and $\epsilon_w$ are the recorded CM embedding and conjugate-prime flag.

For every $i\le m$ and class $c$, require an $\mathcal O_E$-linear isomorphism $L_{i,c}^\#/L_{i,c}\simeq\mathcal O_E/(T_u)$. Put $K_{i,v,c}=L_{i,c}+P_vL_{i,c}^\#$. For all $i\ge0$ choose additive maps $$p_{i,v,c}:L_{i,c}^\#\longrightarrow V_{i,v,c},\qquad p^k_{i,v,c}:K_{i,v,c}\longrightarrow V^k_{i,v,c},$$ semilinear for $r_v$. For $i\le m$ they are onto, with kernels $P_vL_{i,c}^\#$ and $P_vK_{i,v,c}$. The prescribed finite functional satisfies $f_{i,v,c}(p(z))=0$ exactly when $z\in K_{i,v,c}$. If $f(p(z))=1$, require $p^k(T_uz)=t_e$ whenever $T_uz\in K_{i,v,c}$, with the prescribed distinguished vector $t_e$.

Hypothesis (local lattice modifications). For every $i$, $v$, $c$ and $z\in L_{i,c}^\#$ choose a Hermitian isometry $\gamma^\uparrow_z$ of $X_i$. For $i\le m$ and $f(p(z))=1$, put $c'=\operatorname{up}(i,v,c,p(z))$. The lattices $\gamma^\uparrow_zL_{i,c'}$ and $L_{i,c}$ have the same localization at every maximal ideal other than $P_v$ and $\bar P_v$, and $$(\gamma^\uparrow_zL_{i,c'})_{P_v}=(L_{i,c}^\#)_{P_v},\qquad (\gamma^\uparrow_zL_{i,c'}^\#)_{P_v}=(L_{i,c}^\#+\mathcal O_ET_u^{-1}z)_{P_v}.$$ For every $x\in L_{i,c'}^\#$ with $T_u\gamma^\uparrow_zx\in L_{i,c}^\#$, require $f_{i,v,c'}(p(x))=f_{i,v,c}(p(T_u\gamma^\uparrow_zx))$. For every other label $v'$, the residue functionals of $x$ and $\gamma^\uparrow_zx$ agree whenever the latter belongs to $L_{i,c}^\#$.

For each finite dual functional $g$ on $V^k_{i,v,c}$ choose an isometry $\gamma^\downarrow_g$. For $i\le m$ and $g\ne0$, put $c'=\operatorname{dn}(i,v,c,g)$. The lattices $\gamma^\downarrow_gL_{i,c'}$ and $L_{i,c}$ agree away from $P_v,\bar P_v$, and $$(\gamma^\downarrow_gL_{i,c'}^\#)_{P_v}=(L_{i,c})_{P_v}.$$ Require $f_{i,v,c'}(p(x))=g(p^k(\gamma^\downarrow_gx))$ whenever $\gamma^\downarrow_gx\in K_{i,v,c}$, and equality of every other label's residue functional whenever $\gamma^\downarrow_gx\in L_{i,c}^\#$.

For every $i$, residue-field unit $a$ and class $c$ choose a dilation isometry $\gamma_a$. For $i\le m$ and $c'=\operatorname{dil}(i,v,a,c)$, require $$\gamma_aL_{i,c'}=L_{i,c},\qquad f_{i,v,c'}(p(x))=a f_{i,v,c}(p(\gamma_ax)),$$ whenever $\gamma_ax\in L_{i,c}^\#$; the other labels' residue functionals are unchanged.

For each raising, lowering and dilation modification at stage zero or $1\le i\le m$, use the prescribed isometry $\gamma$ above. The old and new classes belong to the same branch at positive stages, and there exist $\kappa\in U$ and unitary finite $\eta$, identity outside the corresponding $F$-place, with $$\gamma y_{c'}=y_c\eta\kappa.$$ For raising this is required when $f(p(z))=1$, and for lowering when $g\ne0$.

Hypothesis (initial local comparisons and reference lattices). Choose $\pi_{g,a}\in\mathcal O_E\cap E_0$ with $\pi_{g,a}\bar\pi_{g,a}=g_a$, independent of the source. At every $v\mid g_a$, the initial splitting sends $1\otimes b$ to $(b,b)$ and the first component of $\bar\pi_{g,a}$ has absolute value less than $1$. The first split image of the completed initial lattice is the initial frame times $\mathcal O_v^k$. The image of $\pi_u$ annihilates its chosen finite local module at $v\mid T_u$. Choose additive equivalences from those modules to the prescribed $k_v$; they send the initial local functional of $t$ to $f_{0,v,c}(p(z))$ whenever $y_ct=\operatorname{crd}(z)$.

At every positive stage, branch and $v\mid T_u$, choose an additive map from the completed dual base lattice to $k_v$ whose value at $t$ is $f_{i,v,c}(p(z))$ whenever $y_ct=\operatorname{crd}(z)$. Every $X_i$ for $i\le m$, and $X'$, has an $E$-basis orthonormal for its Hermitian form whose $\mathcal O_E$-span is the recorded reference lattice. For each source require $c_u\pi_u=\pi_{u_0}$ and $$\Lambda+\bar\pi_u\Lambda^\#=L_0$$ in coordinates, initially and at every positive stage and branch, where $L_0$ is the corresponding reference lattice.

Hypothesis (secondary lattices and terminal extension). For every secondary class $c$ choose a lattice $M_c\subset X'$. On the fixed reference lattice of $X'$ choose local unitary stabilizer subgroups, equal to the full stabilizer away from $g_0g_1$ and containing $(x-1)L_{0,v}\subset g_aL_{0,v}$ at $v\mid g_a$; their adelic group is exactly their unitary componentwise product. Choose secondary class representatives and injective stabilizer maps with the same double-quotient, lattice-completion and stabilizer-image conditions above.

Choose $z_0\in E z\subset X_m$ with $h(z_0,z_0)=T_u$ and Hermitian isometries $\gamma_c$ satisfying $$\gamma_cL_{m,\operatorname{til}(c)}=i(M_c)+\mathcal O_Ez_0.$$ For every terminal dual vector $x$ and $a\in\mathcal O_E$ with $a=h(z_0,\gamma_cx)$, require $f_{m,v,\operatorname{til}(c)}(p(x))=r_v(a)$. The terminal stabilizer image of the prescribed secondary stabilizer, conjugated by $\gamma_c$, acts on $i(X')$ as its secondary stabilizer image and fixes $z_0$.
