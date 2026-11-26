---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/BlochKatoSelmerVanishes.lean",
  "declarations": [
    "UpperTheory.V.Af.AttC",
    "UpperTheory.V.Af.AttachedSys",
    "UpperTheory.V.Af.BlochKatoSelmerVanishes",
    "UpperTheory.V.Af.FrobEig",
    "UpperTheory.V.Af.IsBK",
    "UpperTheory.V.Af.KillsMu",
    "UpperTheory.V.Af.Level",
    "UpperTheory.V.Af.LevelAt",
    "UpperTheory.V.Af.LevelAway",
    "UpperTheory.V.Af.algSat"
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

## Hypotheses on the points of the deformation rings of a sum of three characters

[Definition / hypothesis AGR.D097](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.RigidityFirstCase/)

This page states three hypotheses of the theorem ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)). Each concerns the local points of the deformation rings defined in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)): the first two assert the vanishing of Selmer groups of adjoint representations at these points, and the third places the representations of the points in a class of automorphic representations.

**Vanishing of $H^1_f$.** Let $\overline{\mathbb Q}$ be an algebraic closure of $\mathbb Q$, $G_{\mathbb Q}=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$, $\ell$ a prime and $G_{\mathbb Q_\ell}=\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell)$. Let $V$ be a finite-dimensional vector space over $\overline{\mathbb Q}_\ell$, with its $\ell$-adic topology, and let $G_{\mathbb Q}$ act on $V$ by linear maps. A *cocycle* is a continuous map $a:G_{\mathbb Q}\to V$ with $a(gh)=a(g)+g\,a(h)$ for all $g,h$, and a *coboundary* is a map $g\mapsto gx-x$ with $x\in V$. A cocycle $a$ satisfies the *Selmer conditions* if the following two conditions hold.

1. For every prime $p\ne\ell$ there are a place $A$ of $\overline{\mathbb Q}$ above $p$ and an element $x\in V$ with $a(s)=sx-x$ for every $s$ in the inertia group of $A$.
2. There is an embedding of fields $j:\overline{\mathbb Q}\to\overline{\mathbb Q}_\ell$ for which the following holds. Let $D_j$ be the group of pairs $(g,s)\in G_{\mathbb Q}\times G_{\mathbb Q_\ell}$ with $s\circ j=j\circ g$; it acts on $V$ through $g$ and on the crystalline period ring $B_{\rm cris}$ through $s$. Then there is $z\in V\otimes_{\mathbb Q_\ell}B_{\rm cris}$ with $$a(g)\otimes1=(g,s)z-z\qquad\text{for all }(g,s)\in D_j.$$

We write $H^1_f(\mathbb Q,V)=0$ if every cocycle that satisfies the Selmer conditions is a coboundary. Here $B_{\rm cris}$ is the ring that carries the structure of Fontaine's crystalline period ring in local period data for the prime $\ell$, in the sense of ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)); one choice of local period data is used for each $\ell$.

**Setting of the hypotheses.** Let $K$, $\ell$, $\mathcal O$, $N$, $e$, $\psi$, a datum $\mathfrak D$ with its character $\eta$ and its complex conjugation $c$, a universal lift $(R^{\rm loc},r^{\rm loc})$, an element $g_1\in G_{\mathbb Q}$ such that $(c,g_1)$ is marked, a deformation ring $(S,r_S)$ of $\mathfrak D$ at $g_1$ formed with $(R^{\rm loc},r^{\rm loc})$, and a local point $f$ of $S$ be as in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)), with the homomorphism $r_f:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ and the representation $\rho_f$ of $G_K$. Let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields. Conditions (I) and (II), the adjoint action $\operatorname{ad}r_f$ and the homomorphisms that extend the corner of $r_f$ are defined on that page. The conditions $\mathcal A_K$ and $\mathcal M_e$ and the class $\mathcal R_1(\iota,e,N)$ are defined in ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

Each of the following three hypotheses is the assertion that its statement holds for all these data.

**Hypothesis (P1): rigidity at irreducible automorphic points.** If $r_f$ satisfies condition (I) and $\mathcal A_K(\iota;\rho_f\otimes\epsilon_\ell^{-1})$ holds, then $H^1_f(\mathbb Q,M_3(\overline{\mathbb Q}_\ell))=0$ for the adjoint action $\operatorname{ad}r_f$ of $G_{\mathbb Q}$ on $M_3(\overline{\mathbb Q}_\ell)$.

