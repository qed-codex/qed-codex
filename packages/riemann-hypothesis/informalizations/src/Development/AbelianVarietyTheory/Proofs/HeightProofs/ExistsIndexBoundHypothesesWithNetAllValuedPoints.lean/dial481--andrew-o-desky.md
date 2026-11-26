---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean",
  "declarations": [
    "GlobalTheory.InputsAtRecord.inputsNet_recPlus"
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

## Uniform constants for which the inputs of the lattice index bound hold at every stage of the moduli tower

[Theorem ARAK.0024](https://andrewodesky.com/rh/lean/GlobalTheory.InputsAtRecord.inputsNet_recPlus/)

**Summary.** There are a real number $C_L$ and two functions $C_q,Z_0\colon\mathbb R^2\to\mathbb R$, independent of all data, with the following property. For every choice of the global data, of the geometric record and of the numerical parameters described below, if the record satisfies the conditions (R) at stage $j$, the parameters satisfy the conditions (P), and $Z_0(C_A,C_K)\le z$, then the four groups of statements (I) to (IV) and the inequalities (V) hold.

**The data.**

*Global data.* Choose the ranks and host data of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), using its notation $k,m,t,n,r,f,E,q,d,g_0,g_1$ and its level-prime set. Write $p_1,p_2$ for the primes $p_\Delta,p'_\Delta$, and put $\rho_E=|d_E|^{1/[E:\mathbb Q]}$. Choose the member data of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), and write $\mathbb L$ for its coefficient field $K$. Assume the coefficient map $O\to\mathbb L$ is injective. In addition choose elements $\pi_0,\pi_1\in\mathcal O_E$ with $\pi_i\bar\pi_i=g_i$ and similar elements for the other prescribed integers, and a natural number $p$.

*Size parameters.* Real numbers $x>1$ and $0<\varepsilon<1/52$; we put $L=x^{\varepsilon}$, $b=e^{L}$ and $z=f\,r\,L$. A real number $\delta_2\in(0,1]$. Let $\lambda_1=\operatorname{Re}\,(L'/L)(1,\chi_d)$ for the quadratic character $\chi_d$ modulo $d$, and $\omega=\gamma+\log(2\pi/\rho_E)-\lambda_1$ with $\gamma$ Euler's constant. For real $C,A$ write $P(C,A)=Cz^{A}$ and $P_0(C,A)=C\,(fr+L+\log|d_E|+|\omega|)^{A}$.

*Geometric record.* For each stage $j\in\{1,\dots,m\}$: a scheme $X_j$, smooth and quasi-projective over a number field, which represents on reduced schemes a moduli problem of abelian schemes with an action of $\mathcal O_E$, a rigidified symmetric relatively ample line bundle, and two level structures, of a type fixed by a projective $\mathcal O_E$-module with a unimodular alternating form. A number field $F\subset\mathbb C$ containing all conjugates of $E$, whose ring of integers is identified with $O$. For each embedding $\sigma\colon F\to\mathbb C$, a finite family of domains with maps to complex points of $X_j$ carrying extra structure. Three further components, among them auxiliary moduli data, which were not expanded. The record is required to satisfy a list of some forty conditions, which has not been expanded. Stages $j<m$ are called *indefinite* and the stage $j=m$ *definite*.

*Forms at stage $j$.* A *weight* $w$ consists of, for each $\tau$ in a finite index set attached to the global data, non-increasing tuples $a^+_\tau\in\mathbb N^{k+j-1}$ and $a^-_\tau\in\mathbb N^{m-j}$, and an even integer $n_w\ge0$; weights are added and multiplied by natural numbers entrywise. The *size* of $w$ is $|w|=\deg w+f\max(m-j,1)\,r\,n_w+1$ with *degree* $\deg w=\sum_\tau(\sum_ia^+_{\tau,i}+\sum_ia^-_{\tau,i})$. Put $\dim_j=f\big((k+j-1)(m-j)+\binom{k+j-1}2+\binom{m-j}2\big)$. From the record the formalization builds, for each weight $w$:

- a finite-dimensional $F$-vector space $S_w$ of cusp forms of weight $w$ on $X_j$, inside a commutative ring in which the product of forms of weights $w,w'$ is a form of weight $w+w'$;
- for each $\sigma\colon F\to\mathbb C$ a norm $\|\cdot\|_\sigma$ on $S_w$; the *mean logarithmic norm* of $G\ne0$ is $h(G)=\frac1{[F:\mathbb Q]}\sum_\sigma\log\|G\|_\sigma$;
- for each finite place $\lambda$ of $F$ a set $\mathcal P_\lambda$ of points and for $y\in\mathcal P_\lambda$ a function $v_y$ from forms to $(-\infty,\infty]$ with $v_y(GG')=v_y(G)+v_y(G')$, $v_y(G+G')\ge\min(v_y(G),v_y(G'))$, and $v_y(aG)=v_\lambda(a)+v_y(G)$ for $a\in F^\times$;
- the $\mathcal O_F$-module $M_w=\{G\in S_w: v_y(G)\ge0\text{ for all }\lambda\text{ and }y\in\mathcal P_\lambda\}$ of *integral* forms;
- two $\mathcal O_F$-submodules $\Theta_w$ and $\Theta'_w$ of $S_w$, each consisting of the forms of $S_w$ in the $\mathcal O_F$-span of a given set of forms;
- linear maps $G\mapsto G_{\gamma,\chi}$ on $S_w$, indexed by a label $\gamma$ and a matrix $\chi$ of size $m-j$ over $E$.

The constructions of the cusp forms, the norms, the points, the two sets of forms and the maps $G\mapsto G_{\gamma,\chi}$ have not been expanded. In the conclusion the sets $\mathcal P_\lambda$ are enlarged by a second family of such functions, on which integral forms are also nonnegative.

*Numerical parameters.* Three weights $\kappa,w_L,w_F$ at stage $j$; natural numbers $T,n_P,n_W$; real numbers $h_0,C_2,A_2,C_T$ and $C_K,C_A,C_1,A_1,C_c,A_c,C_{Rc}$. Put $c=\rho_E^{7}\,P(C_2,A_2)\,(\deg w_L)^2/\min(g_0,g_1)$ and $w_0=w_F+\dim_j\cdot w_L$.

*Derived objects.* Four elements $s_W,s_F,s_0,s_K\in\mathcal O_F$ and a function $\nu$ from the finite places of $F$ to $\mathbb R$, given by explicit formulas in the data which have not been expanded. The lattice $W=s_W\Theta_{w_L}$ and, for $y\in\mathcal P_\lambda$, the *depth* $\operatorname{dp}(y)=\inf_{G\in W}v_y(G)$. For a weight $w$ and $s\in\mathcal O_F$, the lattice $\Theta'_w(s)=s\,(g_0g_1)^{f r n_w}\,\Theta'_w$. For a finite place $\lambda$ write $\ell(\lambda)=\log N(\lambda)/[F:\mathbb Q]$.

**Hypotheses.**

(R) *Conditions on the record at stage $j$.* Seven conditions: a list of nine conditions on the auxiliary moduli data (not expanded); two normalisations of the record (not expanded); the product of $q$, $d$, the level primes and one further integer of the data is positive; a component of the auxiliary data equals $p$; the level ideal of the record is contained in two principal ideals determined by $\pi_0,\pi_1$; and $F$ is algebraically closed in a ring attached to every component of $X_j$.

(P) *Conditions on the parameters.* All of the following.

- $x\le fr\le x^{C_A}$; $\log|d_E|\le C_Afr L$; $x^{-\varepsilon}\le\delta_2$; $\log g_i\le9L+1$; $|\lambda_1|\le x^{\varepsilon}$; $|\omega|\le C_AL$; $\log p_i\le L$; $2fm\le\rho_E$.
- Twenty-six explicit conditions tying the weights to $T,n_P,n_W,h_0$: among them $n_\kappa=r+t=n_P+Tn_W$; $n_{w_F}=n_P$, $n_{w_L}=n_W$ and $w_F=\kappa-Tw_L$ on the entries $a^\pm$; $w_L$ obtained from $\kappa$ by floor division of its gaps by $T+\dim_j+2$; lower bounds on the gaps and last entries of $\kappa$; $|\kappa|\le C_Kkfb$; $|w_L|\le C_Kkfb/T$; lower bounds on $T$ and $n_W$; $\log[F:\mathbb Q]$ and $\log|d_F|/[F:\mathbb Q]$ bounded by an explicit multiple of $L$; and ten inequalities involving $C_1$ and $z$, among them $1000\le C_1$ and $C_1^{20}\le z$.
- Six explicit inequalities between $\rho_E$, $P(C_2,A_2)$, $\deg w_L$, $T$, $\dim_j$, $\min(g_0,g_1)$, $c$ and the integers of the global data; six explicit inequalities between $b$, the sizes of $\kappa,w_L,w_F$, $T$, $P(C_2,A_2)$, $\rho_E$ and $g_i$; and $T\le x^{C_T}$.
- $C_1=C_2$, $A_1=A_2$, $C_c=C_2$, $A_c=A_2$, $C_{Rc}=7$, $12\le A_2$; $4C_K\le P(C_2,A_2)^2f$; $f^2\le\rho_E$; $8\le r$; $3\le\deg w_L$; and $\Phi(n_W)\le P(C_2,A_2)$ for an explicit function $\Phi$ of $n_W,m,f,r$.
- A condition stating that $(C_2,A_2)$ arise from one of the formalization's choices of parameters (not expanded).

**Conclusion.**

(I) *Base statements.*

1. (a) The scalars $s_W,s_F,s_0,s_K$ are nonzero; for every $\sigma$, $\log|\sigma(s_W)|\ge\max\big(0,\tfrac12\deg w_L\cdot\log\min(g_0,g_1)\big)$; and for one $p_i$ and $C=\log(g_0g_1)+\log(f^2qd)+2\log p_i$: $\log|\sigma(s_W)|\le C|w_L|$, $\log|\sigma(s_F)|\le C|w_F|$, $\log|\sigma(s_0)|\le2C|w_0|$, $\log|\sigma(s_K)|\le2C|\kappa|$. (b) For a real number $G$ given by an explicit expression in the data, the same $p_i$ and a parameter at most $1009z$: there is a finite set of forms generating $W$ over $\mathcal O_F$, with $\log\|\cdot\|_\sigma\le m_\sigma$ on the set and $\frac1{[F:\mathbb Q]}\sum_\sigma m_\sigma\le G|w_L|$; and there are finite subsets of $\Theta'_{w_F}(s_F)$, $\Theta'_{w_0}(s_0)$, $\Theta'_\kappa(s_K)$ spanning $S_{w_F}$, $S_{w_0}$, $S_\kappa$ over $F$ with $h\le G|w_F|$, $G|w_0|$, $G|\kappa|$ respectively. (c) $W$, $\Theta'_{w_F}(s_F)$, $\Theta'_{w_0}(s_0)$ and $\Theta'_\kappa(s_K)$ consist of integral forms. (d) $\nu\ge0$, $\nu$ has finite support, and $\sum_\lambda\nu_\lambda\ell(\lambda)\le\big(2L+\log(g_0g_1)+\log(f^2qd)+4\big)|w_L|$. (e) There is an integral form of the weight $w_2$ with $w_2+w_F=(\dim_j+4)w_L$, and at an indefinite stage also one of the weight $w_1$ with entries $a^\pm(w_1)=2a^\pm(w_L)$ and $n_{w_1}=2n_W-2$, whose product with every nonzero cusp form is nonzero and whose $\log\|\cdot\|_\sigma$ is at most an explicit multiple of $\dim_j|w_L|$. (f) The conditions of the first three items of (P) hold.
2. $M_\kappa$ is a lattice in $S_\kappa$: it is finitely generated over $\mathcal O_F$ and spans $S_\kappa$.
3. Every nonzero $G\in M_\kappa$ has $h(G)\ge-P_0(C_L,2)\,(1+\log|\kappa|)\,|\kappa|$.
4. At an indefinite stage: let $S^\circ_\kappa\subset S_\kappa$ be the common kernel of the maps $G\mapsto G_{\gamma,\chi}$ over the pairs $(\gamma,\chi)$ for which some nonzero vector $\xi$ of a dual lattice attached to $\gamma$ has $\sum_\tau\operatorname{Re}\tau(\chi(\xi,\xi))\le\tfrac12\rho_E^{7}\,Tc\,(2f(m-j))^2(m-j)$; let $Q=M_\kappa/(M_\kappa\cap S^\circ_\kappa)$ and $\varrho$ its rank. Assume $\log[F:\mathbb Q]\le z^4$, $\log\big(|d_F|^{1/[F:\mathbb Q]}\big)\le z^4$, $n_\kappa=r+t$, $a^+_{\tau,k+j-1}\ge1$ for all $\tau$, $|\kappa|\le C_Kkfb$, $0<T$, $0<c$ and $Tc\le1$. Then there is a finitely supported function $\beta\ge0$ on the finite places of $F$ with $\sum_\lambda\beta_\lambda\ell(\lambda)\le C_q(C_A,C_K)\,z^4|\kappa|$ such that, for all $\theta_1,\dots,\theta_\varrho\in M_\kappa$ which together with $S^\circ_\kappa$ span $S_\kappa$ over $F$ and satisfy $h(\theta_i)\le z^4|\kappa|$, there is a finitely supported function $\mu$ with $\sum_\lambda\mu_\lambda\ell(\lambda)\le\varrho\,C_q(C_A,C_K)\,z^4|\kappa|$ such that the localisation at each $\lambda$ of $Q/\langle\theta_1,\dots,\theta_\varrho\rangle$ has finite length at most $\mu_\lambda+\varrho\beta_\lambda$.
5. $\|GG'\|_\sigma\le\|G\|_\sigma\|G'\|_\sigma$ for forms $G,G'$ of any two weights and every $\sigma$.

There exist a family $\mathcal G$ and real numbers $G_c,P_H,P_{rw},P_{et},P_d$ such that (II), (III) and (IV) hold. The family $\mathcal G$ consists of forms $u_1,\dots,u_N\in S_{w_L}$, forms $\theta'_1,\dots,\theta'_\Delta\in S_{w_F}$, a natural number $\ell_0$ with a form $\eta$ of the weight having all $a^\pm=0$ and $n=2\cdot5^4\,r\,\ell_0$, real numbers $m_\sigma$, and further components on which (II) to (IV) impose nothing.

(II) *A net of evaluations.* For each $\sigma\colon F\to\mathbb C$ there are a finite set $N_\sigma$ and $\sigma$-semilinear maps $\operatorname{ev}_y\colon S_\kappa\to\mathbb C$ ($y\in N_\sigma$), exchanged by complex conjugation between $\sigma$ and $\bar\sigma$, such that $\tfrac14\|G\|_\sigma\le\max_{y\in N_\sigma}|\operatorname{ev}_y(G)|\le\|G\|_\sigma$ for all $G\in S_\kappa$, and $\log(16|N_\sigma|)\le1041\,z^3(1+\log|\kappa|)$. For one embedding $\sigma_0$: $F$-linearly independent forms have $\mathbb C$-linearly independent vectors $(\operatorname{ev}_y(G))_{y\in N_{\sigma_0}}$, and $\log|N_{\sigma_0}|\le P_d$.

(III) *The family.*

- $u_1,\dots,u_N$ are integral and generate $W$ over $\mathcal O_F$; $\log N\le P_{rw}(|w_L|-1)$; $\log\|u_k\|_\sigma\le m_\sigma$ and $\frac1{[F:\mathbb Q]}\sum_\sigma m_\sigma\le G_c|w_L|$.
- $\theta'_i\in\Theta'_{w_F}(s_F)$ and $h(\theta'_i)\le G_c|w_F|$ for all $i$.
- At an indefinite stage: $\ell_0>0$, $\eta\ne0$, the product of $\eta$ with every nonzero cusp form is nonzero, and $\log\|\eta\|_\sigma\le200000\,z^2\,\ell_0$ for all $\sigma$.
- $1041\,z^3(1+\log|\kappa|)\le P_d$; $G_c\le z^4$; $G_c$ is at least an explicit expression in $L$, $z$, the degrees and discriminants of $F$ and $E$, $g_0,g_1$, $q$, $d$ and $p_1,p_2$; and eighteen explicit inequalities between $G_c,P_H,P_{rw},P_{et},P_d$, $P_0(C_L,2)$, $C_K$, $C_q(C_A,C_K)z^4$, $\rho_E$, $P(C_2,A_2)$, $z^4$, $\log|\kappa|$, $\dim_j$ and the degree and discriminant of $F$.
- With $D$ the dimension of the $F$-span of $M_\kappa$: $\binom{T-1}{\dim_j}\,\Delta\le D$; $\varrho\le22\dim_j^2D/T$; and at each finite place $\lambda$ the span of the second set of products in the next item has dimension at most $22\dim_j^2D/T$ over a field $K_\lambda$ attached to $\lambda$ and $N$.
- At each finite place $\lambda$: the classes of the $\theta'_i$ form a basis over $K_\lambda$ of a module $\mathcal M_\lambda$ attached to $\lambda$, the $u_k$ and the weight $w_F$; and the image of $S^\circ_\kappa$ lies in the $K_\lambda$-span of two sets of products: the $\theta'_i$ times monomials of degree $T$ in $\dim_j+1$ elements built from the $u_k$, and the elements of $\Theta'_{w_0}(s_0)$ times monomials of degree $T-\dim_j$. The field $K_\lambda$, the module $\mathcal M_\lambda$ and these elements have not been expanded.

(IV) *Points and heights.*

- For every $\lambda$ and every $y$ in the enlarged set $\mathcal P_\lambda$: at an indefinite stage $v_y(\eta)\ge0$ and, if $v_y(\eta)<\infty$, $\operatorname{dp}(y)\le\nu_\lambda+\frac{c}{2\ell_0}v_y(\eta)$; at the definite stage $\operatorname{dp}(y)\le\nu_\lambda$.
- For every $\lambda$ there are a form $g_\lambda\in S_{w_F}$ and, for each point $\zeta$ of an algebra $A_\lambda$ attached to $\lambda$ and the $u_k$, a point $y_\zeta\in\mathcal P_\lambda$ and an integer $a_\zeta$, such that: $A_\lambda$ is finite-dimensional over $K_\lambda$ and reduced, and $\mathcal M_\lambda$ is free of rank one over $A_\lambda$ on the class of $g_\lambda$; $\operatorname{dp}(y_\zeta)$ is finite, and so is $v_{y_\zeta}(\eta)$ at an indefinite stage; $a_\zeta=e_\zeta v_{y_\zeta}(g_\lambda)$ and $e_\zeta\operatorname{dp}(y_\zeta)\in\mathbb Z$, where $e_\zeta$ is the order at $\zeta$ of a uniformiser at $\lambda$; the order at $\zeta$ of the class of a form $G$ of weight $w+k\,w_L$ ($w$ the zero weight or $w_F$) is $e_\zeta\big(v_{y_\zeta}(G)-k\operatorname{dp}(y_\zeta)\big)$; and a lifting property holds. Let $I_\lambda$ be the length of the quotient of a ball in $\mathcal M_\lambda$ by the span of the $\theta'_i$. Then every $I_\lambda$ is finite, $\sum_\lambda I_\lambda\ell(\lambda)$ converges, and $$2\sum_\lambda I_\lambda\ell(\lambda)\le\Delta\log\Delta+2\sum_ih(\theta'_i)+\tfrac83\dim_j(\dim_j+4)\,\Delta P_{rw}|w_L|+2(\dim_j+4)(\dim_j+1)\,\Delta\,(2G_c+6P_H)|w_L|.$$ At an indefinite stage, moreover, the following sum over $\lambda$ converges and $$\frac1{\ell_0}\sum_\lambda\Big(\sum_\zeta e_\zeta f_\zeta\,v_{y_\zeta}(\eta)\Big)\ell(\lambda)\le2\cdot5^4r\Big((\dim_j+1)\Delta(2G_c+6P_H)|w_L|+\tfrac43\dim_j\Delta P_{rw}|w_L|\Big)+\Delta P_{et},$$ with $f_\zeta$ the residue degree at $\zeta$. The algebra $A_\lambda$, the ball and the lifting property have not been expanded.

(V) $\Phi(n_W)\le P(C_2,A_2)$; $\log|\sigma(s_W)|\ge\tfrac12\deg w_L\cdot\log(g_0g_1)$ for every $\sigma$; $f^2\le\rho_E$; $8\le r$; $3\le\deg w_L$.

**The three constants.** They are obtained from three theorems, whose statements were read.

- $C_L>0$ is such that (I.3) holds for every stage and every weight of every record satisfying its conditions, whenever the first item of (P) holds.
- $C_q$ is such that (I.4) holds at every indefinite stage of every such record, whenever (P) holds and $M_\kappa$ is a lattice.
- $Z_0$ is such that $Z_0(C_A,C_K)\le z$ together with (P) implies $G_c\le z^4$ and the eighteen inequalities of (III), for explicit values of $G_c,P_H,P_{rw},P_{et},P_d$. The proof takes $Z_0(a,b)=C_L+|b|+|C_q(a,b)|$.
