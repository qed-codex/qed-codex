---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/CountsIrreducibilityConstants.lean",
  "declarations": [
    "GlobalTheory.Cp.D3"
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

## Data, families of data, classes of families, and properties of all sufficiently constrained families of a class

[Definition / hypothesis THETA.D028](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)

**Datum.** A *datum* $D$ consists of the choices satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) and its cited hypotheses. Use the fields, group, ranks, primes and ideal of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). In this entry write $K=E_0=\mathbb Q(\sqrt{-d})$, and write $\Lambda$ for the coefficient field of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). Put $TT=T$, $N(j)=N_j$, $c_E=Q_Sqd$, $p_{\mathrm{aux}}=p_\Delta$ and $p'_{\mathrm{aux}}=p'_\Delta$.

Write $W$ for the finite source-index set. Its elements are called words. For $u\in W$, let $T_u$ be its prime and let $D_\Gamma(u)$ be the positive integer $D_G$ of its column chain in ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)). For $h=0,1$, use the finite generator-place label set $V_h=\mathcal V_h$ and units $\alpha_{h,v,j}=\chi_{h,v,j}$ of ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)).

Let $\gamma:\operatorname{Gal}(E/\mathbb Q)\xrightarrow\sim\{\pm1\}^2\times A$ be the chosen Galois isomorphism, so that $\gamma(\sigma_g)=g$ in the notation of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Write $$\operatorname{Art}_E(a)=\sigma_{\alpha(a)}\qquad\bigl(a\in(\mathbb Z/c_E\mathbb Z)^\times\bigr).$$ For a prime $p\nmid c_E$, let $h_p$ be the $A$-coordinate of $\gamma(\operatorname{Art}_E(p))$ and let $\nu_p$ be its additive order.

**Size data.** *Size data* $L$ for a datum $D$ is a record that contains a *scale*, namely real numbers $x>1$, $0<\varepsilon<1/52$ and $J\ge 1$, together with further numerical choices (integers attached to the elements of $TT$, a finite set of places of $\Lambda$, real-valued functions on places, and others not expanded). From a scale we form $$\mathcal{L}=x^{\varepsilon},\qquad b=e^{\mathcal{L}},\qquad X'=\exp\bigl(x^{\varepsilon/3}\bigr),\qquad \delta_1=x^{-\varepsilon/8}.$$

**Family.** Let $\varepsilon$ be a real number. A *family with parameter $\varepsilon$* has the data of ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), with the shared data of ([Shared data in an arithmetic family](https://andrewodesky.com/rh/s/family-shared-data.html)) and constants of ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)). Write $x_1,I_x,D(x,i),L(x,i),J$ for its starting scale, member sets, member data, size data and common interval parameter. The data $D(x,i),L(x,i)$ are defined for every real $x$ and every $i\in I_x$.

A pair $(x,i)$ with $i\in I_x$ is called a *member* of the family. We write $n,k,m,t,f,r,N(j),W,T_u,D_\Gamma(u)$ for the corresponding components of $D(x,i)$ and $\mathcal{L},b,X',\delta_1$ for the quantities formed from the scale of $L(x,i)$.

The fixed constants, their four ordered lists, and the lower-bound requirements for a family are those in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)). Write $$c_{\rm pre}=\mathcal C_{\rm pre},\quad c_{\rm out}=\mathcal C_{\rm out},\quad c_{\rm mid}(C_H)=\mathcal C_{\rm mid}(C_H),\quad c_{\rm last}=\mathcal C_{\rm last},$$ and $C_{Tu}=C_T$, $C_{sz}=C_{\rm size}$. A family is *large for a threshold $K$ with $C_H$* when those lower-bound requirements hold.

**Class of families.** A *class of families* is a property $\mathcal{C}$ of families, defined for families of every parameter $\varepsilon$.

**Sufficiently constrained families.** Let $\mathcal{C}$ be a class of families and let $P(\mathrm{Fm},C_H)$ be a property of a family and a real number. We say that *$P$ holds for all sufficiently constrained families of $\mathcal{C}$* if there is $\varepsilon_1>0$ such that for every $\varepsilon$ with $0<\varepsilon\le\varepsilon_1$ there is a threshold $K$ such that $P(\mathrm{Fm},C_H)$ holds for every family $\mathrm{Fm}$ with parameter $\varepsilon$ in $\mathcal{C}$ and every real number $C_H$ such that $\mathrm{Fm}$ is large for $K$ with $C_H$.

