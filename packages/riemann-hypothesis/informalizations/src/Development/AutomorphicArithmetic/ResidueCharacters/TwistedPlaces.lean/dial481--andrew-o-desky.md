---
{
  "module": "src/Development/AutomorphicArithmetic/ResidueCharacters/TwistedPlaces.lean",
  "declarations": [
    "Formalism.MainNotions.TwistedPlaces.AdmT",
    "Formalism.MainNotions.TwistedPlaces.Tab"
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

## Local congruence tables

[Definition / hypothesis GC.D249](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)

Assume Hypothesis (fields and Galois data) in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), with its notation $A,n,e,a_0,q,d,Q_S,Q,E,F,E_0,\Sigma,T,T_2,a_*,g_0,g_1,p_\Delta,p'_\Delta$ and ranks $f,r,n_V,N_j,r_S$. Assume also that the generator and excluded primes split completely in $E$. The parameter and weight conditions below are imposed throughout.

The scale is $x>1$, $0<\varepsilon<1/52$, $J\ge1$, with $$L=x^\varepsilon,\quad b=\exp L,\quad a=xb,\quad X'=\exp(x^{\varepsilon/3}),\quad b'=a/X',\quad w_0=b'/(xn),\quad X''=a/w_0,\quad\varepsilon_0=\varepsilon/J.$$ Use the selected embeddings $\Sigma_{\rm top},\Sigma_{\rm thick},\Sigma_{\rm thin}$ in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). There are integer weights $a_v,b_v$ for $v\in T$, positive real numbers $S,\eta$, and $\delta_2=|T_2|/n\in(0,1]$. Let $h_E$ be the class number of $E$ and put $$H=\prod_{a=0}^1|\mathrm{GL}_r(\mathbb F_{g_a})|^f.$$

Let $K$ be a totally complex Galois number field with an embedding in $\mathbb C$ and an embedding $E\hookrightarrow K$ that commutes with complex conjugation. At its finite places $w$ choose types $\mu_w$, a distinguished type $\mu_0$, and alternatives $\mu_w^{\rm tw}$, with $\mu_w\in\{\mu_0,\mu_w^{\rm tw}\}$ and both assignments invariant under conjugation of $w$. A place is twisted when $\mu_w\ne\mu_0$. For every type $\mu$ and lift $1\le j\le m$, fix finite-dimensional complex Hermitian spaces $M_j,M_{\mu,j}$ and a linear map $\theta_{\mu,j}:M_{\mu,j}\to M_j$. Define $$d_j=\dim_{\mathbb C}\operatorname{im}\theta_{\mu_0,j}^{*},\qquad d_{j,w}=\dim_{\mathbb C}\operatorname{im}\theta_{\mu_w^{\rm tw},j}^{*}.$$ Let $\mathcal S$ be a finite set of finite places of $K$.

Use the local coefficient indices, rings, Hecke algebras, modules, eigenspaces and local congruence quantities of ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), with this coefficient field $K$ and these stages and places. In particular, use its $I(j,w)$, $V_i$, $V_{i,\pi}$, $m_{i,\pi}$, $\Lambda_i$, $\eta_i$, $c_{i,\pi}$ and normalized length $\operatorname{len}_{\ell_i}$. Require $Y_i\subseteq Z_i$ for every $i$.

A table consists of real numbers $s_{i,\pi}$, $A_{i,\lambda}$, $B_i$, $c_{j,\ell}$, $u_{j,\ell}$, subsets $\mathcal B_i$ of the places $\lambda$ of $E$, and a finite exceptional set $\mathcal X\subset\mathbb Z_{\ge0}$. For $C\in\mathbb R$, its local congruence table conditions are the following seventeen requirements.

First, away from $g_0,g_1$, for each twisted $i$, $$\eta_i\le\sum_{\pi\in Y_i}m_{i,\pi}\{c_{i,\pi}+v_{\ell_i}(H)\},\qquad \sum_{i\in I(j,v)}\sum_{\pi\in Y_i}m_{i,\pi}\le d_{j,v},\qquad d_{j,v}=d_j.$$ The dimension equality holds also at the generator primes. For every selected $\pi$ at a twisted index away from the generator primes, $$c_{i,\pi}\le s_{i,\pi}+\sum_{\lambda\mid\ell_i}A_{i,\lambda}+W_{\ell_i}+v_{\ell_i}(h_E)+B_i+\ell_i^{-2},\qquad W_\ell=\sum_{1\le a<t}s_{\ell,a}.$$ Here $s_{\ell,a}=h_{\ell,a}$, the nonnegative rational numbers with their finite-localization-length comparison in ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)). Away also from $\mathcal P_0,q,d$, $$B_i\le Cfn t^2n_VL^2.$$ At every twisted index and every $\pi\in Y_i$, $s_{i,\pi}+\ell_i^{-2}\le\nu_{\ell_i}+2\ell_i^{-2}$, and $u_{j,\ell}+\ell^{-2}\le2\ell^{-2}$ at the generator primes. For a prime $\ell$, let $\chi_\ell:\operatorname{Gal}(\overline E/E)\to\mathbb Z_\ell^\times$ be the cyclotomic character and define $$\nu_\ell=\min\{a\in\mathbb Z_{\ge0}:\exists\gamma,\ \ell^{a+1}\nmid\chi_\ell(\gamma)^{tr}-1\},$$ with value zero if the set is empty; set $\nu_\ell=0$ for nonprime $\ell$.

The next five requirements bound the $A_{i,\lambda}$ separately at primes split in the distinguished imaginary quadratic field, inert primes below $\ell_A$ with large order, inert primes at least $\ell_A$, and inert primes below $\ell_A$ with small order, together with a condition on the subsets $\mathcal B_i$. The precise inequalities are given in the conventions below.

For a twisted index with $\ell_i>\ell_*$ outside $\{g_0,g_1\}\cup\mathcal X$, require $A_{i,\lambda}=B_i=0$. Also require $$|\mathcal X|\le(|T|+2)(S+3\eta+t+8b/\ell_*+9),\qquad \ell\le3b\quad(\ell\in\mathcal X).$$ At $\ell\in\mathcal P_0$ or $\ell=3$ require $$\sum_{\lambda\mid\ell}A_{i,\lambda}+B_i\le Cfm b\log x+Cx^CL^2.$$ At $\ell=q,d$ require the same left side to be at most $$M_\ell=Cf\{r(b/\ell+S+t+\eta+L)+mb\}+C(frt)^CL,\qquad M_\ell\le2Cfm b.$$ For a prime $\ell$ and $1\le j\le m$, define the weighted defect $$\eta_{j,\ell}=\sum_{\substack{w\in\mathcal S\\\mu_w\ne\mu_0\\\operatorname{char}(w)=\ell}} \frac{\log Nw}{[K:\mathbb Q]}e(w/\ell)\sum_{i\in I(j,w)}\eta_i,$$ where $Nw$ is the absolute norm of the prime ideal of $w$ and $e(w/\ell)$ its ramification index. For $\ell=g_0,g_1$, require $\eta_{j,\ell}$ to be at most $$\log\ell\,d_j(c_{j,\ell}+u_{j,\ell}+W_\ell+v_\ell(h_E)+\ell^{-2}),\qquad c_{j,\ell}\le Cx^C\eta.$$ Finally require the polynomial bounds listed below.
