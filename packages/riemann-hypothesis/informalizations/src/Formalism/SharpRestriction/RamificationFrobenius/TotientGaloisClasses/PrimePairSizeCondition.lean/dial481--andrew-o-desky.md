---
{
  "module": "src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/PrimePairSizeCondition.lean",
  "declarations": [
    "Formalism.HC.PChar"
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
