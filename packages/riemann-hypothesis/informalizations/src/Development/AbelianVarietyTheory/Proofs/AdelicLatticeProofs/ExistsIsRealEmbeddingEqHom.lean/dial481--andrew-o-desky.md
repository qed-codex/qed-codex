---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ExistsIsRealEmbeddingEqHom.lean",
  "declarations": [
    "GlobalTheory.CNorm.hasseNorm"
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

## Local norms in a cyclic extension are global norms

[Theorem ANT.0276](https://andrewodesky.com/rh/lean/GlobalTheory.CNorm.hasseNorm/)

Let $L/K$ be a cyclic Galois extension of number fields and $a\in K^\times$. Suppose that for every finite or infinite place $v$ of $K$ there is $z_v\in K_v\otimes_K L$ with $$N_{(K_v\otimes_K L)/K_v}(z_v)=a.$$ Then there is $x\in L$ with $N_{L/K}(x)=a$.