**Hypothesis (P2): rigidity at points of block form.** Suppose that $r_f$ satisfies condition (II), and let $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ be a continuous homomorphism that extends the corner of $r_f$ and satisfies $\det W=\eta$ and $\mathcal M_e(\iota;W)$. Then $H^1_f(\mathbb Q,M_2(\overline{\mathbb Q}_\ell))=0$ for every linear action of $G_{\mathbb Q}$ on $M_2(\overline{\mathbb Q}_\ell)$ of the following kind: there are a complex conjugation $c'\in G_{\mathbb Q}$ and a matrix $P\in\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ such that $${}^tW(s)\,P\,W(c'sc'^{-1})=P,\qquad s\cdot X=W(s)\,X\,W(s)^{-1},\qquad c'\cdot X=-P^{-1}\,{}^tX\,P$$ for all $s\in G_K$ and $X\in M_2(\overline{\mathbb Q}_\ell)$.

**Hypothesis (P3): irreducible automorphic points belong to $\mathcal R_1$.** If $r_f$ satisfies condition (I) and $\mathcal A_K(\iota;\rho_f\otimes\epsilon_\ell^{-1})$ holds, then $\rho_f\in\mathcal R_1(\iota,e,N)$.

## Special automorphic representations of a definite unitary group at two places above l

[Definition / hypothesis AGR.D281](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.FieldOK/)

Throughout, $E$ is a CM field with maximal totally real subfield $E^+$, $\bar E$ is an algebraic closure of $E$, $G_E=\operatorname{Aut}(\bar E/E)$, $\ell$ is a prime, $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ is an isomorphism of fields, and $a\ge1$ is an integer. The definite unitary group $\mathcal U$ in $a$ variables over $E$, its automorphic representations, the representations that occur in a space of functions on $\mathcal U$ at a finite place or at an embedding $E\to\mathbb C$, Satake multisets, weights $\lambda=(\lambda_0\ge\dots\ge\lambda_{a-1})$, the sets $J(\lambda)=\{k-\lambda_k:0\le k<a\}$ and the embeddings $E\to\mathbb C$ that lie over a finite place are those of ([Satake multisets and weights of definite unitary forms](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)). This page defines the automorphic representations of $\mathcal U$ that are special at two places above $\ell$, and the conditions on a representation of $G_E$ that are used with them.

**Places.** For a finite place $w$ of $E$, write $w^+$ for the place of $E^+$ below $w$, $E_w$ for the completion and $N(w)$ for the cardinality of the residue field. The place $w$ is *split* if some other place of $E$ lies above $w^+$, and *nonsplit* otherwise. For a finite set $S$ of finite places of $E$, write $S^+=\{s^+:s\in S\}$.

**Field conditions and eligible places.** Let $d$ be a positive integer. The triple $(E,\ell,d)$ *satisfies the field conditions* if $-d$ is a square in $E$ and in $\mathbb Q_\ell$, the degree $[E^+:\mathbb Q]$ is even, and every nonsplit finite place of $E$ is unramified over $E^+$ and does not divide $\ell$. A finite place $w$ of $E$ is *eligible* for $d$ if it is split and $-d$ is a square in $\mathbb Q_q$, where $q$ is the prime number below $w$.

**The type condition.** Let $w_0$ be a finite place of $E$. A complex vector space $U$ of functions on $\mathcal U$ *satisfies the type condition at $w_0$* if there are an integer $m\ge1$, a compact open subgroup $\Gamma$ of $GL_a(E_{w_0})$ whose only element of finite order is the identity, a surjective homomorphism $\theta\colon\Gamma\to\mathbb Z/\ell^m\mathbb Z$ and a nontrivial character $\chi\colon\mathbb Z/\ell^m\mathbb Z\to\mathbb C^\times$ with the following two properties.

- Every smooth irreducible complex representation $(\sigma,V)$ of $GL_a(E_{w_0})$ that has a nonzero vector $\xi$ with $\sigma(\gamma)\xi=\chi(\theta(\gamma))\xi$ for all $\gamma\in\Gamma$ is cuspidal.
- Some nonzero $f\in U$ satisfies $R_gf=\chi(\theta(g_{w_0}))f$ for every $g\in\mathcal U_{w_0}$ with $g_{w_0}\in\Gamma$.

Here a smooth representation $(\sigma,V)$ of $GL_a(E_{w_0})$ is *cuspidal* if its Jacquet module with respect to the unipotent radical of every proper parabolic subgroup that contains the diagonal matrices is zero, as in ([Galois representations with local conditions, given a fixed-point trace formula](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one/)).

**Rapidly increasing weights.** A weight $\lambda$ is *rapidly increasing* if the elements $j_k=k-\lambda_k$ of $J(\lambda)$, which satisfy $j_0<j_1<\dots<j_{a-1}$, also satisfy $$j_{i+1}-j_0>a\,(j_i-j_0)\qquad(0\le i\le a-2).$$

