---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CharpolyOfDiagWith.lean",
  "declarations": [
    "GlobalTheory.SenLines.eigWith_of_diagWith"
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

## Specializing the eigenvalue multiset of a diagonalizable operator

[Theorem ALG.1086](https://andrewodesky.com/rh/lean/GlobalTheory.SenLines.eigWith_of_diagWith/)

Let $O$ be a commutative ring, $F,k$ fields with $O$-algebra structures, and assume $O\to F$ is injective. Let $Q$ be a finite free $O$-module, $f\in\operatorname{End}_O(Q)$, and $S$ a finite multiset in $O$. Suppose $f_F$ has an eigenbasis over $F$ whose eigenvalues, counted with multiplicity, are the images of $S$. Then $Q\otimes_O k$ is finite-dimensional and $$\det(T-f_k)=\prod_{s\in S}(T-\bar s)\quad\text{in }k[T],$$ where $f_F,f_k$ are the scalar extensions and $\bar s$ is the image of $s$ in $k$.
