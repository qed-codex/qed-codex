---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PrimeSetBoundDataOfPrimitiveChar.lean",
  "declarations": [
    "UpperTheory.V.PrimePair",
    "UpperTheory.V.ThmBab",
    "UpperTheory.V.ThmBcFree"
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

## Simultaneous localization bounds in cyclotomic layers

[Theorem GC.0086](https://andrewodesky.com/rh/lean/UpperTheory.V.Win.thmBab_of_lemmaK/)

Assume the condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), the assertions of ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)) and ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)), the class-group assertion in ([Class-group ranks in cyclotomic towers](https://andrewodesky.com/rh/lean/UpperTheory.V.FW.ferreroWashington/)), and the existence of a real constant satisfying the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)). There exist functions $R_0,R_\ell$ with values in $\mathbb N$ and a constant $C_K>0$ with the following property. The arguments of $R_0,R_\ell$ are presentations of abelian fields as fixed fields in cyclotomic fields.

Let $F\subseteq\mathbb Q(\mu_m)$ be such a presented field, let $\mathcal B$ be a finite set of odd primes, and, for each $\ell\in\mathcal B$, let $L_\ell$ be a presented abelian field containing $\mu_\ell$. Let $C_t\ge1$, $A\in\mathbb R$, and $0<\varepsilon<1/52$. Put $$R=R_0(F)+\sum_{\ell\in\mathcal B}R_\ell(L_\ell),\qquad J=2^{R+2}\left(\frac{2C_KC_t}{\varepsilon}\right)^R,\qquad j_\ell=\lfloor\log_\ell R_\ell(L_\ell)\rfloor+3.$$ Here the integer logarithm is taken to be $0$ at $0$. There is $X_0$, chosen before the functions below, such that the following holds.

Let $\nu,t:\mathbb R\to\mathbb N$ satisfy, for every $x\ge2$, $$\nu(x)\ge2,\qquad 2^{\nu(x)}\le x^A,\qquad 2\le t(x)\le x^{C_t}.$$ For every $X\ge X_0$ and primes $q,d$ satisfying $$q\equiv3\pmod8,\qquad d\equiv7\pmod{16},\qquad (qd,m)=1,\qquad \log(qd)\le X^{\varepsilon/(4J)},$$ there exists $Y$ with $X^{1/J}\le Y$ and $Y^2\le X$ such that the following two bounds hold simultaneously for every $Y\le x\le Y^2$.

For $$E=F\,\mathbb Q(\mu_{2^{\nu(x)+2}})^+\mathbb Q(\sqrt{-q},\sqrt{-d}),$$ every length in the next sum is finite and $$\sum_{1\le r<t(x)}\operatorname{length}_{\mathbb Z_2}\mathcal S_{2,r}(E)\le\exp(x^{4\varepsilon/5}).$$ For each $\ell\in\mathcal B$ and every cyclotomic layer $L'/L_\ell$ of degree $\ell^{j_\ell}$, every length in the next sum is finite and $$\sum_{1\le r<t(x)}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(L')\le\exp(x^{4\varepsilon/5}).$$ The assertions hold for every isomorphic realization of the specified fields and for all algebraic closures and compatible local coefficient data.

## Summing the negative localization lengths

[Theorem GC.0087](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.thmBcFree_of/)

Assume the character-eigenspace bound specified below. There is a real constant $C_-$ with the following property. Let $F\subseteq\mathbb Q(\mu_m)$ be an abelian field given by a fixing subgroup, and put $o=[F:\mathbb Q]$. Let $\nu,t\ge2$, and let $q,d$ be primes with $q\equiv3\pmod8$, $d\equiv7\pmod{16}$ and $(qd,m)=1$. Let $$E=F\mathbb Q(\mu_{2^{\nu+2}})^+\mathbb Q(\sqrt{-q},\sqrt{-d})$$ be a CM field, put $n=[E:\mathbb Q]$, and let $F_E$ be its cyclotomic conductor, the least positive integer $M$ for which $E$ embeds in $\mathbb Q(\mu_M)$. For every odd prime $\ell$ and $1\le r<t$, the eigenspace $\mathcal S_{\ell,r}(E)^-$ on which natural complex conjugation acts by $(-1)^{r+1}$ has finite length. For every finite set $\mathcal P$ of odd primes, $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)^-\le3nt^2\log(tF_E)+C_-\sum_{\substack{\ell\mid o\\\ell\text{ odd prime}}}\ell n^2t^2\bigl(\log(t\ell F_E)\bigr)^2.$$ The assertions are uniform in the algebraic closure and compatible local coefficient data. Here $\mathcal S$ is the localization kernel defined in ([Bound for localization kernels](https://andrewodesky.com/rh/lean/UpperTheory.One.vwin_of_row/)).

## Auxiliary moduli of a primitive Dirichlet character and their characters

[Definition / hypothesis GC.D255](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)

This page fixes notation for a primitive Dirichlet character $\chi$: three constants and a finite set of primes determined by $\chi$, the moduli $N=\operatorname{lcm}(2^{\nu+2},N_\chi)\,qd$ formed with two auxiliary primes $q$ and $d$, and the Dirichlet characters modulo $N$ that are trivial on a subgroup $H$ of $(\mathbb Z/N\mathbb Z)^\times$. It then defines, for an odd prime $\ell$, an integer $e$ and a Dirichlet character $\psi$ modulo $N$, two cases called II and III, and an exponent attached to each.

**Constants of a primitive character.** Let $\chi$ be a primitive complex Dirichlet character, of conductor $N_\chi\ge1$ and of order $o$.

- $p_K$ is the least prime $p\ge7$ with $p\equiv3\pmod4$ and $p\nmid N_\chi$, and $h_K$ is the class number of $\mathbb Q(\sqrt{-p_K})$.
- $p_1$ is the least prime $p$ with $p\equiv1\pmod{o'}$ and $p\nmid2N_\chi p_K$, where $o'$ is the largest odd divisor of $o$.
- $\mathcal B_\chi$ is the finite set of primes that consists of $3$ and of the odd primes that divide $o\,N_\chi\,p_K\,h_K\,p_1$.

**Auxiliary triples and their moduli.** An *auxiliary triple* for $\chi$ is a triple $(\nu,q,d)$ of an integer $\nu\ge2$ and primes $q$ and $d$ such that $$q\equiv3\pmod8,\qquad d\equiv7\pmod{16},\qquad q\nmid N_\chi,\qquad d\nmid N_\chi.$$ Its *modulus* is $$N=\operatorname{lcm}\bigl(2^{\nu+2},N_\chi\bigr)\,q\,d.$$ The integers $2^{\nu+2}$, $N_\chi$, $q$ and $d$ divide $N$. Let $H\subset(\mathbb Z/N\mathbb Z)^\times$ be the subgroup of the classes $a$ that satisfy the following four conditions: $a\equiv\pm1\pmod{2^{\nu+2}}$; $\chi(a)=1$; $a$ is a square modulo $q$; and $a$ is a square modulo $d$.

**The characters of the modulus.** Let $\ell$ be a prime and let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. A *Dirichlet character modulo $N$ with values in $\mathcal O$* is a homomorphism $\psi:(\mathbb Z/N\mathbb Z)^\times\to\mathcal O^\times$; its order is its order in the group of these homomorphisms. For an integer $e\ge0$ let $$\mathscr X_{\mathcal O}(e)$$ be the set of the Dirichlet characters $\psi$ modulo $N$ with values in $\mathcal O$ that are trivial on $H$ and satisfy $\psi(-1)=(-1)^e$.

**Factors and components of a character.** Let $\psi$ be a Dirichlet character modulo $N$ with values in $\mathcal O$.

- For a prime $p$, write $N=p^kN'$ with $p\nmid N'$. For $a\in(\mathbb Z/N\mathbb Z)^\times$ let $\tilde a\in(\mathbb Z/N\mathbb Z)^\times$ be the class with $\tilde a\equiv a\pmod{p^k}$ and $\tilde a\equiv1\pmod{N'}$. The *component of $\psi$ at $p$* is the Dirichlet character $\psi_p$ modulo $N$ with $\psi_p(a)=\psi(\tilde a)$.
- The character $\psi$ is in exactly one way a product $\psi=\psi'\psi''$ of two powers of $\psi$ such that the order of $\psi'$ is prime to $\ell$ and the order of $\psi''$ is a power of $\ell$. Put $$\psi^{*}=\psi'\cdot(\psi'_\ell)^{-1},\qquad\psi^{\dagger}=\psi'\cdot(\psi'_2)^{-1},$$ where $\psi'_\ell$ and $\psi'_2$ are the components of $\psi'$ at $\ell$ and at $2$.
- $c_2(\psi)$ is the exponent of $2$ in the conductor of the component $\psi_2$ of $\psi$ at $2$. The conductor of a Dirichlet character modulo $N$ is the least divisor $M$ of $N$ such that the character factors through $(\mathbb Z/M\mathbb Z)^\times$.

**Cases II and III.** Let $(\nu,q,d)$ be an auxiliary triple for $\chi$ with modulus $N$, let $\ell$ be an odd prime, $\mathcal O$ as above, $e\ge0$ an integer and $\psi$ a Dirichlet character modulo $N$ with values in $\mathcal O$.

- $(\ell,e,\psi)$ is *in case II* if $e\ge2$, the order of $\psi^{*}$ is even, and at least one of $\ell\in\mathcal B_\chi$ and $(\ell-1)\mid2e$ holds.
- $(\ell,e,\psi)$ is *in case III* if $\ell\notin\mathcal B_\chi$, $(\ell-1)\mid2e$, the order of $\psi$ is odd, and $\psi\ne1$.

Let $f_0$ be the multiplicative order of $\ell$ modulo $\operatorname{lcm}\bigl(4,\operatorname{ord}\psi^{\dagger}\bigr)$, and let $n_0$ be the exponent of $2$ in $\ell^{f_0}-1$. The *exponents* of the two cases are the least integers $n_{\rm II}(\ell,\psi)\ge0$ and $n_{\rm III}(\ell,\psi)\ge0$ with $$2^{\,n_{\rm II}(\ell,\psi)}\ge\max\bigl(\ell\,N\,4^{n_0},\ 2^{\,c_2(\psi)+6}\,o\,\ell^3N_\chi^2\bigr),\qquad2^{\,n_{\rm III}(\ell,\psi)}\ge\max\bigl(\ell\,N_\chi\,p_1\,4^{n_0},\ 8\ell^2\bigr).$$
