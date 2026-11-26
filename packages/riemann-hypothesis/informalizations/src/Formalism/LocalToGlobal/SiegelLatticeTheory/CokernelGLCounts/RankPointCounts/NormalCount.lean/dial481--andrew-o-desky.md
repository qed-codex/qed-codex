---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/NormalCount.lean",
  "declarations": [
    "Formalism.L2.SG.NGCut.NormalCount.NormCountG_holds"
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

## Counting a fixed CM norm in a fractional ideal

[Theorem ANT.1304](https://andrewodesky.com/rh/lean/Formalism.L2.SG.NGCut.NormalCount.NormCountG_holds/)

Let $E$ be a CM number field, with complex conjugation $x\mapsto\bar x$. Let $J\subset E$ be a nonzero fractional ideal of $\mathcal O_E$, and let $m\in E^\times$. For every finite set $S\subset E$ such that $$x\in J,\qquad x\bar x=m\quad(x\in S),$$ one has $$|S|\,N(J)^2\le 2[E:\mathbb Q]^2\,|N_{E/\mathbb Q}(m)|,$$ where $N(J)$ is the absolute ideal norm extended multiplicatively to fractional ideals.
