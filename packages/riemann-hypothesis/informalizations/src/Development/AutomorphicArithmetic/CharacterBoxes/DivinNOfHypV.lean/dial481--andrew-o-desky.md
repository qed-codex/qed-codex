---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean",
  "declarations": [
    "UpperTheory.Top.FamilyClassConnected",
    "UpperTheory.Top.HypV"
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

## Compatible arithmetic data on intervals

[Theorem AGR.0100](https://andrewodesky.com/rh/lean/UpperTheory.Top.topDesWin/)

Under Hypotheses (family existence), (cohomological and character conditions), and (uniform comparisons) below, the arithmetic data and counting inequalities can be realized simultaneously on arbitrarily large intervals.

Fix a primitive Dirichlet character $\psi$ of order $o$. Let $\mathcal P_\psi$ be the set of primitive characters inducing the powers $\psi^j$, $0\le j<o$, and put $c=(3o+1)^{-1}$. For a nonprincipal primitive character $\chi$ and $y>0$, define $$\kappa_\chi=\frac{L'(1,\chi)}{L(1,\chi)},\qquad g_\chi(y)=\sum_{1\le r\le y}\Lambda(r)\chi(r)(y/r-1)+y\kappa_\chi,$$ where $\Lambda$ is the von Mangoldt function. For the principal primitive character, of modulus $1$, define $$g_1(y)=\sum_{1\le r\le y}\Lambda(r)(y/r-1)-y\log y+(1+\gamma_{\!E})y,$$ where $\gamma_{\!E}$ is Euler's constant.

There are fixed nonnegative bounds $E_D,E_P$ and $\varepsilon_1>0$ such that, for every $0<\varepsilon<\min\{\varepsilon_1,1/52\}$, one can choose a family $\mathcal F\in\mathscr E$ and real constants $K,c_H,e_K,C_L,x_0$ with $x_0\ge3$. Let $\mathcal W$ be the occupied scales of $\mathcal F$ in $[3,\infty)$. Hypothesis (cohomological and character conditions) below gives $$\forall Y_0\in\mathbb R\quad\exists Y\ge\max\{1,Y_0\}:\qquad [Y,Y^{3/2}]\subset\mathcal W.$$ For every $x\in\mathcal W$ with $x\ge x_0$, the following data are obtained simultaneously from $\mathcal F$. The constants $K,c_H,e_K,C_L,x_0$ are independent of $x$.

1. There are a finite abelian group $H$, written additively, and a cyclic subgroup $H_0\le H$ of index $o$. Put $$n=|H|,\qquad G=(\mathbb Z/2\mathbb Z)^2\times H,\qquad \iota(t)=((0,0),t),$$ $$\Phi=\{((0,\beta),h):\beta\in\mathbb Z/2\mathbb Z,\ h\in H\},\qquad s_0=((1,0),0),\qquad c_0=((1,1),0),$$ $$\chi_C((\alpha,\beta),h)=(-1)^\alpha,\qquad P_t(g)=c_0+g+\iota(t).$$ Here $(-1)^\alpha$ is $1$ at $\alpha=0$ and $-1$ at $\alpha=1$. Write $\widehat G=\operatorname{Hom}(G,\mathbb C^\times)$, with trivial character $1$.

There are an integer $R\ge1$ and a surjective homomorphism $\rho:(\mathbb Z/R\mathbb Z)^\times\to G$. For $\gamma\in\widehat G$, let $\chi_\gamma$ be the primitive character inducing $\gamma\circ\rho$, and set $$h_\gamma(y)=g_{\chi_\gamma}(y),\qquad \kappa(\gamma)=\begin{cases}\kappa_{\chi_\gamma},&\gamma\ne1,\\0,&\gamma=1.\end{cases}$$ For every prime $p$ there are $I_p\le G$ and $F_p\in G$ such that, writing $v_p(r)$ for the exponent of $p$ in $r$, $$\prod_{p\mid r}\frac1{|I_p|}\sum_{z\in I_p}\gamma(v_p(r)F_p+z)=\chi_\gamma(r) \qquad(r\ge1,\ \gamma\in\widehat G).$$ There are primes $q\equiv3\pmod8$, $d\equiv7\pmod{16}$ with $\left(\frac{-d}{q}\right)=1$, and a finite set $S$ of primes satisfying $$2,q\in S,\qquad d\notin S,\qquad I_d=\{0,s_0\},$$ $$I_p=\{0\}\quad(p\notin S\cup\{d\}),\qquad I_p\subset\Phi,\quad F_p\in\Phi\quad(p\in S).$$

Define $$\Psi_0=\{\gamma\in\widehat G:\gamma(\iota(u))=1\text{ for all }u\in H_0\},\qquad \mathcal K=\{\gamma\in\widehat G:\chi_\gamma\in\mathcal P_\psi\}.$$ Every member of $\mathcal P_\psi$ occurs as $\chi_\gamma$, and $$\mathcal K\subset\Psi_0,\qquad \gamma(s_0)=1\quad(\gamma\in\mathcal K).$$ The only member of $\mathcal K$ trivial on $\iota(H)$ is $1$. Moreover, $$|\kappa(\gamma)|\le4\log x,\qquad |h_\gamma(x)|\le x^{1/2+\varepsilon} \qquad(\gamma\in\Psi_0\setminus\mathcal K).$$

2. There are sets $T\subset H$, $T_2\subset H_0$, integers $m,N\ge0$, a positive integer $k$, nonnegative reals $\eta,\theta$, a function $a:H\to\mathbb R$, and weights $w_{u,j}:G\to\mathbb R$ for every $u\in H$ and $0\le j<m$. Set $$L=x^\varepsilon,\qquad b=e^L,\qquad a_{\rm ref}=xb,\qquad X'=\exp(x^{\varepsilon/3}),\qquad b'=xb/X'.$$ Write $a_t=a(t)$. The size conditions are $$|T|\ge\tfrac12nx^{-\varepsilon/8},\qquad |T_2|/n\ge x^{-\varepsilon},$$ $$x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2},\qquad xm\le k\le n^2x^{1/2-\varepsilon}.$$ For every $h\in H$, $$\left||T\cap(h+H_0)|-\lambda(h)|T|\right|\le x^{-1+\varepsilon}|T|,\qquad \lambda(h)=\begin{cases}4c,&h\in H_0,\\3c,&h\notin H_0.\end{cases}$$ For $t\in T$, $|a_t/b-x|\le1$. For every $u\in H$ and $0\le j<m$, the function $w_{u,j}$ is positive on $\Phi$, takes values in $[b,b+\eta+1]$ on $\{((0,1),s+u):s\in T_2\}$, and is at most $2b'$ at the other points of $\Phi$. For every such $u,j$, $$b'X'=xb,\qquad a_t/w_{u,j}(g)\le N\quad(t\in T,\ g\in\Phi),$$ $$|h_\gamma(y)|\le y\theta\quad(\gamma\in\widehat G,\ y\ge X'/3),$$ $$2(2n)(x+1)\theta\le1/x,\qquad6(2n)(x+1)(\eta+1)\le b/x.$$
3. There are choices of all the further real parameters and nonempty finite sets in ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) satisfying its eleven numerical conditions and seven size conditions. The translation index set is $H$, its translation map is the identity on $H$, and its group, arithmetic data, $\kappa,x,\varepsilon,n,m,b,b',k,T,T_2,a_t,w_{u,j},N$ are the data just specified. Its real parameter $a$ is $a_{\rm ref}$, its value of $f$ is $2n$, and its error exponents satisfy $$0\le e_D\le E_D,\qquad0\le e_P\le E_P.$$ The bounds $E_D,E_P$ are independent of $\varepsilon,x$ and the translation. The other bounding constants in the seven size conditions are fixed after $\varepsilon$ and the family, before $x$. In particular its nonnegative budgets $B_0,N_c$ satisfy $$B_0\le2nmbx^\varepsilon,\qquad N_c\le|T_2|kbx^{2\varepsilon}/n^2.$$

## Properties of field data, their supply condition and their classes of families

[Definition / hypothesis ANT.D267](https://andrewodesky.com/rh/lean/UpperTheory.Top.FReq/)

This entry defines four notions that occur together: a property of field data, the supply condition for such a property, the class of families that the property defines, and the kernel bound for a family. The notation for fields is that of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)); families, members, data and size data are those of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)).

