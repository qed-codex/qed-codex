---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/MainFin.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne"
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
