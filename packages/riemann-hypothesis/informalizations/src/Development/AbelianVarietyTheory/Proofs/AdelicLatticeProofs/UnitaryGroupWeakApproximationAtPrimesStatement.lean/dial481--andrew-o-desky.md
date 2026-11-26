---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/UnitaryGroupWeakApproximationAtPrimesStatement.lean",
  "declarations": [
    "GlobalTheory.T.unitaryGroup_weak_approximation_at_primes"
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

## Rational unitary approximation with an adelic lattice congruence

[Theorem ANT.0500](https://andrewodesky.com/rh/lean/GlobalTheory.T.unitaryGroup_weak_approximation_at_primes/)

Let $E/F$ be a quadratic extension of number fields, $c$ its nontrivial involution, and $J\in M_n(E)$ nonsingular with $c(J)=J^t$. Put $h(x,y)=x^tJc(y)$, $R=\mathbb A_{F,f}\otimes_FE$, and let $U(h)$ be its isometry group. Let $L\subset E^n$ be a finitely generated $\mathcal O_E$-module spanning $E^n$. For every $g\in U(h)(R)$ and positive integers $N,D$, there are $\gamma\in U(h)(E)$ and $t\in\mathbb N$, $\gcd(t,N)=1$, such that $$t(\gamma g-1)\widehat L\subseteq D\widehat L.$$
