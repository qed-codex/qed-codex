---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LatticeDataThicknessBound.lean",
  "declarations": [
    "GlobalTheory.CongL.CrysDRU",
    "GlobalTheory.CongL.FieldOK",
    "GlobalTheory.CongL.GenAtU",
    "GlobalTheory.CongL.IsSysU",
    "GlobalTheory.CongL.SatU"
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

## Systems of Hecke eigenvalues on a definite unitary group and their l-adic polynomial approximation

[Definition / hypothesis AGR.D280](https://andrewodesky.com/rh/lean/GlobalTheory.Cong.Levels/)

Throughout, $E$ is a CM field with maximal totally real subfield $E^+$, $\ell$ is a prime, $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ is an isomorphism of fields, $|\cdot|_\ell$ is the $\ell$-adic absolute value of $\overline{\mathbb Q}_\ell$, and $a\ge1$ is an integer. The definite unitary group $\mathcal U$ in $a$ variables over $E$, the representations of $GL_a(E_w)$ that occur in a space of functions on $\mathcal U$ at a finite place $w$, and Satake multisets are those of ([Satake multisets and weights of definite unitary forms](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)); split places, the place $w^+$ of $E^+$ below $w$ and the multisets $R_w(B)$ are those of ([Special automorphic representations of a definite unitary group at two places above l](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.FieldOK/)). This page defines the systems of Hecke eigenvalues of a space of functions on $\mathcal U$ and the approximation of one family of $\ell$-adic numbers by linear combinations of others.

**Level families.** A *level family* is a family $K=(K_w)$ of subgroups $K_w\subseteq GL_a(E_w)$, one for every finite place $w$ of $E$. Let $w_0$ and $v'$ be finite places of $E$, and let $U$ be a complex vector space of functions on $\mathcal U$. The space $U$ *has level $K$ away from $w_0$ and $v'$* if, for every split place $w$ of $E$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$, every smooth irreducible representation $(\sigma,V)$ of $GL_a(E_w)$ that occurs in $U$ at $w$ has a nonzero vector fixed by $K_w$.

**Systems of Hecke operators.** Let $K$ be a level family. A *system of Hecke operators for $K$*, indexed by a set $J$, consists of the following for every $j\in J$:

- a split finite place $w_j$ of $E$ that does not divide $\ell$;
- a function $f_j\colon GL_a(E_{w_j})\to\mathbb C$ with finite support such that $|\iota^{-1}(f_j(g))|_\ell\le1$ for all $g$;
- a function $z_j$ that assigns a complex number $z_j(\sigma)$ to every smooth irreducible complex representation $(\sigma,V)$ of $GL_a(E_{w_j})$, such that $$\sum_{g}f_j(g)\,\sigma(g)v=z_j(\sigma)\,v\qquad\text{for every }v\in V\text{ fixed by }K_{w_j}.$$

The system is *rational* if every value $f_j(g)$ is a rational number.

**Systems of eigenvalues.** Let $U$ be a complex vector space of functions on $\mathcal U$. A family $\theta=(\theta_j)_{j\in J}$ of elements of $\overline{\mathbb Q}_\ell$ is a *system of eigenvalues of $U$* for a system of Hecke operators indexed by $J$ if $\theta_j=\iota^{-1}(z_j(\sigma))$ for every $j\in J$ and every smooth irreducible representation $\sigma$ of $GL_a(E_{w_j})$ that occurs in $U$ at $w_j$.

**Power sums of a Satake multiset.** For every complex vector space $U$ of functions on $\mathcal U$ and every finite place $w$ of $E$ at which $U$ has a Satake multiset, fix one Satake multiset $B(U,w)$ of $U$ at $w$. For an integer $n$, put $$s_n(U,w)=\sum_{z\in R_w(B(U,w))}z^{\,n}$$ if $U$ has a Satake multiset at $w$, and $s_n(U,w)=0$ otherwise.

**Polynomial approximation.** Let $I$ be a set, let $\eta\in\overline{\mathbb Q}_\ell^{\,I}$ and let $\mathcal S\subseteq\overline{\mathbb Q}_\ell^{\,I}$. The family $\eta$ is *polynomially approximated by $\mathcal S$* if, for every real number $\varepsilon>0$, there are a finite subset $\mathcal S_0\subseteq\mathcal S$ and coefficients $c_\xi\in\overline{\mathbb Q}_\ell$, $\xi\in\mathcal S_0$, such that $$\Bigl|P(\eta)-\sum_{\xi\in\mathcal S_0}c_\xi\,P(\xi)\Bigr|_\ell\le\varepsilon\qquad\text{for every }P\in\mathbb Z[X_i:i\in I].$$ The subset $\mathcal S_0$ and the coefficients depend on $\varepsilon$ and not on $P$.

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

## Satake multisets and weights of definite unitary forms

[Definition / hypothesis AGR.D101](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)

Let $E$ be a CM field, $E^+$ its maximal totally real subfield, $a\ge0$ an integer, and $\mathbb A_E$ the adele ring of $E$. Complex conjugation of $E$ induces an involution $g\mapsto\bar g$ on the matrices with entries in $\mathbb A_E$. The *definite unitary group in $a$ variables over $E$* is the unitary group of the identity Hermitian form, $$\mathcal U=\{g\in GL_a(\mathbb A_E):{}^t\bar g\,g=I_a\},$$ with the topology induced from $GL_a(\mathbb A_E)$. It acts on the complex-valued functions on $\mathcal U$ by right translation, $(R_gf)(h)=f(hg)$. This page defines the automorphic representations of $\mathcal U$ and, for such a representation, its Satake multisets at the finite places of $E$, its weights at the embeddings of $E$ in $\mathbb C$, and a condition that relates these weights to the Hodge–Tate multisets of a representation of the Galois group of $E$.

**Subgroups and components.** The field $E$ is embedded diagonally in $\mathbb A_E$, and $\mathcal U_{\mathbb Q}=\mathcal U\cap GL_a(E)$ denotes the subgroup of the elements of $\mathcal U$ with entries in $E$. Let $\mathcal U^\infty$ be the subgroup of the elements of $\mathcal U$ whose component at every infinite place of $E$ is the identity, and $\mathcal U_\infty$ the subgroup of the elements whose component at every finite place of $E$ is the identity.

For a finite place $w$ of $E$, let $E_w$ be the completion of $E$ at $w$, $\mathcal O_w$ its valuation ring, and $N(w)$ the cardinality of its residue field. Let $\mathcal U_w$ be the subgroup of the elements of $\mathcal U^\infty$ whose component is the identity at every finite place of $E$ that does not lie above the place of $E^+$ below $w$. For $g\in\mathcal U$, write $g_w\in GL_a(E_w)$ for the component of $g$ at $w$. For an embedding $\tau\colon E\to\mathbb C$, let $\mathcal U_\tau$ be the subgroup of the elements of $\mathcal U_\infty$ whose component is the identity at every infinite place of $E$ other than the place of $\tau$, and write $g_\tau\in GL_a(\mathbb C)$ for the component of $g$ at the place of $\tau$, read through the isomorphism of the completion with $\mathbb C$ that extends $\tau$.

**Occurrence of a local representation.** Let $U$ be a complex vector space of functions $\mathcal U\to\mathbb C$. A representation $(\sigma,V)$ of $GL_a(E_w)$ on a complex vector space *occurs in $U$ at $w$* if it is irreducible and there is a nonzero complex-linear map $F\colon V\to U$ such that $$F(\sigma(g_w)v)=R_gF(v)\qquad(g\in\mathcal U_w,\ v\in V).$$ A representation of $GL_a(\mathbb C)$ *occurs in $U$ at $\tau$* if the same condition holds with $\mathcal U_\tau$ and $g_\tau$ in place of $\mathcal U_w$ and $g_w$.

**Automorphic forms and automorphic representations.** An *automorphic form* on $\mathcal U$ is a continuous function $\phi\colon\mathcal U\to\mathbb C$ with the following three properties: $\phi(\gamma g)=\phi(g)$ for all $\gamma\in\mathcal U_{\mathbb Q}$ and $g\in\mathcal U$; there is an open subgroup of $\mathcal U^\infty$ all of whose elements $k$ satisfy $R_k\phi=\phi$; and the functions $R_k\phi$ with $k\in\mathcal U_\infty$ span a finite-dimensional space. An *automorphic representation* of $\mathcal U$ is a nonzero complex vector space $U$ of automorphic forms on $\mathcal U$ that is stable under $R_g$ for every $g\in\mathcal U$ and whose only subspaces stable under all the $R_g$ are $0$ and $U$. The space $U$ is *unramified at $w$* if there is a nonzero $f\in U$ with $R_gf=f$ for all $g\in\mathcal U_w$ with $g_w\in GL_a(\mathcal O_w)$.

**Satake multisets.** Put $\mathcal K_w=GL_a(\mathcal O_w)$. A representation $(\sigma,V)$ of $GL_a(E_w)$ on a complex vector space is *smooth* if the stabilizer of every vector is open, and *spherical* if its subspace $V^{\mathcal K_w}$ of vectors fixed by $\mathcal K_w$ is nonzero. A finite multiset $B$ of nonzero complex numbers is a *Satake multiset of $U$ at $w$* if there is a smooth irreducible representation $(\sigma,V)$ of $GL_a(E_w)$ that occurs in $U$ at $w$, is spherical, and satisfies the following condition: $|B|=a$, and for every nonzero $v\in V^{\mathcal K_w}$, every uniformizer $\varpi\in E_w$ and every integer $0\le j\le a$, $$\sum_{c}\sigma(c)v=N(w)^{j(a-j)/2}e_j(B)\,v,\qquad D_j(\varpi)=\operatorname{diag}(\underbrace{\varpi,\ldots,\varpi}_{j},1,\ldots,1),$$ where $c$ runs over a set of representatives of the cosets $c\mathcal K_w$ contained in $\mathcal K_wD_j(\varpi)\mathcal K_w$. Here $e_j(B)$ is the $j$-th elementary symmetric function of the elements of $B$, counted with multiplicity, and the power of $N(w)$ is the positive real power.

**Weights.** A *weight* is a sequence of integers $\lambda=(\lambda_0,\dots,\lambda_{a-1})$ with $\lambda_0\ge\dots\ge\lambda_{a-1}$; these are the dominant integral weights of length $a$ of ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)). For a weight $\lambda$, put $c=\lambda_{a-1}$ if $a>0$ and $c=0$ if $a=0$, and $\nu_k=\lambda_k-c\ge0$ for $0\le k<a$. Let $X=(X_{ik})_{0\le i,k<a}$ be a square matrix of variables. Let $V_\lambda$ be the space of the polynomials $P\in\mathbb C[X_{ik}]$ that are homogeneous of degree $\nu_k$ in the variables of column $k$ of $X$, for every $k$, and that are unchanged, for every pair of columns $i<k$, by the substitution that adds $t$ times column $i$ to column $k$, where $t$ is a further variable. This is the polynomial dual Weyl module $\nabla_\nu(\mathbb C)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)), for $a$ rows and $a$ columns. The group $GL_a(\mathbb C)$ acts on $V_\lambda$ by $$(\sigma_\lambda(g)P)(X)=(\det g)^c\,P({}^tg\,X)\qquad(g\in GL_a(\mathbb C)),$$ where $P({}^tg\,X)$ is the result of replacing each variable $X_{ik}$ by the $(i,k)$ entry $\sum_bg_{bi}X_{bk}$ of the matrix ${}^tg\,X$; this is the row substitution of that page for the matrix ${}^tg$. A weight $\lambda$ *occurs in $U$ at $\tau$* if the representation $(\sigma_\lambda,V_\lambda)$ occurs in $U$ at $\tau$. Define $$J(\lambda)=\{k-\lambda_k:0\le k<a\}.$$ The integers $k-\lambda_k$ are distinct, so $J(\lambda)$ has $a$ elements.

