---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/OddResidueBounds/ActFacts.lean",
  "declarations": [
    "UpperTheory.V.Odd.actFacts"
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

## Galois quotients of a compatible cyclotomic action

[Theorem ANT.1242](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.actFacts/)

Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, $N\ge1$, and $\rho:(\mathbb Z/N\mathbb Z)^\times\to\operatorname{Aut}_{\mathbb Q}(E)$ a homomorphism. Assume that whenever $b\in(\mathbb Z/N\mathbb Z)^\times$ and a field automorphism $\sigma$ of $\Omega$ acts on all $N$th roots of unity by $\zeta\mapsto\zeta^b$, its restriction to $E$ is $\rho(b)$, using the specified embedding of $E$ in $\Omega$. Then $\rho$ is surjective, $E/\mathbb Q$ is abelian Galois, and $$\#\bigl((\mathbb Z/N\mathbb Z)^\times/\ker\rho\bigr)=[E:\mathbb Q]=[(\mathbb Z/N\mathbb Z)^\times:\ker\rho].$$ For every $M\ge1$ with $N\mid M$, composition with reduction modulo $N$ gives an action of $(\mathbb Z/M\mathbb Z)^\times$ with the analogous compatibility on $M$th roots of unity.
