---
{
  "module": "src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/BernsteinNarrowness/BernsteinClosure/RamifiedMultiplicityOne.lean",
  "declarations": [
    "PositivityTheory.BernsteinRamification.Close.ramifiedMultiplicityOne"
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

## Uniqueness of a ramified local restriction map

[Theorem REP.1694](https://andrewodesky.com/rh/lean/PositivityTheory.BernsteinRamification.Close.ramifiedMultiplicityOne/)

Let $E/F$ be number fields with an $F$-automorphism $\sigma$ and a base datum. Fix two geometric theta data $G,G_1$ of sizes $(a,a')$ and $(a_1,a'_1)$, a common character datum with splitting characters $\alpha,\beta$ and exceptional finite set $T$, their Weil actions, and their archimedean and finite coefficient maps. Assume both full matching packages and an adapted hyperbolic plane as in ([A hyperbolic plane adapted to lattices and split bases](https://andrewodesky.com/rh/lean/PositivityTheory.ThKG.Tow.Pln.exists_plane/)), with embedding of the smaller space, specified basis positions, integral-lattice splitting, and Cartan compatibility. Assume one of the following two steps: $$a_1=a,\ a'_1+2=a',\ p_1=p,\ q_1+1=q,\ \chi=\beta,\ r=a/2;$$ $$a_1+2=a,\ a'_1=a',\ p_1+1=p,\ q_1=q,\ \chi=\alpha,\ r=a'/2.$$ Here $(p,q)$ and $(p_1,q_1)$ are the auxiliary signature parameters of $G,G_1$.

For every $v\in T$, let $P_v,P_{1,v}$ be the finite coefficient spaces. Consider complex-linear maps $\lambda,\lambda':P_v\to P_{1,v}$ equivariant for the adapted Levi and unipotent action, with multiplier $\chi(t)|N_{E/F}(t)|^r$ in the prescribed local convention. If $\lambda\ne0$, then $$\lambda'=c\lambda\qquad\text{for some }c\in\mathbb C.$$ The equivariance is tested on Schwartz–Bruhat representatives through the prescribed coefficient projections.
