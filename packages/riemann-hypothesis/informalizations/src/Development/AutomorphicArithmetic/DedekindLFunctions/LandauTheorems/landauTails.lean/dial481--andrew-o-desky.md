---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauTails.lean",
  "declarations": [
    "Deduction.landau_tails"
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

## Concentration of the high-derivative Laplace kernel

[Theorem ANT.0142](https://andrewodesky.com/rh/lean/Deduction.landau_tails/)

For every real $\delta>0$, there exist real numbers $\sigma>2$ and $A$ such that for every real $U\ge1$ there is an integer $k\ge0$, with $k\ge U$, satisfying $$\int_{(0,\infty)\setminus[U,(1+\delta)U]}\frac{u^ke^{(2-\sigma)u}}{k!}\,du\le\frac{A}{\sigma^k}.$$
