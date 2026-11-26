---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/CompactLocalSets/Overlap.lean",
  "declarations": [
    "PositivityTheory.KB.LocalOverlapAverage.overlapG_holds"
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

## A compact-set integral bound for an invariant function

[Theorem REP.0464](https://andrewodesky.com/rh/lean/PositivityTheory.KB.LocalOverlapAverage.overlapG_holds/)

Let $G$ be a Hausdorff topological group with its Borel measurable structure, let $\Gamma\subseteq G$ be a countable subgroup, and let $\mu$ be a left-invariant measure. Let $D$ be a fundamental domain for left translation by $\Gamma$. Assume $\Gamma\cap K$ is finite for every compact $K\subseteq G$.

For every compact $K\subseteq G$ there is $M\in\mathbb N$ such that every measurable $f:G\to[0,\infty]$ satisfying $f(\gamma x)=f(x)$ for $\gamma\in\Gamma$ obeys $$\int_K f\,d\mu\le M\int_D f\,d\mu.$$ The integrals are extended nonnegative integrals.
