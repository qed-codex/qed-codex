---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsLargePrimeInRayClass.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.DegOneRay.exists_degOne_prime_in_rayClass",
    "GlobalTheory.CompanionTheory.DegOneRay.exists_degree_one_frobenius_prime"
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

## Degree-one primes with a prescribed Frobenius action

[Theorem ANT.0320](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.DegOneRay.exists_degree_one_frobenius_prime/)

Let $F$ be a number field, $\Omega$ an algebraic closure of $F$, and $L\subseteq\Omega$ a finite Galois extension of $F$. Fix $g\in\operatorname{Gal}(L/F)$ and a finite set $S$ of nonzero primes of $\mathcal O_F$. There are a nonzero prime $\mathfrak p\notin S$ of $\mathcal O_F$, of residue degree $1$ over $\mathbb Z$, and a prime ideal $P\subseteq\mathcal O_L$ above $\mathfrak p$, such that $$g(x)-x^{N\mathfrak p}\in P\qquad(x\in\mathcal O_L),$$ where $N\mathfrak p=|\mathcal O_F/\mathfrak p|$.

## Large degree-one primes in a narrow ray class

[Theorem ANT.1207](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.DegOneRay.exists_degOne_prime_in_rayClass/)

Let $F$ be a number field and let $\mathfrak f,\mathfrak a\subset\mathcal O_F$ be nonzero ideals with $\mathfrak a+\mathfrak f=\mathcal O_F$. Let $W\subset\mathcal O_F$ be a finite set of nonzero elements and let $B\ge0$ be an integer. There is a prime ideal $\mathfrak c$ such that $$N\mathfrak c\text{ is a rational prime},\quad N\mathfrak c>B,\quad \mathfrak c+\mathfrak f=\mathcal O_F,\quad W\cap\mathfrak c=\varnothing,$$ and there are nonzero totally positive $a,b\in\mathcal O_F$ with $$a\equiv b\equiv1\pmod{\mathfrak f},\qquad(a)\mathfrak c=(b)\mathfrak a.$$
