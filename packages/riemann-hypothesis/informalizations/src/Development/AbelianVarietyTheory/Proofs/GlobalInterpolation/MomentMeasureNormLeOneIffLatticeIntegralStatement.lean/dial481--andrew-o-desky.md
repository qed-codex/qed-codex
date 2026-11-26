---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MomentMeasureNormLeOneIffLatticeIntegralStatement.lean",
  "declarations": [
    "GlobalTheory.T.momentMeasure_norm_le_one_iff_latticeIntegral"
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

## A measure norm criterion for integral lattice moments

[Theorem PHT.1063](https://andrewodesky.com/rh/lean/GlobalTheory.T.momentMeasure_norm_le_one_iff_latticeIntegral/)

Let $g,r\ge0$ be integers, let $q$ be prime, let $\iota:\mathbb C\simeq\mathbb C_q$ be a field isomorphism, and let $\lambda:\overline{\mathbb Q}\to\mathbb C_q$ agree with $\iota$ on algebraic numbers. Fix $\delta\in\mathbb C^\times$ and $\Omega\in\mathbb C_q$ with $|\Omega|_q=1$. Let $(d,H,\Lambda)$, $b_1,\ldots,b_r\in\Lambda$, $t\in\mathbb C^g$, an entire $G:\mathbb C^g\to\mathbb C$, and a bounded $\mathbb C_q$-linear functional $\mu$ on $C(\mathbb Z_q^r,\mathbb C_q)$ satisfy the lattice and interpolation conditions below. Then $$\|\mu\|\le1\quad\Longleftrightarrow\quad G\text{ has integral moments on }\frac{\Omega}{\iota(\delta)}\Lambda.$$
