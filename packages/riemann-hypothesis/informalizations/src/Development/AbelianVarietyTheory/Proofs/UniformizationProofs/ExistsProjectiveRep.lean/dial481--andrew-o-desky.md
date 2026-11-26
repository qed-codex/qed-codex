---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsProjectiveRep.lean",
  "declarations": [
    "GlobalTheory.ThetaRep.exists_projective_rep"
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

## A projective representation of torsion by theta-group operators

[Theorem AV.1038](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaRep.exists_projective_rep/)

Assume the two abelian-scheme law packages described below. Let $S$ be locally Noetherian and $(A,L)/S$ a principally polarized abelian scheme of relative dimension $g$. Let $F$ be algebraically closed, $p:\operatorname{Spec}F\to S$, and $N\ge0$ with $N\ne0$ in $F$. Put $V=H^0(A_F,L_F^{\otimes N})$.

There are operators $\Phi_a\in\operatorname{GL}_F(V)$ for $a\in A_F[N](F)$ and scalars $e(a,b)\in F^\times$, with $$\dim_FV=N^g,$$ such that every $\Phi_a$ is the action of some theta-group element over $a$. For each $a,b$ there is $r\in F^\times$ with $$\Phi_{a+b}=r\Phi_a\Phi_b,$$ and $$\Phi_a\Phi_b=e(a,b)\Phi_b\Phi_a,$$ where $e(a,b)$ is the theta-group Weil commutator for $L_F^{\otimes N}$. If $e(a,b)=1$ for every $b$, then $a=0$.
