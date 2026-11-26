---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/EigenvalueSeparation/StableEigenspaces/FiniteTypes/FintypeHolds.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.E.E3.fintype_holds"
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

## Finite-dimensional automorphic forms with fixed local data

[Theorem AGR.1276](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.E.E3.fintype_holds/)

Let $E$ be a CM number field, $N\ge0$, $G=\mathrm{GL}_N(\mathbb A_E)$, $K$ an open subgroup of $\mathrm{GL}_N(\mathbb A_{E,f})$, and $K_\infty$ the product of the archimedean unitary maximal compact groups. Let $W\subseteq\{K_\infty\to\mathbb C\}$ be a finite-dimensional complex subspace. Let $S$ be a set of smooth automorphic forms on $G$ such that $$\varphi(xu)=\varphi(x)\quad(u\in K),\qquad [k\mapsto\varphi(xk)]\in W\quad(x\in G,\ \varphi\in S).$$ For each complex embedding $\tau:E\hookrightarrow\mathbb C$, fix a multiset $m_\tau$ of complex numbers, and suppose that $\operatorname{span}_{\mathbb C}S$ has infinitesimal character $m_\tau$ at $\tau$. Then $$\dim_{\mathbb C}\operatorname{span}_{\mathbb C}S<\infty.$$ The hypothesis on $K$ is openness; compactness of $K$ is not separately assumed.