The weight $\lambda$ is a highest weight of $\sigma_\lambda$ for the group of upper triangular matrices, in the following sense. Let $\Delta_k(X)$ be the determinant of the first $k$ rows and columns of $X$, and put $\nu_a=0$. The polynomial $\prod_{k=1}^{a}\Delta_k(X)^{\nu_{k-1}-\nu_k}$ lies in $V_\lambda$; the operator $\sigma_\lambda(g)$ fixes it when $g$ is upper triangular with diagonal entries $1$, and multiplies it by $\prod_{k=0}^{a-1}s_k^{\lambda_k}$ when $g$ is the diagonal matrix with entries $s_0,\dots,s_{a-1}$.

**Lacunary sets, embeddings over a place, lacunary weights.** A finite set $J$ of integers is *lacunary* if any two disjoint nonempty subsets $J_1,J_2$ of $J$ have different averages: $$|J_2|\sum_{h\in J_1}h\ne|J_1|\sum_{h\in J_2}h.$$ Let $\ell$ be a prime and $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ an isomorphism of fields. An embedding $\tau\colon E\to\mathbb C$ *lies over* a finite place $w$ of $E$ if $|\iota^{-1}(\tau(x))|_\ell<1$ for every $x$ in the prime ideal of $w$; then $w$ lies above $\ell$. The space $U$ has a *lacunary weight at $w$* if there are an embedding $\tau$ over $w$ and a weight $\lambda$ that occurs in $U$ at $\tau$ for which $J(\lambda)$ is lacunary.

**Hodge–Tate multisets containing the weights of $U$.** Let $\bar E$ be an algebraic closure of $E$, $G_E=\operatorname{Aut}(\bar E/E)$, and $\rho\colon G_E\to GL_n(\overline{\mathbb Q}_\ell)$ a representation. Places $A$ of $\bar E$ above $w$, their decomposition groups $D_A$, local data at $A$, embeddings that extend to the field $K_w$ of the local data, and Hodge–Tate multisets are those of ([Local conditions on an l-adic representation of the Galois group of a number field](https://andrewodesky.com/rh/lean/GlobalTheory.RoadWGeo.ESAt/)). The *Hodge–Tate multisets of $\rho$ at $w$ contain the weights of $U$* if, for every place $A$ of $\bar E$ above $w$, all local data at $A$, every embedding $\tau\colon E\to\overline{\mathbb Q}_\ell$ that extends to $K_w$, and every weight $\lambda$ that occurs in $U$ at $\iota\circ\tau$, there is a Hodge–Tate multiset of $\rho|_{D_A}$ at $\tau$ that contains every element of $J(\lambda)$.
