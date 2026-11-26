---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/TwCrys.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Geo.twCrys"
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

## Preservation of crystallinity under a prescribed character twist

[Theorem PHT.0427](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.twCrys/)

Let $E$ be a number field with algebraic closure $\Omega$, let $\ell$ be prime, let $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and let $d\ge0$. Let $\rho:G_E\to\operatorname{GL}_d(\overline{\mathbb Q}_\ell)$ and $\chi:G_E\to\overline{\mathbb Q}_\ell^\times$ be continuous. Fix a finite prime $w$ of $E$, $c\in\mathbb C$, and integers $m_\tau$ indexed by embeddings $\tau:E\hookrightarrow\mathbb C$. Assume the full rank-one comparison condition below for $\chi$ at $w$. If $\rho$ is crystalline in every compatible local comparison at $w$, so is $\rho\otimes\chi$.