**Standard conditions on a family.** The following conditions on a family $\mathrm{Fm}$ with parameter $\varepsilon$ are used to define classes. Here $M(j)$ is Minkowski's number $$M(j)=\prod_{p\le j+1\ \text{prime}} p^{\sum_{i=0}^{j}\lfloor j/(p^i(p-1))\rfloor}.$$

All eventual thresholds below may be chosen larger than $x_1$. At an auxiliary scale $Y\ge1$, write $$X_1=\exp(Y^{\varepsilon/5}),\qquad X_2=\exp(Y^{\varepsilon/5}(\log Y)^2).$$

For a positive denominator $a=2^v a_0$ with $a_0$ odd, the Kronecker symbol used here is $$\left(\frac{D}{a}\right)=\left(\frac{D}{a_0}\right)_{\!J}\kappa(D)^v,$$ where the subscript $J$ denotes the Jacobi symbol, and $\kappa(D)$ is $0$ for even $D$, $1$ for $D\equiv1,7\pmod8$, and $-1$ for $D\equiv3,5\pmod8$.

- (N1) Eight of the constants have prescribed values: $C_p=1$, $e_P=12$, $c_{TO}=28e_P+41$, $C_t=c_{TO}+24$, $C_{\eta F}=6$, $C_c=2$, $c_w=9/10$ and $C_{YL}=9$. At every member with $x>x_1$: $\mathfrak c=\mathcal O_K$; a component $v$ of the parameters that the datum attaches to the elements of an index set is the same for all elements; $g_0,g_1\le e^{9\mathcal{L}}$; $p_{\mathrm{aux}},p'_{\mathrm{aux}}<X'$; and three integer components $j_0$, $L_w$, $T_O$ of the member are given by $j_0=\lceil\log_5(nN(m)/m)\rceil$, $L_w=10\lceil(C_t+4)\log x\rceil+2\lceil 30/\varepsilon\rceil+22$ and $T_O=\lceil x^{c_{TO}}\rceil$.
- (N2) At every member with $x>x_1$: $x^{2+8\varepsilon}\le n\le 2x^{2+8\varepsilon}$, $\sqrt{x\delta_1}\le m\le 2\sqrt{x\delta_1}$ and $x^{9/2+10\varepsilon}\le k\le 2x^{9/2+10\varepsilon}$.
- (N3) At every member with $x>x_1$, let $r_*$ be the least prime that does not divide $$c_E(p_{\mathrm{aux}}-1)(p'_{\mathrm{aux}}-1)\operatorname N\mathfrak c,$$ and let $q_*$ be the least prime satisfying $q_*\equiv1\pmod{r_*c_E}$ and $q_*\nmid\operatorname N\mathfrak c$. Then $q_*<X'$. Here $\operatorname N\mathfrak c=|\mathcal O_K/\mathfrak c|$; a least element of an empty subset of $\mathbb N$ is assigned the value $0$.
- (N4) There is $x_0$ such that at every member with $x\ge x_0$, the weighted prime sum defined below satisfies $$\sum_{p\in\mathcal P_*}\frac{\log p}{p} \left(2\,\mathbf1_{\{\Sigma(p)>x^{-\varepsilon}\}}+4\Sigma(p)\right)\le x^{-9}.$$ The indicator $\mathbf1$ is $1$ when its subscripted condition holds and $0$ otherwise.
- (a) There is $x_0$ such that at every member with $x\ge x_0$ and for every word $u$, $D_\Gamma(u)$ divides $M(2fN(m))$.
- (b) There is $x_0$ such that at every member with $x\ge x_0$, for each $h\in\{0,1\}$ and $v\in V_h$, the $2m+1$ elements $$1,\quad \alpha_{h,v,j},\quad\alpha_{h,v,j}^{-1}\quad(0\le j<m)$$ are pairwise distinct, each $\alpha_{h,v,j}$ is a square in $\mathbb F_{g_h}^{\times}$, and their prime-to-$\ell$ parts are pairwise distinct for every prime $\ell\notin\mathcal B(r,g_h)$. Here $$\mathcal B(r,g)=\{g\}\cup\{\ell\text{ prime}:\exists a\in\{1,\ldots,r\},\ g^a<\ell^{4v_\ell(g^a-1)}\}.$$ For an element $z$ of finite order $n$, write $n=\ell^a n'$ with $\ell\nmid n'$. Its prime-to-$\ell$ part is $z^{\ell^a b}$, where $\ell^a b\equiv1\pmod{n'}$; this is $1$ when $n'=1$.
- (c) There is $x_0$ such that at every member with $x\ge x_0$ there is a real $Y$ with $x^{1/J}\le Y\le x$ for which the two zero-free-region conditions below hold.
- (d) There is $x_0$ such that at every member with $x\ge x_0$ there is a real $Y$ with $x^{1/J}\le Y\le x$ such that $$\sqrt{X_1}<q\le X_1,\qquad \sqrt{X_2}<d\le X_2,$$ $$q\equiv3\pmod8,\qquad d\equiv7\pmod{16},\qquad \left(\frac{-d}{q}\right)=1,$$ $$\left(\frac{-d}{p}\right)=1\quad\text{for every prime }p\le Y^{\varepsilon/5},\qquad \log(Q_Sqd)\le2Y^{\varepsilon/5}(\log Y)^2.$$ The choices of $x_0$ and $Y$ in (c) and (d) are separate.
- (e) $C_{YL}\le 9$.
- (f) There is $x_0$ such that at every member with $x\ge x_0$ and for every word $u$, every prime dividing $D_\Gamma(u)$ is at most $2fN(m)+1$.
- (g) ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)) holds, using the selected theta-input sets and the twists at the coefficient places of this family.
- (h) There are a real number $C_H$ and positive real numbers $C_5$, $c_6$, $C_b$ for which seven conditions on the family, which involve these numbers and the constant $3$, hold (not expanded).
- (i) There is $x_0$ such that at every member with $x\ge x_0$ and for every word $u$, $$b^{m/2}\le T_u,\qquad \log T_u\le C_{Tu}\,m\,\mathcal L.$$
- (j) There are $C$ and $x_0$ such that at every member with $x\ge x_0$ and for every word $u$, $\log D_\Gamma(u)\le C\,fN(m)\log\bigl(fN(m)\bigr)$.

