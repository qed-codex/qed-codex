---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThmS6CoreS.lean",
  "declarations": [
    "UpperTheory.V.Aut.BPrime_s"
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

## Lifts of a sum of three characters with the sign character of the Gaussian field: deformation data, universal lifts and points

[Definition / hypothesis AGR.D283](https://andrewodesky.com/rh/lean/UpperTheory.V.UnitaryThreeInertia.HostData/)

Let $\psi$ be a Dirichlet character with values in an $\ell$-adic ring $\mathcal O$, let $e\ge0$ be an integer, and put $\Psi=\epsilon_\ell^e\psi$, where $\epsilon_\ell$ is the $\ell$-adic cyclotomic character. Together with the quadratic character $\eta_4$ of $\mathbb Q(i)$, the sum $\Psi\oplus1\oplus\Psi^{-1}$ is a homomorphism from a Galois group $\Gamma$ of $\mathbb Q$ to the group $\mathcal G_3(\mathcal O)=\mathrm{GL}_3(\mathcal O)\rtimes\{\pm1\}$. This page defines the lifts of this homomorphism that satisfy prescribed conditions at the primes dividing $\ell N$, their universal lifts, and the homomorphisms $\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ that arise from a universal lift. It then defines four properties that the theorem ([Selmer lengths and trace congruences over the Gaussian field](https://andrewodesky.com/rh/lean/UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host/)) assumes: an automorphy condition $\mathcal P_K(\iota;r)$, rigidity of a homomorphism, property (V) of a deformation datum, and the vanishing of its residual Selmer group of weight $-2$.

**Setting.** Let $\Omega$ be an algebraic closure of $\mathbb Q$ and $G=\operatorname{Gal}(\Omega/\mathbb Q)$, with its Krull topology. For a valuation subring $A$ of $\Omega$, the decomposition group $D_A\subset G$ and the inertia group $I_A\subset D_A$ are defined in ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)). A *place of $\Omega$ above a prime $p$* is a valuation subring of $\Omega$ whose maximal ideal contains $p$. A *complex conjugation* of $\Omega$ is an element $\sigma\in G$ for which there is an embedding of fields $j:\Omega\to\mathbb C$ with $j(\sigma(x))=\overline{j(x)}$ for all $x\in\Omega$.

Let $\ell$ be a prime and let $\mathcal O\subset\overline{\mathbb Q}_\ell$ be a *coefficient ring* for $\ell$: a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. Write $\mathfrak m_{\mathcal O}$ for its maximal ideal and $k=\mathcal O/\mathfrak m_{\mathcal O}$. Let $N\ge1$ and $e\ge0$ be integers and $\psi$ a Dirichlet character modulo $N$ with values in $\mathcal O$. As in ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)), $\psi$ is also regarded as a character of $G$, and $\epsilon_\ell:G\to\mathbb Z_\ell^\times$ is the $\ell$-adic cyclotomic character. Let $\eta_4:G\to\{\pm1\}$ be the homomorphism with $\eta_4(g)=1$ exactly when $g$ fixes the square roots of $-1$ in $\Omega$.

The following notions are defined in ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)), and the definitions given there apply to every modulus $N\ge1$: the component $\psi_p$ of $\psi$ at a prime $p$; the factorization $\psi=\psi'\psi''$ into a character $\psi'$ of order prime to $\ell$ and a character $\psi''$ of $\ell$-power order; and the exponent $c_2(\psi)$ of $2$ in the conductor of $\psi_2$.

**Admissible triples.** Let $S_b$ be the set of the primes $p\ne\ell$ that divide $N$ and for which the component of $\psi''$ at $p$ is nontrivial. The triple $(\ell,e,\psi)$ is *admissible* if there is an integer $o_1\ge1$ with the following three properties.

1. $\ell$ is odd, $e\ge1$, $N$ is even, and $\psi(-1)=(-1)^e$.
2. For every odd prime $p$, the order of the component of $\psi'$ at $p$ divides $2o_1$.
3. $c_2(\psi)\ge4$, and $8\,o_1\,p^2<2^{c_2(\psi)}$ for $p=\ell$ and for every $p\in S_b$.

**Deformation data.** Let $S$ be the set of the primes that divide $\ell N$. Let $N_S\subset G$ be the smallest closed normal subgroup that contains $I_A$ for every place $A$ of $\Omega$ above a prime outside $S$, and put $$\Gamma=G/N_S,\qquad\pi:G\to\Gamma,$$ with the quotient topology on $\Gamma$. A *deformation datum* for $(\Omega,\ell,\mathcal O,N,e,\psi)$ is a quadruple $\mathfrak F=\bigl((A_p)_{p\in S},c,\eta,\Psi\bigr)$ that consists of

