---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/DecompSigmaOrd.lean",
  "declarations": [
    "UpperTheory.V.GradeZeroInterpolatingElement.OnComp",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.AllIrr",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.Good",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.IsPt",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.PtIn",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.RigidAt",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.XVan",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.aVal",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.condL",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.condP",
    "UpperTheory.V.GradeZeroInterpolatingElement.Raw.sha"
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

## Symplectic lifts of a sum of four characters and their specializations

[Definition / hypothesis AGR.D034](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Raw/)

The theorem ([Finiteness and automorphy for the symplectic lifts of a sum of four characters](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt/)) concerns the lifts of a diagonal representation $\bar\theta\oplus\bar\Psi\oplus\bar\alpha\oplus1$ of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ over a finite field of characteristic $\ell$, with $\theta=\alpha\Psi$, to symplectic representations with multiplier $\theta$ that satisfy conditions at $\ell$ and at finitely many other primes. This page defines the datum that supplies the characters, the lifts in question, called the points of the datum, and the representations over $\overline{\mathbb Q}_\ell$ obtained from the points, called its specializations. The last section defines the data to which the theorem applies.

**Matrices.** Rows and columns of $4\times4$ matrices are indexed by $1,2,3,4$. Put $$J=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}.$$ Let $R$ be a commutative ring and $\nu\in R$. A matrix $g\in M_4(R)$ is *symplectic with multiplier $\nu$* if ${}^tg\,J\,g=\nu J$. A matrix $X\in M_4(R)$ is *of block form* if $X_{ij}=0$ whenever $i-j$ is odd; its *corner* is $$X^{\square}=\begin{pmatrix}X_{11}&X_{13}\\X_{31}&X_{33}\end{pmatrix}.$$ Put $\lambda=(1,0,1,0)$ and $\mu=(1,1,0,0)$. The *weight* of the position $(i,j)$ is $w(i,j)=(\lambda_i-\lambda_j,\ \mu_i-\mu_j)\in\mathbb Z^2$.

**Lifts.** Let $\mathcal O$ be a complete discrete valuation ring with maximal ideal $\mathfrak m_{\mathcal O}$ and residue field $k$. Let $\mathcal C_{\mathcal O}$ be the class of complete Noetherian local $\mathcal O$-algebras $R$ whose structure map $\mathcal O\to R$ is local and induces an isomorphism of residue fields; the residue field of $R$ is identified with $k$. Let $\Gamma$ be a topological group and $\bar r:\Gamma\to\mathrm{GL}_4(k)$ a homomorphism. A *lift* of $\bar r$ over $R\in\mathcal C_{\mathcal O}$ is a homomorphism $r:\Gamma\to\mathrm{GL}_4(R)$ with the following two properties.

1. For all $i,j$ and every integer $n\ge0$, the map $g\mapsto r(g)_{ij}\bmod\mathfrak m_R^n$ from $\Gamma$ to $R/\mathfrak m_R^n$ is locally constant.
2. The composite of $r$ with $\mathrm{GL}_4(R)\to\mathrm{GL}_4(k)$ is $\bar r$.

