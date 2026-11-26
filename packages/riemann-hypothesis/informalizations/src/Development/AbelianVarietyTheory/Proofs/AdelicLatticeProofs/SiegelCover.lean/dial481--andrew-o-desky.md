---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/SiegelCover.lean",
  "declarations": [
    "GlobalTheory.ClassFin.siegel_cover"
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

## A Siegel set covers the real special linear group modulo integers

[Theorem ARAK.0400](https://andrewodesky.com/rh/lean/GlobalTheory.ClassFin.siegel_cover/)

For every finite linearly ordered coordinate set $I$, there is $C\in\mathbb R$ such that every $g\in\operatorname{Mat}_I(\mathbb R)$ with $\det g=1$ admits $\gamma\in\operatorname{Mat}_I(\mathbb Z)$ and real matrices $k,n$ and numbers $a_i$ with $$\det\gamma=1,\qquad g\gamma=k\operatorname{diag}(a_i)n,$$ $$k^{\mathsf T}k=1,\quad\det k=1,\quad a_i>0,\quad\prod_i a_i=1,\quad a_i\le Ca_j\ (i<j),$$ $$n_{ii}=1,\quad n_{ij}=0\ (j<i),\quad |n_{ij}|\le C\ (i,j\in I).$$
