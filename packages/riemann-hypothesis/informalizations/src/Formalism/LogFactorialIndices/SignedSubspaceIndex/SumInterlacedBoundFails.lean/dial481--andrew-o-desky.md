---
{
  "module": "src/Formalism/LogFactorialIndices/SignedSubspaceIndex/SumInterlacedBoundFails.lean",
  "declarations": [
    "Formalism.LatticeIndexTer.sumInterlacedBound"
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

## Cancellation for interlacing weights

[Theorem ALG.0121](https://andrewodesky.com/rh/s/interlacing-cancellation.html)

Put $\phi(t)=t\log t-t$ for $t>0$ and $\phi(0)=0$. Let $k\ge0$ be an integer and $S$ a real number. Let real numbers $c_i$ satisfy $0\le c_i\le S$ for $0\le i\le k$. Let real numbers $c'_i$ satisfy $c_i\ge c'_i\ge c_{i+1}$ for $0\le i<k$. For every $w\ge1$, $$\left|\sum_{i=0}^{k}\phi(w+c_i)-\sum_{i=0}^{k-1}\phi(w+c'_i)\right|\le(w+2S)\log(w+S+2).$$
