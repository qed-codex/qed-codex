---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SphericalEmbeddings/PseSat.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.N3.PseSat.satPerm"
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

## Uniqueness of spherical inducing parameters

[Theorem REP.1145](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.N3.PseSat.satPerm/)

Let $k$ be a nonarchimedean local field, $n\ge0$, and let $\pi$ be a smooth irreducible spherical complex representation of $\operatorname{GL}_n(k)$. For $\xi=(\xi_1,\ldots,\xi_n)\in(\mathbb C^\times)^n$, write $I(\xi)$ for normalized induction from the standard Borel of the unramified characters whose values on a uniformizer are $\xi_i$. If $\pi$ is a subquotient of $I(\xi)$ and there is a nonzero intertwiner $\pi\to I(\eta)$, then $$\eta=\xi\circ\sigma\qquad\text{for some }\sigma\in S_n.$$
