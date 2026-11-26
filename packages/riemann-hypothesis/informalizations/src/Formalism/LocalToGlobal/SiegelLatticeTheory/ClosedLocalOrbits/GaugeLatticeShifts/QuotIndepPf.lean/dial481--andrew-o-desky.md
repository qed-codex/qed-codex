---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/QuotIndepPf.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.QuotIndep.quotIndep"
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

## Independence of integrals on a homogeneous quotient

[Theorem ALG.1296](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.QuotIndep.quotIndep/)

Let $G$ be a second-countable locally compact Hausdorff topological group, with its Borel measurable structure, and let $S\subseteq G$ be a closed subgroup. Let $\mu_S$ be a measure on $S$ invariant under left and right multiplication, finite on compact sets, positive on nonempty open sets, and $s$-finite, meaning a countable sum of finite measures. Let $\mu,\nu_1,\nu_2$ be measures on $G$ such that for every measurable $h:G\to[0,\infty]$, $$\int_G h(x)\,d\mu(x)=\int_G\int_S h(sx)\,d\mu_S(s)\,d\nu_j(x)\qquad(j=1,2).$$ For every measurable $f:G\to[0,\infty]$ invariant under left multiplication by $S$, $$\int_G f\,d\nu_1=\int_G f\,d\nu_2.$$ These are nonnegative extended integrals.
