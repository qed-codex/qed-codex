---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LineBundleIsoOfGenericIsoNormalLocalBase.lean",
  "declarations": [
    "GlobalTheory.lbIso_of_generic_normal_local"
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

## Line bundle isomorphism detected on the generic fibre

[Theorem AG.0840](https://andrewodesky.com/rh/lean/GlobalTheory.lbIso_of_generic_normal_local/)

Let $R$ be a normal Noetherian local domain with fraction field $K$. Let $p:X\to\operatorname{Spec}R$ be smooth, quasicompact and geometrically integral, and suppose $p$ has a section $e:\operatorname{Spec}R\to X$. Put $X_K=X\times_R\operatorname{Spec}K$. For line bundles $L,M$ on $X$, $$L|_{X_K}\simeq M|_{X_K}\quad\Longrightarrow\quad L\simeq M.$$
