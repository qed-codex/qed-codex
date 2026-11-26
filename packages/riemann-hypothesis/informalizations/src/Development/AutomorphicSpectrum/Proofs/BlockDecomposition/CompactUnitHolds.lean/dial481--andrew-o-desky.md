---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CompactUnitHolds.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.CompUnitary.isUnitarisable_of_embedding"
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

## Unitarisability from functions on a compact quotient

[Theorem REP.1305](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.CompUnitary.isUnitarisable_of_embedding/)

Let $G$ be a locally compact, second-countable Hausdorff topological group, with its Borel measurable structure, and let $\Gamma\subset G$ be a discrete subgroup. Assume there is a compact set $C\subset G$ such that for each $g\in G$ some $\gamma\in\Gamma$ satisfies $\gamma g\in C$.

Let $L,H$ be groups, $p:L\to H$ a surjective homomorphism, $\iota:L\to G$ a homomorphism, and $\rho$ a representation of $H$ on a complex vector space $V$. Suppose there is an injective complex-linear map $f:V\to\mathbb C^G$ such that each $f(v)$ is continuous and left $\Gamma$-invariant, and $$f(\rho(p(x))v)(y)=f(v)(y\iota(x))\qquad(x\in L,\ v\in V,\ y\in G).$$ Then $V$ admits a positive-definite Hermitian form invariant under $\rho(H)$.
