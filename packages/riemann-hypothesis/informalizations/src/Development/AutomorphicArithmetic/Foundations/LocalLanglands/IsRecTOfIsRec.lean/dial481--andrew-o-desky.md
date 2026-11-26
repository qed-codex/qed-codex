---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean",
  "declarations": [
    "UpperTheory.Zero.LLC.RecTExists"
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

## Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties

[Definition / hypothesis AGR.D077](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)

This statement is used as a hypothesis by other theorems of the catalogue, and the Lean project proves it. It asserts that for every number field $E$ and every finite place $w$ of $E$ there is a map from the irreducible smooth representations of the groups $\mathrm{GL}_n(E_w)$, $n\ge 0$, to Weil-Deligne representations that satisfies properties 1 to 12 below. Properties 7 to 11 are required only for the *good* representations defined below.

**Setting.** Let $E$ be a number field, $\bar E$ an algebraic closure of $E$, $w$ a finite place of $E$, $k=E_w$ the completion, $\mathcal O_k$ its ring of integers with maximal ideal $\mathfrak m_k$, and $q$ the number of elements of the residue field of $w$. Let $A$ be a valuation ring of $\bar E$ lying over $w$, with absolute value $|\cdot|_A$. Let $D\supset I\supset P$ be the decomposition group of $A$ in $\operatorname{Gal}(\bar E/E)$, its inertia subgroup, and the wild inertia subgroup $P=\{g\in I:\ |g(x)-x|_A<|x|_A\text{ for all }x\ne 0\}$.

**Weil group.** The Weil group $W\subset D$ consists of the $g\in D$ whose action on the residue field of $A$ is an integer iterate of the Frobenius automorphism $x\mapsto x^q$. The number of iterations is the degree $\deg g$; negative degrees mean iterations of the inverse automorphism. Thus $I=\ker\deg$ and an arithmetic Frobenius element has degree $1$. A homomorphism from $W$ to $\mathbb C^\times$ or to $\mathrm{GL}_n(\mathbb C)$ is *smooth* if it is trivial on an open subgroup of $I$.

**Local Artin maps.** A *global Artin map* for $E$ is a homomorphism $\operatorname{Art}:\mathbb A_E^\times\to\operatorname{Gal}(\bar E/E)^{\mathrm{ab}}$ (the quotient by the closure of the commutator subgroup) which is continuous, open and surjective, whose kernel is the closure of $E^\times\cdot(\mathbb A_{E,\infty}^\times)^0$, where $(\mathbb A_{E,\infty}^\times)^0$ is the connected component of the identity in the group $\mathbb A_{E,\infty}^\times=\prod_{v\mid\infty}E_v^\times$ of ideles with component $1$ at every finite place, and such that for every finite place $v$ and every valuation ring $A'$ of $\bar E$ over $v$: the image of the units of $E_v$ is the image of the inertia group of $A'$; the image of the uniformizers of $E_v$ is the set of classes of $g^{-1}$ with $g$ an arithmetic Frobenius element of $A'$; and the closure of the image of $E_v^\times$ is the image of the decomposition group of $A'$.

A *local Artin map* for $(E,w,A)$ is a homomorphism $\operatorname{art}:W\to k^\times$ such that

- $\operatorname{art}$ is surjective and its restriction to $I$ is continuous;
- $\operatorname{ord}_w(\operatorname{art}(g))=-\deg g$ for all $g\in W$;
- every smooth character of $W$ has the form $\chi\circ\operatorname{art}$ with $\chi$ a character of $k^\times$ with open kernel;
- for every global Artin map $\operatorname{Art}$ and every $g\in W$, $\operatorname{Art}$ sends the idele with component $\operatorname{art}(g)$ at $w$ and $1$ elsewhere to the class of $g$.

**Weil-Deligne representations.** A Weil-Deligne representation of dimension $n\ge 0$ is a pair $(R,N)$ in which $R:W\to\mathrm{GL}_n(\mathbb C)$ is a smooth homomorphism with every $R(g)$ semisimple and $N$ is a nilpotent $n\times n$ matrix with $$R(g)N=q^{\deg g}NR(g)\qquad(g\in W).$$ Let $\mathcal G$ be the set of isomorphism classes of Weil-Deligne representations of all dimensions. On $\mathcal G$ we use: the dimension; the direct sum $\oplus$; the tensor product $(R\otimes R',\,N\otimes1+1\otimes N')$; the dual $(R^\vee,-N^{\mathsf T})$; the twist $u(s)$ of a class $u=(R,N)$ by the character $g\mapsto q^{s\deg g}$, for real $s$; and the characteristic polynomial $\det(X-R(g))$ of $R(g)$, for $g\in W$. A smooth character $\xi$ of $W$ is identified with the class $(\xi,0)$ of dimension $1$. The class $\operatorname{Sp}(m)$, $m\ge 1$, is $\mathbb C^m$ with basis $e_0,\dots,e_{m-1}$, with $R(g)e_i=q^{(i-(m-1)/2)\deg g}e_i$, $Ne_i=e_{i+1}$ and $Ne_{m-1}=0$. A class $(R,N)$ is *irreducible* if $R$ is an irreducible representation of $W$, and *tame* if $R$ is trivial on $P$.

**Representations of $\mathrm{GL}_n(k)$.** Let $\mathcal A$ be the disjoint union over $n\ge 0$ of the sets of isomorphism classes of irreducible smooth complex representations of $\mathrm{GL}_n(k)$; $n$ is the *degree* of the class. For $\pi\in\mathcal A$ of degree $n$, a character $\chi$ of $k^\times$ with open kernel and a real number $s$, write $\pi\chi$ for $\pi\otimes(\chi\circ\det)$ and $\pi(s)$ for $\pi\otimes|\det|^s$, where $|\cdot|$ is the normalized absolute value of $k$: for an additive Haar measure $\mu$, $|t|=\mu(t\mathcal O_k)/\mu(\mathcal O_k)$ for $t\in k^\times$. Characters of $k^\times$ with open kernel are the classes of degree $1$.

For classes $\pi_1,\dots,\pi_h$ of degrees $n_1,\dots,n_h$, choose representatives $\rho_i$ on spaces $V_i$. Their *normalized parabolic induction* $\pi_1\times\dots\times\pi_h$ is the following representation of $G=\mathrm{GL}_{n_1+\dots+n_h}(k)$. Let $Q\subset G$ be the block upper triangular subgroup with block sizes $n_1,\dots,n_h$. For $b\in Q$ with diagonal blocks $b_1,\dots,b_h$, put $$\delta_Q(b)=\prod_{i=1}^h|\det b_i|^{\sum_{j>i}n_j-\sum_{j<i}n_j}.$$ The representation space consists of functions $f:G\to V_1\otimes_{\mathbb C}\cdots\otimes_{\mathbb C}V_h$ satisfying $$f(bx)=\delta_Q(b)^{1/2}\big(\rho_1(b_1)\otimes\cdots\otimes\rho_h(b_h)\big)f(x)$$ for all $b\in Q$ and $x\in G$, and having an open stabilizer under right translation. The action is $(x_0f)(x)=f(xx_0)$. For $h=0$, the tensor product and the induced representation are $\mathbb C$ with the trivial action of $\mathrm{GL}_0(k)$.

A representation $\sigma$ is the *irreducible quotient* of a representation $\Pi$ if $\sigma$ is irreducible and there is a surjection $\Pi\to\sigma$ whose kernel is the only maximal proper subrepresentation of $\Pi$.

A class $\sigma$ of degree $n$ is *cuspidal* if $n\ge 1$ and the space of $U$-coinvariants of $\sigma$ is zero for every subgroup $U\ne1$ of $\mathrm{GL}_n(k)$ that is conjugate, by a permutation matrix, to the unipotent radical of a block upper triangular subgroup. A multiset of cuspidal classes is a *cuspidal support* of a class $\pi$ if its members can be listed as $\sigma_1,\dots,\sigma_h$ in such a way that $\pi$ is a quotient of a subrepresentation of $\sigma_1\times\dots\times\sigma_h$. A class has *depth zero* if it has a nonzero vector fixed by the kernel of $\mathrm{GL}_n(\mathcal O_k)\to\mathrm{GL}_n(\mathcal O_k/\mathfrak m_k)$.

A *segment* is a pair $\Delta=(\sigma,m)$ of a cuspidal class $\sigma$ and an integer $m\ge 1$; its terms are $\sigma,\sigma(1),\dots,\sigma(m-1)$, and $L(\Delta)$ denotes the class of the irreducible quotient of $\sigma\times\sigma(1)\times\dots\times\sigma(m-1)$, when this representation has one. A segment $\Delta=(\sigma,m)$ *precedes* $\Delta'=(\sigma',m')$ if the union of their sets of terms is the set of terms of a segment, neither set of terms contains the other, and $\sigma'=\sigma(j)$ for an integer $j>0$.

A class $\pi\in\mathcal A$ is *good* if it has a cuspidal support each of whose members $\sigma$ satisfies at least one of the following conditions: $\sigma$ has degree $1$; or there is a continuous ring isomorphism $\mathbb Q_p\to k$ for a prime $p$, and $\sigma=\sigma_0\chi$ for a class $\sigma_0$ of depth zero and a character $\chi$ of $k^\times$ with open kernel.

**The hypothesis.** For every number field $E$, algebraic closure $\bar E$, finite place $w$ and valuation ring $A$ of $\bar E$ over $w$, there are a map $\operatorname{rec}:\mathcal A\to\mathcal G$ and a local Artin map $\operatorname{art}$ for $(E,w,A)$ with the following properties.

1. $\dim\operatorname{rec}(\pi)$ is the degree of $\pi$.
2. $\operatorname{rec}(\chi)=\chi\circ\operatorname{art}$ for every character $\chi$ of $k^\times$ with open kernel.
3. Let $\Delta_1=(\sigma_1,m_1),\dots,\Delta_h=(\sigma_h,m_h)$ be segments such that $\Delta_i$ does not precede $\Delta_j$ for $i<j$. Suppose that every $L(\Delta_i)$ exists and that $L(\Delta_1)\times\dots\times L(\Delta_h)$ has an irreducible quotient, and let $\pi$ be the class of this quotient. Then $$\operatorname{rec}(\pi)=\bigoplus_{i=1}^h\operatorname{rec}(\sigma_i)\big(\tfrac{m_i-1}2\big)\otimes\operatorname{Sp}(m_i).$$
4. If $\pi$ is cuspidal, then $\operatorname{rec}(\pi)$ is irreducible.
5. $\operatorname{rec}(\pi(s))=\operatorname{rec}(\pi)(s)$ for real $s$.
6. If $\pi$ has central character $\omega$, then $|\det R(g)|=|\omega(\operatorname{art}(g))|$ for $\operatorname{rec}(\pi)=(R,N)$ and all $g\in W$.
7. If $\pi$ is good, then $\operatorname{rec}(\pi\chi)=\operatorname{rec}(\pi)\otimes\operatorname{rec}(\chi)$.
8. If $\pi$ is good with central character $\omega$, then $\det R(g)=\omega(\operatorname{art}(g))$ for $\operatorname{rec}(\pi)=(R,N)$ and all $g\in W$.
9. If $\pi$ is good and $\pi'$ is the class of the smooth dual of $\pi$, then $\operatorname{rec}(\pi')=\operatorname{rec}(\pi)^\vee$.
10. If $\pi'$ is good and $\operatorname{rec}(\pi)=\operatorname{rec}(\pi')$, then $\pi=\pi'$.
11. If $\pi$ is good and of depth zero, then $\operatorname{rec}(\pi)$ is tame.
12. (Depth-zero cuspidal types.) Suppose there is a continuous ring isomorphism $i:\mathbb Q_p\to k$ for a prime $p$. Let $n\ge 1$, let $E'\subset\bar E$ be a finite extension of $E$ and $w'$ the place of $E'$ below $A$, and suppose that $p\notin w'^2$ and that the residue field $\mathbb F'$ of $w'$ has $p^n$ elements, so that $E'_{w'}$ is the unramified extension of degree $n$ of $\mathbb Q_p$. Let $\operatorname{art}'$ be a local Artin map for $(E',w',A)$. Let $\theta:\mathbb F'^\times\to\mathbb C^\times$ be a character such that $\theta,\theta^p,\dots,\theta^{p^{n-1}}$ are distinct, and let $\tau$ be an irreducible complex representation of $\mathrm{GL}_n(\mathbb F_p)$ which has no nonzero vector fixed by the unipotent radical of any proper standard maximal parabolic subgroup and whose character satisfies $$\operatorname{tr}\tau(\gamma)=(-1)^{n-1}\sum_{j=0}^{n-1}\theta\big(z^{p^j}\big)$$ for every $\gamma\in\mathrm{GL}_n(\mathbb F_p)$ with irreducible characteristic polynomial and every root $z\in\mathbb F'$ of that polynomial. Let $\pi\in\mathcal A$ have degree $n$ and suppose that there is a nonzero linear map from the space of $\tau$ to the space of $\pi$ which is equivariant for $\mathrm{GL}_n(\mathbb Z_p)$, acting on $\tau$ through reduction modulo $p$ and on $\pi$ through $i$. Then $\operatorname{rec}(\pi)=(R,N)$ has $N=0$, and for every $t$ in the inertia group of $A$ over $E'$ and every $z\in\mathbb F'^\times$ that is the reduction of the unit $\operatorname{art}'(t)$ of $E'_{w'}$, $$\det\big(X-R(t)\big)=\prod_{j=0}^{n-1}\Big(X-\theta\big(z^{p^j}\big)\Big).$$
