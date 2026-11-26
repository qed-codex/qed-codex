---
{
  "module": "src/Development/DiscreteGroups/GlobalIrreducibility/LConvDens.lean",
  "declarations": [
    "DiscreteGroups.sglob.LConv.finiteOfAlt"
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

## Finite rank from alternating operator identities

[Theorem REP.1646](https://andrewodesky.com/rh/lean/DiscreteGroups.sglob.LConv.finiteOfAlt/)

Let $G$ be a group, $H$ a complex Hilbert space, and $\pi:G\to\operatorname{End}_{\mathrm{cont},\mathbb C}(H)$ a representation by isometries. Assume every bounded operator commuting with every $\pi(g)$ is a scalar multiple of the identity. Let $e$ be a bounded operator with $e^2=e$. If there exists $d\ge0$ such that, for every $g_1,\ldots,g_d\in G$, $$\sum_{\sigma\in S_d}\operatorname{sgn}(\sigma) (e\pi(g_{\sigma(1)})e)\cdots(e\pi(g_{\sigma(d)})e)=0,$$ then $e(H)$ is contained in the span of finitely many vectors of $H$.
