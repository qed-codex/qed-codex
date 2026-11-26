---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThetaLawsUnitPeriod.lean",
  "declarations": [
    "GlobalTheory.MomOne.GenusOne.thetaLaws_unit_period"
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

## A unit p-adic period for translated CM theta functions

[Theorem PHT.0077](https://andrewodesky.com/rh/lean/GlobalTheory.MomOne.GenusOne.thetaLaws_unit_period/)

Let $d,q$ be primes with $d\equiv7\pmod{16}$. Suppose either $q=2$ and $d\equiv7\pmod8$, or $q\ne2$ and the Jacobi symbol $\left(\frac{-d}{q}\right)=1$. Write $C_q$ for the completed algebraic closure of $\mathbb Q_q$. Put $$\Lambda=\mathbb Z+\mathbb Z\frac{1+i\sqrt d}{2},\quad H(z,w)=\frac{2z\overline w}{\sqrt d},\quad g_2=60\sum_{0\ne\lambda\in\Lambda}\lambda^{-4},\quad g_3=140\sum_{0\ne\lambda\in\Lambda}\lambda^{-6}.$$ Let $\delta\in\mathbb C$ satisfy $\delta^{12}=g_2^3-27g_3^2$. There is an entire even function $\theta$ with $\theta(0)=1$, with every zero in $\frac12+\Lambda$, and $$W_x\theta=\theta\qquad(x\in\Lambda),$$ where $T_x f(z)=f(z+x)e^{-\pi H(z,x)-\pi H(x,x)/2}$ and $W_x=e^{\pi i|x|^2}T_x$. Moreover $\delta\ne0$ and, for every field isomorphism $\iota:\mathbb C\simeq C_q$, there is $\Omega\in C_q$ with $|\Omega|_q=1$ such that the three properties below hold for $\omega=\Omega/\iota(\delta)$.

Use the formal logarithm $\log(1+T)=\sum_{n\ge1}(-1)^{n+1}T^n/n$. For an entire function $f$, define $$\widehat f(T)=\sum_{n\ge0}\iota\!\left(\frac{f^{(n)}(0)}{n!}\right)(\omega\log(1+T))^n.$$ Call $t\in\mathbb C$ prime-to-$q$ torsion if some positive integer $s$ prime to $q$ satisfies $st\in\Lambda$. Then:

1. Every coefficient of $\widehat{T_t\theta}$ has $q$-adic norm at most $1$ for every such $t$.
2. Let $t\in\mathbb C$ and let $n,s\ge0$ be integers with $\gcd(s,q)=1$ and $st\in\Lambda$. For $v\in\Lambda$ with $|\iota(\overline v)|_q\le q^{-2n}$, put $y=sv/q^n$. For $\xi=\iota(e^{-2\pi i\operatorname{Im}H(1,y)})$, $$\xi^{q^n}=1,\qquad \widehat{W_y(T_t\theta)}=S_\xi(\widehat{T_t\theta}).$$
3. For integers $a,m\ge0$, $c_1,\ldots,c_m\in C_q$, prime-to-$q$ torsion points $s_1,\ldots,s_m,t$, and $B\in\mathbb R$, a coefficient bound $B$ for $\sum_jc_j(\widehat{T_{s_j}\theta})^a$ implies the same bound for $\sum_jc_j(\widehat{T_t(T_{s_j}\theta)})^a$.
