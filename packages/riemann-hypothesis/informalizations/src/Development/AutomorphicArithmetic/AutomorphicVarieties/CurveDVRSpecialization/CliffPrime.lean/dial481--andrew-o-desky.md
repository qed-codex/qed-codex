---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CurveDVRSpecialization/CliffPrime.lean",
  "declarations": [
    "UpperTheory.V.Pr.cliffPrime"
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

## Restriction of a prime-dimensional irreducible representation

[Theorem REP.0449](https://andrewodesky.com/rh/lean/UpperTheory.V.Pr.cliffPrime/)

Let $G$ be a group, $\kappa$ an algebraically closed field, $n$ a prime, and $r:G\to\operatorname{GL}_n(\kappa)$ irreducible. If $U\triangleleft G$, at least one of the following holds:

- $r|_U$ is irreducible.
- Every $r(u)$, $u\in U$, is scalar.
- There are a basis $b_1,\ldots,b_n$ of $\kappa^n$, distinct characters $\lambda_i:U\to\kappa^\times$, and a homomorphism $\pi:G\to S_n$ acting transitively on $\{1,\ldots,n\}$, such that $$r(u)b_i=\lambda_i(u)b_i\quad(u\in U),\qquad r(g)b_i\in\kappa b_{\pi(g)i}\quad(g\in G).$$
