---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/PolynomialDerivatives/SupPerp.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.LC.semiFam"
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

## Common kernels and images for a family closed under adjoints

[Theorem ALG.0478](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.LC.semiFam/)

Let $V$ be a finite-dimensional complex vector space with a positive-definite Hermitian form $\phi$, linear in the second argument. Let $I$ be any index set and let $T_i\in\operatorname{End}_{\mathbb C}(V)$. Suppose that for each $i$ there is $j$ such that $$\phi(T_iv,w)=\phi(v,T_jw)\qquad(v,w\in V).$$ Put $K=\bigcap_{i\in I}\ker T_i$ and $W=\sum_{i\in I}\operatorname{im}T_i$. Every $v\in V$ has a decomposition $v=v_0+w$ with $v_0\in K$, $w\in W$, and $K\cap W=\{0\}$.
