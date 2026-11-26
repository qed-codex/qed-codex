---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CentralEigenThetaIsFockVectorBoundedDegree.lean",
  "declarations": [
    "GlobalTheory.SeeSaw.CenFockPf.cenFock"
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

## Finite polynomial degree for a prescribed central theta eigenfunction

[Theorem THETA.0785](https://andrewodesky.com/rh/lean/GlobalTheory.SeeSaw.CenFockPf.cenFock/)

Fix the source's full CM unitary arithmetic datum, an additive adelic character $\psi$ and compatible infinite embeddings $\theta$. Let $S,T$ be based Hermitian spaces with the definite-space and Weil-kernel data specified in the conventions. Write $\omega$ for the Weil action and $f_0$ for its specified vacuum. For any function $\chi:U(S)(\mathbb A)\to\mathbb C$, there is a finite-dimensional subspace $W$ of the polynomial algebra in variables indexed by an infinite place and a pair of basis indices of $T,S$ with the following property.

If $f$ is a theta function in the oriented Heisenberg model of ([Uniform approximation of a theta function by sums of products](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_function_orthogonal_sum_approx_finite_sums/)), is a lattice vacuum for the two chosen lattices, and satisfies $$\omega(z,1)f=\chi(z)f\qquad(z\in Z(U(S)(\mathbb A))\cap U(S)(F\otimes_{\mathbb Q}\mathbb R)),$$ then $f=P(a^+)f_0$ for some $P\in W$.
