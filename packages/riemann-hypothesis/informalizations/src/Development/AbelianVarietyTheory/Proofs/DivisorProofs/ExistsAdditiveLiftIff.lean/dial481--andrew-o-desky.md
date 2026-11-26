---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAdditiveLiftIff.lean",
  "declarations": [
    "GlobalTheory.BirigidLift.exists_additive_lift_iff",
    "GlobalTheory.BirigidLift.exists_lift_of_cupSquare"
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

## Lifting a biadditive line bundle from its crystalline pairing

[Theorem PHT.1020](https://andrewodesky.com/rh/lean/GlobalTheory.BirigidLift.exists_lift_of_cupSquare/)

Let $R,R_0$ be commutative rings, $I\subset R$ an ideal with divided powers $\kappa$, and $\pi:R\to R_0$ a ring map. Assume the Grothendieck–Messing, abelian de Rham, and dual-abelian-scheme packages below. Let $A,B$ be abelian schemes over $R$ of constant relative dimensions $g,g'$, and identify $A_0,B_0$ with their group-scheme pullbacks to $R_0$.

Write $D_A,D_B$ for the duals of primitive crystalline $H^1$ of $A_0,B_0$ over $(R,I,\kappa)$, and $F_A\subset D_A$, $F_B\subset D_B$ for the inverse images of the lifted de Rham Hodge filtrations. Assume the cup-product conditions below for $C=A_0\times_{R_0}B_0$. Let $P_0$ be a line bundle on $A_0\times B_0$, additive in each variable. Suppose its crystalline Chern class has an expression $$c_1(P_0)=\sum_{j=1}^q\operatorname{pr}_A^*a_j\smile\operatorname{pr}_B^*b_j$$ with primitive classes $a_j,b_j$, and put $\varphi(x,y)=\sum_jx(a_j)y(b_j)$. If $$\varphi(F_A,F_B)=0,$$ there is a line bundle $P$ on $A\times_RB$, additive in each variable, whose pullback is isomorphic to $P_0$.

## Lifting a line bundle additive in each variable

[Theorem AV.1048](https://andrewodesky.com/rh/lean/GlobalTheory.BirigidLift.exists_additive_lift_iff/)

Assume the abelian deformation and cohomology laws specified below. Let $\pi:R\twoheadrightarrow R_0$ be a surjective homomorphism of commutative rings, with kernel $I$ and nilpotent divided powers $\gamma$ on $I$. Let $A,B$ be abelian schemes over $R$ of constant relative dimensions $g,g'$, with specified reductions $A_0,B_0$ over $R_0$. Let $l:A_0\times_{R_0}B_0\to A\times_RB$ be a map whose two projections are the specified reduction maps.

Let $P_0$ be a line bundle on $A_0\times B_0$, additive in each variable, and let $$\varphi_0:M(A_0)\times M(B_0)\longrightarrow R$$ be a crystalline correspondence form for $P_0$. Let $F_A\subseteq M(A_0)$ and $F_B\subseteq M(B_0)$ be the lifted Hodge submodules. Then there exists a line bundle $P$ on $A\times B$, additive in each variable and satisfying $l^*P\simeq P_0$, if and only if $$\varphi_0(F_A,F_B)=0.$$
