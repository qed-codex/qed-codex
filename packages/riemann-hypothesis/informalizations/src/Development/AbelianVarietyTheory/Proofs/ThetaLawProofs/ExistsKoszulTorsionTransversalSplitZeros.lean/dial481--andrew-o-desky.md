---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsKoszulTorsionTransversalSplitZeros.lean",
  "declarations": [
    "GlobalTheory.KeyKa.KoszulEx.exists_kosVal"
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

## The degree and unit squared torsion of a split zero scheme

[Theorem AV.0670](https://andrewodesky.com/rh/lean/GlobalTheory.KeyKa.KoszulEx.exists_kosVal/)

Assume the source's universal polarized-abelian-scheme laws listed below. Let $R$ be a noetherian local ring, let $(A,L)$ be polarized abelian data of dimension $g\ge1$ over $R$, and fix a generating rigidification of $L$ at the identity, a section of $L$ nonzero somewhere on every fibre, and a tangent basis $v_1,\ldots,v_g$. Let $n\ge1$ and $\ell>gn$. Choose sections $s_1,\ldots,s_g$ of $L^n$, bases $b_j$ of $H^0(A,L^{\ell-jn})$ with $(\ell-jn)^g$ members for $0\le j\le g$, and arbitrary families of that size for other $j\ge0$.

Suppose their common zeros are covered by disjoint sections $z_1,\ldots,z_d:\operatorname{Spec}R\to A$, each lying in a chosen trivializing chart of $L$. Require every $s_i$ to vanish on each $z_a$, the determinant of their derivatives along $(v_i)$ in that chart to be a unit, and the images of the $z_a$ to be disjoint on every base point. Then $$d=g!n^g.$$ Moreover the augmented Koszul matrix $D$, formed from multiplication by the $s_i$ in the bases $b_j$ and the evaluation matrix at the $z_a$, admits squared torsion in $R^\times$ in the sense below.
