---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BoundOfNatDegree.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.LinRec.recBound"
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

## An exponential bound for a linear recurrence

[Theorem ALG.1268](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.LinRec.recBound/)

Let $p\in\mathbb C[T]$ be monic and let $\kappa\in\mathbb R$ satisfy $|z|<e^\kappa$ for every root $z$ of $p$. Write $d=\deg p$. There is $C\ge0$, depending only on $p$ and $\kappa$, such that whenever $M\ge0$ and $u:\mathbb N\to\mathbb C$ satisfy $$\sum_{j=0}^d p_j u(i+j)=0\quad(i\ge0),\qquad |u(j)|\le M\quad(0\le j<d),$$ where $p_j$ is the coefficient of $T^j$, one has $$|u(i)|\le C e^{\kappa i}M\qquad(i\ge0).$$
