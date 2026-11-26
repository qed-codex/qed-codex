---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyFieldEqGaloisCohomologyStatement.lean",
  "declarations": [
    "GlobalTheory.T.etaleCohomology_field_eq_galoisCohomology"
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

## Étale cohomology of a field and Galois cohomology

[Theorem GC.1311](https://andrewodesky.com/rh/lean/GlobalTheory.T.etaleCohomology_field_eq_galoisCohomology/)

Let $q\ge1$, let $K$ be a field with $q\in K^\times$, and let $\Omega$ be a separable closure of $K$. Put $G=\operatorname{Gal}(\Omega/K)$. Let $i,n\ge0$, let $\zeta\in\Omega$ be a primitive $q$-th root of unity, and let $M$ be a discrete $\mathbb Z/q\mathbb Z$-representation of $G$ with a basis consisting of one vector $b$. Assume that for every $\sigma\in G$ and every integer $a\ge0$, $$\sigma\zeta=\zeta^a\quad\Longrightarrow\quad\sigma b=(a\bmod q)^i b.$$ There is an isomorphism of additive groups $$H^n_{\mathrm{\acute et}}(\operatorname{Spec}K,\mathbb Z/q\mathbb Z(i))\simeq H^n_{\mathrm{cont}}(G,M).$$
