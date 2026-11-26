---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/ThetaGrpActsLinearly.lean",
  "declarations": [
    "GlobalTheory.thetaGrp_acts_linearly"
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

## Linear operators attached to theta-group elements

[Theorem AV.1516](https://andrewodesky.com/rh/lean/GlobalTheory.thetaGrp_acts_linearly/)

Assume that for every scheme $S$ and every abelian scheme $A/S$, pullback gives an isomorphism $\Gamma(S,\mathcal O_S)\simeq\Gamma(A,\mathcal O_A)$. Let $(A,L)$ be a principally polarized abelian scheme over any scheme $S$: $A$ has constant relative dimension, and $L$ is rigidified, symmetric, relatively ample, and has trivial translation stabilizer, let $k\in\mathbb Z$, and let $T\to S$ be any scheme. Put $R=\Gamma(T,\mathcal O_T)$ and $V=H^0(A_T,L_T^{\otimes k})$.

An element $\theta=(x,\varphi)$ consists of $x\in A(T)$ and a nowhere-zero trivialization $\varphi$ of $L_T^{\otimes k}\otimes(t_x^*L_T^{\otimes k})^{-1}$. There are $R$-linear automorphisms $\rho(\theta)$ of $V$ such that their action on sections is precisely $s\mapsto\varphi\,t_x^*s$. If the two composed trivializations attached to $\theta_x,\theta_y$ differ by $c\in R^\times$ in the order $\theta_x\theta_y=c\theta_y\theta_x$, then $$\rho(\theta_x)\rho(\theta_y)=c\,\rho(\theta_y)\rho(\theta_x).$$ Elements over the same point $x$ act by operators differing by a scalar in $R^\times$. For every pair $\theta_x,\theta_y$ there is an element over $x+y$ whose operator is $\rho(\theta_x)\rho(\theta_y)$.
