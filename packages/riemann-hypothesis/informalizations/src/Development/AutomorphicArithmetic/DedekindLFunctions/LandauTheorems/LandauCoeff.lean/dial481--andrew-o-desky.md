---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LandauCoeff.lean",
  "declarations": [
    "Deduction.landau_coeff"
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

## Derivatives of the Laplace transform

[Theorem ANT.0128](https://andrewodesky.com/rh/lean/Deduction.landau_coeff/)

Let $g:\mathbb R\to\mathbb R$ be measurable, with $|g(u)|\le C_0e^{2u}$ for $u\ge0$ and some real $C_0$. Let $Z\subset\{\Re s>0\}$ be such that every point of the open right half-plane has a punctured neighborhood disjoint from $Z$. Suppose $\Phi$ is holomorphic on $\{\Re s>0\}\setminus Z$, agrees with $\int_0^\infty g(u)e^{-su}\,du$ for $\Re s>2$, and at each $\rho\in Z$ has a simple pole with nonzero residue, positive real when $\rho$ is real. Then, for integers $k\ge0$ and $\Re s>2$, $$\frac{(-1)^k}{k!}\Phi^{(k)}(s)=\int_0^\infty g(u)\frac{u^k e^{-su}}{k!}\,du.$$
