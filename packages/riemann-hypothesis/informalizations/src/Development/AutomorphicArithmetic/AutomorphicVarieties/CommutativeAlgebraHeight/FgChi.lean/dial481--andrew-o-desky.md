---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebraHeight/FgChi.lean",
  "declarations": [
    "UpperTheory.V.CA.f_gma"
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

## Rank-one idempotents in a multiplicity-free Cayley–Hamilton algebra

[Theorem ALG.0939](https://andrewodesky.com/rh/lean/UpperTheory.V.CA.f_gma/)

Let $B$ be a complete Noetherian commutative local ring, $E$ a possibly noncommutative $B$-algebra, $k$ a field with a local $B$-algebra structure, and $n\ge0$. Let $D$ be a determinant polynomial law of degree $n$ on $E$, satisfying the Cayley–Hamilton identities. Write $\chi_x(T)=D_{B[T]}(T\otimes1-1\otimes x)$. Suppose $\pi:E\to k^n$ is a surjective $B$-algebra homomorphism and $$\chi_x(T)\bmod k=\prod_{i=1}^n(T-\pi_i(x))\qquad(x\in E).$$ Then $$\ker\pi=\operatorname{Jac}(E),$$ and there are $e_1,\ldots,e_n\in E$ with $$\sum_i e_i=1,\qquad e_i^2=e_i,\qquad e_ie_j=0\ (i\ne j),\qquad\pi(e_i)=(\delta_{ij})_j,$$ $$D_{B[T]}(1+T\otimes e_i)=1+T\qquad(1\le i\le n).$$
