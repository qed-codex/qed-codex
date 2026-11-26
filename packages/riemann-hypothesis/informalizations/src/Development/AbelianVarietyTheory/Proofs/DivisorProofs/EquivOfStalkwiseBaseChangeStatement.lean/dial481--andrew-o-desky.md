---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EquivOfStalkwiseBaseChangeStatement.lean",
  "declarations": [
    "GlobalTheory.T.equiv_of_stalkwise_base_change"
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

## A cohomology equivalence from strictly henselian base changes

[Theorem AG.0491](https://andrewodesky.com/rh/lean/GlobalTheory.T.equiv_of_stalkwise_base_change/)

Let $R$ be a commutative ring, let $F$ be a sheaf of $R$-modules on the big étale site of schemes, and let $S$ be a scheme. Let $E,E'$ be simplicial presheaves of sets on schemes, with maps $\alpha:E\to E'$ and $p:E'\to S$, where $S$ is viewed as its constant simplicial representable presheaf. Assume that, on affine schemes, sections of $F$ commute with filtered colimits of rings. In each simplicial degree assume that both $E$ and $E'$ are represented by schemes quasi-compact and quasi-separated over $S$.

Suppose that for every ring $O$ and morphism $s:\operatorname{Spec}O\to S$ satisfying the conditions below, base change induces an isomorphism $$H^n(E'\times_S\operatorname{Spec}O,F)\longrightarrow H^n(E\times_S\operatorname{Spec}O,F)\qquad(n\in\mathbb Z).$$ Then $\alpha^*:H^n(E',F)\to H^n(E,F)$ is an isomorphism for every $n\in\mathbb Z$.
