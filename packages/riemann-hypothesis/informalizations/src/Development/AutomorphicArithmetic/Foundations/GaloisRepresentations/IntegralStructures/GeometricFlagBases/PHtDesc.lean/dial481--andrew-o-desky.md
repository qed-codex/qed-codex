---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PHtDesc.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Geo.htDesc_of"
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

## Etale classes descend through finite field extensions

[Theorem AG.1133](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.htDesc_of/)

Let $q\ge0$ be an integer and let $\Omega/k$ be an algebraic extension of fields. Let $X\to\operatorname{Spec}k$ be quasi-compact and quasi-separated. For all integers $n,i$, every class $$y\in H_q^n(X_\Omega,i)$$ is pulled back from $H_q^n(X_L,i)$ for some intermediate field $k\subseteq L\subseteq\Omega$ finite over $k$. Here $X_L=X\times_kL$ and $H_q^n(-,i)$ denotes the source's etale cohomology with its $q$-twist coefficient sheaf; no invertibility or positivity condition on $q$ is imposed in this statement.