**Special representations.** Let $w_0$ and $v'$ be finite places of $E$ above $\ell$. An automorphic representation $U'$ of $\mathcal U$ is *special at $(w_0,v')$* if it has the following three properties.

- (S1) $U'$ satisfies the type condition at $w_0$.
- (S2) $U'$ has a Satake multiset at $v'$.
- (S3) There is an embedding $\tau_0\colon E\to\mathbb C$ that lies over $v'$ such that every weight that occurs in $U'$ at $\tau_0$ is rapidly increasing.

**Weights away from two places.** Every embedding $\tau\colon E\to\mathbb C$ lies over exactly one finite place $u_\tau$ of $E$, the place of the prime ideal $\{x\in\mathcal O_E:|\iota^{-1}(\tau(x))|_\ell<1\}$; it lies above $\ell$. Let $U$ and $U'$ be complex vector spaces of functions on $\mathcal U$. The space $U'$ *has the weights of $U$ away from $w_0$ and $v'$* if, for every embedding $\tau\colon E\to\mathbb C$ with $u_\tau^+\ne w_0^+$ and $u_\tau^+\ne v'^+$, a weight occurs in $U'$ at $\tau$ if and only if it occurs in $U$ at $\tau$.

**Multisets in general position.** A multiset $B=\{\beta_1,\dots,\beta_a\}$ of $a$ nonzero complex numbers is *in general position* if the following three conditions hold.

- (G1) $\beta_i^{\,c}\ne\beta_j^{\,c}$ for all $i\ne j$ and all integers $1\le c\le a$.
- (G2) $\beta_i\beta_k\ne\beta_j^{\,2}$ for all indices $i,j,k$ with $j\ne i$ and $j\ne k$.
- (G3) $\prod_i\beta_i^{\,m_i}\ne\prod_i\beta_i$ for all integers $0\le m_1,\dots,m_a\le a$ with $\sum_im_i=a$ that are not all equal to $1$.

A complex vector space $U$ of functions on $\mathcal U$ *is in general position at a finite place $w$* if every Satake multiset of $U$ at $w$ is in general position.

**The Frobenius polynomial.** For a finite place $w$ of $E$ and a multiset $B$ of $a$ nonzero complex numbers, put $$R_w(B)=\bigl\{N(w)^{(a-1)/2}\beta:\beta\in B\bigr\},\qquad P_{w,B}(X)=\prod_{z\in R_w(B)}\bigl(X-\iota^{-1}(z)\bigr)\in\overline{\mathbb Q}_\ell[X],$$ where $N(w)^{(a-1)/2}$ is the positive real power. Let $\rho\colon G_E\to GL_a(\overline{\mathbb Q}_\ell)$ be a representation. We say that *$\rho$ is unramified at $w$ with Frobenius polynomial $P_{w,B}$* if, for every place $A$ of $\bar E$ above $w$, the representation $\rho$ is trivial on the inertia group $I_A$ and $\rho(\sigma)^{-1}$ has characteristic polynomial $P_{w,B}$ for every Frobenius element $\sigma$ at $A$.

**Crystalline with the weights of $U$.** Let $w$ be a finite place of $E$ and $U$ a complex vector space of functions on $\mathcal U$. We say that *$\rho$ is crystalline and de Rham at $w$ with the weights of $U$* if, for every place $A$ of $\bar E$ above $w$ and all local data at $A$, the representation $\rho|_{D_A}$ is crystalline and de Rham and, for every embedding $\tau\colon E\to\overline{\mathbb Q}_\ell$ that extends to the field $K_w$ of the local data and every weight $\lambda$ that occurs in $U$ at $\iota\circ\tau$, the set $J(\lambda)$ is a Hodge–Tate multiset of $\rho|_{D_A}$ at $\tau$.

**Power sums on the Weil–Deligne representation.** Let $A$ be a place of $\bar E$ above a finite place $w$, with local data at $A$, let $g\in W_A$ and let $n\ge0$ be an integer. For a homomorphism $r\colon D_A\to GL_a(\overline{\mathbb Q}_\ell)$, write $$p_n(r;g)=\sum_{x}x^n,$$ where $x$ runs over the roots, counted with multiplicity, of the characteristic polynomial of $g$ on $\operatorname{WD}(r)$. For a multiset $B$ of $a$ nonzero complex numbers we say that *$\rho$ has the Frobenius power sums of $B$ at $w$* if, for every place $A$ of $\bar E$ above $w$, all local data at $A$, every $g\in W_A$ and every integer $n\ge0$, $$p_n(\rho|_{D_A};g)=\sum_{z\in R_w(B)}z^{-n\deg g}.$$ A monic complex polynomial is determined by the power sums of its roots, so the condition says that every $g\in W_A$ has characteristic polynomial $\prod_{z\in R_w(B)}(X-z^{-\deg g})$ on $\operatorname{WD}(\rho|_{D_A})$.
