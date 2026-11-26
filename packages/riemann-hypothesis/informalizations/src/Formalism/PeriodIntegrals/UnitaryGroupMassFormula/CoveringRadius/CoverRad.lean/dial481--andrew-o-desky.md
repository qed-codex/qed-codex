---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CoveringRadius/CoverRad.lean",
  "declarations": [
    "PI.Tr2.coverDiv"
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

## A covering radius bound from the dual lattice

[Theorem ALG.1208](https://andrewodesky.com/rh/lean/PI.Tr2.coverDiv/)

Let $V$ be a finite-dimensional real inner product space, and let $M\subset V$ be a discrete additive subgroup whose real span is $V$. Put $$M^*=\{y\in V:\langle x,y\rangle\in\mathbb Z\text{ for every }x\in M\}.$$ If $\kappa>0$ and $\|y\|\ge\kappa$ for every nonzero $y\in M^*$, then for every $x\in V$ there exists $z\in M$ such that $$\|x-z\|\le\frac{\dim_{\mathbb R}V}{2\kappa}.$$
