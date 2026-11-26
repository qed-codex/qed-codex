---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/WeakOfAtt.lean",
  "declarations": [
    "UpperTheory.V.Z.Win.PotUnl",
    "UpperTheory.V.Z.Win.Unl1",
    "UpperTheory.V.Z.Win.WitA"
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

## Automorphy with a conditional local window condition

[Definition / hypothesis GC.D007](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.AutOnAlt/)

Let $K$ be a CM field, $\Omega$ an algebraic closure of $\mathbb Q$, $\ell$ a prime and $\iota\colon\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism. Let $a$ assign a $3\times3$ matrix over $\overline{\mathbb Q}_\ell$ to each element of $\operatorname{Gal}(\Omega/\mathbb Q)$.

The **automorphy and window condition** on $a$ is the existence of an embedding $K\hookrightarrow\Omega$ and a representation $\rho\colon\operatorname{Gal}(\Omega/K)\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ whose matrices are the restrictions of $a$, such that the twist $\rho\otimes\chi_\ell^{-1}$ has both properties below. Here $\chi_\ell$ is the $\ell$-adic cyclotomic character.

1. There is a regular algebraic conjugate self-dual cuspidal representation of $\mathrm{GL}_3(\mathbb A_K)$ to which the twist is attached via $\iota$ (the attachment condition is not expanded).
2. If the twist is continuous, then at every prime above $\ell$ an invariant-flag condition implies a stronger invariant-flag condition; and, for every regular algebraic cuspidal representation to which the twist is attached, there is a real number $t$ such that a window condition with parameter $t$ holds at every prime not above $\ell$ and at every prime above $\ell$ satisfying the stronger invariant-flag condition. The flag and window conditions are not expanded.

## Level, attachment and comparison conditions on l-adic Galois representations

[Definition / hypothesis AGR.D051](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)

This page defines conditions on a representation of the Galois group of a number field with coefficients in $\overline{\mathbb Q}_\ell$: a condition on its restrictions to inertia and decomposition groups, called the level condition; attachment to a newform and to a cuspidal automorphic representation; a comparison condition, which bounds the local components of the automorphic representations to which the representation is attached; and two conditions that combine these. It then defines two classes of three-dimensional representations of the Galois group of an imaginary quadratic field.

**Setting.** Let $F$ be a number field, $\overline F$ an algebraic closure of $F$ and $G_F=\operatorname{Gal}(\overline F/F)$. Let $\ell$ be a prime, $\overline{\mathbb Q}_\ell$ an algebraic closure of $\mathbb Q_\ell$ with the absolute value $|\cdot|_\ell$ normalized by $|\ell|_\ell=1/\ell$, and $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ an isomorphism of fields. Write $\epsilon_\ell:G_F\to\mathbb Z_\ell^\times\subset\overline{\mathbb Q}_\ell^\times$ for the $\ell$-adic cyclotomic character. A *representation* is a homomorphism $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ with $n\ge0$; it is continuous only where this is said. It is *irreducible* if $n\ge1$ and the only subspaces of $\overline{\mathbb Q}_\ell^n$ that $r(G_F)$ maps to themselves are $0$ and $\overline{\mathbb Q}_\ell^n$, and *semisimple* if every such subspace has a complement of the same kind. Two representations $r,r'$ are *isomorphic* if $r'(s)=g\,r(s)\,g^{-1}$ for some $g\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ and all $s$. For a character $\chi:G_F\to\overline{\mathbb Q}_\ell^\times$, the twist $r\otimes\chi$ is $s\mapsto\chi(s)r(s)$. For an extension $F'\subset\overline F$ of $F$, the restriction of $r$ to $G_{F'}$ is written $r|_{G_{F'}}$.

Let $v$ be a finite place of $F$, with residue field of cardinality $q_v$. A *place of $\overline F$ above $v$* is a valuation subring $A$ of $\overline F$ whose maximal ideal $\mathfrak m_A$ meets the ring of integers of $F$ in the prime ideal of $v$. Its decomposition group $D_A$ is the stabilizer of $A$ in $G_F$; its inertia group $I_A$ consists of the $s\in D_A$ with $s(x)-x\in\mathfrak m_A$ for all $x\in A$; a *Frobenius element at $A$* is an $s\in D_A$ with $s(x)-x^{q_v}\in\mathfrak m_A$ for all $x\in A$. A representation is *triangular on $D_A$ with diagonal characters $\kappa_1,\dots,\kappa_n$*, where the $\kappa_i:D_A\to\overline{\mathbb Q}_\ell^\times$ are homomorphisms, if there is $g\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ such that, for every $s\in D_A$, the matrix $g\,r(s)\,g^{-1}$ is upper triangular with diagonal entries $\kappa_1(s),\dots,\kappa_n(s)$, in this order.

For an integer $M\ge1$ let $F(\mu_M)\subset\overline F$ be the field generated over $F$ by the $M$-th roots of unity. A homomorphism defined on $G_F$ is trivial on $G_{F(\mu_M)}$ exactly when it is trivial on every element of $G_F$ that fixes all $M$-th roots of unity.

**The level condition.** Let $M\ge1$ be an integer and $\mathbf m=(m_1,\dots,m_n)\in\mathbb Z^n$. A representation $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ satisfies $\mathcal L_\ell(M;\mathbf m;r)$ if the following three conditions hold.

1. $r$ is continuous.
2. For every finite place $v\nmid\ell$ of $F$ there are a place $A$ of $\overline F$ above $v$, characters $\chi_1,\dots,\chi_n:G_F\to\overline{\mathbb Q}_\ell^\times$ that are trivial on $G_{F(\mu_M)}$, and $g\in\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ such that $g\,r(s)\,g^{-1}$ is the diagonal matrix with entries $\chi_1(s),\dots,\chi_n(s)$ for every $s\in I_A$.
3. For every place $v\mid\ell$ of $F$ there are a place $A$ of $\overline F$ above $v$, characters $\chi_1,\dots,\chi_n:G_F\to\overline{\mathbb Q}_\ell^\times$ that are trivial on $G_{F(\mu_M)}$, and homomorphisms $\kappa_1,\dots,\kappa_n:D_A\to\overline{\mathbb Q}_\ell^\times$ such that $r$ is triangular on $D_A$ with diagonal characters $\kappa_1,\dots,\kappa_n$, such that $$\kappa_i(s)=\epsilon_\ell(s)^{m_i}\chi_i(s)\qquad(s\in I_A,\ 1\le i\le n),$$ and such that at least one of the following holds: $\kappa_i\ne\kappa_j\cdot\epsilon_\ell|_{D_A}$ for all $i,j$; or the restriction of $r$ to $D_A$ is potentially crystalline.

**Newforms and attachment to a newform.** Let $k\ge1$ and $M\ge1$ be integers and $\chi$ a complex Dirichlet character modulo $M$. For a holomorphic function $g$ on the upper half-plane with $g(z+1)=g(z)$, write $g=\sum_na_n(g)q^n$, $q=e^{2\pi iz}$. Say that $g$ *has character $\chi$* if $g|_k\gamma=\chi(d)\,g$ for every $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(M)$, where $|_k$ is the weight-$k$ action. For a prime $p$ and $\lambda\in\mathbb C$, say that $g$ *satisfies the Hecke relation at $p$ with eigenvalue $\lambda$* if $$a_{pn}(g)+\chi(p)\,p^{k-1}a_{n/p}(g)=\lambda\,a_n(g)\qquad(n\ge1),$$ where $a_{n/p}(g)=0$ if $p\nmid n$. A *newform of weight $k$*, level $M$ and character $\chi$ is a cusp form $f$ of weight $k$ for $\Gamma_1(M)$ with character $\chi$ such that $a_1(f)=1$; $f$ satisfies the Hecke relation at every prime $p\nmid M$ with eigenvalue $a_p(f)$; and, for every divisor $M'\ne M$ of $M$ and every Dirichlet character $\chi'$ modulo $M'$, the only cusp form $g$ of weight $k$ for $\Gamma_1(M')$ with character $\chi'$ that satisfies the Hecke relation (for $\chi'$) with eigenvalue $a_p(f)$ at all but finitely many primes $p$ is $g=0$.

