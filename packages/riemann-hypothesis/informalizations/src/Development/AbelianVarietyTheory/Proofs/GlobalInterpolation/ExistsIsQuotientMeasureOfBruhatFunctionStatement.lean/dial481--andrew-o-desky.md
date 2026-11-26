---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsIsQuotientMeasureOfBruhatFunctionStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_isQuotientMeasure_of_bruhat"
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

## A quotient integration formula from an averaging function

[Theorem REP.0420](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_isQuotientMeasure_of_bruhat/)

Let $G,H$ be measurable groups and $j:H\to G$ a measurable homomorphism. Suppose multiplication on $G$ is jointly measurable, and multiplication on $H$ is separately measurable with measurable inversion. Let $m$ be an $s$-finite left-invariant measure on $G$, and $m_H$ an $s$-finite right-invariant, inversion-invariant measure on $H$. Suppose there is a measurable $b:G\to[0,\infty]$ such that $$\int_H b(j(h)g)\,dm_H(h)=1\qquad(g\in G).$$ There is a measure $\nu$ on the quotient $j(H)\backslash G$ such that for every measurable $f:G\to[0,\infty]$, $$\int_Gf(g)\,dm(g)=\int_{j(H)\backslash G}\int_Hf(j(h)s(c))\,dm_H(h)\,d\nu(c).$$ Here the quotient carries its quotient measurable structure and $s(c)$ is the fixed choice of representative of each coset used in the quotient integral.
