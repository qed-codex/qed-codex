---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/AlgWitt.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.NcS.IntWittAlg.algWitt"
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

## An integral isometry between orthogonal frames

[Theorem ALG.0767](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.NcS.IntWittAlg.algWitt/)

Let $S$ be a commutative ring with an involutive ring endomorphism $\sigma$, and let $O\subseteq S$ be a subring stable under $\sigma$. Let $J,J'\in M_n(O)$ satisfy $\sigma(J)^t=J$ and $J'J=1$, and put $$h(v,w)=\sigma(v)^tJw.$$ Let $\beta_i,\beta'_i\in O$ for $1\le i\le a$ satisfy $\beta_i\beta'_i=1$. Assume that for every $i$ and every $t\in O$ there exist $\lambda,c\in O$ such that $$\lambda\sigma(\lambda)=1,\qquad(\beta_i-\sigma(\lambda)t)c=1.$$ If vectors $x_i,y_i\in O^n$ satisfy $$h(x_i,x_j)=h(y_i,y_j)=\begin{cases}\beta_i,&i=j,\\0,&i\ne j,\end{cases}$$ then there is $g\in\operatorname{GL}_n(S)$ such that $$\sigma(g)^tJg=J,\qquad g,g^{-1}\in M_n(O),\qquad gy_i=x_i\quad(1\le i\le a).$$
