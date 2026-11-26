---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/ExistsMonicFactorLiftOfPowMulSubOnePow.lean",
  "declarations": [
    "UpperTheory.exists_monic_factor_lift_of_pow_mul_sub_one_pow"
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

## Lifting two monic factors across a Henselian ideal

[Theorem ALG.1016](https://andrewodesky.com/rh/lean/UpperTheory.exists_monic_factor_lift_of_pow_mul_sub_one_pow/)

Let $A$ be a commutative ring and $I\subset A$ an ideal such that $(A,I)$ is a Henselian pair. If a monic polynomial $g\in A[T]$ satisfies $$\bar g=T^n(T-1)^m\quad\text{in }(A/I)[T]\qquad(n,m\ge0),$$ there are monic polynomials $P,Q\in A[T]$ with $$g=PQ,\qquad\bar P=T^n,\qquad\bar Q=(T-1)^m.$$
