---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/ExpBound.lean",
  "declarations": [
    "PositivityTheory.RgUd.expBound"
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

## Exponents in generic unitary parabolic induction

[Theorem REP.0066](https://andrewodesky.com/rh/lean/PositivityTheory.RgUd.expBound/)

Let $k$ be a nonarchimedean local field and let $\pi_1,\ldots,\pi_h$ be smooth irreducible complex representations of $\operatorname{GL}_{n_1}(k),\ldots,\operatorname{GL}_{n_h}(k)$, with $\sum_i n_i=N$. Suppose their normalized parabolic induction $\pi_1\times\cdots\times\pi_h$ is irreducible, unitarisable and generic.

For any $j$ with $n_j>0$, suppose $\pi_j$ has central character $\omega_j$ and, for a real number $s$, $$|\omega_j(z)|=|z|_k^{n_js}\qquad(z\in k^\times).$$ Then $|s|<\tfrac12$.
