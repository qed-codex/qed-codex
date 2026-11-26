---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/FirstEmbeddingOne.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.W.wordFusion_list"
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

## Products preserving RTT and shifted determinant identities

[Theorem ALG.1029](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.W.wordFusion_list/)

Let $R$ be a commutative ring, $B$ an $R$-algebra which may be noncommutative, and let $(M^{(1)},q_1),\ldots,(M^{(s)},q_s)$ be a finite ordered list, with $M^{(j)}:R\to M_2(B)$ and $q_j:R\to R$. Put $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, and let $P$ be the $4\times4$ permutation matrix interchanging the two indices in $\{1,2\}^2$. For $A\in M_2(B)$ set $$A^{[1]}_{(i,k),(j,l)}=A_{ij}\delta_{kl},\qquad A^{[2]}_{(i,k),(j,l)}=\delta_{ij}A_{kl}.$$ Suppose each pair $M=M^{(j)}$, $q=q_j$ satisfies, for every $Y,Y'\in R$, $$((Y'-Y)I_4-P)M(Y')^{[1]}M(Y)^{[2]}=M(Y)^{[2]}M(Y')^{[1]}((Y'-Y)I_4-P),$$ $$M(Y+1)^tJM(Y)=q(Y)J,\qquad M(Y)JM(Y+1)^t=q(Y)J.$$ Assume every entry of $M^{(i)}(Y)$ commutes with every entry of $M^{(j)}(Y')$ whenever $i<j$, for every $Y,Y'$. Then $$M(Y)=M^{(1)}(Y)\cdots M^{(s)}(Y),\qquad q(Y)=\prod_{j=1}^sq_j(Y)$$ satisfy the same three identities.
