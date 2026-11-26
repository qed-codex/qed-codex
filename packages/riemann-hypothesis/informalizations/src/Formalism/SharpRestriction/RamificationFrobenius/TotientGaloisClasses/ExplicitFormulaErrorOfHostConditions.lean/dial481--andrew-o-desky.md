---
{
  "module": "src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean",
  "declarations": [
    "Formalism.HC.EAtH",
    "Formalism.HC.Level",
    "Formalism.HC.Level.Gm",
    "Formalism.HC.Level.cyc"
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

## Weighted sums of regularized smoothed character sums

[Definition / hypothesis ANT.D268](https://andrewodesky.com/rh/lean/Formalism.HC.Level/)

Let $\mathcal K$ be a finite set of primitive Dirichlet characters that contains the principal character $1$ of modulus $1$ and, with every $\chi$, its conjugate $\overline\chi$. Let $o\ge0$ be an integer. Either let $\xi\in\mathcal K$ be an odd real-valued character, or let no such character be chosen. For $\chi\in\mathcal K$ let $g_\chi$ be the function of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)). The *weighted sum attached to $\mathcal K$, $\xi$ and $o$* is the real-valued function $$G_{\mathcal K}(x)=g_1(x)+\sum_{\chi\in\mathcal K\setminus\{1\}}w_\chi\,\Re g_\chi(x)\qquad(x>0),$$ where $w_\xi=1$ if a character $\xi$ is chosen, and $w_\chi=(3o+1)^{-1}$ for every other $\chi\in\mathcal K\setminus\{1\}$.

**The powers of a primitive character.** Let $\psi$ be a primitive Dirichlet character of conductor $M\ge1$, and let $o\ge1$ be its order, the least positive integer for which $\psi^o$ is the principal character modulo $M$. For $0\le j<o$ let $\chi_j$ be the primitive character that induces $\psi^j$: the primitive character of conductor dividing $M$ that agrees with $\psi^j$ on the integers coprime to $M$. Put $$\mathcal P_\psi=\{\chi_j:0\le j<o\}.$$ The set $\mathcal P_\psi$ contains $\chi_0=1$ and $\chi_1=\psi$, and it contains the conjugate of each of its members. The *weighted sum of $\psi$* is the weighted sum attached to $\mathcal P_\psi$, to no character $\xi$, and to the order $o$ of $\psi$: $$G_\psi(x)=g_1(x)+\frac1{3o+1}\sum_{\chi\in\mathcal P_\psi\setminus\{1\}}\Re g_\chi(x)\qquad(x>0).$$

## Character and counting conditions at a single scale

[Definition / hypothesis ANT.D069](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)

The two hypotheses of this page are conditions on a finite abelian CM extension of $\mathbb Q$, on a set of primitive Dirichlet characters, and on numerical data attached to them, at one real number $x\ge1$. Hypothesis (character conditions) requires the characters of the set to be realized by characters of the Galois group, and bounds the smoothed character sums of the other characters of the group at $x$. Hypothesis (counting conditions) requires data that satisfy the hypotheses of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) for the local data of the field.

**The characters.** Let $\mathcal K$ be a finite set of primitive Dirichlet characters that contains the principal character $1$ of modulus $1$ and, with every $\chi$, its conjugate $\overline\chi$. Let $o\ge0$ be an integer. Either let $\xi\in\mathcal K$ be an odd real-valued character, or let no such character be chosen. For a primitive Dirichlet character $\chi$, let $g_\chi$ be the function of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)), and for nonprincipal $\chi$ put $\kappa_\chi=L'(1,\chi)/L(1,\chi)$.

**The field and its group.** Assume Hypothesis (abelian CM field with reciprocity map) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). It fixes, among other data, an abelian group $A$ of order $n$ with an element $a_0$, primes $q,d$, a modulus $Q=Q_Sqd$, a number field $E$ with Galois group $\{\pm1\}^2\times A$ over $\mathbb Q$, and a surjective homomorphism $\alpha:(\mathbb Z/Q\mathbb Z)^\times\to\{\pm1\}^2\times A$. We call these data the field. Write $$H=A,\qquad H_0=\langle a_0\rangle,\qquad n=|H|,\qquad G=(\mathbb Z/2\mathbb Z)^2\times H,$$ with $G$ written additively. For $t\in H$ put $\iota(t)=((0,0),t)$, and define $$\Phi=\{((0,\beta),h):\beta\in\mathbb Z/2\mathbb Z,\ h\in H\},\qquad s_0=((1,0),0),\qquad c_0=((1,1),0),\qquad P_t(g)=c_0+g+\iota(t).$$ Identify $\{\pm1\}^2\times A$ with $G$ by sending $(\epsilon_q,\epsilon_d,a)$ to $((\alpha',\beta'),a)$, where $\epsilon_d=(-1)^{\alpha'}$ and $\epsilon_q=(-1)^{\beta'}$. The elements $c$ and $\delta$ and the subgroup $G_d$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) correspond to $c_0$, $s_0$ and $\Phi$. Let $$\rho:(\mathbb Z/Q\mathbb Z)^\times\longrightarrow G$$ be $\alpha$ followed by this identification. Write $\widehat G=\operatorname{Hom}(G,\mathbb C^\times)$, with trivial character $1$, and $$\Psi_0=\{\gamma\in\widehat G:\gamma(\iota(u))=1\text{ for every }u\in H_0\}.$$ For $\gamma\in\widehat G$, let $\chi_\gamma$ be the primitive Dirichlet character that induces the character $\gamma\circ\rho$ modulo $Q$.

