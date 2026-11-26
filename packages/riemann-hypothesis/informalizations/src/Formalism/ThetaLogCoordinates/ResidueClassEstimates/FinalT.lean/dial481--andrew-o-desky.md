---
{
  "module": "src/Formalism/ThetaLogCoordinates/ResidueClassEstimates/FinalT.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.BranchingDimensions.Top.lemma_t_one"
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

## A bound for the final Weyl dimension along a branching path

[Theorem REP.0864](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.BranchingDimensions.Top.lemma_t_one/)

Choose integers $r,K,N\ge0$, a sign $\epsilon_i\in\{+,-\}$ for every $i\ge0$, and integers $B_i\ge0$. Put $k=r+K$, $n_0=N-r$, $k'=K-2N$, and $b_* =\sum_{i=1}^{n_0}B_i$. Assume the parameter conditions below. Let $\mu_0,\ldots,\mu_N\in\mathbb Z^k$ be dominant weights, with $\mu_0=0$. At a $+$ step, require $$\mu_{i-1,j}\le\mu_{i,j},\qquad \mu_{i,j+1}\le\mu_{i-1,j};$$ at a $-$ step, require these inequalities with $\mu_i,\mu_{i-1}$ exchanged. For $1\le i\le n_0$, the size $\sum_j\mu_{i,j}$ changes by $+B_i$ or $-B_i$ according to the sign. For $1\le h\le r$, require $\mu_{n_0+h,j}=b_*$ for $0\le j<h$. Define $$w(\mu)=\prod_{0\le i<j<K}\frac{\mu_{N,r+i}-\mu_{N,r+j}+j-i}{j-i},\qquad R=\prod_{i=1}^{n_0}\binom{B_i+k-1}{k-1}.$$ Then $$w(\mu)\le e^{9N^2\log(1+2aN)}R.$$ If $\mu$ fails the typicality conditions below, then also $$w(\mu)\le\exp\left(9N^2\log(1+2aN)-\min\left\{\frac{\Lambda k'}{16k},\frac{k'}{12}\right\}\right)R.$$
