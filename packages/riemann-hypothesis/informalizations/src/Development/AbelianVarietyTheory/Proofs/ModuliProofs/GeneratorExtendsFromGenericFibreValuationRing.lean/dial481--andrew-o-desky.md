---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/GeneratorExtendsFromGenericFibreValuationRing.lean",
  "declarations": [
    "GlobalTheory.ValGenExtend.triv_of_triv_generic"
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

## Generic triviality of a line bundle over a valuation ring

[Theorem AG.1618](https://andrewodesky.com/rh/lean/GlobalTheory.ValGenExtend.triv_of_triv_generic/)

Let $O$ be a valuation domain of Krull dimension at most one whose fraction field $K$ is algebraically closed. Let $f:X\to\operatorname{Spec}O$ be smooth, quasicompact and geometrically integral, and let $$X_K=X\times_{\operatorname{Spec}O}\operatorname{Spec}K,\qquad j:X_K\to X.$$ For every line bundle $M$ on $X$, $$j^*M\simeq\mathcal O_{X_K}\quad\Longrightarrow\quad M\simeq\mathcal O_X.$$
