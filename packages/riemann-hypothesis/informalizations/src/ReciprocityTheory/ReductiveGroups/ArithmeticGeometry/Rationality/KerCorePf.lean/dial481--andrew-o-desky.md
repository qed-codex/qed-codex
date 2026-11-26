---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/Rationality/KerCorePf.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FreeQuotientRank.kerCore_holds"
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

## Separating a quotient by functionals over one number field

[Theorem ALG.0633](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FreeQuotientRank.kerCore_holds/)

Let $K$ be a number field, $V$ a finite-dimensional $K$-vector space, and $W\subseteq V$ a subspace. For every number field $L$ with a $K$-algebra structure, prescribe a family $\mathcal F_L$ of $K$-linear maps $V\to L$. Assume:

1. Every member of $\mathcal F_L$ vanishes on $W$.
2. If every member of every $\mathcal F_L$ vanishes on $v\in V$, then $v\in W$.
3. For every $K$-embedding $e:L\hookrightarrow L'$ between such fields and every $f\in\mathcal F_L$, the composite $e\circ f$ belongs to $\mathcal F_{L'}$.

There are a number field $L/K$, an integer $r\ge0$, maps $g_1,\ldots,g_r\in\mathcal F_L$, and $L$-linear functionals $\lambda_1,\ldots,\lambda_r$ on $L\otimes_K V$ such that $$\lambda_i(1\otimes v)=g_i(v),\qquad\bigcap_{i=1}^r\ker\lambda_i=L\otimes_K W,\qquad \dim_K W+r=\dim_K V.$$
