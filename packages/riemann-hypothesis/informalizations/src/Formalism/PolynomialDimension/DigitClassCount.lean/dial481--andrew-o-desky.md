---
{
  "module": "src/Formalism/PolynomialDimension/DigitClassCount.lean",
  "declarations": [
    "Formalism.CountingSumsFrames.Top.densityLower"
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

## A lower bound for a sum of harmonic dimension ratios

[Theorem REP.0647](https://andrewodesky.com/rh/lean/Formalism.CountingSumsFrames.Top.densityLower/)

For integers $k,a,b\ge0$ put $$P_k(a)=\binom{a+k}{k},\qquad H_k(a,b)=P_k(a)P_k(b)-\begin{cases}0,&a=0\text{ or }b=0,\\P_k(a-1)P_k(b-1),&a,b>0.\end{cases}$$ Let $k\ge5$, $a>0$, $b\ge0$, and let $L,B\in\mathbb R$ satisfy $L\ge0$ and $B>0$. Set $J=\lfloor LB/(k+1)\rfloor+1$. If $b+J+k+1\le2B$, then $$\left(1-\frac{kLB}{(k+1)a}\right)(1-e^{-L/3})\le\sum_{j=0}^{J-1}\frac{H_k(a,b)}{P_k(a+j)P_k(b+j)}.$$
