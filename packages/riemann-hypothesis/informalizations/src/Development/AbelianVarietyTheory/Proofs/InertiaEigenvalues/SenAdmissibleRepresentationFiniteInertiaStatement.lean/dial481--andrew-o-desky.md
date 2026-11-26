---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SenAdmissibleRepresentationFiniteInertiaStatement.lean",
  "declarations": [
    "GlobalTheory.T.sen_admissible_representation_finite_inertia"
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

## Finite inertia from a trivialization over the completed algebraic closure

[Theorem PHT.1365](https://andrewodesky.com/rh/lean/GlobalTheory.T.sen_admissible_representation_finite_inertia/)

Let $\ell$ be prime, let $K\subseteq\overline{\mathbb Q}_\ell$ be a finite extension of $\mathbb Q_\ell$, let $I$ be a finite set, and let $\rho:G_K\to\operatorname{GL}_I(\mathbb Q_\ell)$ be continuous in every matrix entry. Let $\mathbb C_\ell$ be the completion of $\overline{\mathbb Q}_\ell$ with its natural Galois action. Suppose there is $M\in\operatorname{GL}_I(\mathbb C_\ell)$ such that $$\rho(g)\,g(M)=M\qquad(g\in G_K).$$ Then $\rho(I_K)$ is a finite set, where $I_K$ is the inertia subgroup of $G_K$.
