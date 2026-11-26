---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaMapPullO1PowerHodgeStatement.lean",
  "declarations": [
    "GlobalTheory.T.theta_map_pull_O1_power_hodge"
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

## Powers of a theta-coordinate bundle and the Hodge bundle

[Theorem AV.0901](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_map_pull_O1_power_hodge/)

Fix the unitary PEL datum in the conventions, level, moduli scheme $X$, and coefficient field $F$, and put $g=\tfrac12[E:\mathbb Q](p+q)$. Let $o$ be a commutative ring, $m,n\ge0$, and $f:X_F\to\mathbb P_o^n$. Assume $m$ is odd, $m\ge3$, $m\in o^\times$, $n+1=m^{4g}$, and $f$ is the source's level-$m$ theta-coordinate map for the universal principally polarized group and its rigidified line bundle.

Let $Y$ be a normal projective flat model over $F$ in the model package in the conventions, with generic identification $j:X_F\to Y$, and let $h:Y\to\mathbb P_o^n$ satisfy $h\circ j=f$. Let $\Omega/F$ be a field extension, let $Z$ be a rational model of $\Omega$ over $F$, and let $i:Z\hookrightarrow Y$ be an open immersion compatible with the structure maps to $\operatorname{Spec}F$. Writing $\lambda_Y=\det\operatorname{Lie}(G_Y/Y)^\vee$ for the Hodge line bundle of the model's semiabelian group, there is an isomorphism $$i^*(h^*\mathcal O(1))^{\otimes8(n+1)!} \simeq i^*\lambda_Y^{\otimes4((n+1)!)^2}.$$
