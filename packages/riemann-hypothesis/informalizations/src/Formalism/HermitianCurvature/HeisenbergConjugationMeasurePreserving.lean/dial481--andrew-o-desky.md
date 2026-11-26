---
{
  "module": "src/Formalism/HermitianCurvature/HeisenbergConjugationMeasurePreserving.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.Final.sz_eaSize"
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

## A logarithmic bound for an Euler product normalization

[Theorem ANT.1088](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.Final.sz_eaSize/)

Let $I$ be finite with $|I|=f$, let $k,r,g_1,g_2,T\ge0$ be integers, and set $m=2r+2$ and $n=k+m-1$. Fix real $v,d_F$, a sequence $V_j$, positive numbers $U_i$ for $i\in I$, and real numbers $L_j$. Assume $$v>0,\quad d_F=(2v)^f,\quad V_k>0,\quad k\ge2,\quad g_1,g_2\ge4,\quad T\ge2.$$ For every $k<j\le n$ assume $$L_j>0,\qquad |\log L_j|\le f\log\zeta(j).$$ Define $$E=\left(\prod_{j=k+1}^nL_j\right)\left(\prod_{j=k+1}^n(1-g_1^{-j})\right)^f\left(\prod_{j=k+1}^n(1-g_2^{-j})\right)^f(1-T^{-k})^{-f}.$$ Then $E>0$ and $$|\log E|\le f\frac8{2^k}.$$