**The weighted prime sum in (N4).** The sum uses the integer weights $a_t,b_t$ of the size data, for $t\in TT$. Extend them by zero to functions $\widetilde a,\widetilde b:A\to\mathbb Z$. At each member, the family supplies a map $s:A\times A\to A$ such that $$s(h,t)\in t+\langle h\rangle,\qquad s(h,t+h)=s(h,t),$$ and a real-valued function $\kappa^{\mathrm I}(p,\nu,T,\mathbf a,\mathbf b)$ for natural numbers $p,\nu$, subsets $T\subseteq\{0,\ldots,\nu-1\}$ and vectors $\mathbf a,\mathbf b\in\mathbb Z^\nu$. The map $s$ chooses one representative in each coset of $\langle h\rangle$. These choices and the function $\kappa^{\mathrm I}$ may depend on the member. Four nonnegative real constants $C_\Lambda,C_\rho,C_N,C_{\mathrm{II}}$ are fixed throughout the family.

First define the following numbers at the member's scale. For a real $z$, put $\lceil z\rceil_+=\max(0,\lceil z\rceil)$, and use natural logarithms unless a base is specified: $$H=2+8\varepsilon,\quad K_*=\left\lceil\frac{8(H+2)}{\varepsilon}\right\rceil_+, \quad R_*=K_*+1,\quad U=\lceil1/\delta_1\rceil_+,$$ $$B_*=(6R_*+1)U,\quad M_*=\left\lceil(H+3)\log x\,10^{6R_*+1}\right\rceil_+,\quad G_*=(M_*+5)B_*,$$ $$N_*=\left\lceil\max\{6\exp(1)G_*\delta_1,(H+3)\log_2 x\}\right\rceil_++1.$$ Set $$a_*=xb,\qquad p_*=k^2x^{26},\qquad \Lambda_*=C_\Lambda N_*^2\log a_*,$$ $$\rho_*= \frac{8n\delta_1x^\varepsilon\Lambda_*}{k} +\frac{C_\rho C_N\log x\,\Lambda_*}{k}.$$ The relevant primes form the set $$\mathcal P=\left\{p\text{ prime}:p\nmid c_E,\ \left(\frac{-d}{p}\right)=-1,\ \left(\frac{p}{q}\right)=-1\right\}.$$ For $p\in\mathcal P$, put $$L_1(p)=\left\lceil\log_p\bigl((kx^{26})^4\bigr)\right\rceil_+, \qquad L_2=2\max\bigl(\{0\}\cup\{L_1(p):p\in\mathcal P\}\bigr).$$ This maximum is finite: $p\ge2$ bounds $L_1(p)$ by $\lceil\log_2((kx^{26})^4)\rceil_+$. Let $\mathcal P_*$ consist of the primes $p\in\mathcal P$ such that $p<X'$, $\nu_p\ge x^{\varepsilon/4}$, and, if $p\ge p_*$, there is no integer $d_0\ge1$ with $$X'(1-\rho_*)\le p^{d_0}\le X'(1+\rho_*).$$

