---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMixedHeightOfArchimedeanIntegralsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_mixedHeight_of_archimedean_integrals"
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

## Mixed arithmetic heights from archimedean integration and reciprocity

[Theorem ARAK.1320](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_mixedHeight_of_archimedean_integrals/)

Assume the following global archimedean integration and reciprocity conditions: logarithmic norms of rational sections are integrable against the indicated top Chern measures on every integral projective arithmetic variety, and the mixed archimedean integrals satisfy reciprocity for two nonzero sections with no common codimension-one zero.

Let $R$ be a commutative integral ring finite over $\mathbb Z$, let $X$ be projective over $\operatorname{Spec}R$, and let $m\ge0$. There is a family of real numbers $$T_d(L_1,\ldots,L_d;x)\qquad(d\ge0),$$ for Hermitian line bundles $L_i$ on $X$ and points $x\in X$, with the following properties whenever the closure of $x$ has dimension $d\le m$: it is invariant under isometries of the bundles, symmetric in them, and additive under tensor product in each argument. At dimension zero, $$T_0(x)=\log\operatorname{card}_0\kappa(x),$$ where $\operatorname{card}_0$ is ordinary cardinality for finite fields and zero for infinite fields, with $\log0=0$.

For an integral closed subscheme $Y\subset X$ of dimension $e+1\le m$, a nonzero rational section $r$ of a Hermitian line bundle $M$ restricted from $X$ to $Y$, and Hermitian line bundles $L_1,\ldots,L_e$ restricted from $X$, the family satisfies $$T_{e+1}(M,L_1,\ldots,L_e;Y) =\sum_z\operatorname{mult}_z(\operatorname{div}r)\,T_e(L_1,\ldots,L_e;z)-A(L_1,\ldots,L_e;M,r).$$ Here evaluation at a subscheme means evaluation at its generic point, and $A$ is the symmetric polarization, divided by $e!$, of the archimedean logarithmic-norm integral against the Chern measure of a tensor combination of the $L_i$.
