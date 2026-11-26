---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/ZetaEulerProducts/ZetaOrd.lean",
  "declarations": [
    "PositivityTheory.Lord.zeta_zo_nonpos"
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

## Orders of a Dedekind zeta function at nonpositive integers

[Theorem ANT.0592](https://andrewodesky.com/rh/lean/PositivityTheory.Lord.zeta_zo_nonpos/)

Let $K$ be a number field with $r_1$ real places and $r_2$ complex places. For every integer $j\le0$, put $$m=r_1\mathbf1_{2\mid j}+r_2-\mathbf1_{j=0}.$$ There is a function $u$, holomorphic near $j$ and nonzero at $j$, such that the continued Dedekind zeta function satisfies $$\zeta_K(s)=(s-j)^m u(s)$$ in a punctured neighborhood of $j$.
