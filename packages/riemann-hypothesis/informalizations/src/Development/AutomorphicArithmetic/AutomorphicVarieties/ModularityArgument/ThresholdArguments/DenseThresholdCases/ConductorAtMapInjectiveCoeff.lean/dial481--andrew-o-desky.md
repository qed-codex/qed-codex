---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean",
  "declarations": [
    "UpperTheory.V.Th.sp4Main_alt"
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

## Selmer lengths and trace congruences in dimension four

[Theorem AGR.1.1773](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.sp4Main_alt/)

The data for $(\Omega,\ell,\mathcal O)$, their characters, their points and their specializations are defined in ([Symplectic lifts of a sum of four characters and their specializations](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Raw/)). The irreducible and the rigid specializations of a datum, its Selmer length, the Selmer lengths with conditions at a set of primes, the number $e_{\mathcal O}$ and the graded models of a datum are defined in ([Irreducible and rigid specializations, Selmer lengths and graded models of a symplectic datum of four characters](https://andrewodesky.com/rh/lean/UpperTheory.V.GradeZeroInterpolatingElement.Irr/)). The condition $\mathcal A^{\rm q}(\iota;r)$ and the class $\mathcal R_4(\iota,e,M)$ of four-dimensional representations are defined in ([Automorphy over imaginary quadratic fields and a class of four-dimensional l-adic representations of the Galois group of Q](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Win.IsAutQA/)). The constants $N_\chi$, $o$, $p_K$, $h_K$ and $p_1$ of a primitive Dirichlet character $\chi$, the auxiliary triples $(\nu,q,d)$ for $\chi$ and their moduli, the sets $\mathscr X_{\mathcal O}(e)$ of Dirichlet characters and cases II and III are defined in ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)). For an algebraic closure $\Omega$ of $\mathbb Q$ write $G=\operatorname{Gal}(\Omega/\mathbb Q)$, write $I_A\subset D_A\subset G$ for the inertia group and the decomposition group of a valuation subring $A$ of $\Omega$, and, for a prime $\ell$, write $\epsilon_\ell:G\to\mathbb Z_\ell^\times$ for the $\ell$-adic cyclotomic character. A *coefficient ring* for a prime $\ell$ is a discrete valuation ring $\mathcal O\subset\overline{\mathbb Q}_\ell$ that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module.

**Theorem 1.** Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell$ an odd prime, $\mathcal O$ a coefficient ring for $\ell$, and $\mathfrak D$ a datum for $(\Omega,\ell,\mathcal O)$, with characters $\theta$, $\Psi$ and $\alpha$ and with $\rho_0=\operatorname{diag}(\theta,\Psi,\alpha,1)$. Assume the following seven conditions.

1. $\mathfrak D$ has a graded model.
2. The assertions of the theorems ([Cotangent length bounded by valuations at graded orbits](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/)) and ([Lengths of modules of liftable derivations bounded by a cotangent length](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.mprime_holds/)) hold.
3. Assertions (2)–(4) and (9)–(12) of ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)) hold.
4. Hypothesis (S) below holds for $\Omega$ and $\ell$.
5. For every point $\rho$ of $\mathfrak D$, over a ring $R$, the weight-zero subalgebra $R_0(\rho)\subset R$ is a finitely generated $\mathcal O$-module.
6. For every specialization $r$ of $\mathfrak D$ such that $r(g)$ is of block form for every $g\in G$, the corners $r(g)^{\square}$, $g\in G$, do not span the $\overline{\mathbb Q}_\ell$-vector space $M_2(\overline{\mathbb Q}_\ell)$.
7. Every irreducible specialization of $\mathfrak D$ is rigid for $\mathfrak D$.

Let $g\in G$ be such that $$\operatorname{tr}r(g)\ne\operatorname{tr}\rho_0(g)\qquad\text{for every irreducible specialization }r\text{ of }\mathfrak D.$$ Then the Selmer length $L$ of $\mathfrak D$ is finite, and there is a finite set $\Xi$ of irreducible specializations of $\mathfrak D$, no two distinct members of which are conjugate, such that $$\frac L{e_{\mathcal O}}\le2\sum_{r\in\Xi}v_\ell\bigl(\operatorname{tr}r(g)-\operatorname{tr}\rho_0(g)\bigr).$$

**Theorem 2.** Assume the hypotheses (H1)–(H9) listed below. Let $\star$ be one of the two cases II and III. For every primitive Dirichlet character $\chi$ there is a natural number $C$ with the following property. Let $(\nu,q,d)$ be an auxiliary triple for $\chi$, with modulus $N$, and let $t\ge0$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1.$$ Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell$ an odd prime, $\mathcal O$ a coefficient ring for $\ell$, $e$ an integer with $0<e<t$, and $\psi\in\mathscr X_{\mathcal O}(e)$ a character such that $(\ell,e,\psi)$ is in case $\star$. Then the Selmer length $L$ of $(\epsilon_\ell^e\psi)^{-1}$ formed with $\mathcal O$ and $N$, in the sense of ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)), is finite, and $$\frac L{e_{\mathcal O}}\,\log\ell\le(\ell Ne)^C.$$

