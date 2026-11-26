---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/FFInertBHolds.lean",
  "declarations": [
    "PI.OmVe.Top.fFInertB_holds"
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

## Counting independent tuples with a corank-one Hermitian Gram matrix

[Theorem ANT.0964](https://andrewodesky.com/rh/lean/PI.OmVe.Top.fFInertB_holds/)

Let $k$ be a finite field with $q$ elements, let $K/k$ be a quadratic field extension, and let $\sigma$ be its nontrivial $k$-automorphism, with $\sigma^2=1$. Let $0\le a\le M$, and let $J\in M_M(K)$ be nonsingular and $\sigma$-Hermitian. Let $T\in M_a(K)$ be $\sigma$-Hermitian and suppose there is $i_0$ such that $$T_{i_0j}=T_{ji_0}=0\quad\text{for every }j,\qquad\det(T+E_{i_0i_0})\ne0.$$ The number of linearly independent tuples $x_1,\ldots,x_a\in K^M$ satisfying $$\bigl(\sigma(x_i)^tJx_j\bigr)_{i,j}=T$$ is $$q^{2Ma-a^2}\prod_{j=M-a}^{M}\left(1-(-1)^jq^{-j}\right).$$
