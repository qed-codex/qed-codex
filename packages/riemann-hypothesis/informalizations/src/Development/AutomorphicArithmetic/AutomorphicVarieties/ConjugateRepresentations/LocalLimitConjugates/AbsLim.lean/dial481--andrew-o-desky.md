---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/LocalLimitConjugates/AbsLim.lean",
  "declarations": [
    "UpperTheory.V.Cj.H.absLim"
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

## Strong limit of scaled resolvents

[Theorem ALG.1143](https://andrewodesky.com/rh/lean/UpperTheory.V.Cj.H.absLim/)

Let $H$ be a complex Hilbert space, $D\subseteq H$ a complex linear subspace, and $A:D\to D$ linear and symmetric: $\langle Av,w\rangle=\langle v,Aw\rangle$ for $v,w\in D$. Let $s_k\in\mathbb R$ tend to zero. For every $k$, suppose both $(A+is_k)D$ and $(A-is_k)D$ have zero orthogonal complement in $H$. Suppose bounded complex linear operators $T_k:H\to H$ satisfy $$T_k(Av+is_kv)=v\quad(v\in D),\qquad |s_k|\,\|T_kw\|\le\|w\|\quad(w\in H).$$ Let $P:H\to H$ be bounded and complex linear, with $$\langle Pw,Av\rangle=0,\qquad w-Pw\in\overline{A(D)}\quad(w\in H,\ v\in D).$$ Then $is_kT_kw\to Pw$ in norm for every $w\in H$.
