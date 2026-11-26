---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/DualFockLinear/FockRLinDual.lean",
  "declarations": [
    "Formalism.MainNotions.TestSideCounting.multDiv_kapFl"
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

## A prime-power bound for multinomial factorial divisibility

[Theorem ALG.0685](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TestSideCounting.multDiv_kapFl/)

Let $O$ be a commutative local ring, $p$ a prime with $p\in\mathfrak m_O$, and $n,k\ge0$. For $d_1,\ldots,d_n\in\mathbb N$, put $$\kappa=\sum_{s=1}^n k\lfloor\log_p d_s\rfloor,$$ using $\lfloor\log_p0\rfloor=0$. For every array of nonnegative integers $(\alpha_{sj})$ with $\sum_{j=1}^k\alpha_{sj}=d_s$ for all $s$, one has, in $O$, $$\prod_{s=1}^n d_s!\ \mid\ p^\kappa\prod_{s=1}^n\prod_{j=1}^k\alpha_{sj}!.$$
