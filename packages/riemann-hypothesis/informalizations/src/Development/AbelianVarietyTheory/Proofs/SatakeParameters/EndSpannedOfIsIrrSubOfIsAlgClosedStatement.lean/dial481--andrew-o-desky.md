---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/EndSpannedOfIsIrrSubOfIsAlgClosedStatement.lean",
  "declarations": [
    "GlobalTheory.T.endSpanned_of_isIrrSub_of_isAlgClosed'"
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

## Irreducibility and the span of representation matrices

[Theorem ALG.0211](https://andrewodesky.com/rh/lean/_private.Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.LinkedUnramifiedChains.DerivativeDivisibility.IrrOpen.0.UpperTheory.V.J.isIrr_iff_span/)

Let $k$ be an algebraically closed field, $\Gamma$ a group, $n\ge1$, and $\rho:\Gamma\to\operatorname{GL}_n(k)$ a representation. Then $\rho$ is irreducible if and only if $$\operatorname{span}_k\{\rho(g):g\in\Gamma\}=M_n(k).$$

Let $a\ge0$ be an integer, let $\sigma:\Gamma\to\operatorname{GL}_a(k)$ be a representation, and let $U\subseteq k^a$ be a nonzero invariant subspace with no proper nonzero invariant subspace. Every $k$-linear map $\varphi:U\to U$ is the restriction to $U$ of a matrix $$X\in\operatorname{span}_k\{\sigma(g):g\in\Gamma\}\subseteq M_a(k).$$