A scale $s=(x,\varepsilon,J)$, with $x>1$, $0<\varepsilon<1/52$ and $J\ge1$, and the numbers $\mathcal L=x^{\varepsilon}$, $b=e^{\mathcal L}$, $X'=\exp(x^{\varepsilon/3})$ and $\delta_1=x^{-\varepsilon/8}$ formed from it are those of the second of these entries.

**Property of field data.** A *property of field data* is a property $G(s,\mathfrak E,T,t)$ of a scale $s$, data $\mathfrak E$ satisfying Hypothesis (abelian CM field with reciprocity map) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), a finite subset $T$ of the group $A$ of $\mathfrak E$, and an integer $t\ge0$. Data satisfying Hypothesis (fields and Galois data) of the same entry contain such $\mathfrak E$, $T$ and $t$. We say that $G$ *holds at a member* $(x,i)$ of a family when $G(s,\mathfrak E,T,t)$ holds for the scale $s$ of the size data $L(x,i)$ and for the data $\mathfrak E$, the set $T$ and the integer $t$ of the datum $D(x,i)$.

**The class of families of a property.** Let $G$ be a property of field data and let $\lambda$ be a real number. The class $\mathcal E(G,\lambda)$ consists of the families $\mathcal F$, of any parameter, with the following two properties.

