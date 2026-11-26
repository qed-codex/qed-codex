---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockOperatorsLieRepresentationCommuteStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockOperators_lie_representation_commute"
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

## Commuting Lie actions in a polynomial oscillator model

[Theorem REP.0962](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockOperators_lie_representation_commute/)

Let $p,q,r,s\ge0$, put $I=\{1,\ldots,p\}\sqcup\{1,\ldots,q\}$ and $J=\{1,\ldots,r\}\sqcup\{1,\ldots,s\}$, with the indicated two blocks, and use the polynomial ring $\mathcal P=\mathbb C[X_{ij}:(i,j)\in I\times J]$. An index $u=(i,j)$ is positive when $i,j$ lie in blocks of the same sign. Define operators on $\mathcal P$ by $$a_u=\begin{cases}\partial_u,&u\text{ positive},\\X_u,&u\text{ negative},\end{cases}\qquad b_u=\begin{cases}X_u,&u\text{ positive},\\-\partial_u,&u\text{ negative},\end{cases}$$ where $X_u$ denotes multiplication. Put $$\omega(Y)=\sum_{u,v\in I\times J}Y_{uv}\left(b_ua_v+\frac12\delta_{uv}\operatorname{id}\right),\quad A(Y)=\omega(Y\otimes I_J),\quad B(Z)=\omega(I_I\otimes Z).$$ Then $\omega$, $A$, and $B$ preserve Lie brackets: $$\omega([Y,Y'])=[\omega(Y),\omega(Y')],\quad A([Y,Y'])=[A(Y),A(Y')],\quad B([Z,Z'])=[B(Z),B(Z')].$$ Their two factor actions commute: $$A(Y)B(Z)=B(Z)A(Y)\qquad(Y\in M_I(\mathbb C),\ Z\in M_J(\mathbb C)).$$
