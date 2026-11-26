---
{
  "module": "src/CompanionTheory/HarishChandraModules/KFiniteAnalyticVectors/FundamentalDomainCusps/FiniteDimensionalFromLinearForms.lean",
  "declarations": [
    "CompanionTheory.D.gk.RF.compact_integral_quotient_bound",
    "CompanionTheory.D.gk.RF.young_convolution_inequality"
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

## A convolution inequality on a group quotient

[Theorem REP.1354](https://andrewodesky.com/rh/lean/CompanionTheory.D.gk.RF.young_convolution_inequality/)

Let $G$ be a locally compact, second-countable Hausdorff topological group with its Borel measurable structure, and let $\mu$ be a Haar measure which is also right invariant. Let $\Gamma\subseteq G$ be a countable subgroup and let $D\subseteq G$ be a fundamental domain for its left action, in the measure-theoretic sense. Let $f,\theta:G\to[0,\infty]$, with $f$ measurable and $\theta$ almost everywhere measurable for $\mu$, and assume $f(\gamma x)=f(x)$ for $\gamma\in\Gamma$. Then $$\int_D\left(\int_G\theta(y)f(xy)\,d\mu(y)\right)^2d\mu(x) \le\left(\int_G\theta(y)\,d\mu(y)\right)^2\int_D f(x)^2\,d\mu(x).$$ All integrals and products are interpreted in the extended nonnegative reals.

## A compact-set integral bound from a quotient L2 norm

[Theorem REP.1383](https://andrewodesky.com/rh/lean/CompanionTheory.D.gk.RF.compact_integral_quotient_bound/)

Let $G$ be a locally compact, second countable Hausdorff topological group with its Borel measurable structure and a left Haar measure $\mu$. Let $\Gamma\subset G$ be a countable subgroup such that $C\cap\Gamma$ is finite for every compact subset $C\subset G$. Let $D$ be a measurable fundamental domain for the left action of $\Gamma$.

For every compact $B\subset G$ there is a finite constant $M\in[0,\infty)$ such that every measurable left-$\Gamma$-invariant function $f:G\to[0,\infty]$ satisfies $$\left(\int_B f\,d\mu\right)^2\le M\int_D f^2\,d\mu.$$ The integrals and inequality are understood in the extended nonnegative reals.
