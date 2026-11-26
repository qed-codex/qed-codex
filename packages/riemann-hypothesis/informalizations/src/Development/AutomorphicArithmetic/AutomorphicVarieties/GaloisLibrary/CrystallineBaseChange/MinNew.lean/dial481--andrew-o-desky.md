---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/CrystallineBaseChange/MinNew.lean",
  "declarations": [
    "UpperTheory.V.Br.minNew"
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

## Realizing almost all eigenvalues by a newform

[Theorem ANT.0372](https://andrewodesky.com/rh/lean/UpperTheory.V.Br.minNew/)

Let $N\ge1$, $k\ge1$, and let $\chi$ be a complex Dirichlet character modulo $N$. Let $g$ be a normalized weight-$k$ cusp form for $\Gamma_1(N)$ of character $\chi$ satisfying the Hecke eigenvalue relation at every prime. There exist a level $M\ge1$, a character $\chi'$ modulo $M$, and a normalized newform $f$ of weight $k$ and character $\chi'$ such that $f$ satisfies the eigenvalue relation at every prime and $$a_f(p)=a_g(p)\qquad\text{for all but finitely many primes }p.$$
