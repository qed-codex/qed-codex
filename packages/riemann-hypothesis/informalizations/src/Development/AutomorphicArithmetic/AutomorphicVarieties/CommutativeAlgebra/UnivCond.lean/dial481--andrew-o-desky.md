---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/UnivCond.lean",
  "declarations": [
    "UpperTheory.V.Alg.univ_cond"
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

## Representing a nonempty closed deformation condition by a quotient

[Theorem AGR.0866](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.univ_cond/)

Let $O$ be a local commutative ring with residue field $k$, $I$ a finite set, $\Gamma$ a group with a topology, and $\bar r:\Gamma\to\operatorname{GL}_I(k)$. Work with the coefficient algebras and lifts described below. Suppose a lift $r$ over $R$ represents a condition $P_0$ on lifts. Suppose another condition $P$ is closed: for every lift $u$ over a coefficient algebra $A$, there is an ideal $J\subseteq A$ such that, for every coefficient algebra $B$ and $O$-algebra map $f:A\to B$, $$P(f_*u)\quad\Longleftrightarrow\quad f(J)=0.$$ If there is at least one lift over some coefficient algebra satisfying both $P_0$ and $P$, there are a coefficient algebra $R'$ and a surjective $O$-algebra map $p:R\to R'$ such that $p_*r$ represents $P_0\wedge P$.
