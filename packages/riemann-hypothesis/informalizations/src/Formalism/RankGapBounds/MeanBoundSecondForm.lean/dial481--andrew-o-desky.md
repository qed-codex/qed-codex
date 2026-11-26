---
{
  "module": "src/Formalism/RankGapBounds/MeanBoundSecondForm.lean",
  "declarations": [
    "Formalism.RankGapBounds.WeightedMeanData.Data.DIV"
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

## Target slope and map-height condition

[Definition / hypothesis ARAK.D237](https://andrewodesky.com/rh/lean/Formalism.RankGapBounds.WeightedMeanData.Data.DIV/)

Let $U$ be a set and, for each $u\in U$, let $W_u$ be a set. Let $T$ be a finite set and $m\ge0$ an integer. Let $x,\varepsilon,a,\Lambda,B_0,N_c,\gamma,v,\ell_1,c_D,e_D$ be real numbers, let $a_t$ be a real number for each $t\in T$, and let $\mu_u,F_u,h_{u,z},T_{u,z}$ be real numbers for $u\in U$ and $z\in W_u$. Put $$\phi(y)=y\log y-y,\qquad\lambda=\gamma+\log(\pi/v)-\ell_1.$$ The target slope and map-height condition is the inequality $$\mu_u+h_{u,z}-F_u\le\sum_{t\in T}\left[m\{\phi(a_t)-a_t\lambda\}-a_t\log T_{u,z}\right]+c_D|T|a\Lambda+c_Dm(B_0+N_c)x^{e_D\varepsilon}$$ for every $u\in U$ and $z\in W_u$.
