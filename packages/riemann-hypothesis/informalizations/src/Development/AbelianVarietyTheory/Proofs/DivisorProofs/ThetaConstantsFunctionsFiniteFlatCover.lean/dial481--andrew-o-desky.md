---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaConstantsFunctionsFiniteFlatCover.lean",
  "declarations": [
    "GlobalTheory.UMin.thList_cover"
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

## Theta constants after a finite faithfully flat base extension

[Theorem AV.0778](https://andrewodesky.com/rh/lean/GlobalTheory.UMin.thList_cover/)

Let $G\to S$ be a commutative group scheme and $L$ a line bundle on $G$ with a rigidification $\rho$ at the identity. Let $R$ be a commutative noetherian ring, let $x:\operatorname{Spec}R\to S$, and suppose $(G_x,L_x)$ is isomorphic, as a group scheme with line bundle, to a polarized abelian scheme of relative dimension $g$ with the polarization conditions below. Fix a section $\theta\in\Gamma(G_x,L_x)$ and an odd integer $m\ge0$ that is a unit in $R$. Put $N=m^{4g}$.

There exist a finite faithfully flat commutative $R$-algebra $R_1$ and elements $c_1,\ldots,c_N\in R_1$ such that, for every field $K$ and compatible maps $i:R\to K$, $i_1:R_1\to K$, there are distinct points $p_1,\ldots,p_N\in G_x(K)$ satisfying $$[m^2]p_a=0,\qquad\text{the normalized theta value of }\theta_K\text{ at }p_a\text{ is }i_1(c_a).$$ Every $m^2$-torsion point after every algebraically closed field extension $K\subseteq K'$ is the image of one of the $p_a$.
