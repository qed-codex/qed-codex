---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitaryActionHermitianInvariantsTransitive.lean",
  "declarations": [
    "GlobalTheory.JR.HermInv.herm_invariants"
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

## Invariants and regular orbits of a Hermitian matrix with a vector

[Theorem REP.1017](https://andrewodesky.com/rh/lean/GlobalTheory.JR.HermInv.herm_invariants/)

Let $F\subset E$ be nontrivially normed fields with a normed $F$-algebra structure on $E$ and an involution $x\mapsto\bar x$. Assume the field conditions below. Fix $r\ge0$. For a triple $X=(A,v,d)$ with $A=A^*\in M_r(E)$, $v\in E^r$, $d\in F$, its invariants are $$\det(TI-A)=T^r+\sum_{i=0}^{r-1}p_iT^i,\qquad b_i=v^*A^iv\ (0\le i<r),\qquad d.$$ Every such triple has invariants $a=(p,b,d)\in F^r\times F^r\times F$. The action $$g\cdot(A,v,d)=(gAg^*,gv,d)\qquad(g\in U_r(E))$$ preserves them. Define $b_k$ for $k\ge r$ by $b_{k+r}=-\sum_{j=0}^{r-1}p_jb_{k+j}$ and put $H(a)=(b_{i+j})_{0\le i,j<r}$. If $\det H(a)\ne0$, any two triples with invariants $a$ are related by a unique $g\in U_r(E)$. Such a triple exists if and only if $$h^*h=H(a)\quad\text{for some }h\in M_r(E).$$
