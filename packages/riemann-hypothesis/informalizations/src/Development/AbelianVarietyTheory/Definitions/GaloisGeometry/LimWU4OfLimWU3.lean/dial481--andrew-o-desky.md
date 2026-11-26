---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWU4OfLimWU3.lean",
  "declarations": [
    "GlobalTheory.CongL.CongFinOdd",
    "GlobalTheory.CongL.LimFinOdd",
    "GlobalTheory.CongL.SeedFinOdd"
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

## Galois representations of special automorphic representations of a definite unitary group of odd rank

[Theorem AGR.1.1774](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne/)

Assume the following hypothesis.

- **Hypothesis G.** The statement of ([Galois representations with local conditions, given a fixed-point trace formula](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one/)) holds without its assumption of ([A fixed-point trace formula for finite étale correspondences](https://andrewodesky.com/rh/lean/UpperTheory.Gal.LocalSmoothExtension.HolomorphicLefschetzFormula/)). That is, for all $E$, $\bar E$, $\ell$, $\iota$, $a$, $d$, $x$, $U$, $w_0$ and $v'$ that satisfy the conditions of that theorem, including its conditions (a) to (d), its assertions 1, 2 and 3 hold.

Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\bar E$ be an algebraic closure of $E$ and $G_E=\operatorname{Aut}(\bar E/E)$, let $\ell$ be a prime, let $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $a$ be an odd positive integer. Let $d$ be a positive integer such that $(E,\ell,d)$ satisfies the field conditions. Let $\mathcal U$ be the definite unitary group in $a$ variables over $E$. Let $T$ be a finite set of nonsplit finite places of $E$, let $w_0$ and $v'$ be split places of $E$ above $\ell$ with $w_0^+\ne v'^+$, let $U$ be a complex vector space of functions on $\mathcal U$, and let $S$ and $Y$ be finite sets of finite places of $E$.

Then there is a finite set $Z_0$ of finite places of $E$ with the following two properties.

**The places of $Z_0$.** Every $z\in Z_0$ is eligible for $d$, does not divide $\ell$, and satisfies $z^+\ne w_0^+$ and $z^+\notin S^+$.

**The representation.** Let $U'$ be an automorphic representation of $\mathcal U$ that satisfies the following four conditions.

- (a) $U'$ is unramified at every nonsplit finite place of $E$ outside $T$.
- (b) $U'$ is special at $(w_0,v')$ and has the weights of $U$ away from $w_0$ and $v'$.
- (c) $U'$ has a Satake multiset at every split place $w$ of $E$ with $w^+\ne w_0^+$ and $w^+\notin S^+$.
- (d) $U'$ is in general position at every place of $Z_0$.

Then there is a continuous semisimple representation $\rho\colon G_E\to GL_a(\overline{\mathbb Q}_\ell)$ with the following four properties.

1. There are a dense open subset $G'$ of $G_E$ and a finite set $X$ of finite places of $E$ such that the following holds for every place $w\notin X$ of $E$ that is eligible for $d$, does not divide $\ell$ and satisfies $w^+\notin S^+$, every Satake multiset $B$ of $U'$ at $w$ and every place $A$ of $\bar E$ above $w$: the representation $\rho$ is trivial on the inertia group $I_A$, and $\rho(\sigma)^{-1}$ has characteristic polynomial $P_{w,B}$ for every Frobenius element $\sigma$ at $A$ that lies in $G'$.
2. Let $w\in Y$ be eligible for $d$, with $w\nmid\ell$ and $w^+\notin S^+$, and let $B$ be a Satake multiset of $U'$ at $w$ that is in general position. Then $\rho$ is unramified at $w$ with Frobenius polynomial $P_{w,B}$.
3. Let $w\in Y$ be a place above $\ell$ with $w^+\ne w_0^+$, $w^+\ne v'^+$ and $w^+\notin S^+$. Then $\rho$ is crystalline and de Rham at $w$ with the weights of $U'$.
4. Let $w$ be as in property 3, and let $B$ be a Satake multiset of $U'$ at $w$ that is in general position. Then $\rho$ has the Frobenius power sums of $B$ at $w$.

## l-adic approximation of the Hecke eigenvalues of an automorphic representation of a definite unitary group by those of special representations

[Theorem AGR.1.1775](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.congFinOdd_of_ex/)

Assume ([Hypothesis: l-adic approximation of Hecke eigenvalues with a change of weight at a place above l](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.WtLacEx/)).

Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\ell$ be a prime, let $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $a$ be an odd positive integer. Let $\mathcal U$ be the definite unitary group in $a$ variables over $E$. Let $T$ be a finite set of nonsplit finite places of $E$, and let $U$ be an automorphic representation of $\mathcal U$ that is unramified at every nonsplit finite place of $E$ outside $T$. Let $w_0$ and $v'$ be split places of $E$ above $\ell$ with $w_0^+\ne v'^+$.

Then there is a level family $K=(K_w)$ with the following four properties.

1. $U$ has level $K$ away from $w_0$ and $v'$.
2. For every split place $w$ of $E$ with $w^+\ne w_0^+$, the group $K_w$ is open and compact in $GL_a(E_w)$.
3. For every split place $w$ of $E$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$ at which $U$ has a Satake multiset, $K_w=GL_a(\mathcal O_w)$.
4. Let $Z$ and $W$ be finite sets of split places of $E$ such that $U$ has a Satake multiset at every place of $Z\cup W$, every $z\in Z\cup W$ satisfies $z^+\ne w_0^+$ and $z^+\ne v'^+$, and every place of $W$ lies above $\ell$. Then there are nonzero complex numbers $c_{w,n}$, for the finite places $w$ of $E$ and the integers $n$, such that the following two assertions hold for every system of Hecke operators for $K$, with index set $J$, and every system of eigenvalues $\theta=(\theta_j)_{j\in J}$ of $U$ for it.

    

   - (A) For an automorphic representation $U'$ of $\mathcal U$ and a system of eigenvalues $\theta'$ of $U'$ for the same system of Hecke operators, let $\Theta(U',\theta')$ be the family indexed by the disjoint union of $J$ and $W\times\mathbb Z$ with the entry $\theta'_j$ at $j\in J$ and the entry $\iota^{-1}\bigl(c_{w,n}\,s_n(U',w)\bigr)$ at $(w,n)\in W\times\mathbb Z$. Then $\Theta(U,\theta)$ is polynomially approximated by the set of the families $\Theta(U',\theta')$ in which $U'$ is unramified at every nonsplit finite place of $E$ outside $T$, has level $K$ away from $w_0$ and $v'$, is special at $(w_0,v')$, has the weights of $U$ away from $w_0$ and $v'$, and is in general position at every place of $Z\cup W$.
   - (B) If the system of Hecke operators is rational, there is a subfield $L$ of $\overline{\mathbb Q}_\ell$ of finite degree over $\mathbb Q_\ell$ that contains $\theta_j$ for every $j\in J$.

## Galois representations of automorphic representations of a definite unitary group of odd rank

[Theorem AGR.1.1776](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Lim.limFinOdd_of/)

Assume that the statements of ([Galois representations of special automorphic representations of a definite unitary group of odd rank](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne/)) and of ([l-adic approximation of the Hecke eigenvalues of an automorphic representation of a definite unitary group by those of special representations](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.congFinOdd_of_ex/)) hold without their assumptions, which are Hypothesis G for the first and ([Hypothesis: l-adic approximation of Hecke eigenvalues with a change of weight at a place above l](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.WtLacEx/)) for the second.

Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\bar E$ be an algebraic closure of $E$ and $G_E=\operatorname{Aut}(\bar E/E)$, let $\ell$ be a prime, let $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $a$ be an odd positive integer. Let $d$ be a positive integer such that $(E,\ell,d)$ satisfies the field conditions. Let $\mathcal U$ be the definite unitary group in $a$ variables over $E$. Let $T$ be a finite set of nonsplit finite places of $E$, and let $U$ be an automorphic representation of $\mathcal U$ that is unramified at every nonsplit finite place of $E$ outside $T$. Let $w_0$ and $v'$ be split places of $E$ above $\ell$ with $w_0^+\ne v'^+$.

Then there is a continuous semisimple representation $\rho\colon G_E\to GL_a(\overline{\mathbb Q}_\ell)$ with the following three properties.

1. For every place $w$ of $E$ that is eligible for $d$ and does not divide $\ell$, and every Satake multiset $B$ of $U$ at $w$, the representation $\rho$ is unramified at $w$ with Frobenius polynomial $P_{w,B}$.
2. For every place $w$ of $E$ above $\ell$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$ at which $U$ has a Satake multiset, $\rho$ is crystalline and de Rham at $w$ with the weights of $U$.
3. Let $w$ be a place of $E$ above $\ell$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$, let $B$ be a Satake multiset of $U$ at $w$, let $A$ be a place of $\bar E$ above $w$ with local data at $A$, and let $g\in W_A$. Then there are a set $\mathcal C$ of continuous representations $G_E\to GL_a(\overline{\mathbb Q}_\ell)$ and, for every embedding $\tau\colon E\to\overline{\mathbb Q}_\ell$, a multiset $J_\tau$ of integers, such that the following two assertions hold.

    

   - (a) For every $\rho'\in\mathcal C$, the representation $\rho'|_{D_A}$ is crystalline, and $J_\tau$ is a Hodge–Tate multiset of $\rho'|_{D_A}$ at $\tau$ for every embedding $\tau\colon E\to\overline{\mathbb Q}_\ell$ that extends to the field $K_w$ of the local data.
   - (b) For every integer $n\ge0$ and every real number $\varepsilon>0$ there are a finite subset $\mathcal C_0\subseteq\mathcal C$ and coefficients $c_{\rho'}\in\overline{\mathbb Q}_\ell$, $\rho'\in\mathcal C_0$, such that $$\Bigl|\operatorname{tr}\rho(h)-\sum_{\rho'\in\mathcal C_0}c_{\rho'}\operatorname{tr}\rho'(h)\Bigr|_\ell\le\varepsilon\qquad(h\in G_E)$$ and $$\Bigl|\iota^{-1}\Bigl(\sum_{z\in R_w(B)}z^{-m\deg g}\Bigr)-\sum_{\rho'\in\mathcal C_0}c_{\rho'}\,\iota^{-1}\bigl(p_m(\rho'|_{D_A};g)\bigr)\Bigr|_\ell\le\varepsilon\qquad(0\le m\le n).$$