**Hypotheses of Theorem 2.**

- (H1) The three assertions of ([Finiteness and automorphy for the symplectic lifts of a sum of four characters](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt/)) hold for all the data $\Omega$, $\chi$, $(\nu,q,d)$, $t$, $\ell$, $\mathcal O$, $e$, $\psi$ and $\mathfrak D$ that satisfy the conditions of that theorem.
- (H2) The twelve assertions of ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)) hold.
- (H3) The assertion of the theorem ([Cotangent length bounded by valuations at graded orbits](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/)) holds.
- (H4) The assertion of the theorem ([Lengths of modules of liftable derivations bounded by a cotangent length](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.mprime_holds/)) holds.
- (H5) The assertion of the theorem ([A homogeneous presentation for a framed deformation problem](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.lemmaP/)) holds.
- (H6) Hypothesis (T) below holds.
- (H7) Hypothesis (R) below holds.
- (H8) Hypothesis (B) below holds.
- (H9) Hypothesis (S) below holds for every algebraic closure $\Omega$ of $\mathbb Q$ and every prime $\ell$.

**Hypothesis (S)**, for an algebraic closure $\Omega$ of $\mathbb Q$ and a prime $\ell$. The following two assertions hold.

- (S1) Let $\psi:G\to\overline{\mathbb Q}_\ell^\times$ be a homomorphism with open kernel, let $e\ge1$ be an integer, and put $\Theta=(\epsilon_\ell^e\psi)^{-1}$. Let $z:G\to\overline{\mathbb Q}_\ell$ be a continuous map with $z(gh)=z(g)+\Theta(g)\,z(h)$ for all $g,h\in G$. Suppose that for every valuation subring $A$ of $\Omega$ there is $m\in\overline{\mathbb Q}_\ell$ with $z(g)=\Theta(g)\,m-m$ for all $g\in I_A$, and that for every place $A$ of $\Omega$ above $\ell$ there is $m\in\overline{\mathbb Q}_\ell$ with $z(g)=\Theta(g)\,m-m$ for all $g\in D_A$. Then there is $m\in\overline{\mathbb Q}_\ell$ with $z(g)=\Theta(g)\,m-m$ for all $g\in G$.
- (S2) For every coefficient ring $\mathcal O$ for $\ell$, every homomorphism $\psi:G\to\mathcal O^\times$ with open kernel and every integer $e\ge1$, the Selmer length of $(\epsilon_\ell^e\psi)^{-1}$ with conditions at $\{\ell\}$ is finite.

