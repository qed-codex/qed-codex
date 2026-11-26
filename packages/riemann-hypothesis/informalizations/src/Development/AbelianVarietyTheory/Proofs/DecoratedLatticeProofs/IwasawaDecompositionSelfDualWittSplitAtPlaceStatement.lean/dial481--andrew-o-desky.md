---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IwasawaDecompositionSelfDualWittSplitAtPlaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.iwasawa_decomposition_selfDual_wittSplit_at_place"
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

## A local Iwasawa decomposition for a self-dual Witt-split lattice

[Theorem REP.0223](https://andrewodesky.com/rh/lean/GlobalTheory.T.iwasawa_decomposition_selfDual_wittSplit_at_place/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM extension $E/F$. Let $S,S_0$ be Hermitian spaces with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Choose a Hermitian Witt decomposition $S=S_0\perp\mathbb H^\rho$, with the ordered isotropic bases of the hyperbolic part fixed. Let $L\subset S$, $L_0\subset S_0$ be full self-dual $\mathcal O_E$-lattices. Let $v$ be a finite place of the base field satisfying the local condition below. Suppose the completed lattice at $v$ decomposes along the individual hyperbolic coordinate lines and $L_{0,v}$: a vector belongs to $L_v$ exactly when each of its hyperbolic coordinate projections belongs to $L_v$ and its $S_0$-projection belongs to $L_{0,v}$.

Every adelic unitary element $h$ supported at $v$ has a decomposition $$h=n\,m(t)\,\iota(\gamma)\,\kappa,$$ where $n$ is in the unipotent group of the fixed isotropic flag and supported at $v$, $t\in\operatorname{GL}_\rho(E\otimes_F\mathbb A_F)$ is diagonal with its Levi image $m(t)$ supported at $v$, $\gamma\in U(S_0)(\mathbb A_F)$ is supported at $v$, and $\kappa$ is supported at $v$ and preserves $L_v$.
