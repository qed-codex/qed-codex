---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/ExistsIsLieBasisBaseChange.lean",
  "declarations": [
    "GlobalTheory.exists_isLieBasis_baseChange"
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

## Base change of a Lie algebra basis

[Theorem AV.1473](https://andrewodesky.com/rh/lean/GlobalTheory.exists_isLieBasis_baseChange/)

Let $f:R\to R'$ be a homomorphism of commutative rings, let $G/R$ and $G'/R'$ be commutative group schemes, and let $\varphi:G'\to G$ identify $G'$ with the group-scheme pullback along $\operatorname{Spec}R'\to\operatorname{Spec}R$. Suppose $G\to\operatorname{Spec}R$ is smooth. Let $v_1,\ldots,v_n$ be a basis of $\operatorname{Lie}(G/R)$, represented as identity-based points over the dual numbers $R[\varepsilon]/(\varepsilon^2)$. There is a basis $v'_1,\ldots,v'_n$ of $\operatorname{Lie}(G'/R')$, represented over $R'[\varepsilon]/(\varepsilon^2)$, satisfying $$\varphi\circ v'_i=v_i\circ\operatorname{Spec}(f[\varepsilon])\qquad(1\le i\le n).$$ The map $f[\varepsilon]$ applies $f$ to both dual-number coefficients.