For a homomorphism of rings $f:R\to R'$ and a homomorphism $r:\Gamma\to\mathrm{GL}_4(R)$, write $f\circ r$ for the homomorphism $g\mapsto\bigl(f(r(g)_{ij})\bigr)_{i,j}$. If $r$ is a lift over $R$ and $f:R\to R'$ is a homomorphism of $\mathcal O$-algebras in $\mathcal C_{\mathcal O}$, then $f\circ r$ is a lift over $R'$. The restriction of a lift of $\bar r$ to a subgroup $\Gamma'\subset\Gamma$, with the induced topology, is a lift of $\bar r|_{\Gamma'}$.

A *condition on lifts* of $\bar r$ is a property $P$ of pairs $(R,r)$, where $R\in\mathcal C_{\mathcal O}$ and $r$ is a lift of $\bar r$ over $R$. Let $P$ be such a condition and $\rho_0:\Gamma\to\mathrm{GL}_4(\mathcal O)$ a homomorphism. A lift $r$ of $\bar r$ over $R$ is *joined to $\rho_0$ by $P$* if there are an integral domain $B\in\mathcal C_{\mathcal O}$, a lift $\rho$ of $\bar r$ over $B$ such that $(B,\rho)$ has property $P$, and homomorphisms of $\mathcal O$-algebras $x:B\to\mathcal O$ and $y:B\to R$ with $$x\circ\rho=\rho_0,\qquad y\circ\rho=r.$$

**The Galois group.** Let $\Omega$ be an algebraic closure of $\mathbb Q$ and $G=\operatorname{Gal}(\Omega/\mathbb Q)$, with the Krull topology. For a valuation subring $A$ of $\Omega$, with maximal ideal $\mathfrak m_A$, the decomposition group $D_A$ is the stabilizer of $A$ in $G$, and the inertia group $I_A$ consists of the $s\in D_A$ with $s(x)-x\in\mathfrak m_A$ for all $x\in A$. A *place of $\Omega$ above* a prime $p$ is a valuation subring $A$ of $\Omega$ with $p\in\mathfrak m_A$; a *Frobenius element* at such a place is an $s\in D_A$ with $s(x)-x^p\in\mathfrak m_A$ for all $x\in A$. A valuation subring $A$ of $\Omega$ is *away from* a set $U$ of primes if no element of $U$ lies in $\mathfrak m_A$. An element $c\in G$ is a *complex conjugation* if there is an embedding of fields $j:\Omega\to\mathbb C$ with $j(c(x))=\overline{j(x)}$ for all $x\in\Omega$.

Let $\ell$ be an odd prime and let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module; it is complete. Write $\epsilon:G\to\mathbb Z_\ell^\times\subset\mathcal O^\times$ for the $\ell$-adic cyclotomic character, and $\bar\gamma:G\to k^\times$ for the reduction modulo $\mathfrak m_{\mathcal O}$ of a character $\gamma:G\to\mathcal O^\times$.

**The datum.** A *datum* $\mathfrak D$ for $(\Omega,\ell,\mathcal O)$ consists of the following objects, which satisfy conditions (D1)–(D9) below.

- A finite set $S$ of primes with $2\in S$ and $\ell\in S$, and an integer $e\ge2$.
- For each prime $p$, a place $A_p$ of $\Omega$ above $p$; write $D_p=D_{A_p}$ and $I_p=I_{A_p}$.
- A complex conjugation $c\in G$.
- Homomorphisms $\psi,\xi,\omega:G\to\mathcal O^\times$.
- For each prime $p$ an element $\sigma_p\in G$; elements $\phi\in G$ and $g_0\in G$; and an element $s_0\in D_\ell$.

From these objects form the characters $$\Psi=\epsilon^e\psi,\qquad\alpha=\epsilon\,\omega^{-1}\xi,\qquad\beta=\Psi\alpha^{-1},\qquad\theta=\alpha\Psi$$ of $G$ with values in $\mathcal O^\times$, the homomorphism $$\rho_0=\operatorname{diag}(\theta,\Psi,\alpha,1):G\longrightarrow\mathrm{GL}_4(\mathcal O),$$ and its reduction $\bar r=\operatorname{diag}(\bar\theta,\bar\Psi,\bar\alpha,1):G\to\mathrm{GL}_4(k)$. Let $S_b$ be the set of the primes $p\in S$ with $p\ne\ell$ such that $\ell$ divides the order of the group $\psi(I_p)$, and put $T=\{\ell\}\cup S_b$.

For a character $\gamma:G\to\mathcal O^\times$, the *vanishing condition* $\mathrm V(\gamma)$ is the following assertion. Let $z:G\to k$ be a locally constant map with $z(gh)=z(g)+\bar\gamma(g)\,z(h)$ for all $g,h\in G$. Suppose that $z(g)=0$ for every valuation subring $A$ of $\Omega$ away from $T$ and every $g\in I_A$ with $\bar r(g)=1$, and that for every $p\in T$ there is $m_p\in k$ with $z(g)=\bar\gamma(g)\,m_p-m_p$ for all $g\in D_p$. Then there is $m\in k$ with $z(g)=\bar\gamma(g)\,m-m$ for all $g\in G$.

The conditions on the objects are the following.

- (D1) The kernel of $\psi$ is open in $G$; $I_A\subset\ker\psi$ for every valuation subring $A$ of $\Omega$ away from $S$; and $\Psi(c)=1$.
- (D2) $\omega^{\ell-1}=1$ and $\bar\omega=\bar\epsilon$.
- (D3) The kernel of $\xi$ is open in $G$; $\xi^m=1$ for an integer $m\ge1$ prime to $\ell$; $I_A\subset\ker\xi$ for every valuation subring $A$ of $\Omega$ away from $S$; $I_p\subset\ker\xi$ for every $p\in T$; and $\xi(c)=-1$.
- (D4) For every $p\in T$, the element $\sigma_p$ is a Frobenius element at $A_p$; and $\epsilon(\sigma_\ell)=1$.
- (D5) $\bar\xi(\sigma_p)\,\bar\Psi(\sigma_p)^i\ne1$ for every $p\in T$ and every integer $i$.
- (D6) The vanishing conditions $\mathrm V(\gamma)$ and $\mathrm V(\gamma^{-1})$ hold for $\gamma=\alpha$, $\gamma=\beta$ and $\gamma=\theta$.
- (D7) The sequence $\sigma_\ell^{\,\ell^{n!}}$, $n=0,1,2,\dots$, converges to $\phi$ in $G$.
- (D8) $\bar\alpha(g_0)\ne1$ and $\bar\Psi(g_0)\ne1$.
- (D9) $s_0\in I_\ell\cap\ker\psi\cap\ker\omega$, and $\epsilon(s_0)$ has infinite order in $\mathbb Z_\ell^\times$.

**The local conditions.** Let $\mathfrak D$ be a datum, and write $(\kappa_1,\kappa_2,\kappa_3,\kappa_4)=(\theta,\Psi,\alpha,1)$. In the following two conditions the elements of $\mathcal O$ act on $M_4(R)$ through the structure map $\mathcal O\to R$.

The condition $P_\ell$ on a lift $\rho$ of $\bar r|_{D_\ell}$ over $R\in\mathcal C_{\mathcal O}$ requires the following four properties, in which $$\Pi_i=\prod_{j\ne i}\bigl(\rho(s_0)-\kappa_j(s_0)\bigr)\in M_4(R)\qquad(1\le i\le4).$$

1. $\rho(g)$ is symplectic with multiplier $\theta(g)$ for every $g\in D_\ell$.
2. The characteristic polynomial of $\rho(s_0)$ is $\prod_{j=1}^4\bigl(X-\kappa_j(s_0)\bigr)$.
3. $\Pi_j\,\rho(g)\,\Pi_i=0$ for every $g\in D_\ell$ and all $i<j$.
4. $\Pi_i\,\bigl(\rho(s)-\kappa_i(s)\bigr)\,\Pi_i=0$ for every $s\in I_\ell$ and every $i$.

For a prime $p\in S_b$, the condition $P_p$ on a lift $\rho$ of $\bar r|_{D_p}$ over $R\in\mathcal C_{\mathcal O}$ requires that $\rho(g)$ is symplectic with multiplier $\theta(g)$ for every $g\in D_p$, and that $\rho(g)=1$ for every $g\in I_p\cap\ker\psi$.

**Points and specializations.** Let $\mathfrak D$ be a datum. A *point* of $\mathfrak D$ over $R\in\mathcal C_{\mathcal O}$ is a lift $\rho$ of $\bar r$ over $R$ with the following five properties.

1. $\rho(g)$ is symplectic with multiplier $\theta(g)$ for every $g\in G$.
2. $\rho(g)=1$ for every valuation subring $A$ of $\Omega$ away from $T$ and every $g\in I_A$ with $\bar r(g)=1$.
3. The matrix $\rho(\phi)$ is of block form, and the entries in positions $(1,3)$ and $(3,1)$ of the matrix $\rho(g_0)+\theta(g_0)\,\rho(g_0^{-1})$ are $0$.
4. The restriction $\rho|_{D_\ell}$ is joined to $\rho_0|_{D_\ell}$ by $P_\ell$.
5. For every $p\in S_b$, the restriction $\rho|_{D_p}$ is joined to $\rho_0|_{D_p}$ by $P_p$.

The *weight-zero subalgebra* of a point $\rho$ over $R$ is the $\mathcal O$-subalgebra $R_0(\rho)\subset R$ generated by the products $$\prod_{a=1}^{m}\rho(g_a)_{i_aj_a}\qquad\Bigl(m\ge0,\ g_a\in G,\ \sum_{a=1}^{m}w(i_a,j_a)=(0,0)\Bigr).$$ A *specialization* of $\mathfrak D$ is a homomorphism $r:G\to\mathrm{GL}_4(\overline{\mathbb Q}_\ell)$ of the form $r=y\circ\rho$, where $\rho$ is a point of $\mathfrak D$ over a ring $R\in\mathcal C_{\mathcal O}$ and $y:R\to\overline{\mathbb Q}_\ell$ is a homomorphism of $\mathcal O$-algebras.

**Data of case II and of case III.** A Dirichlet character $\eta$ modulo an integer $M\ge1$ with values in $\mathcal O$ is also regarded as a character of $G$: if $g\in G$ acts on the $M$-th roots of unity in $\Omega$ by $\zeta\mapsto\zeta^a$, then $\eta(g)=\eta(a)$. Let $\chi$ be a primitive Dirichlet character and $(\nu,q,d)$ an auxiliary triple for $\chi$, with modulus $N$, in the sense of ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)); that page defines the prime $p_1$, cases II and III and the exponents $n_{\rm II}$ and $n_{\rm III}$. Let $e'\ge0$ be an integer and $\varphi$ a Dirichlet character modulo $N$ with values in $\mathcal O$.

