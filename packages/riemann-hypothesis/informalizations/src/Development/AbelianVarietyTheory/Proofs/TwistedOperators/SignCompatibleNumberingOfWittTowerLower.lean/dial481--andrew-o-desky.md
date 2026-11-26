---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/SignCompatibleNumberingOfWittTowerLower.lean",
  "declarations": [
    "GlobalTheory.WittSign.hasSignature_of_isWittLower"
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

## Signature after adding hyperbolic planes

[Theorem ALG.0712](https://andrewodesky.com/rh/lean/GlobalTheory.WittSign.hasSignature_of_isWittLower/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$, and let $T,T'$ be Hermitian spaces with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Let $i,p,q\in\mathbb N$, and let $\tau$ belong to the selected CM type of $E$. Suppose $\dim T=\dim T'+2i$, there is an isometric embedding $T'\hookrightarrow T$, and its orthogonal complement contains an $i$-dimensional totally isotropic subspace. If the complex Hermitian form on $T'$ at $\tau$ has signature $(p,q)$, then that on $T$ at $\tau$ has signature $(p+i,q+i)$.
