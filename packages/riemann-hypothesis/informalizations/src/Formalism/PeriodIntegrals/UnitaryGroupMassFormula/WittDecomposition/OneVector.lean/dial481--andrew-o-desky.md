---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/WittDecomposition/OneVector.lean",
  "declarations": [
    "PI.Witt.one_vector_holds"
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

## An isometry carrying one vector to another

[Theorem ALG.1058](https://andrewodesky.com/rh/lean/PI.Witt.one_vector_holds/)

Let $K$ be a field of characteristic zero with an involution $a\mapsto\bar a$, let $V$ be a $K$-vector space, and let $B$ be a Hermitian form, conjugate-linear in the first variable. If $$B(x,x)=B(y,y)\ne0,$$ there is a $K$-linear automorphism $g$ of $V$ such that $$B(gz,gw)=B(z,w)\quad(z,w\in V),\qquad gx=y,$$ and $gz=z$ whenever $B(x,z)=B(y,z)=0$.