- a place $A_p$ of $\Omega$ above $p$, for every $p\in S$;
- an element $c\in\Gamma$ that is the image under $\pi$ of a complex conjugation of $\Omega$;
- homomorphisms $\eta:\Gamma\to\{\pm1\}$ and $\Psi:\Gamma\to\mathcal O^\times$ with $$\eta\circ\pi=\eta_4,\qquad\Psi\circ\pi=\epsilon_\ell^e\,\psi.$$

Fix a deformation datum $\mathfrak F$. For a map $f$ defined on $\Gamma$ and $g\in G$ we write $f(g)$ for $f(\pi(g))$. For $p\in S$ put $D_p=D_{A_p}$ and $I_p=I_{A_p}$, and $$D_p^+=\{g\in D_p:\eta(g)=1\},\qquad I_p^+=I_p\cap D_p^+,\qquad I_p^1=\{s\in I_p^+:\Psi(s)\equiv1\pmod{\mathfrak m_{\mathcal O}}\}.$$

**The group $\mathcal G_3$.** For a commutative ring $R$, the group $\mathcal G_3(R)=\mathrm{GL}_3(R)\rtimes\{\pm1\}$ is defined in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)), together with the following notions for a homomorphism $r$ from a group to $\mathcal G_3(R)$: its components $r(\gamma)=(\dot r(\gamma),\nu(\gamma))$, its sign $\nu$, the homomorphism $f\circ r$ to $\mathcal G_3(R')$ defined by a homomorphism of rings $f:R\to R'$, the weight $b-a$ of the position $(a,b)$ of a $3\times3$ matrix, and the adjoint action $\gamma\cdot X$ on $M_3(R)$ defined by $r$. For an integer $j$ let $M_3(R)_j\subset M_3(R)$ be the submodule of the matrices whose entries at the positions of weight different from $j$ are $0$. For $t\in R^\times$ put $T(t)=\operatorname{diag}(t,1,t^{-1})\in\mathrm{GL}_3(R)$. For an $\mathcal O$-algebra $R$ let $$r_0^R:\Gamma\to\mathcal G_3(R),\qquad r_0^R(\gamma)=\bigl(T(\Psi(\gamma)),\ \eta(\gamma)\bigr),$$ where $\Psi(\gamma)$ stands for its image in $R$. It is a homomorphism with sign $\eta$.

**Lifts.** Let $R$ be an $\mathcal O$-algebra that is a local ring, with maximal ideal $\mathfrak m_R$, and let $g_1\in\Gamma$. A *lift for $\mathfrak F$ at $g_1$ over $R$* is a homomorphism $r:\Gamma\to\mathcal G_3(R)$ with the following six properties.

1. $r$ has sign $\eta$, and every entry of $\dot r(\gamma)-T(\Psi(\gamma))$ lies in $\mathfrak m_R$, for every $\gamma\in\Gamma$.
2. For every integer $n\ge0$, the map $\gamma\mapsto\dot r(\gamma)\bmod\mathfrak m_R^n$ from $\Gamma$ to $M_3(R/\mathfrak m_R^n)$ is locally constant.
3. $\dot r(c)=1$, and the entries in positions $(1,2)$ and $(2,1)$ of the matrix $\dot r(g_1)-\dot r(c\,g_1^{-1}c)$ are $0$.
4. There is $h\in\mathrm{GL}_3(R)$, with all entries of $h-1$ in $\mathfrak m_R$, such that $h^{-1}\dot r(g)\,h$ is upper triangular for every $g\in D_\ell^+$ and has the diagonal entries $\Psi(s),1,\Psi(s)^{-1}$, in this order, for every $s\in I_\ell^+$.
5. For every $p\in S_b$ there is $h\in\mathrm{GL}_3(R)$, with all entries of $h-1$ in $\mathfrak m_R$, such that $h^{-1}\dot r(g)\,h$ is diagonal for every $g\in D_p^+$ and equals $T(\Psi(s))$ for every $s\in I_p^+$.
6. For every $p\in S$ with $p\ne\ell$ and $p\notin S_b$, and every $s\in I_p^1$, $r(s)=1$.

**Marked elements and universal lifts.** An element $g_1\in\Gamma$ is *marked* if $$\eta(g_1)=1\qquad\text{and}\qquad\Psi(g_1)^2-1\in\mathcal O^\times.$$ Let $\mathcal C_{\mathcal O}$ be the class of complete Noetherian local $\mathcal O$-algebras of ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)). A *universal lift for $\mathfrak F$ at $g_1$* is a pair $(R,u)$ of a ring $R\in\mathcal C_{\mathcal O}$ and a lift $u$ for $\mathfrak F$ at $g_1$ over $R$ such that, for every $R'\in\mathcal C_{\mathcal O}$ and every lift $r'$ for $\mathfrak F$ at $g_1$ over $R'$, there is exactly one homomorphism of $\mathcal O$-algebras $f:R\to R'$ with $f\circ u=r'$.