1. For every real number $y$ there is a real number $Y\ge\max\{y,1\}$ such that every $x$ with $Y\le x\le Y^{\lambda}$ is an occupied scale of $\mathcal F$, in the sense of ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)).
2. $G$ holds at every member $(x,i)$ of $\mathcal F$ with $x>x_1$.

**The supply condition.** Let $\lambda$ be a real number and let $G$ be a property of field data. The *supply condition for $G$ with exponent $\lambda$* is the following statement. For every $\varepsilon$ with $0<\varepsilon<1/52$ there are real numbers $$C_2,\qquad C_8\ge1,\qquad C_5>0,\qquad c_6>0,\qquad C_b>0,\qquad x_0,\qquad J\ge1$$ and a set $\mathcal W\subseteq\mathbb R$ such that:

- for every real number $y$ there is $Y\ge\max\{y,1\}$ with $[Y,Y^{\lambda}]\subseteq\mathcal W$;
- for every $x\in\mathcal W$ with $x>1$ and $x\ge x_0$ there are data satisfying Hypothesis (fields and Galois data) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), whose real constant is the number $C_2$ above, and a natural number $q_0$, such that conditions 1 to 16 below hold for the scale $s=(x,\varepsilon,J)$, and $G(s,\mathfrak E,T,t)$ holds for the data $\mathfrak E$, the set $T$ and the integer $t$ contained in them.

In conditions 1 to 16 the symbols $A,n,n_0,o,q,d,Q_S,Q=Q_Sqd,E,E_0,\alpha,k,m,t,f=2n,r=k+m-1,g_0,g_1,p_\Delta,p'_\Delta,\mathcal P_{\rm lev},\mathfrak c,s_0,T,T_2,L_w$ are those of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), and $\mathcal L,b,X',\delta_1$ are formed from $s$. The Kronecker symbol $\left(\frac{D}{a}\right)$ is the one defined in ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)). For a primitive Dirichlet character $\chi$, the function $g_\chi$ and the number $\kappa_\chi=L'(1,\chi)/L(1,\chi)$, for $\chi$ nonprincipal, are those of ([Compatible arithmetic data on intervals](https://andrewodesky.com/rh/lean/UpperTheory.Top.topDesWin/)).

*The ranks.*

1. $x^{2+8\varepsilon}\le n\le2x^{2+8\varepsilon}$, $\ \sqrt{x\delta_1}\le m\le2\sqrt{x\delta_1}$ and $x^{9/2+10\varepsilon}\le k\le2x^{9/2+10\varepsilon}$.
2. $r+t=8fr+4+\lceil x^{377}\rceil\,n_W$, where $n_W=8\bigl\lceil\tfrac{10}{8}\,r\bigl(f+f^2(k-1)^3\mathcal L^2/m\bigr)\bigr\rceil$.

*The primes $q$ and $d$.*

3. There is a real number $Y$ with $x^{1/J}\le Y\le x$ such that, with $X_1=\exp(Y^{\varepsilon/5})$ and $X_2=\exp\bigl(Y^{\varepsilon/5}(\log Y)^2\bigr)$, $$\sqrt{X_1}<q\le X_1,\qquad\sqrt{X_2}<d\le X_2,\qquad\log Q\le2Y^{\varepsilon/5}(\log Y)^2,$$ $\left(\frac{-d}{p}\right)=1$ for every prime $p\le Y^{\varepsilon/5}$, and the two zero-free-region conditions in (c) of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)) hold for this $Y$ and for $q$, $d$, $Q_S$, $E$ and $\alpha$.
4. Every primitive Dirichlet character $\chi$ that agrees on the integers coprime to $8qd$ with $a\mapsto\left(\frac{-q}{a}\right)$, with $a\mapsto\left(\frac{-d}{a}\right)$ or with their product satisfies $$|g_\chi(x)|\le x^{1/2+\varepsilon},\qquad|\kappa_\chi|\le C_5\log x.$$
5. The quadratic character $\chi_d$ modulo $d$ satisfies $|\operatorname{Re}\kappa_{\chi_d}|\le x^{\varepsilon}$.

