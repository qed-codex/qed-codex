---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean",
  "declarations": [
    "UpperTheory.Top.topDesWin"
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
