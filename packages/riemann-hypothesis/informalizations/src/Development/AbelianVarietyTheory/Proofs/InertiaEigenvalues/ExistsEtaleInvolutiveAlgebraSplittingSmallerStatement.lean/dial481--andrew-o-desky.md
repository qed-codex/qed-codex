---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsEtaleInvolutiveAlgebraSplittingSmallerStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_etaleInvolutiveAlgebraSplitting_smaller"
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

## Splitting a reduced algebra together with its scalar extension and involution

[Theorem ALG.0530](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_etaleInvolutiveAlgebraSplitting_smaller/)

Assume the normed quadratic-extension conditions below on $E/F$. Let $K$ be a nonzero finite-dimensional reduced commutative $F$-algebra which is not a field. Let $L$ be a commutative $F$-algebra supplied with compatible $K$- and $E$-algebra structures identifying $L$ with $E\otimes_FK$. Suppose $L$ has an involution fixing the image of $K$ and extending that of $E$. Give $K,L$ their finite-dimensional $F$-module topologies and Borel structures, and suppose $K$ is a locally compact topological ring.

There exist pairs $(K_1,L_1)$ and $(K_2,L_2)$ satisfying the same algebra, topology, scalar-extension, and involution conditions, and $F$-algebra isomorphisms $$K\simeq K_1\times K_2,\qquad L\simeq L_1\times L_2,$$ compatible with the maps from $K$, from $E$, and with the involutions, such that $$\dim_FK_1<\dim_FK,\qquad\dim_FK_2<\dim_FK.$$
