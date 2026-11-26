---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/OfSteps.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.NumbersDVR.GenericDimBound.full"
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

## A dimension bound for the generic fiber over a discrete valuation ring

[Theorem AG.0246](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.GenericDimBound.full/)

Let $O$ be a discrete valuation ring and $K=\operatorname{Frac}O$. Let $B$ be a finite set and $I_b$ finite coordinate sets. Put $$A=O[X_{b,i}:b\in B,\ i\in I_b],$$ with the grading that gives all variables in the $b$th block degree $e_b\in\mathbb N^B$. Let $P\subset A$ be a multihomogeneous prime ideal such that $P\cap O=0$ and, for every block $b$, some variable $X_{b,i}$ does not belong to $P$. Writing $P_K=PA_K$ in $A_K=K[X_{b,i}]$, one has $$\dim(A_K/P_K)+1\le\dim(A/P).$$
