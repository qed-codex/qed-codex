---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ContConeOfQcqsAffineStatement.lean",
  "declarations": [
    "GlobalTheory.T.contCone_of_isLimit_of_qcqs_affine_transitions"
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

## Etale cohomology along inverse limits with affine transition maps

[Theorem AG.0282](https://andrewodesky.com/rh/lean/GlobalTheory.T.contCone_of_isLimit_of_qcqs_affine_transitions/)

Let $R$ be a commutative ring and $\mathcal F$ a sheaf of $R$-modules on the etale site of schemes. Suppose its functor $A\mapsto\mathcal F(\operatorname{Spec}A)$ preserves filtered colimits of commutative rings. Let $(X_i)_{i\in I}$ be a diagram indexed by a small cofiltered category, with each $X_i$ quasicompact and quasiseparated and every transition morphism affine. Suppose $X=\varprojlim_i X_i$ exists, with projections $\pi_i$. For every $n\in\mathbb Z$:

1. Every $x\in H^n_{\mathrm{et}}(X,\mathcal F)$ equals $\pi_i^*y$ for some $i$ and $y\in H^n_{\mathrm{et}}(X_i,\mathcal F)$.
2. If $\pi_i^*y=0$, there are $k$ and a transition arrow $f:k\to i$ for which $f^*y=0$.
