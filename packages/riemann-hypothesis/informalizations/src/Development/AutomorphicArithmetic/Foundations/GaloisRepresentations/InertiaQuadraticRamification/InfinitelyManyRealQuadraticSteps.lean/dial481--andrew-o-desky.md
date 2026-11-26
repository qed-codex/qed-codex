---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/InertiaQuadraticRamification/InfinitelyManyRealQuadraticSteps.lean",
  "declarations": [
    "UpperTheory.Gal.UnramifiedFromSplittingCriterion.freshChar_holds"
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

## A finite-order character with new ramification

[Theorem ANT.1252](https://andrewodesky.com/rh/lean/UpperTheory.Gal.UnramifiedFromSplittingCriterion.freshChar_holds/)

Let $F$ be a number field, $\Omega$ an algebraic closure, $G=\operatorname{Gal}(\Omega/F)$, $U\subseteq G$ an open subgroup, $T$ a finite set of finite primes of $F$, and $n\ge1$. There is a character $\psi:G\to\mathbb C^\times$ whose kernel is open, contains the commutator subgroup, and contains every complex conjugation, such that $\psi^n=1$ and $\psi$ is trivial on every decomposition group above $T$.

There is a prime $u\notin T$ with prime absolute norm $p=Nu$ such that, for every place $A$ of $\Omega$ above $u$, its decomposition group $D_A$ lies in $U$ and some $\tau\in I_A$ has $\operatorname{ord}(\psi(\tau))=n$. For every finite prime $t$ with $p\notin t$, $\psi$ is trivial on every inertia group above $t$.
