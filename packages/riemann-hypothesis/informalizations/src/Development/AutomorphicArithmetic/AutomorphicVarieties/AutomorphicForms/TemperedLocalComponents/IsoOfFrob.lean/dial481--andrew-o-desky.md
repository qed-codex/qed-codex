---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/TemperedLocalComponents/IsoOfFrob.lean",
  "declarations": [
    "UpperTheory.V.Af.isoOfFrob"
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

## Semisimple Galois representations determined by Frobenius

[Theorem AGR.1253](https://andrewodesky.com/rh/s/u4-frobenius-determines-semisimple.html)

Assume the source's full second automorphic-input package. Let $F$ be a number field, $\Omega$ an algebraic closure of $F$, $\ell$ prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism, and $n\ge0$. Let $r,r':\operatorname{Gal}(\Omega/F)\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ be continuous semisimple representations. Suppose that outside finitely many finite primes $w$, both representations are unramified and, for every choice of a place of $\Omega$ above $w$ and Frobenius lift $\sigma$, their inverse-Frobenius characteristic polynomials, transported by $\iota$, equal one common polynomial $\prod_{b\in B_w}(T-b)$ for a multiset $B_w$ of complex numbers. Then $r\simeq r'$.
