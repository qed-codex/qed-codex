---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/TwJ.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Geo.twJ"
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

## Occurrence of filtration jumps after a character twist

[Theorem PHT.1703](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Geo.twJ/)

Let $E$ be a number field with algebraic closure $\Omega$, $\ell$ a prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and $d\ge0$. Let $\rho:G_E\to\operatorname{GL}_d(\overline{\mathbb Q}_\ell)$ and $\chi:G_E\to\overline{\mathbb Q}_\ell^\times$ be continuous. Fix a finite place $w$, $c\in\mathbb C$, and integers $m_\tau$ for embeddings $\tau:E\to\mathbb C$. Assume the following full rank-one comparison condition for $\chi$: for every compatible local period and coefficient comparison it is crystalline and de Rham with jump multiset $\{m_\tau\}$, and its Weil characteristic polynomial at $\gamma$ is $T-c^{-\deg\gamma}$; away from $\ell$ its Frobenius eigenvalue is $c$.

Let $Q(\tau,j)$ be any predicate on embeddings and integers. Suppose in every compatible local comparison at $w$, and every embedding induced by a finite local coefficient extension, there exists a filtration-jump multiset of $\rho$ containing every $j$ with $Q(\tau,j)$. Then the occurrence assertion just stated holds for $\rho\otimes\chi$ with predicate $$Q'(\tau,j)=Q(\tau,j-m_\tau).$$ Thus all the prescribed occurring jumps are shifted by $m_\tau$; the conclusion is an occurrence assertion, without an assertion that these are all the jumps.
