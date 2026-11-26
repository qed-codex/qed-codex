---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/ASWitt.lean",
  "declarations": [
    "witt_lift"
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

## Lifting Artin–Schreier surjectivity to Witt vectors

[Theorem PHT.0752](https://andrewodesky.com/rh/lean/witt_lift/)

Let $p$ be prime and let $k$ be a commutative ring of characteristic $p$. Suppose the Artin–Schreier map $y\mapsto y^p-y$ is surjective on $k$. Then for every $x\in W_p(k)$ there exists $y\in W_p(k)$ such that $$W_p(\operatorname{Frob}_p)(y)-y=x.$$
