---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/QuotGlobalHolds.lean",
  "declarations": [
    "GlobalTheory.IwLevel.quotGlobal_holds"
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

## Quotients of abelian schemes by finite flat subgroups

[Theorem AV.1602](https://andrewodesky.com/rh/lean/GlobalTheory.IwLevel.quotGlobal_holds/)

Let $S$ be a locally Noetherian scheme, $A\to S$ an abelian scheme, $H\to S$ a finite flat group scheme, and $i:H\to A$ a group-scheme homomorphism that is a monomorphism. There are an abelian scheme $B\to S$ and a finite flat surjective group-scheme homomorphism $q:A\to B$ such that $$H\times_S A\longrightarrow A\times_B A,\qquad(h,a)\longmapsto(i(h)a,a)$$ is an isomorphism. Equivalently, the square with upper arrows $(h,a)\mapsto i(h)a$ and $(h,a)\mapsto a$, and lower arrows $q,q$, is Cartesian.
