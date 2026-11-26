---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/LintegralIndicatorNeTop.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.CV.pf_QInt"
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

## A uniform bound for compactly supported quotient integrals

[Theorem ALG.0193](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.CV.pf_QInt/)

Let $G$ be a second-countable locally compact Hausdorff topological group with its Borel measurable structure and left Haar measure $\mu$. Let $T\subseteq G$ be a closed subgroup with a left Haar measure $\nu$ also invariant under inversion. For every compact $C\subseteq G$ there is $A\ge0$ such that the following holds.

If $B\ge0$ and $F:G\to\mathbb C$ is measurable, left $T$-invariant, vanishes outside $TC$, and satisfies $|F(x)|\le B$ for $x\in C$, then $$\int_{T\backslash G}|F|\,d(\mu/\nu)<\infty,\qquad \left|\int_{T\backslash G}F\,d(\mu/\nu)\right|\le AB.$$
