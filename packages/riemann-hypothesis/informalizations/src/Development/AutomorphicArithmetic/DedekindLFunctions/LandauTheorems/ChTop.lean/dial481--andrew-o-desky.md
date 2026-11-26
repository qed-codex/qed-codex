---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean",
  "declarations": [
    "Deduction.ch_top"
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

## Prime-power count bound

[Theorem ANT.0103](https://andrewodesky.com/rh/lean/Deduction.ch_top/)

Let $H$ be a finite abelian group of order $n$, written additively, and put $G=(\mathbb Z/2\mathbb Z)^2\times H$. Let $N,q,d\ge0$ be integers; for every integer $p\ge0$, let $I_p$ be a subgroup of $G$ and $F_p$ an element of $G$; and let $\kappa$ be a complex-valued function on the group $\widehat G$ of characters of $G$. From these data, ([Weighted prime-power count and its main term](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.characterSumData.ASK/)) defines the subset $\Phi\subset G$ of $f=2n$ elements, the character $\chi_C$ of $G$, the count $A(s,t,\omega)$ and its main term $M(s,\omega)$.

Let $U$ be a finite set, let $\tau:U\to H$ be a map, and for each $u\in U$ let $W_u$ be a nonempty finite set. Let $T$ and $T_2$ be subsets of $H$, let $m\ge0$ be an integer, let $a_t$ be a real number for each $t\in T$, and let $w:H\times\{0,\ldots,m-1\}\times G\to\mathbb R$ be a function. Let $$x,\ \varepsilon,\ a,\ b,\ b',\ k,\ L,\ \Lambda,\ B_0,\ N_c,\ v,\ \lambda_g,\ X'',\ e_K,\ K,\ \bar\delta,\ \bar\eta,\ \bar e$$ be real parameters and $$c_D,\ c_E,\ c_H,\ c_T,\ c_S,\ c_Q,\ c_P,\ e_D,\ e_P,\ c_*$$ real constants. For each $u\in U$, let $\mu^C_u,\mu^{C,-}_u,F_u,G_u,I_u,S_u,\delta_u,\eta_u,e_u$ be real numbers, and for each $u\in U$ and $z\in W_u$, let $d_{u,z},T_{u,z},h_{u,z},\mu^N_{u,z},\mu^{N,+}_{u,z},\mu^M_{u,z},\mu^{M,+}_{u,z},E_{u,z}$ be real numbers.

The conditions and the conclusion are written with the quantities that the introduction forms from these data: the functions $w_{u,j}$ on $G$ and their values $w_{u,j,\rho}$, the sums $\mathcal A_u$, $\mathcal M_u$ and $A_0$, the function $\phi$, and the numbers $\lambda_\Omega$, $P_0$, $s_u$, $U_u$ and $Q_{u,z}$.

Assume the following eleven numerical conditions. A condition that contains an index $u$, $z$, $z'$, $t$, $j$ or $\rho$ is assumed for all $u\in U$, all $z,z'\in W_u$, all $t\in T$, all integers $0\le j<m$ and all $\rho\in\Phi$.

1. $x,b,k,v>0$, $a,b'\ge0$, $f>0$, $a_t\ge0$, $w_{u,j,\rho},d_{u,z},T_{u,z}>0$, $\mu^N_{u,z}\le\mu^{N,+}_{u,z}$, $c_Q\ge0$, $\bar\delta<1$, $\bar\eta\ge0$, and $0\le\bar e\le1/4$.
2. The numbers $\mu^C_u$, $h_{u,z}$ and $F_u$ satisfy $$\mu^C_u+h_{u,z}-F_u\le\sum_{t\in T}\bigl[m\{\phi(a_t)-a_t\lambda_\Omega\}-a_t\log T_{u,z}\bigr]+c_D|T|a\Lambda+c_Dm(B_0+N_c)x^{e_D\varepsilon}.$$
3. $|E_{u,z}-mA_0\lambda_g|\le c_EmB_0$.
4. $|(h_{u,z}+A_0\log T_{u,z})-(h_{u,z'}+A_0\log T_{u,z'})|\le c_H(|T|a\Lambda+mB_0)$.
5. The logarithms of the numbers $T_{u,z}$ satisfy $$\sum_{j=0}^{m-1}\frac1f\sum_{\rho\in\Phi}\log(w_{u,j,\rho}v/\pi)+m\lambda_g-c_T(\Lambda+m^2\Lambda/k)\le\log T_{u,z}\le c_TmL,$$ $$|\log T_{u,z}-\log T_{u,z'}|\le c_T\log k.$$
6. $-c_S|T|a\Lambda(1+m/k)\le\mu^M_{u,z}$ and $\mu^{M,+}_{u,z}\le c_S|T|a\Lambda$.
7. $\mu^{N,+}_{u,z}\le\mu^{M,+}_{u,z}+G_u+F_u-E_{u,z}+c_QmB_0$ and $\mu^M_{u,z}+G_u+F_u-E_{u,z}-Q_{u,z}\le\mu^N_{u,z}$.
8. $\mathcal A_u-G_u\le P_0$ and $I_u\le P_0$.
9. Whenever $0\le\delta_u<1$, $\eta_u\ge0$, $0\le e_u\le1/4$, and $s_u-\mu^{C,-}_u\le S_u$ with $S_u>0$, the following inequality holds: $$s_u-\mu^C_u\le\log|W_u|+\frac{4U_u\log(1+S_u/U_u)+(\eta_u+4\sqrt{e_u})S_u}{1-\delta_u}.$$
10. $s_u-\mu^{C,-}_u\le S_u$ and $0<S_u\le x^{c_*}b$.
11. $0\le\delta_u\le\bar\delta$, $0\le\eta_u\le\bar\eta$, and $0\le e_u\le\bar e$.

Assume also the following seven size conditions.

1. $x\ge1$, $0<\varepsilon\le1$, $b\ge1$, $xb\le a$, $|T|\ge1$, $m\le x^{1/2+\varepsilon/2}$ and $xm\le k$.
2. $e_K\ge0$, $1\le k\le x^{e_K}$, $k\le a$, $0\le L,\Lambda\le2x^\varepsilon$, $kb'\le a$, $0\le X''\le a$, and $0\le a_t\le2a$ for every $t\in T$.
3. $B_0,N_c\ge0$, $\log|W_u|\le(k-3)\log2$ for every $u\in U$, and $\bar\delta\le1/2$.
4. Each of $c_D,c_E,c_H,c_T,c_S,c_Q,c_P$ lies in $[0,K]$, and $e_D,e_P,c_*\ge0$.
5. $(\bar\eta+4\sqrt{\bar e})x^{c_*}b\le Kx^\varepsilon|T|a$.
6. $B_0\le2nmbx^\varepsilon$ and $N_c\le|T_2|kbx^{2\varepsilon}/n^2$.
7. $\log x\le x^\varepsilon$ and $200(1+K)^2(1+c_*)(1+e_K)\le x^\varepsilon$.

Then, for every $u\in U$, the difference $\mathcal A_u-\mathcal M_u=\sum_{t\in T}\sum_{j=0}^{m-1}\{A(a_t,t,w_{u,j})-\Re M(a_t,w_{u,j})\}$ satisfies $$\mathcal A_u-\mathcal M_u\le x^{(e_D+e_P+3)\varepsilon}\left[|T|a\left(1+\frac{m^2}{k}\right)+m\left(2nmbx^\varepsilon+\frac{|T_2|kbx^{2\varepsilon}}{n^2}\right)\right].$$
