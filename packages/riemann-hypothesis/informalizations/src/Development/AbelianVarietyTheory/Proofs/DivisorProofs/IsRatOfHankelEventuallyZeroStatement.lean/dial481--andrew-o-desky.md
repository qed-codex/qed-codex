---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRatOfHankelEventuallyZeroStatement.lean",
  "declarations": [
    "GlobalTheory.T.isRat_of_hankel_eventually_eq_zero"
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

## Rationality from eventual vanishing of Hankel determinants

[Theorem ALG.0327](https://andrewodesky.com/rh/lean/GlobalTheory.T.isRat_of_hankel_eventually_eq_zero/)

Let $F$ be a field and $\phi(T)=\sum_{j\ge0}c_jT^j\in F[[T]]$. If there is $N\ge0$ such that $$\det(c_{i+j})_{0\le i,j\le n}=0\qquad(n\ge N),$$ then $\phi$ is rational: there are $p,q\in F[T]$ with $q\ne0$ and $q\phi=p$ in $F[[T]]$.
