---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/SoCobLim.lean",
  "declarations": [
    "UpperTheory.V.X.So.cobLim"
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

## Bounded finite-level cohomology kills an integral cocycle

[Theorem GC.0502](https://andrewodesky.com/rh/lean/UpperTheory.V.X.So.cobLim/)

Let $O$ be a discrete valuation ring of characteristic zero, $\Gamma$ a group equipped with a topology, and $\theta:\Gamma\to O^\times$ a nontrivial homomorphism. Let $0\ne p\in\mathfrak m_O$ and $B\in\mathbb N$. Assume that for every $r\ge0$, $$H^1_{\mathrm{cont}}(\Gamma,(O/(p^r))(\theta))$$ is finite of cardinality at most $B$. If $z:\Gamma\to O$ satisfies $$z(gh)=z(g)+\theta(g)z(h)$$ and each reduction $z\bmod\mathfrak m_O^j$ is locally constant, then there exist $a,m\in O$, $a\ne0$, such that $$a\,z(g)=\theta(g)m-m\qquad(g\in\Gamma).$$
