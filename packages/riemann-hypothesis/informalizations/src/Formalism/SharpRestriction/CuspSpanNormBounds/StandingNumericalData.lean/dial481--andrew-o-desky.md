---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean",
  "declarations": [
    "Formalism.MainNotions.S.StandingHypotheses",
    "Formalism.MainNotions.S.StandingNumericalData"
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

## Standing conditions on a datum and its size data

[Definition / hypothesis THETA.D263](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)

The conditions below are imposed on a datum and its size data in the estimates for sums of geometric terms. They are numerical: each is an inequality, an equality or a splitting condition on quantities of the datum.

**Notation.** Let $D$ be a datum, that is, a choice of data satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). From ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) we use the CM field $E$ with maximal real subfield $F$, the root discriminant $\operatorname{rd}_E$, the primes $g_0\ne g_1$, the even integers $k,m$, the integer $f=[F:\mathbb Q]$, and $$r=k+m-1,\qquad r_S=\frac m2-1 .$$ Let $\mathcal W$ be the finite set of sources of $D$; its elements are called source words. Each $u\in\mathcal W$ has a prime $T_u$, a real number $\Gamma_u>1$ and a finite-dimensional space $U_u^0$ of stage-zero column functions, as in ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)); put $$d_u=\dim_{\mathbb C}U_u^0 .$$ Let $D_*$ be the real number of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), $\mathcal T$ the set of embeddings identified with the CM type of $E$, and $d_\tau>0$ $(\tau\in\mathcal T)$ the positive numbers chosen in ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Let $\Delta>0$ be the rational number of ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)).

For $u\in\mathcal W$ and $\tau\in\mathcal T$ the datum has a weight array in the sense of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)). We write its rows as $$U^u_{\tau,i}\ (0\le i<k),\qquad V_{\tau,i}\ (0\le i<k-1),\qquad B_{\tau,j}\ (0\le j<m);$$ the rows $V$ and $B$ and the last entry $U_{\tau,k-1}=U^u_{\tau,k-1}$ do not depend on $u$. Put $$\lambda_\tau=(V_{\tau,0},\dots,V_{\tau,k-2},\,-B_{\tau,0},\dots,-B_{\tau,m-1})\in\mathbb R^{r},$$ and for $x\in\mathbb R^k$ put $\operatorname{Vand}(x)=\prod_{0\le a<c<k}(x_a-x_c)$. An embedding $\tau\in\mathcal T$ is called *top* if it belongs to the set $\Sigma_{\rm top}$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)).

A prime number $p$ *splits completely in $E$* if every maximal ideal $P$ of $\mathcal O_E$ containing $p$ has norm $p$ and satisfies $p\notin P^2$.

Size data $S$ for $D$ contain real numbers $x>1$ and $0<\varepsilon<1/52$; put $\mathcal L=x^{\varepsilon}$ and $b=e^{\mathcal L}$. They also contain a constant $C_\Gamma(S)>0$ with $\log\Gamma_u=C_\Gamma(S)\,m^5f\mathcal L$ for every source word $u$.

**Numerical conditions with constant $C_0$.** For a real number $C_0$, the datum $D$ satisfies the *numerical conditions with constant $C_0$* if (N1) to (N13) hold. Here $u,u'$ range over $\mathcal W$ and $\tau$ over $\mathcal T$.

- (N1) $0\le V_{\tau,i}\le 4k\Delta$ for $0\le i\le k-2$.
- (N2) For each $u$ and each $l$ with $1\le l\le k-2$: either $U^u_{\tau,l}=V_{\tau,l-1}-\tfrac12$ for every $\tau$, or $U^u_{\tau,l}=V_{\tau,l-1}-\tfrac12-\Delta$ for every $\tau$.
- (N3) $4k\Delta\le U^u_{\tau,0}-V_{\tau,0}$.
- (N4) If $\tau$ is not top, then $U^u_{\tau,0}-V_{\tau,0}\le 8k\Delta$.
- (N5) If $\tau$ is not top, then $U^u_{\tau,k-1}=V_{\tau,k-2}-\tfrac12$.
- (N6) If $\tau$ is top, then $3\le B_{\tau,0}+U_{\tau,k-1}$ and $\tfrac12B_{\tau,0}\le -U_{\tau,k-1}$.
- (N7) $V_{\tau,i}<U^u_{\tau,i}$ and $U^u_{\tau,i+1}<V_{\tau,i}$ for $0\le i\le k-2$, and $-B_{\tau,0}<U^u_{\tau,k-1}$.
- (N8) If $u\ne u'$, then for every $\tau$ the lists $U^u_{\tau}$ and $U^{u'}_{\tau}$ differ.
- (N9) Every $T_u$ splits completely in $E$, and $T_u\equiv1\pmod{(g_0g_1)^2}$.
- (N10) $\Gamma_u^{-2}D_*/C_0\le d_u\le\Gamma_u^{-2}D_*\,C_0$.
- (N11) $g_0$ and $g_1$ split completely in $E$.
- (N12) $\operatorname{disc}E=(\operatorname{disc}F)^2$.
- (N13) $T_u\notin\{g_0,g_1\}$.

