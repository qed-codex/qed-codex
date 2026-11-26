---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/NcardEqIffStabilizer.lean",
  "declarations": [
    "GlobalTheory.FieldSize.RaySplit.ncard_eq_finrank_iff"
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

## Complete splitting in a ray-class extension

[Theorem ANT.1550](https://andrewodesky.com/rh/lean/GlobalTheory.FieldSize.RaySplit.ncard_eq_finrank_iff/)

Let $K$ be a totally complex number field and $R/K$ an abelian Galois extension of number fields. Let $n>0$ and assume the ray-class conditions in the conventions below for the modulus $n\mathcal O_K$. For every nonzero prime $\mathfrak p\subseteq\mathcal O_K$ with $n\notin\mathfrak p$, $$\#\{\mathfrak P\subseteq\mathcal O_R:\mathfrak P\cap\mathcal O_K=\mathfrak p\}=[R:K] \quad\Longleftrightarrow\quad \exists\pi\in\mathcal O_K:\ \mathfrak p=(\pi),\ \pi\equiv1\pmod{n\mathcal O_K}.$$ The primes counted on the left are nonzero prime ideals.
