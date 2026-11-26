---
{
  "module": "src/Formalism/LocalRingCardinality/DataHost.lean",
  "declarations": [
    "Formalism.BasicNotions.Host"
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

## Family fields and Galois data

[Definition / hypothesis ANT.D111](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)

Hypothesis (abelian CM field with reciprocity map). The following finite abelian group, number field and homomorphism onto its Galois group are fixed.

Let $A$ be an abelian group with underlying labelled set $\{0,\ldots,n-1\}$. Let $e\ge2$ be an integer and choose $a_0\in A$ and a surjective homomorphism $$\vartheta:A\longrightarrow H_e=(\mathbb Z/2^{e+2}\mathbb Z)^\times/\{\pm1\}.$$ Require $\vartheta(ha_0)=1\Longrightarrow ha_0=0$ for every $h\in\mathbb Z$. Put $n_0=\operatorname{ord}(a_0)$, $o=n/n_0$ and $$G=\{\pm1\}^2\times A,\quad c=(-1,-1,0),\quad \delta=(1,-1,0),\quad G_d=\{(\epsilon_q,1,a)\}.$$ The signs multiply and $A$ adds. Thus $1_G=(1,1,0)$.

Let $q,d$ be primes with $q\equiv3\pmod8$, $d\equiv7\pmod{16}$ and $({-d}/q)=1$. Choose $Q_S>0$ with $$2^{e+2}\mid Q_S,\quad (Q_S,qd)=1.$$ Every odd prime $\ell\mid Q_S$ satisfies $({-d}/\ell)=1$. Put $Q=Q_Sqd$.

Choose a number field $E$, Galois over $\mathbb Q$, an isomorphism $\operatorname{Gal}(E/\mathbb Q)\simeq G$, an element $s_d\in E$ and an embedding $\iota:E\hookrightarrow\mathbb Q(\zeta_Q)$, where $\zeta_Q$ is a chosen primitive $Q$th root. Write $\sigma_g$ for the automorphism corresponding to $g$. Require $$s_d^2=-d,\quad \sigma_{(\epsilon_q,\epsilon_d,a)}s_d=\epsilon_ds_d.$$ There is a homomorphism $\alpha:(\mathbb Z/Q\mathbb Z)^\times\to G$ such that, for every cyclotomic automorphism $\tau$ with $\tau\zeta_Q=\zeta_Q^u$, $$\iota(\sigma_{\alpha(u)}x)=\tau(\iota x)\qquad(x\in E).$$ It is surjective and satisfies $$\alpha(-1)=c,\quad \vartheta(\operatorname{pr}_A\alpha(u))=[u\bmod2^{e+2}],\quad \operatorname{pr}_d\alpha(u)=(u/d),$$ $$u\equiv1\pmod{Q_Sq}\Longrightarrow\alpha(u)\in\{1_G,\delta\},\quad u\equiv1\pmod{Q_Sd}\Longrightarrow\alpha(u)^2=1_G,$$ $$u\equiv d\pmod{Q_Sq}\Longrightarrow\operatorname{pr}_q\alpha(u)=-1.$$

Let $F$ be the maximal real subfield and $E_0=\mathbb Q(s_d)$. The field $E$ is CM, $[E:\mathbb Q]=4n$, $[F:\mathbb Q]=2n$, and $F$ is the fixed field of $\sigma_c$. For every embedding $\tau:E\hookrightarrow\mathbb C$ and every $\sigma\in\operatorname{Gal}(E/\mathbb Q)$, $$\tau\circ\sigma=\overline\tau\quad\Longleftrightarrow\quad\sigma=\sigma_c.$$ Put $\Sigma=\{\tau:E\hookrightarrow\mathbb C:\tau(s_d)=\mathrm i\sqrt d\}$. Require $\tau\in\Sigma\Longleftrightarrow\overline\tau\notin\Sigma$, $|\Sigma|=2n$, and, for $\tau\in\Sigma$, $\tau\circ\sigma_g\in\Sigma\Longleftrightarrow g\in G_d$. There is also a nonzero $a\in E$ with $\sigma_g(a)=\operatorname{pr}_q(g)a$ for every $g\in G$.

The following local Galois conditions are part of the hypothesis. For a rational prime $\ell$, write $Q^{(\ell)}=Q/\ell^{v_\ell(Q)}$. At every prime $P$ of $E$ above $\ell$, the arithmetic Frobenius elements, inertia group and decomposition group have respective images $$\{\alpha(u):u\equiv\ell\pmod{Q^{(\ell)}}\},\quad \{\alpha(u):u\equiv1\pmod{Q^{(\ell)}}\},\quad \{\alpha(u):u\equiv\ell^h\pmod{Q^{(\ell)}}\text{ for some }h\ge0\}.$$ The units $u$ in these sets range over $(\mathbb Z/Q\mathbb Z)^\times$. When $\ell\nmid Q$, arithmetic Frobenius exists, is uniquely $\sigma_{\alpha(\ell)}$, and inertia is trivial. Its second sign coordinate is $({-d}/\ell)$, and its image under $\vartheta\circ\operatorname{pr}_A$ is $[\ell\bmod2^{e+2}]$. Inertia above $d$ is exactly $\{1_G,\delta\}$. Above every $\ell\mid Q_Sq$ the decomposition group lies in $G_d$; above every $\ell\mid Q$ it does not contain $c$. At every nonzero prime of $E$, $\sigma_c$ acts nontrivially on the residue field whenever it belongs to the decomposition group; equivalently $\sigma_c$ is never in inertia.

A rational prime $p$ splits into two primes in $E_0$ if and only if $p=2$ or $p\ne2$ and $({-d}/p)=1$. For every prime $P$ above $p$, the right action of its decomposition group preserves membership of every $g\in G$ in $G_d$ if and only if $p$ splits into two primes in $E_0$.

For a nonzero prime $\mathfrak p$ of $F$, define $\eta_F(\mathfrak p)=1$ if there are two primes above it in $E$, and $-1$ otherwise. Every such $\mathfrak p$ either has two primes above it or has one prime of residue degree two. If $p\nmid Q$ and $g$ is arithmetic Frobenius at a prime above $p$, require $\eta_F(\mathfrak p)=-1\Longleftrightarrow c\in\langle g\rangle$ for the prime $\mathfrak p$ below it. If $p\mid Q$, every such $\mathfrak p$ has $\eta_F(\mathfrak p)=1$.

The relative different $\mathfrak D_{E/E_0}$ is supported above $Q_Sq$. There exists an ideal $\mathfrak b$ of $\mathcal O_E$ with $$\mathfrak D_{E/E_0}=\mathfrak b\overline{\mathfrak b},\qquad \mathfrak b+\overline{\mathfrak b}=\mathcal O_E,\qquad \sigma(\mathfrak b)=\mathfrak b\quad(\sigma\in\operatorname{Gal}(E/E_0)).$$ For every ideal $\mathfrak a$ with $\mathfrak D_{E/E_0}=\mathfrak a\overline{\mathfrak a}$, require $$x\in\mathfrak a^{-1}\quad\Longleftrightarrow\quad \operatorname{Tr}_{E/E_0}(x\overline y)\in\mathcal O_{E_0}\text{ for every }y\in\mathfrak a^{-1}.$$ Write $D_E=\operatorname{disc}E$, $D_F=\operatorname{disc}F$ and $\operatorname{rd}_E=|D_E|^{1/[E:\mathbb Q]}$. Require $$D_E=D_F^2,\quad p\mid D_E\Longrightarrow p\mid Q\ (p\text{ prime}),\quad2d\mid D_E,$$ $$2^{e+1-2^{-e}}\sqrt d\le\operatorname{rd}_E\le(Q_S/2)\sqrt{qd},\qquad4n\le\operatorname{rd}_E^2.$$ Every root of unity $\zeta\in E$ has $N_{E/E_0}(\zeta)=1$.

Hypothesis (fields and Galois data). The following finite group, number fields, ideals and selected sets are fixed for one member of a family.

Assume Hypothesis (abelian CM field with reciprocity map), and put $f=2n$. Choose natural numbers $k,m,t$ satisfying $$k,m\text{ even},\quad t\text{ odd},\quad 2\le m,\quad m+3\le k,\quad k+m+4\le t,\quad3m<t,$$ $$m\le f\le k,\qquad m^2\le k+m(t+1).$$ Write $r=k+m-1$, $n_V=r+t$, $N_j=k+j(t+1)$ and $r_S=m/2-1$.

Require in addition $$q\ne3,\qquad q,d>4tr+1,\qquad Q_S\le n^2,\qquad o^{64}\le2^e.$$ Choose $s_q\in E$ with $$s_q^2=-q,\qquad \sigma_{(\epsilon_q,\epsilon_d,a)}s_q=\epsilon_qs_q.$$ Require $\operatorname{pr}_q\alpha(u)=(u/q)$ for every $u\in(\mathbb Z/Q\mathbb Z)^\times$; thus the sign coordinates of the arithmetic Frobenius at a prime $\ell\nmid Q$ are $((\ell/q),({-d}/\ell))$. For each prime $\ell\mid Q_S$, some unit $u$ modulo $Q$ satisfies $u\equiv1\pmod{Q/\ell}$ and $\alpha(u)\ne1_G$.

Fix an ideal $\mathfrak b_0$ satisfying the three displayed different and invariance conditions. Fix a finite set $\mathcal P_{\rm lev}\subset\mathbb Z_{\ge0}$, distinct primes $g_0,g_1\in\mathcal P_{\rm lev}$, and distinct primes $p_\Delta,p'_\Delta\in\mathcal P_{\rm lev}$ with $$p_\Delta,p'_\Delta\equiv1\pmod{15},\qquad p_\Delta,p'_\Delta\ne g_a\quad(a=0,1).$$ Every member of $\mathcal P_{\rm lev}$ is coprime to $Q_S$.

Fix a nonzero ideal $\mathfrak c\subset\mathcal O_{E_0}$ that is primitive: $\mathfrak c\nsubseteq(m)$ for every integer $m>1$. Every prime ideal containing $\mathfrak c$ has rational-prime norm $\ell$ with $({-d}/\ell)=1$. Require $$\gcd\left(N\mathfrak c,30qdQ_S\prod_{p\in\mathcal P_{\rm lev}}p\right)=1.$$ Choose an integer $s_0\ge0$ such that every odd prime $p\le s_0$ has $({-d}/p)=1$, and $4\ell\le s_0$ for every odd prime $\ell\mid Q_S$.

For a rational prime $p$, the prime classes used in the local hypotheses are defined in the following order. Primes dividing $Q_S$, the prime $q$, and the prime $d$ form three separate ramified classes. Among the remaining primes, the split class consists of those with $({-d}/p)=1$. Put $$\mathcal S_{\rm sig}=\{p:p\nmid Q_Sqd,\ ({-d}/p)\ne1,\ \operatorname{pr}_q\alpha(p)=1\},$$ $$\mathcal I=\{p:p\nmid Q_Sqd,\ ({-d}/p)\ne1,\ \operatorname{pr}_q\alpha(p)\ne1\}.$$ These are respectively the signal and inert classes; every $p$ in the two displayed sets is required to be prime.

Finally choose $\phi_0\in\Sigma$, finite sets $T\subseteq A$ and $T_2\subseteq\mathbb Z_{\ge0}$, a shift $a_*\in A$, an integer $L_w\ge2$ and a real constant $C_2$. For every $s\in T_2$ require $4L_ws<n_0$. For distinct $s_1,s_2,s_3\in T_2$ and integers $i\ne j$ with $0<|i|,|j|\le L_w$, require $$j(s_2-s_1)\ne i(s_3-s_1).$$ The selected embeddings are $$\Sigma_{\rm top}=\{\phi_0\circ\sigma_{(1,1,v)}:v\in T\},\quad \Sigma_{\rm thick}=\{\phi_0\circ\sigma_{(-1,1,sa_0+a_*)}:s\in T_2\},\quad \Sigma_{\rm thin}=\Sigma\setminus(\Sigma_{\rm top}\cup\Sigma_{\rm thick}).$$
