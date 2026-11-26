---
{
  "module": "src/Formalism/LocalToGlobal/PairingIndexBounds/ModelLatticeMoves/MovesComposeU.lean",
  "declarations": [
    "Formalism.L2.PairingIndexBounds.Mv.indexDual",
    "Formalism.L2.PairingIndexBounds.Mv.movesComposeU"
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

## Equality of relative indices under a bicharacter

[Theorem ALG.0960](https://andrewodesky.com/rh/lean/Formalism.L2.PairingIndexBounds.Mv.indexDual/)

Let $k$ be a field, $A,B$ abelian groups, and $c:B\times A\to k^\times$ a bicharacter. Let $A_0,A_1\le A$ and $B_0,B_1\le B$ satisfy $$B_0=\{b\in B:c(b,a)=1\text{ for every }a\in A_0\},$$ $$c(b,a)=1\qquad(b\in B_1,\ a\in A_1),$$ $$a\in A_0,\ c(b,a)=1\text{ for every }b\in B_1\quad\Longrightarrow\quad a\in A_1.$$ If $[A_0:A_0\cap A_1]$ is finite, then $$[B_1:B_1\cap B_0]=[A_0:A_0\cap A_1].$$

## Composition of normalized lattice averaging operators

[Theorem THETA.1035](https://andrewodesky.com/rh/lean/Formalism.L2.PairingIndexBounds.Mv.movesComposeU/)

Let $V$ be a complex vector space, $H$ a Hermitian form linear in the first variable, and $\alpha:V\to\mathbb C$. Put $E(x,y)=\operatorname{Im}H(x,y)$. Let $A,B,\Lambda_0,\Lambda_1,\Lambda_2$ be additive subgroups satisfying the conditions below. Suppose each quotient $\Lambda_j/(\Lambda_i\cap\Lambda_j)$ for $(i,j)=(0,1),(1,2),(0,2)$ is finite. Define $$U_xF(z)=F(z+x)e^{-\pi H(z,x)-\pi H(x,x)/2},$$ $$T_{ij}F=\frac1{\sqrt{[\Lambda_j:\Lambda_i\cap\Lambda_j]}}\sum_{x\in\Lambda_j/(\Lambda_i\cap\Lambda_j)}\alpha(x)U_xF.$$ For every function $F:V\to\mathbb C$ with $\alpha(x)U_xF=F$ for $x\in\Lambda_0$, $$T_{12}(T_{01}F)=T_{02}F.$$
