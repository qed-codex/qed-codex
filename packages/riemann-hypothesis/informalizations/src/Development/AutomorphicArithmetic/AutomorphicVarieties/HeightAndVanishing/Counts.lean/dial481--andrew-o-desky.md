---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean",
  "declarations": [
    "UpperTheory.V.HV.CountI"
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
