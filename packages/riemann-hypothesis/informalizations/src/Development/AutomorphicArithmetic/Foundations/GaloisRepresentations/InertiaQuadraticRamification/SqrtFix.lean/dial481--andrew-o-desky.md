---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/InertiaQuadraticRamification/SqrtFix.lean",
  "declarations": [
    "UpperTheory.Gal.UnramifiedFromSplittingCriterion.sqrtFix"
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

## Local Galois fixing criteria for a square root of an integer

[Theorem ANT.0575](https://andrewodesky.com/rh/lean/UpperTheory.Gal.UnramifiedFromSplittingCriterion.sqrtFix/)

Let $F$ be a number field, let $\Omega/F$ be a field extension, and let $A\subseteq\Omega$ be a valuation ring. Write $v_A$ for its multiplicative valuation and $D_A,I_A\subseteq\operatorname{Aut}_F(\Omega)$ for its decomposition and inertia groups. Let $x\in\Omega$ and $a\in\mathbb Z$ satisfy $x^2=a$.

1. For every rational prime $t$ with $v_A(t)<1$ and $8t\mid a-1$, every element of $D_A$ fixes $x$.
2. If $v_A(2a)=1$, every element of $I_A$ fixes $x$.