Here $F=\mathbb Q$. A representation $V:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ is *attached to the newform $f$* if $V$ is semisimple and, for all but finitely many primes $p$ and every place $A$ of $\overline{\mathbb Q}$ above $p$, $V$ is trivial on $I_A$ and every Frobenius element $s$ at $A$ satisfies $$\iota\bigl(\det(X-V(s^{-1}))\bigr)=X^2-a_p(f)X+\chi(p)\,p^{k-1}.$$

**Attachment to a cuspidal automorphic representation.** Let $F$ be totally complex and let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb A_F)$ in the sense of ([Cuspidal automorphic representations of GL\_a over a totally complex number field](https://andrewodesky.com/rh/lean/GlobalTheory.CuspRep.CuspSub/)). A representation $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ is *attached to $\pi$* if $r$ is semisimple and, for all but finitely many finite places $v$ of $F$, $\pi$ has a multiset $B_v$ of Satake parameters at $v$ such that, for every place $A$ of $\overline F$ above $v$, $r$ is trivial on $I_A$ and every Frobenius element $s$ at $A$ satisfies $$\iota\bigl(\det(X-r(s^{-1}))\bigr)=\prod_{\beta\in B_v}\bigl(X-q_v^{(n-1)/2}\beta\bigr).$$ Suppose in addition that $F$ is a CM field, with complex conjugation $c$. The representation $\pi$ is *conjugate self-dual* if there is a complex bilinear form $B:V_\pi\times V_\pi\to\mathbb C$, nondegenerate in each variable, with the three invariance properties that condition 2 in the definition of polarized pairs on that page requires of its form: $B(h\varphi,c(h)\varphi')=B(\varphi,\varphi')$, $B(\kappa\varphi,\bar\kappa\varphi')=B(\varphi,\varphi')$ and $B(X\varphi,\varphi')+B(\varphi,\bar X\varphi')=0$, with $h$, $\kappa$, $X$ and the conjugations as there.

**The comparison condition.** Let $F$ be a CM field and $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ a representation. For a place $v\mid\ell$ of $F$ consider the two conditions

- $(\mathrm T_v)$: for every place $A$ of $\overline F$ above $v$, $r$ is triangular on $D_A$ with diagonal characters $\kappa_1,\dots,\kappa_n$ such that $\kappa_i\ne\kappa_j\cdot\epsilon_\ell|_{D_A}$ for all $i,j$;
- $(\mathrm T^\infty_v)$: for every place $A$ of $\overline F$ above $v$, $r$ is triangular on $D_A$ with diagonal characters $\kappa_1,\dots,\kappa_n$ such that $\kappa_i^m\ne(\kappa_j\cdot\epsilon_\ell|_{D_A})^m$ for all $i,j$ and all integers $m\ge1$.

The representation $r$ satisfies the *comparison condition* $\mathcal W_F(\iota;r)$ if the following two conditions hold.

1. For every place $v\mid\ell$ of $F$, $(\mathrm T_v)$ implies $(\mathrm T^\infty_v)$.
2. For every regular algebraic cuspidal automorphic representation $\pi$ of $\mathrm{GL}_n(\mathbb A_F)$ to which $r$ is attached, there is a real number $t$ such that the following holds at every finite place $v$ of $F$ with $v\nmid\ell$, and at every place $v\mid\ell$ at which $(\mathrm T^\infty_v)$ holds. The cuspidal support of every local component of $\pi$ at $v$ consists of characters of $F_v^\times$, and every character $\xi$ in the cuspidal support of a local component of $\pi$ at $v$ satisfies $$q_v^{\,t-1/2}<|\xi(\varpi_v)|<q_v^{\,t+1/2},$$ where $\varpi_v$ is a uniformizer of $F_v$, chosen once for each $v$.

For a representation $r$ of $G_{\mathbb Q}$, the condition $\mathcal W^{\rm q}(\iota;r)$ requires $\mathcal W_{F'}(\iota;r|_{G_{F'}})$ for every imaginary quadratic field $F'\subset\overline{\mathbb Q}$ such that $r|_{G_{F'}}$ is irreducible.

