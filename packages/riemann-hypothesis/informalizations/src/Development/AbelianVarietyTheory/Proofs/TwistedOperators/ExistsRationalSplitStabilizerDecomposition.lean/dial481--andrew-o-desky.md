---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRationalSplitStabilizerDecomposition.lean",
  "declarations": [
    "GlobalTheory.RatSplitLat.exists_rat_split_lat"
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

## Decomposition into rational finite part, split support and a lattice stabilizer

[Theorem ANT.0819](https://andrewodesky.com/rh/lean/GlobalTheory.RatSplitLat.exists_rat_split_lat/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM extension $E/F$, and let $V$ be a Hermitian space of rank $n$ with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Let $B\in\operatorname{GL}_n(E)$, and put $L=B\mathcal O_E^n$. For every integer $N>0$ and $g\in U(V)(\mathbb A)$ with infinite component one, there exist $r,s,k$ with infinite component one such that $$g=rsk.$$ The finite component of $r$ equals that of a rational point of $U(V)(F)$. The finite component of $s$ equals one outside a finite set of places of $F$ splitting in $E$ and not dividing $N$. Finally, $$x\in\widehat L\quad\Longleftrightarrow\quad k_fx\in\widehat L$$ for every finite adelic vector $x$.
