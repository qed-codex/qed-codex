---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DvdOfForallEmultiplicityLe.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Short.ChowClosing.chowFormSectionPerfect_of"
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

## Specialization of a Chow form over a perfect field

[Theorem AG.1202](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Short.ChowClosing.chowFormSectionPerfect_of/)

Assume the following four universal cycle-comparison statements: the Chow-form specialization theorem over algebraically closed fields; additivity of hyperplane-section cycles for reduced equidimensional ideals; contraction of minimal primes after extension of a prime polynomial ideal along a field extension; and compatibility of fundamental cycles with field extension from a perfect field.

Let $F$ be perfect, let $n,e\ge0$, and let $I\subset F[X_1,\ldots,X_n]$ be a homogeneous prime defining a nonempty projective variety. Let $f$ be a Chow form for $I$ in $e+1$ blocks of $n$ variables. Let $u=(u_1,\ldots,u_n)\in F^n$ and suppose $\sum u_iX_i\notin I$. Specializing the first block of $f$ to $u$ gives a Chow form, in $e$ blocks, for the divisor cycle cut out by $\sum u_iX_i$ on $I$.
