---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/ExistsTracePowNe.lean",
  "declarations": [
    "UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.finTw"
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

## Nonzero power traces for two exchanged commuting families

[Theorem REP.0413](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.finTw/)

Let $W\ne0$ be a finite-dimensional complex vector space, $X$ any set, and $T_0,T_1:X\to\operatorname{End}_{\mathbb C}(W)$. Suppose $T_0(x)$ commutes with $T_1(y)$ for every $x,y$, and the only subspaces invariant under both families are $0,W$. Let $U$ be a linear automorphism satisfying $$UT_{i+1}(x)=T_i(x)U\qquad(i\in\mathbb Z/2\mathbb Z,\ x\in X).$$ For each $i,x$ such that $T_i(x)$ is injective, there are arbitrarily large integers $j\ge0$ with $$\operatorname{tr}(T_i(x)^jU)\ne0.$$
