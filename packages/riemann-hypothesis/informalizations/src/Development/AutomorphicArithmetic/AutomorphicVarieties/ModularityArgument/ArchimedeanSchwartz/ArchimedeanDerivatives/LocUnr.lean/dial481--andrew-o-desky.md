---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ArchimedeanSchwartz/ArchimedeanDerivatives/LocUnr.lean",
  "declarations": [
    "UpperTheory.V.Z.Inf.locUnr"
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

## Standard local factors from unramified Satake parameters

[Theorem AGR.0231](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Inf.locUnr/)

Let $K$ be a number field, $v$ a finite place with residue cardinality $q$, and $n\ge1$. Let $\pi$ be an irreducible admissible complex representation of $\operatorname{GL}_n(K_v)$ with nonzero $\operatorname{GL}_n(\mathcal O_v)$-invariants. If $z_1,\ldots,z_n\in\mathbb C^\times$ are its Satake parameters in the normalized spherical-Hecke convention specified below, then, for every $s\in\mathbb C$, $$L(s,\pi)=\prod_{i=1}^n(1-z_iq^{-s})^{-1},\qquad L(s,\pi^\vee)=\prod_{i=1}^n(1-z_i^{-1}q^{-s})^{-1}.$$