**Hypothesis (T).** There are natural numbers $c$ and $A$ with the following property. Let $e\ge2$ and $M\ge1$ be integers, let $p\ge5$ be a prime with $p\nmid M$, let $k\ge1$ be an integer, and let $z_1,z_2,z_3\in\mathbb C$ satisfy $z_1^k=z_2^k=z_3^k=1$. Then there is a nonzero integer $\Delta$ with $$\log|\Delta|\le c\,\varphi(k)\,\bigl(M(e+1)\bigr)^A\log p$$ such that the following holds for every prime $\ell\notin\{2,p\}$, every algebraic closure $\Omega$ of $\mathbb Q$, every isomorphism of fields $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$, every place $B$ of $\Omega$ above $p$, every Frobenius element $\sigma\in G$ at $B$, and every finite subset $X$ of $\mathcal R_4(\iota,e,M)$ that does not contain two distinct isomorphic representations. Put $\tau=\iota^{-1}\bigl(p^{e+1}z_1+p^ez_2+pz_3+1\bigr)$. Then $\operatorname{tr}r(\sigma)\ne\tau$ for all $r\in X$, and $$|\Delta|_\ell\le\prod_{r\in X}\bigl|\operatorname{tr}r(\sigma)-\tau\bigr|_\ell.$$

**Hypothesis (R).** Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell$ an odd prime, $\mathcal O$ a coefficient ring for $\ell$, and $\mathfrak D$ a datum for $(\Omega,\ell,\mathcal O)$, with characters $\psi$, $\xi$ and $\omega$. Suppose that there are a primitive Dirichlet character $\chi$, an auxiliary triple $(\nu,q,d)$ for $\chi$, an integer $t\ge0$ such that $q$ and $d$ are both larger than each of the six numbers displayed in Theorem 2, an integer $e_0$ with $0<e_0<t$ and a character $\psi_0\in\mathscr X_{\mathcal O}(e_0)$, formed with this triple, such that $\mathfrak D$ is of case II or of case III for $\chi$, $(\nu,q,d)$, $e_0$ and $\psi_0$. Let $M\ge1$ be an integer such that $\psi$, $\xi$ and $\omega$ are trivial on $\operatorname{Gal}(\Omega/\mathbb Q(\mu_M))$, and let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields. Then every irreducible specialization $r$ of $\mathfrak D$ that satisfies $\mathcal A^{\rm q}(\iota;r)$ is rigid for $\mathfrak D$.

**Hypothesis (B).** Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell$ a prime, $\mathcal O$ a coefficient ring for $\ell$, $\mathbb F$ a field of characteristic $\ell$ and $\varrho:\mathcal O\to\mathbb F$ a homomorphism of rings. Let $a\ge1$, $f\ge1$ and $n\ge0$ be integers, let $\lambda$ be a Dirichlet character modulo $f$ and $\xi'$ a Dirichlet character modulo $2^n$, both with values in $\mathcal O$, and suppose that

1. $4$ divides $\ell^a-1$, and $f$ is odd;
2. $\lambda$ and $\xi'$ are primitive, and the order of $\lambda$ divides $\ell^a-1$;
3. $f\cdot4^{\,v}\le2^n$, where $2^v$ is the largest power of $2$ that divides $\ell^a-1$; and
4. $\lambda(-1)\,\xi'(-1)=-1$.

Let $\gamma_0:G\to\mathbb F^\times$ be the composite of $\varrho$ with the character $\lambda\,\xi'$ of $G$, and let $\gamma$ be $\gamma_0$ or $\gamma_0^{-1}$. Let $z:G\to\mathbb F$ be a locally constant map with $z(gh)=z(g)+\gamma(g)\,z(h)$ for all $g,h\in G$. Suppose that for every valuation subring $A$ of $\Omega$ there is a subgroup $H\subset G$ such that $H\cap I_A\cap\ker\gamma$ has finite index prime to $\ell$ in $I_A\cap\ker\gamma$ and $z(g)=0$ for all $g\in H\cap I_A\cap\ker\gamma$. Then there is $m\in\mathbb F$ with $z(g)=\gamma(g)\,m-m$ for all $g\in G$.
