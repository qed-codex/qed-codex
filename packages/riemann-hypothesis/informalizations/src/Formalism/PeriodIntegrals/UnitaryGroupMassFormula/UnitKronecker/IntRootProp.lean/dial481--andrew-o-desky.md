---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitKronecker/IntRootProp.lean",
  "declarations": [
    "PI.UnitKronW.stepB"
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

## Unit-circle roots of integral polynomials are roots of unity

[Theorem ANT.0586](https://andrewodesky.com/rh/lean/PI.UnitKronW.stepB/)

Let $E$ be a number field and let $p\in E[T]$ be monic with every coefficient integral over $\mathbb Z$. Suppose that for every embedding $\phi:E\hookrightarrow\mathbb C$, every root of $\phi(p)$ has absolute value one. Then every root $\mu$ of every $\phi(p)$ is a root of unity: some integer $m>0$ satisfies $\mu^m=1$.
