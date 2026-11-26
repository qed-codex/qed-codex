---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/SphericalRepGLExistsSatakeParameters.lean",
  "declarations": [
    "GlobalTheory.SatakeExists.main"
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

## A spherical irreducible is a subquotient of an unramified principal series

[Theorem REP.1447](https://andrewodesky.com/rh/lean/GlobalTheory.SatakeExists.main/)

Assume the Bernstein–Zelevinsky finiteness package: for every nonarchimedean local field, smooth irreducibles are admissible, Jacquet modules and parabolic inductions of finite-length representations have finite length, and normalized induction commutes with smooth contragredients. Let $k$ be a nonarchimedean local field with its valuation and topology, let $n\ge0$, and let $\pi$ be a smooth irreducible complex representation of $\operatorname{GL}_n(k)$. If $\pi$ has a nonzero vector fixed by $\operatorname{GL}_n(\mathcal O_k)$, there exist $\alpha_1,\ldots,\alpha_n\in\mathbb C^\times$ such that $\pi$ is a subquotient of the normalized principal series induced from the unramified characters with uniformizer values $\alpha_1,\ldots,\alpha_n$.
