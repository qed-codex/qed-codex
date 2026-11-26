---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/MetricProofs/TailBoundStatementHolds.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Giv.tailBound_holds"
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

## Monge–Ampere mass near a normal-crossing divisor

[Theorem AG.1396](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Giv.tailBound_holds/)

Let $X$ be compact Hausdorff with its Borel structure and a finite holomorphic atlas of complex dimension $e$. Let $\Theta_1,\ldots,\Theta_e$ be smooth strictly positive local potential data. Let $L$ be a smooth local potential datum and $s$ a holomorphic section whose zero divisor $D$ has a simple normal-crossing presentation with finitely many components and nonnegative integer multiplicities, as specified in the conventions. Assume $\log\|s(y)\|\le0$, and put $$\rho(y)=\exp(1)-2\log\|s(y)\|\qquad(y\notin D).$$ There is $C\in\mathbb R$ such that for every $C_1\ge0$ and every collection of smooth real functions $u_i$ with $\Theta_i+u_i$ plurisubharmonic and $$-C_1\log\rho\le u_i\le0\quad\text{on }X\setminus D,$$ the mixed Monge–Ampere measure $\nu$ of $\Theta_i+u_i$ satisfies, for $R\ge\exp(1)$, $$\nu\bigl(D\cup\{y\notin D:\rho(y)\ge R\}\bigr)\le\max\!\left(0,C(C_1+3)\frac{\log R}{R}\right),$$ $$\int_{\{y\notin D:\rho(y)\ge R\}}\log\rho\,d\nu\le\max\!\left(0,C(C_1+3)\frac{(\log R)^2}{R}\right).$$
