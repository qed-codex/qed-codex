---
{
  "module": "src/Formalism/LocalToGlobal/HermitianForms/TiedTwPGen.lean",
  "declarations": [
    "Formalism.L2.Forms.ClassesAtPrimes",
    "Formalism.L2.Forms.ValuationAtPrimes"
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

## Terminal column lattices and period values

[Definition / hypothesis ARAK.D165](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.ClsPTied/)

Use ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)), ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)), ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)) and ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)). Write $n=N_m-1$ for the dimension of $X'$, $G_P$ for its coordinate Gram matrix and $i:E^n\to E^{N_m}$ for the fixed inclusion. All frame, polynomial, normalized Fock-pairing, rational-span, integral-span and permitted-coefficient-place conventions are those of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)).

Hypothesis (secondary class and value presentation). Choose a coordinate level on $X'$ with parameter $T=1$ and a specified bad set, satisfying every coordinate-level condition of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)). For every prescribed secondary class $c$ choose $y_c\in U(X')(\mathbb A_f)$ and a finitely generated lattice $M_c\subset E^n$ with $\widehat M_c=y_c\widehat\Lambda_P$. The classes $[y_c]$ biject with $U(X')(F)\backslash U(X')(\mathbb A_f)/U_P$. The prescribed secondary stabilizer embeds injectively into $U(X')(F)$ with image exactly $U(X')(F)\cap y_cU_Py_c^{-1}$.

The terminal weight is fixed as follows, with zero-based indices. For the arrays $V_{\tau,a},B_{\tau,j},E_{\tau,j}$ in ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)), put $$A_\tau(a)=\frac{m(t+1)}2+\begin{cases} V_{\tau,a},&a<k-1,\\ -B_{\tau,q},&a\ge k-1,\ q<m,\ b=0,\\ -E_{\tau,q}+(t-1)/2-(b-1),&a\ge k-1,\ q<m,\ b>0,\\ 0,&\text{otherwise}, \end{cases}$$ where $q=\lfloor(a-k+1)/(t+1)\rfloor$ and $b=(a-k+1)\bmod(t+1)$ in the cases $a\ge k-1$. Require the recorded dominant integral weight to be $$\sigma_\tau(a)=A_\tau(a)-\left(\frac{n-1}2-a\right),\qquad0\le a<n.$$ Put $\widetilde\sigma=\sigma-\lfloor m(t+1)/2\rfloor$, and let $d_\tau$ be its determinant shift.

Choose a complex linear equivalence $e_W$ from the recorded row-function space to functions on secondary classes and invertible frames of $X'$. It identifies the recorded secondary finite form space with the restrictions at $y_c$ of the character-equivariant adelic polynomial functions of weight $\widetilde\sigma$. For every orthonormal frame $o$, and whenever $$e_W(z)_c=F_{d,o^{-1},P_c},\qquad e_W(z')_c=F_{d,o^{-1},Q_c},\qquad P_c,Q_c\in\mathcal W_\sigma,$$ require $$\operatorname{ipP}(z,z')=\sum_c|\operatorname{Stab}_2(c)|^{-1}\mathcal N_\sigma(Q_c,P_c).$$ A row vector is in the rational terminal coefficient image exactly when it belongs to this finite form space and each class function is $F_{d,1,P_c}$ for a polynomial in the $K$-rational span. For each permitted coefficient place $w$, a rational terminal vector belongs to the recorded local lattice exactly when, for every $c$ and every $\ell_w$-local basis $B$ of $M_c$, its class function is $F_{d,B_\infty^{-1},P}$ for a polynomial in the $w$-integral span. In the untwisted global-lattice version this is required at every coefficient place.

For every embedding $s:K\hookrightarrow\mathbb C$, rational terminal vector $x$ represented by $K$-polynomials $P_c$, and orthonormal frame $o$ for the conjugate Gram matrices, require $$\operatorname{Re}\operatorname{maj}_s(x,x)=\sum_c|\operatorname{Stab}_2(c)|^{-1}\prod_\tau|\det o_\tau|^{2d_\tau}\operatorname{Re}\mathcal N_\sigma\bigl(P_c^s((o_\tau Z_\tau)_\tau),P_c^s((o_\tau Z_\tau)_\tau)\bigr).$$

Hypothesis (terminal extension and period comparison). Choose $z_0\in E z$ in terminal coordinates with $h(z_0,z_0)=T_u$, and rational unitary matrices $\gamma_c$ such that $$\gamma_cL_{m,\operatorname{til}(c)}=i(M_c)+\mathcal O_Ez_0.$$ If $a\in\mathcal O_E$ equals $h(z_0,\gamma_cx)$ for a terminal dual-lattice vector $x$, its prescribed finite functional is $r_v(a)$. The terminal base lattice is $i(\Lambda_P)+\mathcal O_Ez_0$. Its local base functional, followed by the chosen additive equivalence to $k_v$, sends the localization of a rational dual vector $x$ to $r_v(a)$ whenever $a=h(z_0,x)\in\mathcal O_E$.

For each secondary class choose $\kappa_c\in U_m$. For every finite adelic matrix $g$ with $gi=iy_c$ and $gz_0=z_0$, require $$\gamma_cy_{\operatorname{til}(c)}=g\kappa_c.$$ At every $v\mid g_a$, the first $n$ columns of the terminal local frame are $\phi_{a,v}(i)B_{P,a,v}$ and its final column is $\phi_{a,v}(z_0)$.

Choose a complex linear equivalence $e_{W_z}:W_z\simeq\{\text{functions on secondary classes and terminal values}\}$. For every $\varphi,c,s,s'$ with $eY(s)=\gamma_{c,\infty}eY(s')$, require $$e_{W_z}(\operatorname{evz}\varphi)(c,s)=\chi_m(\kappa_c)^{-1}\varphi(\operatorname{til}(c),s').$$ Choose a conjugate-linear map $j_M$ from the period input space to row functions. Its image is exactly the secondary finite form space, and $$\operatorname{period}(w,F)=\operatorname{ipP}(j_MF,w)$$ for every $w,F$. All period spaces and maps here are the recorded ones of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)).
