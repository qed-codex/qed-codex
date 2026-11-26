---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AlgebraicMorseExistsSectionAmpleSubGenerated.lean",
  "declarations": [
    "GlobalTheory.exists_sec_of_ample_sub_generated"
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

## A nonzero section from an intersection inequality

[Theorem AG.0419](https://andrewodesky.com/rh/lean/GlobalTheory.exists_sec_of_ample_sub_generated/)

Let $k$ be an infinite field and $X$ an integral projective $k$-scheme. Let $d\in\mathbb N$ with $\dim X\le d+1$. Let $L,B,M$ be line bundles with $L$ ample, $B$ ample or globally generated, and $[L]=[M]+[B]$ in $\operatorname{Pic}(X)$. If $$(d+1)(B\cdot L^d)<L^{d+1},$$ then $H^0(X,M^{\otimes r})\ne0$ for some integer $r\ge1$.
