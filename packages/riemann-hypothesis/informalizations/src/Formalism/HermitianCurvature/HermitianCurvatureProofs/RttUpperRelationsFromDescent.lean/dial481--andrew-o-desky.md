---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/RttUpperRelationsFromDescent.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.quantum_determinant_from_rtt"
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

## A central quantum determinant from the two by two exchange relation

[Theorem ALG.0755](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.quantum_determinant_from_rtt/)

Let $A$ be a complex algebra, possibly noncommutative, and let $Q:\mathbb C\to M_2(A)$. Let $P$ be the flip matrix on the index set $\{1,2\}^2$, and let $Q_1(z)=Q(z)\otimes1_2$, $Q_2(z)=1_2\otimes Q(z)$, with these matrices defined entrywise below. Assume $$((w-z)1_4-P)Q_1(w)Q_2(z)=Q_2(z)Q_1(w)((w-z)1_4-P)\qquad(z,w\in\mathbb C).$$ For every $z\in\mathbb C$ there exists $\delta_z\in A$ such that, with $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $$Q(z+1)^tJQ(z)=\delta_zJ,\qquad Q(z)JQ(z+1)^t=\delta_zJ,$$ and $$\delta_zQ(w)_{ab}=Q(w)_{ab}\delta_z\qquad(w\in\mathbb C,\ a,b\in\{1,2\}).$$
