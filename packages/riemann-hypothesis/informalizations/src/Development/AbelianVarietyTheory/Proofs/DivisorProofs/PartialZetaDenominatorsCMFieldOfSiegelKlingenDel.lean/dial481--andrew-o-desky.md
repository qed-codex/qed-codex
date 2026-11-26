---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/PartialZetaDenominatorsCMFieldOfSiegelKlingenDel.lean",
  "declarations": [
    "GlobalTheory.ZetaDenom.inZl_mul_zeta"
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

## An integral multiple of a partial zeta value

[Theorem ANT.1186](https://andrewodesky.com/rh/lean/GlobalTheory.ZetaDenom.inZl_mul_zeta/)

Assume the following ray-class integrality theorem for totally real fields: for a prime $\ell$, $n\ge1$, and a rational ray-class function $\epsilon$ of modulus $(\ell^n)$ integral in $\mathbb Z_\ell$ on ideals prime to $\ell$, the special values satisfy $$L(1-k,\epsilon)-N\mathfrak c^{\,k}L(1-k,\epsilon(\mathfrak c\,\cdot))\in\mathbb Z_\ell$$ for every $k\ge1$ and integral ideal $\mathfrak c$ prime to $\ell$, whenever the two displayed values are rational. Let $F$ be totally real, $\ell$ prime, $a,k\ge2$ integers with $\gcd(a,\ell)=1$, and $z:\operatorname{Cl}(\mathcal O_F)\to\mathbb Q$. Suppose $z(C)=\zeta_C(1-k)$, where $\zeta_C$ is holomorphic off $1$ and equals $\sum_{[\mathfrak a]=C}(N\mathfrak a)^{-s}$ for $\operatorname{Re}s>1$, summing over nonzero integral ideals. Then, for every ideal class $C$, $$\bigl(a^{[F:\mathbb Q]k}-1\bigr)z(C)\in\mathbb Z_\ell.$$