**Local data.** For a prime $p$, write $Q=p^{v}Q^{(p)}$ with $p\nmid Q^{(p)}$. Let $u_p\in(\mathbb Z/Q\mathbb Z)^\times$ be the unit with $u_p\equiv p\pmod{Q^{(p)}}$ and $u_p\equiv1\pmod{p^{v}}$, and put $$I_p=\rho\bigl(\{u\in(\mathbb Z/Q\mathbb Z)^\times:u\equiv1\pmod{Q^{(p)}}\}\bigr),\qquad F_p=\rho(u_p).$$ With the numbers $q,d$ and these subgroups $I_p$ and elements $F_p$, form the coefficients $a_\gamma(r)$ of ([Prime-power Fourier identity](https://andrewodesky.com/rh/lean/Deduction.ch_balance/)) for $\gamma\in\widehat G$ and integers $r\ge1$. For a function $\kappa:\widehat G\to\mathbb C$, write $g^\kappa_\gamma$ for the smoothed character sum of ([Prime-power Fourier identity](https://andrewodesky.com/rh/lean/Deduction.ch_balance/)) that is formed with the coefficients $a_\gamma(r)$ and the function $\kappa$.

**Hypothesis (character conditions).** Let $T\subset H$, and let $x\ge1$, $\varepsilon$ and $C$ be real numbers. The character conditions hold for $\mathcal K,\xi,o$, the field and $T$ at $x$, with constants $\varepsilon$ and $C$, when the following five conditions hold.

1. The index of $H_0$ in $H$ is $o$.
2. For every $\chi\in\mathcal K$ there is $\gamma\in\Psi_0$ with $\gamma(s_0)=1$ and $\chi_\gamma=\chi$.
3. Let $\gamma_q\in\widehat G$ be the character $((\alpha',\beta'),h)\mapsto(-1)^{\beta'}$. If a character $\xi$ is chosen, then $\chi_{\gamma_q}=\xi$. If no character is chosen, then $\chi_{\gamma_q}\notin\mathcal K$.
4. For every $h\in H$, $$\Bigl||T\cap(h+H_0)|-\lambda(h)|T|\Bigr|\le x^{-1+\varepsilon}|T|,\qquad\lambda(h)=\begin{cases}4/(3o+1),&h\in H_0,\\3/(3o+1),&h\notin H_0.\end{cases}$$
5. For every $\gamma\in\Psi_0$ such that $\gamma(s_0)=-1$ or $\chi_\gamma\notin\mathcal K$, $$|g_{\chi_\gamma}(x)|\le x^{1/2+\varepsilon},\qquad|\kappa_{\chi_\gamma}|\le C\log x.$$

**Hypothesis (counting conditions).** Let $T\subset H$, and let $x\ge1$ and $\varepsilon,E_D,E_P,K,C_*,e_K$ be real numbers. The counting conditions hold for the field and $T$ at $x$, with constants $\varepsilon,E_D,E_P,K,C_*,e_K$, when there exist

- a finite set $U$, a map $\tau:U\to H$ whose image contains $H_0$, and a nonempty finite set $W_u$ for every $u\in U$;
- a set $T_2\subset H_0$, integers $m,N\ge0$, real numbers $a_t$ for $t\in H$, and a function $w:H\times\{0,\dots,m-1\}\times G\to\mathbb R$, for which we write $w_{h,j}=w(h,j,\cdot)$;
- a function $\kappa:\widehat G\to\mathbb C$ and real numbers $\eta,X',\theta$;
- values of all the other real parameters, constants and indexed real numbers that occur in ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/));

with the following six properties.

1. For every $\gamma\in\widehat G$ with $\gamma\ne1$, and every primitive Dirichlet character $\chi$ such that $\chi(r)=a_\gamma(r)$ for all integers $r\ge1$, $$\kappa(\gamma)=\frac{L'(1,\chi)}{L(1,\chi)}.$$
2. Apply ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) to the group $H$, the numbers $q,d$, the subgroups $I_p$ and elements $F_p$, the cutoff $N$ and the function $\kappa$; to the index set $U$, the map $\tau$ and the sets $W_u$; to the sets $T$ and $T_2$, the integer $m$, the numbers $a_t$ with $t\in T$ and the function $w$; and to the given numbers $x,\varepsilon,K,e_K$. All eleven numerical conditions of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) hold, and so do the first six of its seven size conditions. Its constants $e_D,e_P,c_*$ satisfy $$e_D\le E_D,\qquad e_P\le E_P,\qquad c_*\le C_*.$$
3. Let $a,b,b',k$ be the real parameters of ([Prime-power count bound](https://andrewodesky.com/rh/lean/Deduction.ch_top/)) with these names. Then $$\eta\ge0,\qquad\theta\ge0,\qquad X'>0,\qquad b'>0,\qquad b'X'\le xb,\qquad|a_t/b-x|\le1\quad(t\in T).$$ For every $u\in H_0$ and $0\le j<m$, the function $w_{u,j}$ is positive on $\Phi$, takes values in $[b,b+\eta+1]$ on the set $\{((0,1),s+u):s\in T_2\}$, and is at most $2b'$ at the other points of $\Phi$; moreover $$a_t/w_{u,j}(g)\le N\qquad(t\in T,\ g\in\Phi).$$
4. For every $\gamma\in\widehat G$ and every real $y\ge X'/3$, $$|g^\kappa_\gamma(y)|\le y\theta.$$
5. $2(2n)(x+1)\theta\le1/x$ and $6(2n)(x+1)(\eta+1)\le b/x$.
6. $a\le2xb$, $\ |T|\ge\tfrac12nx^{-\varepsilon/8}$, $\ |T_2|/n\ge x^{-\varepsilon}$, $\ m\ge x^{1/2-\varepsilon}$ and $k\le n^2x^{1/2-\varepsilon}$.
