---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsPolAVFiniteTypeSubring.lean",
  "declarations": [
    "GlobalTheory.KeyTf.exists_polAV_finiteType_subring"
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

## Descent of an abelian scheme and its polarization bundle to finite type

[Theorem AV.1325](https://andrewodesky.com/rh/lean/GlobalTheory.KeyTf.exists_polAV_finiteType_subring/)

Let $S$ be a commutative local domain. Let $A/\operatorname{Spec}S$ be an abelian scheme of constant relative dimension $g$, with a rigidified symmetric relatively ample line bundle $L$ having trivial translation kernel. There are a subring $R\subset S$ finitely generated as a $\mathbb Z$-algebra, an abelian scheme $A_0/\operatorname{Spec}R$ of constant relative dimension $g$, and a rigidified symmetric relatively ample line bundle $L_0$ on $A_0$ with trivial translation kernel, together with a morphism $\varphi:A\to A_0$ inducing a group-scheme isomorphism $$A\simeq A_0\times_{\operatorname{Spec}R}\operatorname{Spec}S$$ and a line-bundle isomorphism $L\simeq\varphi^*L_0$.
