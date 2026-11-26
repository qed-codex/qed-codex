---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TraceLimits/LimFinOddOf.lean",
  "declarations": [
    "UpperTheory.Gal.Lim.limFinOdd_of"
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
