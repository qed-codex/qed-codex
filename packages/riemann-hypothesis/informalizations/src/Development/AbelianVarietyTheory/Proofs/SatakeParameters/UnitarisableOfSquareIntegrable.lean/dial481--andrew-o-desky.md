---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/UnitarisableOfSquareIntegrable.lean",
  "declarations": [
    "GlobalTheory.SqIntUnit.main"
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

## Unitarisability from square-integrable coefficients

[Theorem REP.1728](https://andrewodesky.com/rh/lean/GlobalTheory.SqIntUnit.main/)

Let $k$ be a nonarchimedean local field, $N\ge0$, and $\pi$ a smooth irreducible representation of $G=\operatorname{GL}_N(k)$ on a complex vector space $V$. Suppose that for every $v\in V$, every linear functional $\lambda\in V^*$ whose stabilizer under right translation is open, and every Haar measure on $G/Z(G)$, the function $$g\longmapsto|\lambda(\pi(g)v)|$$ descends to $G/Z(G)$ and belongs to $L^2(G/Z(G))$. Then $\pi$ is unitarisable.
