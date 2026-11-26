---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHomOfFieldPointRelationProper.lean",
  "declarations": [
    "GlobalTheory.FieldPointGraph.exists_hom_of_rel",
    "GlobalTheory.FieldPointGraph.exists_section"
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

## A section selected by field points and specialization

[Theorem AG.0980](https://andrewodesky.com/rh/lean/GlobalTheory.FieldPointGraph.exists_section/)

Let $r:W\to Q$ be a proper morphism of schemes, with $Q$ noetherian and normal. For every field $K$, let $\mathcal G_K$ be a predicate on morphisms $\operatorname{Spec}K\to W$. Suppose:

1. Every $z:\operatorname{Spec}K\to Q$ has a unique lift $c:\operatorname{Spec}K\to W$ with $\mathcal G_K(c)$ and $r\circ c=z$.
2. If $K\to K'$ is a field homomorphism and $\mathcal G_K(c)$ holds, then $\mathcal G_{K'}(c_{K'})$ holds.
3. For every valuation domain $A$ and $u:\operatorname{Spec}A\to W$, the predicate on its fraction-field point implies the predicate on its residue-field point.

There is a section $s:Q\to W$ of $r$ such that $\mathcal G_K(s\circ z)$ holds for every field $K$ and every $z:\operatorname{Spec}K\to Q$.

## A morphism determined by a relation on field-valued points

[Theorem AG.1247](https://andrewodesky.com/rh/lean/GlobalTheory.FieldPointGraph.exists_hom_of_rel/)

Let $q:Q\to S$ and $p:P\to S$ be morphisms of schemes, with $p$ proper and $Q$ noetherian and normal. For every field $K$, let $R_K$ be a relation between $Q(K)$ and $P(K)$. Assume:

1. $R_K(z,w)$ implies $q(z)=p(w)$, and for each $z\in Q(K)$ there is exactly one $w\in P(K)$ with $R_K(z,w)$.
2. For every field homomorphism $K\to K'$, $R_K(z,w)$ implies $R_{K'}(z_{K'},w_{K'})$.
3. For every valuation domain $A$ and pair $u:\operatorname{Spec}A\to Q$, $v:\operatorname{Spec}A\to P$ over $S$, the relation at their fraction-field points implies the relation at their residue-field points.

There is an $S$-morphism $h:Q\to P$ such that $R_K(z,h(z))$ for every field $K$ and $z\in Q(K)$.