**Weights in the ring of a lift.** Let $R$ be an $\mathcal O$-algebra and $u:\Gamma\to\mathcal G_3(R)$ a homomorphism. For an integer $j$ let $R_j(u)$ be the set of the $x\in R$ with the following property: for every $R'\in\mathcal C_{\mathcal O}$, all homomorphisms of $\mathcal O$-algebras $f,f':R\to R'$ and every $t\in R'^\times$ such that $$(f'\circ u)(\gamma)=\bigl(T(t),1\bigr)\,(f\circ u)(\gamma)\,\bigl(T(t),1\bigr)^{-1}\qquad(\gamma\in\Gamma),$$ one has $f'(x)=t^{\,j}f(x)$. Each $R_j(u)$ is an $\mathcal O$-submodule of $R$; $1\in R_0(u)$ and $R_i(u)\,R_j(u)\subset R_{i+j}(u)$; and the entry $\dot u(\gamma)_{ab}$ lies in $R_{b-a}(u)$. The sum $$E(u)=\sum_{j\in\mathbb Z}R_j(u)$$ is therefore an $\mathcal O$-subalgebra of $R$ that contains all the entries $\dot u(\gamma)_{ab}$.

**Homomorphisms with values in $\overline{\mathbb Q}_\ell$.** The field $\overline{\mathbb Q}_\ell$ is an $\mathcal O$-algebra through the inclusion $\mathcal O\subset\overline{\mathbb Q}_\ell$. Let $r,r':\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ be homomorphisms.

- Let $R$ be an $\mathcal O$-algebra, $u:\Gamma\to\mathcal G_3(R)$ a homomorphism and $\xi:E(u)\to\overline{\mathbb Q}_\ell$ a homomorphism of $\mathcal O$-algebras. Then $r$ is *obtained from $u$ by $\xi$* if $r$ has the sign of $u$ and $\dot r(\gamma)_{ab}=\xi\bigl(\dot u(\gamma)_{ab}\bigr)$ for all $\gamma\in\Gamma$ and all $a,b\in\{1,2,3\}$.
- Let $g_1\in\Gamma$. Then $r$ is a *characteristic-zero lift for $\mathfrak F$ at $g_1$* if there are an $\mathcal O$-subalgebra $A\subset\overline{\mathbb Q}_\ell$ that is a discrete valuation ring and a finitely generated $\mathcal O$-module, an element $t\in\overline{\mathbb Q}_\ell^\times$, and a lift $r_A$ for $\mathfrak F$ at $g_1$ over $A$ such that, in $\mathcal G_3(\overline{\mathbb Q}_\ell)$, $$r_A(\gamma)=\bigl(T(t),1\bigr)\,r(\gamma)\,\bigl(T(t),1\bigr)^{-1}\qquad(\gamma\in\Gamma).$$
- $r$ is *irreducible on $\ker\eta$* if the only subspaces of $\overline{\mathbb Q}_\ell^3$ that all the matrices $\dot r(\gamma)$, $\gamma\in\ker\eta$, map to themselves are $0$ and $\overline{\mathbb Q}_\ell^3$.
- $r$ and $r'$ are *isomorphic on $\ker\eta$* if there is $M\in\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ with $M\,\dot r(\gamma)=\dot r'(\gamma)\,M$ for all $\gamma\in\ker\eta$.

**The condition $\mathcal P_K(\iota;r)$.** Let $K$ be a field of degree $2$ over $\mathbb Q$ that contains a square root of $-1$, and let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields. A homomorphism $r:\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ satisfies $\mathcal P_K(\iota;r)$ if the following three assertions hold.

1. For every open subgroup $U$ of $G$ that is contained in $\ker\eta_4$, the only subspaces of $\overline{\mathbb Q}_\ell^3$ that all the matrices $\dot r(g)$, $g\in U$, map to themselves are $0$ and $\overline{\mathbb Q}_\ell^3$.
2. The same holds for the subgroup $U=\ker\eta_4\cap\ker\epsilon_\ell$.
3. There are an embedding of fields $K\to\Omega$, by which $K$ is regarded as a subfield of $\Omega$ and $G_K=\operatorname{Gal}(\Omega/K)$ as a subgroup of $G$, and a homomorphism $\rho:G_K\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ with $\rho(s)=\dot r(s)$ for all $s\in G_K$, such that the twist $\rho\otimes\epsilon_\ell^{-1}$ satisfies the automorphy condition $\mathcal A_K(\iota;\rho\otimes\epsilon_\ell^{-1})$ of ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

**Rigidity.** Let $\overline{\mathbb Q}_\ell[\varepsilon]$ be the ring of dual numbers, $\varepsilon^2=0$. A homomorphism $r:\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ with sign $\eta$ is *rigid for $\mathfrak F$* if the following holds. Let $y:\Gamma\to M_3(\overline{\mathbb Q}_\ell)$ be a continuous map and $r':\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell[\varepsilon])$ a homomorphism with sign $\eta$ such that, for the adjoint action defined by $r$, $$y(\gamma\delta)=y(\gamma)+\gamma\cdot y(\delta),\qquad\dot r'(\gamma)=\bigl(1+\varepsilon\,y(\gamma)\bigr)\,\dot r(\gamma)\qquad(\gamma,\delta\in\Gamma).$$ Suppose that

1. $y(s)=0$ for every $s\in I_p^1$ and every $p\in S$ with $p\ne\ell$ and $p\notin S_b$;
2. there is $h\in\mathrm{GL}_3(\overline{\mathbb Q}_\ell[\varepsilon])$ such that $h^{-1}\dot r'(g)\,h$ is upper triangular for every $g\in D_\ell^+$ and has the diagonal entries $\Psi(s),1,\Psi(s)^{-1}$, in this order, for every $s\in I_\ell^+$; and
3. for every $p\in S_b$ there is $h\in\mathrm{GL}_3(\overline{\mathbb Q}_\ell[\varepsilon])$ such that $h^{-1}\dot r'(g)\,h$ is diagonal for every $g\in D_p^+$ and equals $T(\Psi(s))$ for every $s\in I_p^+$.

Then there is $X\in M_3(\overline{\mathbb Q}_\ell)$ with $y(\gamma)=X-\gamma\cdot X$ for all $\gamma\in\Gamma$.

**Property (V).** In this paragraph $\Gamma$ acts on $M_3(\mathcal O)$ by the adjoint action defined by $r_0^{\mathcal O}$. The deformation datum $\mathfrak F$ *has property (V)* if the following holds for every integer $j\le0$. Let $z:\Gamma\to M_3(\mathcal O)_j$ be a map with the following five properties.

1. $z(\gamma\delta)=z(\gamma)+\gamma\cdot z(\delta)$ for all $\gamma,\delta\in\Gamma$.
2. For all $a,b\in\{1,2,3\}$ and every integer $n\ge0$, the map $\gamma\mapsto z(\gamma)_{ab}\bmod\mathfrak m_{\mathcal O}^n$ is locally constant on $\Gamma$.
3. $z(s)=0$ for every $s\in I_p^1$ and every $p\in S$ with $p\ne\ell$ and $p\notin S_b$.
4. If $j=0$, then $z(s)=0$ for every $s\in I_p$ and every $p\in\{\ell\}\cup S_b$.
5. If $j<0$, then there is $Y\in M_3(\mathcal O)_j$ with $z(g)=Y-g\cdot Y$ for all $g\in D_\ell^+$.

Then there are a nonzero $a\in\mathcal O$ and a matrix $X\in M_3(\mathcal O)$ with $a\,z(\gamma)=X-\gamma\cdot X$ for all $\gamma\in\Gamma$.

**The residual Selmer group of weight $-2$.** In this paragraph $\Gamma$ acts on $M_3(k)$ by the adjoint action defined by $r_0^{k}$; this action maps $M_3(k)_{-2}$ to itself, and $M_3(k)_{-2}$ carries the discrete topology. The *residual Selmer group of weight $-2$ of $\mathfrak F$ is zero* if every continuous map $y:\Gamma\to M_3(k)_{-2}$ with the following three properties is of the form $y(\gamma)=\gamma\cdot Y-Y$ for some $Y\in M_3(k)_{-2}$.

1. $y(\gamma\delta)=y(\gamma)+\gamma\cdot y(\delta)$ for all $\gamma,\delta\in\Gamma$.
2. $y(s)=0$ for every $s\in I_p^1$ and every $p\in S$ with $p\ne\ell$.
3. There is $Y_\ell\in M_3(k)_{-2}$ with $y(g)=g\cdot Y_\ell-Y_\ell$ for all $g\in D_\ell$.
