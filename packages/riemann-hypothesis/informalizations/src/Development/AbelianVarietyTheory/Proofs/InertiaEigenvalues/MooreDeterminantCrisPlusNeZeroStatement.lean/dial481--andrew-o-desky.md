---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MooreDeterminantCrisPlusNeZeroStatement.lean",
  "declarations": [
    "GlobalTheory.T.mooreDeterminant_crisPlus_ne_zero"
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

## A nonzero Frobenius Moore determinant

[Theorem PHT.0370](https://andrewodesky.com/rh/lean/GlobalTheory.T.mooreDeterminant_crisPlus_ne_zero/)

Let $\ell$ be prime and fix the local period datum, compatible Witt-vector datum, and period-ring identifications of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $0\le k\le h$ be integers. Suppose $a_0,\ldots,a_{k-1}\in B_{\mathrm{cris}}^+$ are linearly independent over $\mathbb Q_\ell$ and satisfy $$\varphi^h(a_j)=\ell a_j\qquad(0\le j<k).$$ Then $$\det\bigl(\varphi^i(a_j)\bigr)_{0\le i,j<k}\ne0.$$
