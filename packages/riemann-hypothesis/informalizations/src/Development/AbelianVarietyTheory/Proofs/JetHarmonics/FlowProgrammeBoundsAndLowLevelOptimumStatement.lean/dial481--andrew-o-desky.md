---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/FlowProgrammeBoundsAndLowLevelOptimumStatement.lean",
  "declarations": [
    "GlobalTheory.T.flow_programme_bounds_and_low_level_optimum"
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

## Bounds and finite-level approximation for a cyclic flow programme

[Theorem ALG.0918](https://andrewodesky.com/rh/lean/GlobalTheory.T.flow_programme_bounds_and_low_level_optimum/)

Let $\ell\ge2$, $d\ge1$, and $D:\mathbb Z/d\mathbb Z\to\mathbb R_{\ge0}$. Put $I_d=\{i:0\le i<d,\ i\text{ odd}\}$. A feasible flow is a family $x_{a,i}\ge0$ for $a\in\mathbb Z/d\mathbb Z$, $i\ge0$, satisfying $$\sum_{i\in I_d}\bigl(\ell^i x_{a,i}+x_{a-i,i}\bigr)\le D_a\qquad(a\in\mathbb Z/d\mathbb Z).$$ Set $V(x)=\sum_a\sum_{i\in I_d}x_{a,i}$ and $$F(D)=\frac{\ell}{\ell^2-1}\sum_aD_a-\sup_{x\text{ feasible}}V(x).$$ Then $$\frac1{\ell^2-1}\sum_aD_a\le F(D),\qquad F(tD)=tF(D)\quad(t\ge0).$$ The value $F(D)$ is unchanged if feasibility additionally requires $x_{a,i}=0$ for $i\notin I_d$ and both the objective and constraints are summed over $0\le i<d$. For every $i_0\ge0$, there is a feasible flow vanishing whenever $i\ge i_0$, with $$\frac{\ell}{\ell^2-1}\sum_aD_a-V(x)\le F(D)+\ell^{-i_0}\sum_aD_a.$$
