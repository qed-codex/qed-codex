---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleHomotopyInvarianceAbsIntClosedLocalDomainStatement.lean",
  "declarations": [
    "GlobalTheory.T.etaleHomotopyInvariance_absIntClosedLocalDomain"
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

## Etale affine-line invariance over an absolutely integrally closed local domain

[Theorem AG.0554](https://andrewodesky.com/rh/lean/GlobalTheory.T.etaleHomotopyInvariance_absIntClosedLocalDomain/)

Let $T$ be a commutative local domain in which every monic polynomial of positive degree has a root. Let $q\ge1$ be an integer invertible in $T$. For every $i,n\in\mathbb Z$, the projection $\pi:\operatorname{Spec}T[t]\to\operatorname{Spec}T$ induces an isomorphism $$\pi^*:H^n_{\mathrm{et}}(\operatorname{Spec}T,\mathbb Z/q\mathbb Z(i))\xrightarrow{\sim} H^n_{\mathrm{et}}(\operatorname{Spec}T[t],\mathbb Z/q\mathbb Z(i)).$$
