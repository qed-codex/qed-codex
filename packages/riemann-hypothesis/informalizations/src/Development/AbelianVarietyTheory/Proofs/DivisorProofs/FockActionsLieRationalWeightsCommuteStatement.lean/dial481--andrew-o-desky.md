---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockActionsLieRationalWeightsCommuteStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockActions_lie_rationalWeights_commute"
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

## Commuting Lie actions with rational weights in a polynomial model

[Theorem REP.1339](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockActions_lie_rationalWeights_commute/)

Let $p,q,r,s\ge0$. Give $I=\{1,\ldots,p+q\}$ and $J=\{1,\ldots,r+s\}$ their first-positive, last-negative sign decompositions, and put $\mathcal P=\mathbb C[z_{ij}:i\in I,j\in J]$. For $l=(i,j)$, set $$a_l=\begin{cases}\partial_l&\text{the signs agree},\\z_l&\text{the signs differ},\end{cases}\qquad b_l=\begin{cases}z_l&\text{the signs agree},\\-\partial_l&\text{the signs differ}.\end{cases}$$ For a matrix $C$ indexed by $I\times J$, define $$D(C)=\sum_{l,l'}C_{ll'}\left(b_l a_{l'}+\tfrac12\delta_{ll'}\right),\qquad D_1(X)=D(X\otimes1_J),\quad D_2(Y)=D(1_I\otimes Y).$$ Both $D_1$ and $D_2$ preserve Lie brackets and they commute: $$D_1(X)D_2(Y)F=D_2(Y)D_1(X)F.$$ Furthermore $\mathcal P$ is the sum of the rational simultaneous weight subspaces for the diagonal matrix units of $D_1$, and also the sum of those for $D_2$. A weight subspace of weight $\mu\in\mathbb Q^I$ consists of $F$ with $D_1(E_{ii})F=\mu_iF$ for all $i$, and the second definition uses $\mathbb Q^J$.
