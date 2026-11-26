---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean",
  "declarations": [
    "UpperTheory.V.HV.Coef",
    "UpperTheory.V.HV.Host",
    "UpperTheory.V.HV.Host.Big",
    "UpperTheory.V.HV.Host.CaseI",
    "UpperTheory.V.HV.Host.CaseII",
    "UpperTheory.V.HV.Host.CaseIII",
    "UpperTheory.V.HV.Host.H",
    "UpperTheory.V.HV.Host.N",
    "UpperTheory.V.HV.Host.X",
    "UpperTheory.V.HV.Host.nII",
    "UpperTheory.V.HV.Host.nIII",
    "UpperTheory.V.HV.Vlen",
    "UpperTheory.V.HV.Vn"
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

## Selmer lengths of twisted Dirichlet characters and Estimate I

[Definition / hypothesis GC.D033](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)

This page defines the Selmer group and the Selmer length of a Dirichlet character twisted by a power of the cyclotomic character, and it states a bound for sums of these lengths over primes and characters, called Estimate I.

**The characters.** Fix an algebraic closure $\overline{\mathbb Q}$ of $\mathbb Q$ and write $G_{\mathbb Q}=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$, with its Krull topology. Let $\ell$ be a prime, and let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. Let $N\ge1$ and $e\ge0$ be integers, and let $\psi$ be a Dirichlet character modulo $N$ with values in $\mathcal O$, that is, a homomorphism $(\mathbb Z/N\mathbb Z)^\times\to\mathcal O^\times$.

- For $g\in G_{\mathbb Q}$ let $a(g)\in(\mathbb Z/N\mathbb Z)^\times$ be the class with $g(\zeta)=\zeta^{a(g)}$ for every $N$-th root of unity $\zeta\in\overline{\mathbb Q}$. The character $\psi$ is also regarded as the character $g\mapsto\psi(a(g))$ of $G_{\mathbb Q}$.
- $\epsilon_\ell:G_{\mathbb Q}\to\mathbb Z_\ell^\times$ is the $\ell$-adic cyclotomic character: $g(\zeta)=\zeta^{\epsilon_\ell(g)}$ for every root of unity $\zeta\in\overline{\mathbb Q}$ of $\ell$-power order.
- $\Psi=\epsilon_\ell^e\psi:G_{\mathbb Q}\to\mathcal O^\times$.

**The Selmer group and its length.** Let $M$ be the $\mathcal O$-module $\mathcal O\otimes_{\mathbb Z_\ell}(\mathbb Q_\ell/\mathbb Z_\ell)$ with the discrete topology, on which $G_{\mathbb Q}$ acts by $g\cdot m=\Psi(g)^{-1}m$. Let $H^1(G_{\mathbb Q},M)$ be its first continuous cohomology group: the continuous maps $z:G_{\mathbb Q}\to M$ with $z(gh)=z(g)+g\cdot z(h)$, modulo the maps $g\mapsto g\cdot m-m$ with $m\in M$. It is an $\mathcal O$-module.

For a valuation subring $A$ of $\overline{\mathbb Q}$ with maximal ideal $\mathfrak m_A$, let $$D_A=\{g\in G_{\mathbb Q}:g(A)=A\},\qquad I_A=\{g\in D_A:g(x)-x\in\mathfrak m_A\text{ for all }x\in A\}$$ be its decomposition group and its inertia group. The *Selmer group of $\Psi^{-1}$ formed with $\mathcal O$ and $N$* is the $\mathcal O$-submodule $\mathcal V\subset H^1(G_{\mathbb Q},M)$ of the classes that satisfy the following two conditions.

1. The restriction of the class to $I_A$ is zero for every valuation subring $A$ of $\overline{\mathbb Q}$.
2. The restriction of the class to $D_A$ is zero for every valuation subring $A$ of $\overline{\mathbb Q}$ with $\ell N\in\mathfrak m_A$.

The *Selmer length of $\Psi^{-1}$ formed with $\mathcal O$ and $N$* is $$L=\operatorname{length}_{\mathcal O}\mathcal V,$$ a natural number or $\infty$. Put $e_{\mathcal O}=\operatorname{length}_{\mathcal O}(\mathcal O/\ell\mathcal O)$.

**Estimate I.** Let $\chi$ be a primitive Dirichlet character. Its constants $N_\chi$, $o$, $p_K$, $h_K$ and $p_1$, its set of primes $\mathcal B_\chi$, the auxiliary triples $(\nu,q,d)$ for $\chi$, the modulus $N$ of such a triple and the sets $\mathscr X_{\mathcal O}(e)$ of Dirichlet characters modulo $N$ are defined in ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)). *Estimate I* is the following assertion.

For every primitive Dirichlet character $\chi$ there are a natural number $C$ and primes $r_1$ and $r_2$ with the following property. Let $(\nu,q,d)$ be an auxiliary triple for $\chi$, with modulus $N$, such that $q$ and $d$ are both larger than $r_1$ and $r_2$. Let $t\ge0$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1,$$ and let $e$ be an integer with $0<e<t$. Let $\overline{\mathbb Q}$ be an algebraic closure of $\mathbb Q$. For every prime $\ell$ let $\mathcal O_\ell\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. Let $S$ be a finite set of odd primes such that every $\ell\in S$ satisfies $$\ell\notin\mathcal B_\chi\qquad\text{and}\qquad(\ell-1)\nmid2e.$$ For $\ell\in S$ and $\psi\in\mathscr X_{\mathcal O_\ell}(e)$ write $L_{\ell,\psi}$ for the Selmer length of $(\epsilon_\ell^e\psi)^{-1}$ formed with $\mathcal O_\ell$ and $N$. Then every $L_{\ell,\psi}$ is finite, and $$\sum_{\ell\in S}\log\ell\sum_{\psi\in\mathscr X_{\mathcal O_\ell}(e)}\frac{L_{\ell,\psi}}{e_{\mathcal O_\ell}}\le(Nt)^C.$$
