---
{
  "module": "src/Development/WeilBound/ThetaLifts/LocalTheory/UnramifiedCohomology/UnramifiedDeterminedBySphericalHolds.lean",
  "declarations": [
    "PositivityTheory.ThKG.Loc.unramifiedProportional_holds"
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

## An unramified local map is determined by its vacuum value

[Theorem REP.1523](https://andrewodesky.com/rh/lean/PositivityTheory.ThKG.Loc.unramifiedProportional_holds/)

Let $E/F$ be number fields with an $F$-automorphism $\sigma$ and the source's base datum. Fix two geometric theta data of sizes $(a,a')$ and $(a_1,a'_1)$, a common character datum with splitting characters $\alpha,\beta$ and exceptional finite set $T$, their paired Weil actions, and their real and finite coefficient maps. Assume both full matching packages. Choose a hyperbolic plane and an embedding of the smaller auxiliary space satisfying the source's adapted-plane conditions at specified basis positions $i_0,i_1$.

Let $(p,q),(p_1,q_1)$ be the auxiliary signatures. Assume either $$a_1=a,\quad a'_1+2=a',\quad p_1=p,\quad q_1+1=q,\quad\chi=\beta,\quad r=a/2,$$ or $$a_1+2=a,\quad a'_1=a',\quad p_1+1=p,\quad q_1=q,\quad\chi=\alpha,\quad r=a'/2.$$ For a finite place $v\notin T$, write $P_v,P_{1,v}$ for the finite coefficient spaces and $p_v$ for the first model's coefficient projection. Let $\lambda,\lambda':P_v\to P_{1,v}$ be complex-linear maps satisfying the prescribed Levi and unipotent equivariance, tested on Schwartz–Bruhat representatives, with multiplier $\chi(t)|N_{E/F}t|^r$. If $\varphi_v^0$ is the first model's vacuum vector, then for every $c\in\mathbb C$, $$\lambda'(p_v(\varphi_v^0))=c\lambda(p_v(\varphi_v^0))\quad\Longrightarrow\quad\lambda'=c\lambda.$$
