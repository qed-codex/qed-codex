---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CharacterLevelBounds/ShaFamMono.lean",
  "declarations": [
    "UpperTheory.V.Chr.Psi",
    "UpperTheory.V.Chr.V",
    "UpperTheory.V.Chr.V'",
    "UpperTheory.V.Chr.VS",
    "UpperTheory.V.Chr.cls",
    "UpperTheory.V.Chr.dirG",
    "UpperTheory.V.Chr.nrm",
    "UpperTheory.V.Chr.rho"
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

## Irreducible and rigid specializations, Selmer lengths and graded models of a symplectic datum of four characters

[Definition / hypothesis AGR.D279](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Irr/)

This page continues ([Symplectic lifts of a sum of four characters and their specializations](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Raw/)). For a datum $\mathfrak D$ of that page it defines the irreducible specializations and the rigid ones, the Selmer length of $\mathfrak D$, and the graded models of $\mathfrak D$. A graded model presents a ring that carries a point of $\mathfrak D$ as a quotient of a ring with a grading by $\mathbb Z^2$ for which the entries of the point are homogeneous.

**Setting.** Let $\Omega$ be an algebraic closure of $\mathbb Q$ and $G=\operatorname{Gal}(\Omega/\mathbb Q)$. Let $\ell$ be an odd prime, and let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. Let $\mathfrak D$ be a datum for $(\Omega,\ell,\mathcal O)$. The following notation is that of ([Symplectic lifts of a sum of four characters and their specializations](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Raw/)): the matrix $J$; the weight $w(i,j)\in\mathbb Z^2$ of a position $(i,j)$; the class $\mathcal C_{\mathcal O}$ of rings and the lifts over its members; the inertia group $I_A$ and the decomposition group $D_A$ of a valuation subring $A$ of $\Omega$; the cyclotomic character $\epsilon$; the objects $S$, $e$, $\psi$, $g_0$ of $\mathfrak D$, its characters $\Psi=\epsilon^e\psi$, $\alpha$ and $\theta$, the homomorphism $\rho_0=\operatorname{diag}(\theta,\Psi,\alpha,1)$ and its reduction $\bar r$, the set of primes $T$ and the groups $D_p$; and the points and the specializations of $\mathfrak D$.

**Irreducible specializations.** A specialization $r:G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ of $\mathfrak D$ is *irreducible* if the matrices $r(g)$, $g\in G$, span the $\overline{\mathbb Q}_\ell$-vector space $M_4(\overline{\mathbb Q}_\ell)$. Two homomorphisms $r,r':G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ are *conjugate* if there is $u\in\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ with $r'(g)=u\,r(g)\,u^{-1}$ for all $g\in G$.

**Rigid specializations.** Let $\overline{\mathbb Q}_\ell[\eta]$ be the ring of dual numbers, $\eta^2=0$, an $\mathcal O$-algebra through $\mathcal O\subset\overline{\mathbb Q}_\ell$. A *first-order specialization* of $\mathfrak D$ is a homomorphism $r':G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell[\eta])$ of the form $r'=y\circ\rho$, where $\rho$ is a point of $\mathfrak D$ over a ring $R\in\mathcal C_{\mathcal O}$ and $y:R\to\overline{\mathbb Q}_\ell[\eta]$ is a homomorphism of $\mathcal O$-algebras. Write $r'(g)=r'_0(g)+\eta\,r'_1(g)$ with $r'_0(g),r'_1(g)\in M_4(\overline{\mathbb Q}_\ell)$. Put $$\mathfrak{sp}_4(\overline{\mathbb Q}_\ell)=\{X\in M_4(\overline{\mathbb Q}_\ell):{}^tX\,J+J\,X=0\}.$$ A homomorphism $r:G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ is *rigid* for $\mathfrak D$ if for every first-order specialization $r'$ of $\mathfrak D$ with $r'_0=r$ there is $X\in\mathfrak{sp}_4(\overline{\mathbb Q}_\ell)$ with $$r'_1(g)=X\,r(g)-r(g)\,X\qquad(g\in G).$$

**Selmer lengths.** This definition needs no datum, and in it $\ell$ may be any prime, $2$ included. Let $\psi':G\to\mathcal O^\times$ be a homomorphism, $e'\ge0$ an integer and $P$ a finite set of primes, and put $\Psi'=\epsilon^{e'}\psi'$. Let $M$ be the $\mathcal O$-module $\mathcal O\otimes_{\mathbb Z_\ell}(\mathbb Q_\ell/\mathbb Z_\ell)$ with the discrete topology, on which $G$ acts by $g\cdot m=\Psi'(g)^{-1}m$, and let $H^1(G,M)$ be its first continuous cohomology group, as in ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)). The *Selmer group of $\Psi'^{-1}$ with conditions at $P$* is the $\mathcal O$-submodule of $H^1(G,M)$ of the classes that satisfy the following two conditions.

