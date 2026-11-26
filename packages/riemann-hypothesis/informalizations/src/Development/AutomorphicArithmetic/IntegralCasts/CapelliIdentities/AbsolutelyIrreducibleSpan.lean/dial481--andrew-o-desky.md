---
{
  "module": "src/Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities/AbsolutelyIrreducibleSpan.lean",
  "declarations": [
    "UpperTheory.Reformulated.B.AbsolutelyIrreducibleSpan.ontoSpan"
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

## Full matrix span from an irreducible residual action

[Theorem ALG.0852](https://andrewodesky.com/rh/lean/UpperTheory.Reformulated.B.AbsolutelyIrreducibleSpan.ontoSpan/)

Let $(\mathcal O,\mathfrak m)$ be a commutative local ring with residue field $k$, let $I$ be a finite set, and let $G$ be a monoid. Suppose $\rho:G\to M_I(\mathcal O)$ is a unital monoid homomorphism. Write $\bar\rho:G\to M_I(k)$ for its reduction. Assume:

1. Every $k$-subspace of $k^I$ stable under all $\bar\rho(g)$ is either $0$ or $k^I$.
2. Every matrix commuting with all $\bar\rho(g)$ is a scalar matrix.

Then $$\operatorname{span}_{\mathcal O}\{\rho(g):g\in G\}=M_I(\mathcal O).$$
