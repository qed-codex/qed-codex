---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatFamilyZetaConvergenceHolomorphyStatement.lean",
  "declarations": [
    "GlobalTheory.T.flatFamilyZeta_convergence_holomorphy"
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

## Holomorphy of a dominated Mellin integral

[Theorem ANT.0512](https://andrewodesky.com/rh/lean/GlobalTheory.T.flatFamilyZeta_convergence_holomorphy/)

Let $(X,\mu)$ be a measure space, $f:X\to\mathbb C$, and $a:X\to(0,1]$ measurable. Fix $s_0,s_1\in\mathbb C$ and suppose $x\mapsto f(x)a(x)^{s_1-s_0}$ is integrable. Then $$Z(s)=\int_X f(x)a(x)^{s-s_0}\,d\mu(x)$$ is holomorphic on $\Re s>\Re s_1$ and continuous on $\Re s\ge\Re s_1$. For each $s$ in the closed half-plane the integrand is integrable, and there are a relative neighborhood $U$ of $s$ and an integrable real function $g$ such that $$|f(x)a(x)^{s'-s_0}|\le g(x)\qquad(s'\in U,\ x\in X).$$
