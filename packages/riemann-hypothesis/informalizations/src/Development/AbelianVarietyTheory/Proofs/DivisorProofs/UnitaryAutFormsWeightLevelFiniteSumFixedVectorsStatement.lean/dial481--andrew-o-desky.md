---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryAutFormsWeightLevelFiniteSumFixedVectorsStatement.lean",
  "declarations": [
    "GlobalTheory.T.unitaryAutForms_weight_level_finite_sum_fixed_vectors"
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

## Finite decomposition of unitary automorphic forms at fixed weight and level

[Theorem AGR.1665](https://andrewodesky.com/rh/lean/GlobalTheory.T.unitaryAutForms_weight_level_finite_sum_fixed_vectors/)

Let $E$ be a CM number field, $F=E^+$, and assume $E/F$ is unramified at every finite prime. Let $n\ge1$, and let $U$ be the definite unitary group of the identity Hermitian form on $E^n$. Choose a set $S$ of primes of $E$ containing exactly one prime above each finite prime of $F$. Prescribe a dominant integral weight $\lambda_v$ at every infinite place $v$ of $E$. At each finite prime $w$ of $E$, choose an open subgroup $K'_w$ of the standard integral subgroup $K_w$ of $U(F_{w|F})$, with $K'_w=K_w$ for all but finitely many $w$; at a split prime use the identification $U(F_{w|F})=\mathrm{GL}_n(E_w)$. Let $K$ be the finite adelic subgroup defined by the conditions $K'_w$ for $w\in S$.

For every irreducible automorphic subspace $\pi\subseteq\{\text{complex functions on }U(\mathbb A_F)\}$ of weight $\lambda=(\lambda_v)$, write $\pi^K$ for its fixed-vector space. Set $\mathcal A_{\lambda,K}=\sum_\pi\pi^K$, where the sum is over these subspaces. Then $\mathcal A_{\lambda,K}$ is finite-dimensional, and there exist finitely many such subspaces $\pi_1,\ldots,\pi_r$, each with $\pi_i^K\ne0$, such that $$\mathcal A_{\lambda,K}=\bigoplus_{i=1}^r\pi_i^K.$$ For every other such $\pi_0$ with $\pi_0^K\ne0$, there exists $i$ such that, at every finite prime $w$, each smooth irreducible local component of $\pi_0$ at $w$ also occurs as a local component of $\pi_i$ at $w$.
