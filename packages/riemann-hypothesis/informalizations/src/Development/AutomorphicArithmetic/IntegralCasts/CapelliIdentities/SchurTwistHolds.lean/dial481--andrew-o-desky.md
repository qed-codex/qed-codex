---
{
  "module": "src/Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities/SchurTwistHolds.lean",
  "declarations": [
    "UpperTheory.Reformulated.B.H13.schur_twist_holds"
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

## An irreducible restriction excludes a trivial-on-restriction self twist

[Theorem REP.0385](https://andrewodesky.com/rh/lean/UpperTheory.Reformulated.B.H13.schur_twist_holds/)

Let $k$ be an algebraically closed field, $\Gamma,\Gamma'$ groups, $\varphi:\Gamma'\to\Gamma$ a homomorphism, and $r:\Gamma\to\mathrm{GL}_n(k)$ a representation. Let $\delta:\Gamma\to k^\times$ be a character. Assume $r\circ\varphi$ is irreducible, $\delta\circ\varphi=1$, and $r$ is isomorphic to its twist $g\mapsto\delta(g)r(g)$. Then $\delta=1$.
