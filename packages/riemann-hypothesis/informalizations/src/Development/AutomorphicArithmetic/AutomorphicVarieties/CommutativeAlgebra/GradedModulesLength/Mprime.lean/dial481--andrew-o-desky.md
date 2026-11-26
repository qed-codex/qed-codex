---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/Mprime.lean",
  "declarations": [
    "UpperTheory.V.Alg.M.mprime_holds"
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

## Lengths of modules of liftable derivations bounded by a cotangent length

[Theorem ALG.1756](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.mprime_holds/)

Let $O$ be a discrete valuation ring with finite residue field, $X$ an abelian group, $A=\bigoplus_{i\in X}A_i$ a commutative $O$-algebra graded by $X$, and $x:A\to O$ a homomorphism of $O$-algebras. Let $j\in X$ be a degree with $x(A_j)=0$, and let $(F_i)_{i\in I}$ be a family of elements of $A_j$. Let $c\in O$ be nonzero, let $M$ be an $O$-module, and let $$D:M\longrightarrow\operatorname{Hom}_O(A,O/cO),\qquad\mu\longmapsto D_\mu,$$ be an injective homomorphism of abelian groups such that, for every $\mu\in M$,

1. $D_\mu(F_i)=0$ for every $i\in I$, and
2. $D_\mu$ is the reduction modulo $c$ of a derivation of degree $j$ at $x$.

Then $$\operatorname{length}_OM\le\operatorname{length}_O\bigl(C_j/\langle F_i:i\in I\rangle\bigr).$$