A datum $\mathfrak D$ for $(\Omega,\ell,\mathcal O)$, with objects named as above, is *of case II for $\chi$, $(\nu,q,d)$, $e'$ and $\varphi$* if the following four conditions hold.

1. $(\ell,e',\varphi)$ is in case II.
2. $e=e'$ and $\psi=\varphi$ as characters of $G$.
3. $S$ is the set of the primes that divide $2\ell N$.
4. $\xi=\xi'$ as characters of $G$, for a primitive Dirichlet character $\xi'$ modulo $2^{\,n_{\rm II}(\ell,\varphi)}$ with values in $\mathcal O$ such that $\xi'(-1)=-1$.

It is *of case III for $\chi$, $(\nu,q,d)$, $e'$ and $\varphi$* if the following four conditions hold.

1. $(\ell,e',\varphi)$ is in case III.
2. $e=e'$ and $\psi=\varphi$ as characters of $G$.
3. $S$ is the set of the primes that divide $2\ell Np_1$.
4. $\xi=\xi_0\,\xi'$ as characters of $G$, for a primitive Dirichlet character $\xi'$ modulo $2^{\,n_{\rm III}(\ell,\varphi)}$ with values in $\mathcal O$ such that $\xi'(-1)=-1$, and a Dirichlet character $\xi_0$ modulo $p_1$ with values in $\mathcal O$ whose order equals the order of $\varphi$.