**Size conditions.** For real numbers $C',C_l,C_g,c_b,C_u,c_T,C_T$, the pair $(D,S)$ satisfies the *size conditions with constants $(C',C_l,C_g,c_b,C_u,c_T,C_T)$* if (S1) to (S20) hold.

- (S1) $8\,C_\Gamma(S)\le C'$.
- (S2) $C'm^5f\mathcal L\le k$.
- (S3) $m^4\le f\le k$.
- (S4) $\log f\le\sqrt{r_S}$.
- (S5) $C_l\mathcal L\le f\log k$.
- (S6) $C_lm^2\mathcal L\le k$.
- (S7) $C_l\,mk\Delta\le B_{\tau,j}$ for $0\le j<m$.
- (S8) $C_l\,m\log(\operatorname{rd}_E/2)\le k$.
- (S9) $C_l\,m^3\mathcal L\log\operatorname{rd}_E\le k(\log k)^2$.
- (S10) $\log\operatorname{rd}_E\le\mathcal L/C_l$.
- (S11) $(kb)^8\le g_i\le b^{C_g}$ for $i=0,1$.
- (S12) $\max(k^{C_l},b^{c_b})\le B_{\tau,j}\le b^2$ for $0\le j<m$.
- (S13) $B_{\tau,m-1}\le2B_{\tau,0}$.
- (S14) $U^u_{\tau,0}\le b^{C_u}$.
- (S15) $\operatorname{rd}_E\ge2$.
- (S16) $(kf\mathcal L)^{C_l}\le\Delta$.
- (S17) $C_l\,r^{19}f^5\mathcal L\le B_{\tau,j+1}-B_{\tau,j}$ for $0\le j\le m-2$.
- (S18) $C_l\,km^4+r\,m^{10}<\lambda_{\tau,i}-\lambda_{\tau,i+1}$ for $0\le i\le r-2$.
- (S19) $b^{c_Tm}\le T_u\le b^{C_Tm}$.
- (S20) $0<C_l\le m$.

**Standing conditions.** The pair $(D,S)$ satisfies the *standing conditions with constants $(C_0;C',C_l,C_g,c_b,C_u,c_T,C_T)$* if $C_0\ge1$, $D$ satisfies the numerical conditions with constant $C_0$, and $(D,S)$ satisfies the size conditions with constants $(C',C_l,C_g,c_b,C_u,c_T,C_T)$.

**Conditions on a pair of source words.** Let $u,u'\in\mathcal W$. The *prime conditions for $(u,u')$* are:

- $m\ge4$;
- $T_u$ and $T_{u'}$ are primes, both at least $3$, and both split completely in $E$;
- $g_0$ and $g_1$ are distinct primes that split completely in $E$;
- $\gcd(g_0g_1,\,T_uT_{u'})=1$ and $T_u\equiv T_{u'}\pmod{g_0g_1}$.

For a further real number $A$, the *standing conditions for the pair $(u,u')$ with constants $(C_0;C',C_l,C_g,c_b,C_u,c_T,C_T;A)$* consist of the standing conditions with constants $(C_0;C',C_l,C_g,c_b,C_u,c_T,C_T)$, the prime conditions for $(u,u')$, and $$\frac{T_{u'}}{T_u}\le A,\qquad\frac{T_u}{T_{u'}}\le A,\qquad C_lm^6\mathcal L\le k\log k,\qquad(\log f)^2\le A\,m^2\mathcal L,\qquad\log f\le A\,r_S^2,$$ $$\operatorname{Vand}(U^{u'}_\tau)\le A^k\operatorname{Vand}(U^u_\tau)\quad\text{and}\quad\operatorname{Vand}(U^u_\tau)\le A^k\operatorname{Vand}(U^{u'}_\tau)\qquad\text{for every }\tau\in\mathcal T .$$

**Standing conditions at a member of a family.** Let $\mathrm{Fm}$ be a family with parameter $\varepsilon$, as in ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), with member data $D(x,i)$ and size data $S(x,i)$ for every real $x$ and every $i\in I_x$. Among its constants in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)) are $C_k,C_f,C_w,C_\Delta,C_{\rm count},C_{hr},C_{\rm gap},C_{YL}$ and $C_T$. Put $$C_l(\mathrm{Fm})=\min\{C_f,\,C_w,\,C_\Delta,\,C_{\rm count},\,C_{hr},\,C_{\rm gap}\}.$$ For a real number $C_0$, the *family standing conditions with constant $C_0$* hold at a member $(x,i)$ if $(D(x,i),S(x,i))$ satisfies the standing conditions with constants $$\bigl(C_0;\ C_k,\ C_l(\mathrm{Fm}),\ C_{YL}+1,\ \tfrac14,\ 3,\ \tfrac12,\ C_T\bigr).$$ For source words $u,u'$ of $D(x,i)$ and a real number $A$, the *family standing conditions for the pair $(u,u')$ with constants $(C_0;A)$* are the standing conditions for the pair $(u,u')$ with constants $\bigl(C_0;C_k,C_l(\mathrm{Fm}),C_{YL}+1,\tfrac14,3,\tfrac12,C_T;A\bigr)$.
