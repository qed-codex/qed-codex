---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/DefiniteTraceForms/WeightedCountDefiniteUnitary.lean",
  "declarations": [
    "UpperTheory.Gal.Cnt.trace_definite_forms_identity"
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

## Weighted definite-pair sums and Hecke traces

[Theorem AGR.1674](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Cnt.trace_definite_forms_identity/)

Fix a prime $p$ and the source's full unitary counting datum with parameter $a=1$: a CM field $F$, an imaginary quadratic subfield embedded in $\mathbb Q_p$, a central simple $F$-algebra $C$ of dimension $n^2$ with conjugate-linear involution, its archimedean realizations, and its prescribed local embeddings and comparison maps. Let $\xi$ be a finite-dimensional complex representation of $C^\times\times\mathbb Q^\times$, and $\mathrm{wt}:F[T]\to\mathbb C$ a weight function. Assume that in every permitted definite inner form, the trace of $\xi$ on an element whose underlying $C$-component has separable minimal polynomial of degree $n$ is $\mathrm{wt}$ of that polynomial.

Choose a permitted away-from-$p$ level $K_f$ and function $f$, and a local level $K'$ and function $f'$ at the distinguished parameter-one local group. Assume both source test-function conditions, and assume $f,f'$ are bi-invariant under $K_f,K'$ respectively. Assume also that for every definite form, every allowed away-from-$p$ trivialization, and every rational element whose $C$-component fails to have separable irreducible minimal polynomial of degree $n$, the orbital term of $f\otimes f'$ is zero.

A definite form is an invertible involution-symmetric element $\beta\in C$ whose Hermitian forms have the prescribed positive or negative sign at each infinite place, and which becomes a scalar form after an allowed conjugation away from $p$. A definite pair adds $\gamma\in C^\times$ and $c\in\mathbb Q^\times$ with $\gamma\beta\gamma^*=c\beta$ and separable degree-$n$ minimal polynomial of $\gamma$ over $F$; pairs are identified by $(\beta,\gamma)\mapsto(sy\beta y^*,y\gamma y^{-1})$ for $y\in C^\times$, $s\in\mathbb Q_{>0}$. Here $*$ is the fixed involution. Its counting term is the sum over double cosets modulo the rational centralizer and the two levels, with the test values divided by the orders of their stabilizers; the term is zero if the required local twisted-norm data do not exist.

Then $$\sum_{[P]}\mathbf1_{\{P\ \mathrm{has\ irreducible\ polynomial}\}}\, \mathrm{wt}(P_P)\,O_P(f,f') =\sum_{[B]}\operatorname{tr}\!\left(T_{f\otimes f'}\mid\mathcal A(B,K_fK',\xi)\right).$$ On the left, $[P]$ runs over the definite-pair classes defined above, $P_P$ is their polynomial, and $O_P$ their counting term just defined; on the right, $[B]$ runs over definite forms modulo positive rational scaling and conjugation, and $\mathcal A$ consists of functions transforming by $\xi$ under the rational group and invariant under the level. All sums are unordered sums.