For each $p\in\mathcal P_*$, let $z$ range over the chosen representatives $\{s(h_p,t):t\in A\}$ of $A/\langle h_p\rangle$. Associate to $z$ the subset and weight vectors $$T_z=\{i\in\{0,\ldots,\nu_p-1\}:z+ih_p\in TT\},\qquad \mathbf a_z(i)=\widetilde a(z+ih_p),\quad \mathbf b_z(i)=\widetilde b(z+ih_p).$$ The representatives included in the sum for $\Sigma(p)$ are exactly those satisfying the following three conditions, with $\nu=\nu_p$ and $T=T_z$. Write $$W_\nu(i,L)=\{(i+j)\bmod\nu:0\le j<L\}.$$

1. For every $0\le i<\nu$, $|T\cap W_\nu(i,L_2)|\le K_*$.
2. Put $v=\lfloor\nu/B_*\rfloor$. For every integer $0\le s_0<v$, there is an integer $0\le j\le M_*$ such that, for $s_1=(s_0+j)\bmod v$, each of the intervals of integers $$[s_1B_*+(c-1)U,\ s_1B_*+cU)\qquad(1\le c\le6R_*+1)$$ meets $T$ in the empty set when $c$ is odd and in exactly one even integer when $c$ is even. When $v=0$ this condition is vacuous.
3. For every $0\le i<\nu$, $|T\cap W_\nu(i,G_*)|\le N_*$.

For each such representative define $$\kappa_p(z)= \begin{cases} \min\{1,C_{\mathrm{II}}|T_z|R_*^2kx^{-26}\},&p<p_*,\\ \kappa^{\mathrm I}(p,\nu_p,T_z,\mathbf a_z,\mathbf b_z),&p\ge p_*. \end{cases}$$ Then $\Sigma(p)=m\sum_z\kappa_p(z)$, where $z$ ranges over these representatives. An empty sum is $0$.

**The zero-free-region conditions in (c).** For a real number $B>0$, a primitive real Dirichlet character $\chi$ of conductor $N$ satisfies the bound at $B$ if $$N\le B,\qquad L(s,\chi)\ne0\quad\text{whenever }\operatorname{Re}s>1-\frac1{400},\quad |\operatorname{Im}s|\le B.$$ Every character for which a bound is required below is nonprincipal; $L(s,\chi)$ denotes its entire continuation. Put $$\eta_q(a)=\left(\frac{-q}{a}\right),\qquad \eta_d(a)=\left(\frac{-d}{a}\right),\qquad \eta_8(a)=\left(\frac{2}{a}\right)\quad(a\ge1),$$ and let $Q_S^{\mathrm{odd}}$ be the largest odd divisor of $Q_S$. Evaluate $X_1,X_2$ at the $Y$ in (c). Require both of the following.

1. Every primitive Dirichlet character agreeing on integers coprime to $8qd$ with $\eta_q$ or $\eta_8\eta_q$ satisfies the bound at $8X_1$. Every primitive Dirichlet character agreeing there with one of $\eta_d$, $\eta_8\eta_d$, $\eta_d\eta_q$, $\eta_8\eta_d\eta_q$ satisfies the bound at $8X_1X_2$.
2. Let $\chi$ be any primitive real Dirichlet character of conductor $N$ for which there is a character $\psi:\operatorname{Gal}(E/\mathbb Q)\to\mathbb C^\times$ satisfying $$\chi(a)=\psi(\operatorname{Art}_E(a))\quad\text{for all }a\ge1\text{ coprime to }c_E.$$ If $d\mid N$, require the bound at $8Q_S^{\mathrm{odd}}X_1X_2$. If $q\mid N$ and $d\nmid N$, require the bound at $8Q_S^{\mathrm{odd}}X_1$.

**Refinements of a class.** For a class $\mathcal{C}$, the *first refinement* $\mathcal{C}'$ is the class of families in $\mathcal{C}$ that satisfy (a) to (g), and the *second refinement* $\mathcal{C}''$ is the class of families in $\mathcal{C}'$ that also satisfy (h), (i) and (j).
