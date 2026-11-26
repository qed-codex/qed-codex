---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FiniteInertiaImpliesPotSemistableProofStatement.lean",
  "declarations": [
    "GlobalTheory.T.finiteInertiaImpliesPotSemistable_proof"
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

## Semistable periods after finite extension for finite inertia

[Theorem PHT.1578](https://andrewodesky.com/rh/lean/GlobalTheory.T.finiteInertiaImpliesPotSemistable_proof/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite in a fixed algebraic closure $\overline{\mathbb Q}_\ell$, and let $F$ be the maximal unramified extension of $\mathbb Q_\ell$ inside that closure. Choose the local period datum, integral period-ring datum and compatible identifications in ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $r\ge1$ and $\rho:G_K\to\operatorname{GL}_n(F)$ satisfy: the fixed field of $\operatorname{Frob}^r$ in $F$ is contained in $K$; every matrix entry of every $\rho(g)$ is fixed by $\operatorname{Frob}^r$; and all matrix entries are continuous as maps to $\overline{\mathbb Q}_\ell$. Suppose $\rho(I_K)$ is finite.

There are a finite extension $K'/K$ inside $\overline{\mathbb Q}_\ell$ and $Q\in\operatorname{GL}_n(B_{\mathrm{st}})$ such that $$\rho(g)\,g(Q)=Q\qquad(g\in G_{K'}),$$ where the matrix entries of $\rho$ are embedded into $B_{\mathrm{st}}$.
