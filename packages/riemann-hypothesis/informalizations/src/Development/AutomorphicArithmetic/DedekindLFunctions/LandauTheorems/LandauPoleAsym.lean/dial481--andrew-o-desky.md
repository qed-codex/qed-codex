---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LandauPoleAsym.lean",
  "declarations": [
    "Deduction.landau_pole_asym"
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

## High derivatives near an isolated pole

[Theorem ANT.0122](https://andrewodesky.com/rh/lean/Deduction.landau_pole_asym/)

Let $z,\rho,c\in\mathbb C$ and $r>0$, and write $B(z,r)$ for the open disk of radius $r$ about $z$. Assume $\rho\ne z$, $|\rho-z|<r$, and suppose $\Phi$ is holomorphic on $B(z,r)\setminus\{\rho\}$. Suppose $\Phi(s)=c/(s-\rho)+h(s)$ on a punctured neighborhood of $\rho$, with $h$ holomorphic there and at $\rho$. For every $0<r'<r$ there is a real $M$ such that, for all integers $k\ge0$, $$\left|\frac{(-1)^k\Phi^{(k)}(z)}{k!}-\frac{c}{(z-\rho)^{k+1}}\right|\le\frac{M}{(r')^k}.$$
