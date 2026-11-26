---
{
  "module": "src/Formalism/LocalRingCardinality/DataCoeff.lean",
  "declarations": [
    "Formalism.BasicNotions.DomWeight"
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

## Integral forms on column representations

[Definition / hypothesis THETA.D126](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)

Hypothesis (integral forms on columns). Use the classes $C_i$, groups $G_{i,c}$, sets $Y_i$, finite fields $\mathbb F_v$, operators $r_v$ and period spaces of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), and the coefficient field, places and embedding $\jmath:K\hookrightarrow\mathbb C$ of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). Use ([Rational Hermitian lattices with specified frames](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HLat/)) for the rational lattices and their archimedean norms. Write $N_i=k+i(t+1)$ and $\mathscr V_i=\mathbb C^{C_i\times Y_i}$.

For every $i\ge0$, $v\in\mathcal V_T$, $c\in C_i$, choose $N_i$-dimensional $\mathbb F_v$-vector spaces $L^+_{i,v,c},L^-_{i,v,c}$, a nonzero linear functional $f_{i,v,c}$ on $L^+_{i,v,c}$, and a nonzero vector $t_{i,v,c}\in L^-_{i,v,c}$. Choose maps $$u_{i,v,c}:L^+_{i,v,c}\to C_i,\qquad d_{i,v,c}:(L^-_{i,v,c})^*\to C_i,$$ and assign to every input of either map a complex-linear automorphism of $\mathbb C^{Y_i}$, denoted $U_{i,v,c,x}$ and $D_{i,v,c,g}$ respectively.

Choose an action $a\mapsto a\cdot c$ of $\mathbb F_v^\times$ on $C_i$ for every $(i,v)$, and complex-linear automorphisms $A_{i,v,a,c}$ of $\mathbb C^{Y_i}$. Require $$1\cdot c=c,\qquad(ab)\cdot c=a\cdot(b\cdot c),\qquad |G_{i,a\cdot c}|=|G_{i,c}|.$$ There is an $\mathbb F_v$-linear isomorphism $e:L^+_{i,v,a\cdot c}\to L^+_{i,v,c}$ with $f_{i,v,a\cdot c}=a(f_{i,v,c}\circ e)$. The initial representation satisfies $$(r_v(a)\phi)_c=A_{0,v,a,c}(\phi_{a\cdot c}).$$ For every coefficient place $w$, choose a bijection $\mathcal V_T\simeq\mathcal T$ and a truth value recording a selected subset of places.

A dominant integral weight of length $d$ means an integer row $\lambda_0\ge\cdots\ge\lambda_{d-1}$. Choose such rows $\lambda_{i,\tau}$ of length $N_i$ for every $i\ge0,\tau\in\mathcal T$, and rows $\sigma_\tau$ of length $N_m-1$. For $i\le m$, require $$\lambda_{i,\tau,h}=\begin{cases} U_{\tau,h}-(k-1)/2+h,&h<k,\\ -e_{\tau,b}+k/2+(2b+1)(t+1)/2,&h\ge k,\quad b=\lfloor(h-k)/(t+1)\rfloor. \end{cases}$$ The array $e_{\tau,b}$ is indexed from zero, and $b<i$ in the second branch.

Choose complex subspaces $F_i\subseteq\mathscr V_i$, with $F_0=U^0$, and complex sesquilinear forms $q_{i,c}$ on $\mathbb C^{Y_i}$, conjugate-linear in the first argument. Define $$q_i(\phi,\psi)=\sum_{c\in C_i}|G_{i,c}|^{-1}q_{i,c}(\phi_c,\psi_c).$$ Choose Hermitian lattices $\mathcal L_i$ over $K$, with nondegenerate archimedean frames and finitely generated integral modules spanning their rational spaces, and $\jmath$-semilinear maps $j_i:(\mathcal L_i)_K\to\mathscr V_i$ carrying the specified rational basis to a complex basis of $F_i$. At the chosen complex embedding, require $$\|x\|_{\mathcal L_i}^2=\Re q_i(j_i x,j_i x).$$ For every $v,a$, the operator $r_v(a)$ carries the complex image of the integral module of $\mathcal L_0$ into itself. For every $(i,w,v)$ choose a module $B_{i,w,v}$ over $K_w^0=\{a\in K:v_w(a)\ge0\}$ in $(\mathcal L_i)_K$ whose $K$-span is the whole space.

Choose a finite set $C_P$, finite groups $G^P_c$, a map $\tau_P:C_P\to C_m$ and injective homomorphisms $G^P_c\to G_{m,\tau_P(c)}$. If two final column functions agree at every $\tau_P(c)$, their evaluations in $Z_T$ are equal. Choose a subspace $F_P\subseteq R_T$, a complex sesquilinear form $q_P$ on $R_T$, conjugate-linear in its first argument, and a Hermitian lattice $\mathcal L_P$ with nondegenerate frames and a full finitely generated integral module. Choose a $\jmath$-semilinear map $j_P:(\mathcal L_P)_K\to R_T$ carrying its specified basis to a complex basis of $F_P$ and satisfying $$\|x\|_{\mathcal L_P}^2=\Re q_P(j_Px,j_Px).$$ Finally choose nonnegative reals $b_\tau$ for $\tau\in\mathcal T$ and $a_{i,\jmath',c,c'}$ for every $i\ge0$, complex embedding $\jmath':K\hookrightarrow\mathbb C$, $c\in C_i$ and $c'\in C_{i+1}$.