1. The restriction of the class to $I_A$ is zero for every valuation subring $A$ of $\Omega$.
2. The restriction of the class to $D_A$ is zero for every valuation subring $A$ of $\Omega$ whose maximal ideal contains a prime of $P$.

Its length as an $\mathcal O$-module, a natural number or $\infty$, is the *Selmer length of $\Psi'^{-1}$ with conditions at $P$*. Put $e_{\mathcal O}=\operatorname{length}_{\mathcal O}(\mathcal O/\ell\mathcal O)$. For the datum $\mathfrak D$, the *Selmer length of $\mathfrak D$* is the Selmer length of $\Psi^{-1}$ with conditions at $S$, where $\Psi=\epsilon^e\psi$.

**Weighted presentations.** Let $R$ be an $\mathcal O$-algebra. A *weighted presentation* of $R$ consists of a finite set $\Sigma$, a weight $w_s\in\mathbb Z^2$ for every $s\in\Sigma$, and a surjective homomorphism of $\mathcal O$-algebras $$\pi:\mathcal O[[z_s:s\in\Sigma]]\longrightarrow R$$ whose kernel is homogeneous in the following sense. The weight of a monomial $\prod_sz_s^{n_s}$ is $\sum_sn_sw_s$. For a power series $f$ and $j\in\mathbb Z^2$, let $f_j$ be the sum of the terms of $f$ whose monomials have weight $j$; the series $f$ is *homogeneous of weight $j$* if $f=f_j$. The kernel of $\pi$ is homogeneous if $f_j\in\ker\pi$ for every $f\in\ker\pi$ and every $j\in\mathbb Z^2$.

For $j\in\mathbb Z^2$ let $R_j\subset R$ be the $\mathcal O$-submodule of the images under $\pi$ of the power series that are homogeneous of weight $j$. Then $R_iR_j\subset R_{i+j}$, and the sum $R^{\rm gr}=\sum_jR_j$ is an $\mathcal O$-subalgebra of $R$. The presentation *has an origin* if every $f\in\ker\pi$ has constant term $0$. The *origin* is then the homomorphism of $\mathcal O$-algebras $x_0:R\to\mathcal O$ that sends $\pi(f)$ to the constant term of $f$.

**Graded models.** A *graded model* of $\mathfrak D$ consists of the following objects.

- An integral domain $R\in\mathcal C_{\mathcal O}$ with a weighted presentation $(\Sigma,(w_s),\pi)$ that has an origin $x_0$, such that every weight $w_s$ is the weight $w(i,j)$ of a position $(i,j)$ with $1\le i,j\le4$.
- Integers $d_-\ge1$, $d_+\ge0$ and $d_0\ge0$, and elements $$F_0,\dots,F_{d_-}\in R_{(0,-1)},\qquad E_1,\dots,E_{d_+}\in R_{(0,1)},\qquad Z_1,\dots,Z_{d_0}\in R_{(0,0)}$$ with $x_0(Z_i)=0$ for every $i$.
- A ring $U\in\mathcal C_{\mathcal O}$ and a surjective homomorphism of $\mathcal O$-algebras $\pi_U:R\to U$ whose kernel is the ideal generated by the elements $F_i$, $E_i$ and $Z_i$.
- A point $\rho_U$ of $\mathfrak D$ over $U$.