*The sets $T$ and $T_2$.*

6. $\tfrac12\delta_1n\le|T|\le2\delta_1n$.
7. $x^{-\varepsilon}n\le|T_2|$, $\ 4L_w|T_2|\le n_0$, and $$\frac{n_0\exp\bigl(-C_2\sqrt{\log n_0\,\log L_w}\bigr)}{L_w}\le|T_2|.$$
8. $L_w=10\lceil405\log x\rceil+2\lceil30/\varepsilon\rceil+22$.

*The primes of $\mathcal P_{\rm lev}$.*

9. $\mathcal P_{\rm lev}=\{g_0,g_1,p_\Delta,p'_\Delta,q_0\}$, and every element of $\mathcal P_{\rm lev}$ belongs to the split class of rational primes.
10. For $i=0,1$: $(kb)^8\le g_i\le2(kb)^8$, $\ g_i\equiv1\pmod Q$, and there is $\pi\in\mathcal O_E\cap E_0$ with $\pi\bar\pi=g_i$ and $\pi-1\in Q\mathcal O_E$.
11. $p_\Delta$ and $p'_\Delta$ are at most $Q^{C_8}$, are congruent to $1$ modulo $\operatorname{lcm}(15,Q)$, and each of them has $[E:\mathbb Q]$ prime ideals of $\mathcal O_E$ above it.
12. $q_0$ is prime, $q_0\equiv1\pmod Q$, $q_0\le Q^{C_8}$ and $q_0\notin\{p_\Delta,p'_\Delta\}$.
13. The sets $\mathcal B(r,g_0)$ and $\mathcal B(r,g_1)$ are disjoint, where $$\mathcal B(r,g)=\{g\}\cup\{\ell\text{ prime}:g^a<\ell^{4v_\ell(g^a-1)}\text{ for some }1\le a\le r\}.$$

*Further conditions on the fields.*

14. $\mathfrak c=\mathcal O_{E_0}$, $\ \lfloor x^{\varepsilon/(5J)}\rfloor\le s_0$, $\ J\le C_8$, $\ o\le C_8$ and $Q_S\le C_8n$.
15. Let $\chi$ be a primitive Dirichlet character for which there is a character $\psi\colon\{\pm1\}^2\times A\to\mathbb C^\times$ with $\chi(a)=\psi(\alpha(a))$ for every integer $a\ge1$ coprime to $Q$. Then $$|g_\chi(y)|\le y\exp\bigl(-c_6x^{\varepsilon/8}\bigr)\qquad\text{for every }y\ge X'/3.$$
16. For a prime $p\nmid Q$ let $h_p\in A$ be the third coordinate of $\alpha(p)$ and $\nu_p$ its order. Let $\mathcal P_x$ be the set of primes $p<X'$ of the inert class with $\nu_p\ge x^{\varepsilon/4}$. For $p\in\mathcal P_x$ and $t\in T$, let $z_p(t)$ be the element of the coset $t+\langle h_p\rangle$ with the least label, and call $t$ *bad at $p$* when $z=z_p(t)$ fails one of the conditions 1 to 3 on a representative in the paragraph "The weighted prime sum in (N4)" of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)), formed with $\nu=\nu_p$, with $T_z=\{0\le i<\nu_p:z+ih_p\in T\}$ and with the numbers $K_*,R_*,U,B_*,M_*,G_*,N_*,L_2$ of that paragraph for the present $x,\varepsilon,k,q,d,Q$. Then $$\sum_{p\in\mathcal P_x}\frac{\log p}{p}\,\bigl|\{t\in T:t\text{ is bad at }p\}\bigr|\ \le\ 4C_b\,x^{-2}\,\delta_1n\sum_{p\in\mathcal P_x}\frac{\log p}{p}.$$

**The kernel bound for a family.** A family $\mathcal F$ *satisfies the kernel bound eventually* when there is a real number $x_0$ such that, at every member $(x,i)$ of $\mathcal F$ with $x\ge x_0$, the statement $\mathcal B\bigl(E,t,\sqrt b\bigr)$ of ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)) holds, where $E$ and $t$ are the field and the integer $t$ of the datum $D(x,i)$ and $b$ is formed from the scale of the size data $L(x,i)$.
