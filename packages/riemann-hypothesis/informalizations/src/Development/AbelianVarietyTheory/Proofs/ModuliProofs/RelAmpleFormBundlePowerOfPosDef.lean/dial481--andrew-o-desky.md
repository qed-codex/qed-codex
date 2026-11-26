---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/RelAmpleFormBundlePowerOfPosDef.lean",
  "declarations": [
    "GlobalTheory.PosDefAmple.exists_smul_eq_transpose_mul_self"
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

## An integral Gram factorization after scaling

[Theorem ALG.0293](https://andrewodesky.com/rh/lean/GlobalTheory.PosDefAmple.exists_smul_eq_transpose_mul_self/)

Let $Q\in M_n(\mathbb Z)$ be positive definite when viewed as a real matrix. There exist integers $N\ge1$, $m\ge0$, $d\ne0$, and matrices $C\in M_{m,n}(\mathbb Z)$, $B\in M_{n,m}(\mathbb Z)$ such that $$NQ=C^{\mathsf T}C,\qquad BC=dI_n.$$
