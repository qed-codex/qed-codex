---
{
  "module": "src/Formalism/BranchSandwichDivisors/BranchIsometryProofs/OrthSum.lean",
  "declarations": [
    "Formalism.BranchingDeterminantCap.orthogonal_sum_slope",
    "Formalism.BranchingDeterminantCap.power_slope_mu"
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

## Ranks, degrees, and maximal slopes of an orthogonal sum

[Theorem ARAK.1324](https://andrewodesky.com/rh/lean/Formalism.BranchingDeterminantCap.orthogonal_sum_slope/)

Let $K$ be a totally complex number field with a fixed ring involution, let $d=[K:\mathbb Q]$, and let $V$ be a finite-dimensional $K$-vector space with basis $b$. Give it, at every infinite place $v$, the Hermitian metric obtained by sending its coordinate vector $z$ to $X_v^{-1}z$ with $X_v$ an invertible complex matrix. Let $\rho$ be the resulting real Euclidean realization using one embedding for each complex place; covolumes are measured in the real span of each lattice.

For a nonzero finitely generated $\mathcal O_K$-submodule $L\subset V$, set $$r_K(L)=\dim_K(KL),\qquad \mu(L)=\frac{-2\log\operatorname{covol}(\rho(L))}{d\,r_K(L)}-\log2+\frac{\log|\operatorname{disc}K|}{d},$$ $$\mu_{\max}(L)=2\sup_{0\ne N\subset L}\frac{-\log\operatorname{covol}(\rho(N))}{\operatorname{rank}_{\mathbb Z}N}-\log2+\frac{\log|\operatorname{disc}K|}{d},\qquad \deg(L)=r_K(L)\mu(L).$$ The supremum runs over $\mathcal O_K$-submodules, and $r_K(0)=\deg(0)=0$.

Let $(L_s)_{s\in S}$ be a finite family of finitely generated $\mathcal O_K$-submodules, pairwise orthogonal at every infinite place, and put $L=\sum_sL_s$. Then $$r_K(L)=\sum_sr_K(L_s),\qquad\deg(L)=\sum_s\deg(L_s).$$ For every $c\in\mathbb R$, if each nonzero $L_s$ has $\mu_{\max}(L_s)\le c$ and $L\ne0$, then $\mu_{\max}(L)\le c$.

## Ranks and slopes of repeated orthogonal sums

[Theorem ARAK.1399](https://andrewodesky.com/rh/lean/Formalism.BranchingDeterminantCap.power_slope_mu/)

Let $K$ be a totally complex number field equipped with a ring involution, $V$ a finite-dimensional $K$-vector space with compatible $\mathcal O_K$-module structure, and $b$ a finite basis. At each infinite place $v$, fix an invertible complex matrix $X_v$ specifying the archimedean norm in this basis. Let $A\subset V$ be a nonzero finitely generated $\mathcal O_K$-submodule, and let $n\ge1$.

Give $V^n$ the repeated basis and block-diagonal frames with $n$ copies of $X_v$, and give $A^n$ the product lattice. With $r_K$, $\mu$, and $\mu_{\max}$ denoting rank, arithmetic slope, and maximal arithmetic slope in the normalization of ([Ranks, degrees, and maximal slopes of an orthogonal sum](https://andrewodesky.com/rh/lean/Formalism.BranchingDeterminantCap.orthogonal_sum_slope/)), $$r_K(A^n)=n\,r_K(A),\qquad\mu(A^n)=\mu(A),\qquad\mu_{\max}(A^n)=\mu_{\max}(A).$$
