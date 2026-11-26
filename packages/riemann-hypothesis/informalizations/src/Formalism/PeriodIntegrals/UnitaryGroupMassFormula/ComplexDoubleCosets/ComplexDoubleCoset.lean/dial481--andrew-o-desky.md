---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ComplexDoubleCosets/ComplexDoubleCoset.lean",
  "declarations": [
    "PI.PoincareSeriesInner.W.complex_double_coset"
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

## A double-coset formula for products of Poincare series

[Theorem ALG.0342](https://andrewodesky.com/rh/lean/PI.PoincareSeriesInner.W.complex_double_coset/)

Let $G$ be a measurable group with measurable multiplication and a left-invariant measure $\mu$. Let $\Gamma\le G$ be countable and $S,S'\le\Gamma$. Choose representatives $D,D'\subseteq\Gamma$ for $S\backslash\Gamma,S'\backslash\Gamma$, and $R\subseteq\Gamma$ for $S\backslash\Gamma/S'$. Let $F_\Gamma$ be a measure-theoretic fundamental domain for the left action of $\Gamma$ on $G$, and, for each $r\in R$, let $F_r$ be a measure-theoretic fundamental domain for $S\cap rS'r^{-1}$.

Let $\phi,\psi:G\to\mathbb C$ be measurable, left $S$-invariant and left $S'$-invariant respectively. Assume both sums $\sum_{\delta\in D}|\phi(\delta x)|$ and $\sum_{\delta'\in D'}|\psi(\delta'x)|$ are finite for every $x$, and $$\int_{F_\Gamma}\left(\sum_{\delta\in D}|\phi(\delta x)|\right)\left(\sum_{\delta'\in D'}|\psi(\delta'x)|\right)\,d\mu(x)<\infty.$$ Put $P_D\phi(x)=\sum_{\delta\in D}\phi(\delta x)$, and define $P_{D'}\psi$ similarly. Their product is integrable on $F_\Gamma$, and $$\int_{F_\Gamma}P_D\phi(x)P_{D'}\psi(x)\,d\mu(x)=\sum_{r\in R}\int_{F_r}\phi(x)\psi(r^{-1}x)\,d\mu(x).$$