**The automorphy condition and the modularity condition.** Let $F$ be a CM field. A representation $r:G_F\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)$ satisfies the *automorphy condition* $\mathcal A_F(\iota;r)$ if

1. $r$ is attached to a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb A_F)$ that is regular algebraic and conjugate self-dual, and
2. if $r$ is continuous, then $\mathcal W_F(\iota;r)$ holds.

Let $e\ge0$ be an integer. A representation $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ satisfies the *modularity condition* $\mathcal M_e(\iota;W)$ if $W\otimes\epsilon_\ell^{-e}$ is attached to a newform of weight $2e+1$ and $\mathcal W^{\rm q}(\iota;W)$ holds.

**Two classes of three-dimensional representations.** Let $K\subset\overline{\mathbb Q}$ be an imaginary quadratic field, so that $G_K\subset G_{\mathbb Q}$, and let $e\ge0$ and $M\ge1$ be integers.

The class $\mathcal R_1(\iota,e,M)$ consists of the representations $\rho:G_K\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ with the following four properties.

1. $\rho$ is irreducible.
2. $\mathcal A_K(\iota;\rho\otimes\epsilon_\ell^{-1})$ holds.
3. $\mathcal L_\ell(M;(e,0,-e);\rho)$ holds.
4. For every place $v\mid\ell$ of $K$, the place $A$, the characters $\chi_i$ and the homomorphisms $\kappa_i$ in condition 3 of $\mathcal L_\ell(M;(e,0,-e);\rho)$ can be chosen such that $\kappa_i\ne\kappa_j\cdot\epsilon_\ell|_{D_A}$ for all $i,j$.

The class $\mathcal R_2(\iota,e,M)$ consists of the representations $\rho:G_K\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ for which there is a representation $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ with the following five properties.

1. $W$ is irreducible.
2. $\mathcal M_e(\iota;W)$ holds.
3. $\mathcal L_\ell(M;(e,-e);W)$ holds.
4. $\det W$ is trivial on $G_{\mathbb Q(\mu_{M'})}$ for some integer $M'\ge1$.
5. $\rho$ is isomorphic to $W|_{G_K}\oplus1$: there is $g\in\mathrm{GL}_3(\overline{\mathbb Q}_\ell)$ with $$g\,\rho(s)\,g^{-1}=\begin{pmatrix}W(s)_{11}&0&W(s)_{12}\\0&1&0\\W(s)_{21}&0&W(s)_{22}\end{pmatrix}\qquad(s\in G_K).$$

For an integer $N\ge1$ put $$\mathcal R(\iota,e,N)=\mathcal R_1(\iota,e,N)\cup\mathcal R_2\bigl(\iota,e,N\,|\operatorname{disc}K|\bigr).$$
