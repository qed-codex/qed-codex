---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicCases/SymplecticGSp4.lean",
  "declarations": [
    "UpperTheory.V.Aut.OfCase",
    "UpperTheory.V.Aut.OfChar"
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
