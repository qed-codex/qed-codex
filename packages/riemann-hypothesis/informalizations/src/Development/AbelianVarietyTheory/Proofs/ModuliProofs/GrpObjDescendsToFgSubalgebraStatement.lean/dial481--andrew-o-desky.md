---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/GrpObjDescendsToFgSubalgebraStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_fg_subalgebra_grpObj_model"
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

## Descent of a smooth commutative group to a finite subalgebra

[Theorem AG.0425](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_fg_subalgebra_grpObj_model/)

Let $k,V$ be commutative rings with a $k$-algebra structure on $V$. Let $A$ be a commutative group scheme over $\operatorname{Spec}V$. Suppose its underlying scheme is identified, by a specified Cartesian square, with $$X\times_{\operatorname{Spec}k}\operatorname{Spec}V,$$ where $X\to\operatorname{Spec}k$ is smooth, separated, and quasi-compact. For every finite set $F\subset V$, there are a finitely generated $k$-subalgebra $R\subseteq V$ containing $F$ and a smooth separated quasi-compact commutative group scheme $A_0/\operatorname{Spec}R$, with a group-scheme base-change identification $$A\simeq A_0\times_{\operatorname{Spec}R}\operatorname{Spec}V.$$
