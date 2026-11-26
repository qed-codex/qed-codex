---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/GrpObjOfDenseFibres.lean",
  "declarations": [
    "GlobalTheory.grpObj_of_dense_fibres"
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

## An abelian-scheme group law from a dense set of fibres

[Theorem AG.1013](https://andrewodesky.com/rh/lean/GlobalTheory.grpObj_of_dense_fibres/)

Let $R$ be a reduced commutative ring, and let $Z\to\operatorname{Spec}R$ be smooth, proper, and geometrically connected. Suppose morphisms $$m:Z\times_RZ\to Z,\qquad i:Z\to Z,\qquad e:\operatorname{Spec}R\to Z$$ are given. Assume there is a dense set $S\subseteq\operatorname{Spec}R$ such that, for every $p\in S$, there are a field $K$, a map $x:\operatorname{Spec}K\to\operatorname{Spec}R$ with image containing $p$, and a commutative group scheme $A/K$ identified with $Z\times_RK$, under which the multiplication, inverse, and identity are the pullbacks of $m,i,e$.

Then $Z$ admits a group-scheme structure with exactly these three operations, and is an abelian scheme. Moreover, for every scheme $S'\to\operatorname{Spec}R$, every group scheme $A/S'$, and every cartesian map $\varphi:A\to Z$ over this base map which is compatible with multiplication, $\varphi$ is compatible with the full group structure and identifies $A$ with the group-scheme pullback of $Z$.