These objects satisfy the conditions (M1)–(M4) below.

**(M1) Smoothness at the origin.** Let $\mathfrak p$ be the kernel of the restriction of $x_0$ to $R^{\rm gr}$, and let $\operatorname{Frac}\mathcal O$ be the field of fractions of $\mathcal O$. There are a finite set $\tau$, a weight $u_i\in\mathbb Z^2$ for every $i\in\tau$, and a homomorphism of $\mathcal O$-algebras $$\varphi:R^{\rm gr}\longrightarrow(\operatorname{Frac}\mathcal O)[[T_i:i\in\tau]]$$ with the following five properties, in which the variable $T_i$ has weight $u_i$.

1. For every $j\in\mathbb Z^2$ and every $f\in R_j$, the series $\varphi(f)$ is homogeneous of weight $j$.
2. The constant term of $\varphi(f)$ is $x_0(f)$, for every $f\in R^{\rm gr}$.
3. For every $i\in\tau$ there is $f\in R^{\rm gr}$ such that the coefficient of $T_i$ in $\varphi(f)$ is nonzero and the coefficient of $T_{i'}$ in $\varphi(f)$ is zero for every $i'\ne i$.
4. If $f\in\mathfrak p$ and the coefficient of $T_i$ in $\varphi(f)$ is zero for every $i\in\tau$, then $cf\in\mathfrak p^2$ for some nonzero $c\in\mathcal O$.
5. The number of the $i\in\tau$ with $u_i=j$ is $1$ for $j=(1,0)$, $j=(-1,1)$ and $j=(1,1)$; it is $d_+$ for $j=(0,1)$, $d_-$ for $j=(0,-1)$ and $d_0$ for $j=(0,0)$; and it is $0$ for every other $j\in\mathbb Z^2$.

**(M2) Generation.** Let $R'\in\mathcal C_{\mathcal O}$ and let $f,f':U\to R'$ be homomorphisms of $\mathcal O$-algebras with $f\circ\rho_U=f'\circ\rho_U$. Then $f=f'$.

**(M3) Homogeneous entries.** For every $g\in G$ and every position $(i,j)$ there is $f\in R_{w(i,j)}$ with $\pi_U(f)=\rho_U(g)_{ij}$; and every $f\in R$ with $\pi_U(f)=\rho_U(g)_{ij}$ satisfies $x_0(f)=\rho_0(g)_{ij}$.

**(M4) Derivations from cocycles.** Let $a\in\mathcal O$ be nonzero and let $z:G\to\mathcal O/a\mathcal O$ be a locally constant map with the following four properties.

- (a) $z(gh)=z(g)+\Psi(g)^{-1}z(h)$ for all $g,h\in G$.
- (b) $z(g)=0$ for every valuation subring $A$ of $\Omega$ away from $T$ and every $g\in I_A$ with $\bar r(g)=1$.
- (c) $z(g_0)=0$.
- (d) For every $p\in T$ there is $m_p\in\mathcal O/a\mathcal O$ with $z(g)=\Psi(g)^{-1}m_p-m_p$ for all $g\in D_p$.

Then there is an $\mathcal O$-linear map $\delta:R\to\mathcal O$ with the following four properties.

- (i) $\delta(fh)=x_0(f)\,\delta(h)+x_0(h)\,\delta(f)$ for all $f,h\in R$.
- (ii) $\delta(R_j)=0$ for every $j\ne(0,-1)$.
- (iii) $\delta(f)\in a\mathcal O$ for every $f\in\ker\pi_U$.
- (iv) For every $g\in G$ and every $f\in R$: if $\pi_U(f)=\rho_U(g)_{31}$, then $\delta(f)\equiv\theta(g)\,z(g)\pmod{a\mathcal O}$; and if $\pi_U(f)=\rho_U(g)_{42}$, then $\delta(f)\equiv\Psi(g)\,z(g)\pmod{a\mathcal O}$.
