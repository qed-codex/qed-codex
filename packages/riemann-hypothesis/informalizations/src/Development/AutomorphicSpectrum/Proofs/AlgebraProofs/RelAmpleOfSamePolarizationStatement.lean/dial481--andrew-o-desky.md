---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/RelAmpleOfSamePolarizationStatement.lean",
  "declarations": [
    "GlobalTheory.T.rel_ample_of_same_polarization"
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

## Ampleness for line bundles with the same polarization map

[Theorem AV.1372](https://andrewodesky.com/rh/lean/GlobalTheory.T.rel_ample_of_same_polarization/)

Let $K$ be an algebraically closed field and $A/K$ an abelian scheme. Let $M,L$ be line bundles on $A$. Assume $L$ is relatively ample and that its translation kernel is trivial: for every affine $K$-scheme $T$ and every $x\in A(T)$, local triviality over $T$ of $t_x^*L\otimes L^{-1}$ on $T\times_K A$ implies $x=0$.

For a line bundle $N$, write $$\lambda_N=m^*N\otimes p_1^*N^{-1}\otimes p_2^*N^{-1}\otimes0^*N\quad\text{in }\operatorname{Pic}(A\times_K A),$$ where $m$ is addition, $p_1,p_2$ are the projections, and $0$ is the constant identity map. If $\lambda_M=\lambda_L$, then $M$ is relatively ample.
