---
{
  "module": "src/ReciprocityTheory/DualLattices/TransposeMulSelf.lean",
  "declarations": [
    "ReciprocityTheory.PGsh.charTable"
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

## The square of a finite character-table determinant

[Theorem ALG.0271](https://andrewodesky.com/rh/lean/ReciprocityTheory.PGsh.charTable/)

Let $K$ be a field, $G$ a finite abelian group, and $e:G\simeq\operatorname{Hom}(G,K^\times)$ a bijection of sets. Form the matrix $M=(e(h)(g))_{g,h\in G}$. Then $$(\det M)^2=|G|^{|G|}\quad\text{or}\quad(\det M)^2=-|G|^{|G|},$$ with the integers on the right interpreted in $K$.
