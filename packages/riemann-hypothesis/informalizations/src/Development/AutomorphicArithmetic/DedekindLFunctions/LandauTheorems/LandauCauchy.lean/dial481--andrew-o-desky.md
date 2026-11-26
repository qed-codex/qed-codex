---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LandauCauchy.lean",
  "declarations": [
    "Deduction.landau_cauchy"
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

## Cauchy bound for normalized derivatives

[Theorem ANT.0140](https://andrewodesky.com/rh/lean/Deduction.landau_cauchy/)

Let $z\in\mathbb C$ and $r,r'\in\mathbb R$ with $0<r'<r$. If $\Phi:\mathbb C\to\mathbb C$ is holomorphic on the open disk $B(z,r)$ of radius $r$ about $z$, there exists $M\in\mathbb R$ such that, for every integer $k\ge0$, $$\left|\frac{\Phi^{(k)}(z)}{k!}\right|\le\frac{M}{(r')^k}.$$
