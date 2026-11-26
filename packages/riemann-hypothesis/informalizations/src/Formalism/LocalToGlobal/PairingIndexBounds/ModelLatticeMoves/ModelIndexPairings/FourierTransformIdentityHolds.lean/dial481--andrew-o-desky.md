---
{
  "module": "src/Formalism/LocalToGlobal/PairingIndexBounds/ModelLatticeMoves/ModelIndexPairings/FourierTransformIdentityHolds.lean",
  "declarations": [
    "Formalism.L2.PairingIndexBounds.Mv.model_moves_hold"
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

## A finite translation and character-sum identity

[Theorem ALG.0915](https://andrewodesky.com/rh/lean/Formalism.L2.PairingIndexBounds.Mv.model_moves_hold/)

Let $k$ be a field, $A,B$ abelian groups, and $c:B\times A\to k^\times$ multiplicative in each additive variable. Let $A_1,A_2\subseteq A$ and $B_1,B_2\subseteq B$ be subgroups satisfying $$B_1=\{b:c(b,a)=1\text{ for all }a\in A_1\},\qquad c(B_2,A_2)=1,$$ $$a\in A_1,\quad c(B_2,a)=1\quad\Longrightarrow\quad a\in A_2.$$ Let $S_A\subseteq A_2$ and $S_B\subseteq B_2$ be finite complete representative sets modulo $A_1$ and $B_1$, respectively. If $1_C$ denotes the $k$-valued indicator of a subset $C\subseteq A$, then for every $t\in A$, $$\sum_{a\in S_A}\sum_{b\in S_B}c(b,t+a)1_{A_1}(t+a)=|S_B|\,1_{A_2}(t).$$
