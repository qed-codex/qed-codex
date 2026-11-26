---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRatInPadicIntegersOfTwistedDifferenceStatement.lean",
  "declarations": [
    "GlobalTheory.T.isRatInPadicIntegers_of_twisted_difference"
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

## Integral twisted differences force integrality

[Theorem PHT.0306](https://andrewodesky.com/rh/lean/GlobalTheory.T.isRatInPadicIntegers_of_twisted_difference/)

Let $G$ be a finite abelian group, $\ell$ a prime, $g\in G$, and $q\ge0$ an integer divisible by $\ell$. For $x:G\to\mathbb Q$, suppose $$x(C)-q\,x(Cg)\in\mathbb Z_\ell\qquad(C\in G).$$ Then $x(C)\in\mathbb Z_\ell$ for every $C\in G$, where rational numbers are viewed inside $\mathbb Q_\ell$.
