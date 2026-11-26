---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/DropLevelsBasic.lean",
  "declarations": [
    "GlobalTheory.BasicFlow.dropLevelsBasic"
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

## A sparse flow below a level cutoff

[Theorem ALG.1069](https://andrewodesky.com/rh/lean/GlobalTheory.BasicFlow.dropLevelsBasic/)

Let $\ell\ge2$ and $d\ge1$ be integers, let $W:\mathbb Z/d\mathbb Z\to\mathbb R_{\ge0}$, and put $J=\{i\in\mathbb Z:0\le i<d,\ i\text{ odd}\}$. Call a family $y_{a,i}$, indexed by $a\in\mathbb Z/d\mathbb Z$ and integers $i\ge0$, feasible if all its entries are nonnegative and $$\sum_{i\in J}\ell^i y_{a,i}+\sum_{i\in J}y_{a-i,i}\le W(a)\qquad(a\in\mathbb Z/d\mathbb Z).$$ Let $M$ be the supremum of $\sum_a\sum_{i\in J}y_{a,i}$ over feasible families. For every integer $i_0\ge0$ there is a feasible family $y$ such that $y_{a,i}=0$ whenever $i\ge i_0$ or $i\notin J$, at most $d$ pairs $(a,i)$ have $y_{a,i}\ne0$, and $$\sum_a\sum_{i\in J}y_{a,i}\ge M-\ell^{-i_0}\sum_aW(a).$$
