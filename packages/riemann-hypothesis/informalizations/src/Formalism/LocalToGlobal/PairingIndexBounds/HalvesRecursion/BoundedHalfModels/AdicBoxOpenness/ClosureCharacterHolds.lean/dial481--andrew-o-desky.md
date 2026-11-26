---
{
  "module": "src/Formalism/LocalToGlobal/PairingIndexBounds/HalvesRecursion/BoundedHalfModels/AdicBoxOpenness/ClosureCharacterHolds.lean",
  "declarations": [
    "Formalism.L2.PairingIndexBounds.Rec.closure_character_holds"
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

## A local closure criterion for an integral submodule

[Theorem ALG.0887](https://andrewodesky.com/rh/lean/Formalism.L2.PairingIndexBounds.Rec.closure_character_holds/)

Let $R$ be a Dedekind domain with fraction field $K$, let $\mathfrak p$ be a nonzero prime ideal, and let $I,J$ be finite sets. Let $M\subseteq\operatorname{Mat}_{I\times J}(K)$ be an $R$-submodule. Suppose some $0\ne d\in R$ satisfies $d\operatorname{Mat}_{I\times J}(R)\subseteq M$. For $y\in\operatorname{Mat}_{I\times J}(K)$, $$y\in\overline{M}^{\,\mathfrak p}\quad\Longleftrightarrow\quad \exists s\in R\setminus\mathfrak p:\ sy\in M.$$
