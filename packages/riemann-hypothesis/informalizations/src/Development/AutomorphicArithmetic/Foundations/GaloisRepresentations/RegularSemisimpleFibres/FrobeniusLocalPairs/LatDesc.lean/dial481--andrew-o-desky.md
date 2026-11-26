---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/FrobeniusLocalPairs/LatDesc.lean",
  "declarations": [
    "UpperTheory.Gal.InertialTypesAlt.L.latDesc"
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

## Descent of a Frobenius-stable lattice

[Theorem PHT.1314](https://andrewodesky.com/rh/lean/UpperTheory.Gal.InertialTypesAlt.L.latDesc/)

Let $K/k$ be a finite Galois extension of nonarchimedean local fields, with $\operatorname{char}k=0$ and compatible valuations. Let $F_1/F_0$ be finite fields with $$[F_1:F_0]=[K:k].$$ Suppose there are surjective ring maps $r_k:\mathcal O_k\to F_0$ and $r_K:\mathcal O_K\to F_1$, an automorphism $s\in\operatorname{Gal}(K/k)$, and $\bar s\in\operatorname{Gal}(F_1/F_0)$ such that $r_K$ extends $r_k$ and $$r_K(sx)=\bar s(r_K(x)),\qquad \bar s(z)=z^{|F_0|}.$$ Here the first identity is required whenever $x,sx\in\mathcal O_K$. For every $n\ge0$ and $g\in\mathrm{GL}_n(K)$ satisfying $$g^{-1}s(g)\in\mathrm{GL}_n(\mathcal O_K),$$ there are $h\in\mathrm{GL}_n(k)$ and $\kappa\in\mathrm{GL}_n(\mathcal O_K)$ with $g=h\kappa$.
