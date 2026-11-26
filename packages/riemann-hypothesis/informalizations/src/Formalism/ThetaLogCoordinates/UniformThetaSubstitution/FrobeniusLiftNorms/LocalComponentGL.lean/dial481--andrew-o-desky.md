---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/LocalComponentGL.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.DworkIntegrality.int_of_frob"
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

## Coefficient integrality from a multiplicative Frobenius relation

[Theorem PHT.0815](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.DworkIntegrality.int_of_frob/)

Let $K$ be an ultrametric normed field, $p$ prime with $|p|=p^{-1}$, and $\sigma:K\to K$ a ring homomorphism satisfying $$|\sigma(a)-a^p|\le p^{-1}\qquad(|a|\le1).$$ Let $I$ be a finite set, and let $F,G\in K[[X_i:i\in I]]$ have constant coefficient one. Assume every coefficient of $G-1$ has absolute value at most $p^{-1}$ and $$F^\sigma(X_i^p:i\in I)=F(X)^pG(X),$$ where $F^\sigma$ is obtained by applying $\sigma$ to every coefficient. Then every coefficient of $F$ has absolute value at most one.
