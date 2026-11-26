---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ApartAllEmpty.lean",
  "declarations": [
    "GlobalTheory.CongL.UsPl"
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
