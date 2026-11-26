---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescentFromCompleteRegularChartsStatement.lean",
  "declarations": [
    "GlobalTheory.T.semiAbelian_descent_from_complete_regular_charts"
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

## Descent of semiabelian models from complete local charts

[Theorem AV.1479](https://andrewodesky.com/rh/lean/GlobalTheory.T.semiAbelian_descent_from_complete_regular_charts/)

Let $S$ be a normal Noetherian scheme, $j:X\hookrightarrow S$ a dominant open immersion, and $A\to X$ an abelian scheme with a relatively ample line bundle. Assume that every $x\in S$ has a complete local chart of the following kind: a complete regular local characteristic-zero domain $R$, a map $\xi:\operatorname{Spec}R\to S$ taking its closed point to $x$, a semiabelian scheme $G_R/R$, a lift $y:\operatorname{Spec}\operatorname{Frac}R\to X$, and an identification $$\alpha:G_R\times_R\operatorname{Frac}R\xrightarrow{\sim}y^*A.$$ Require $j\circ y=\xi|_{\operatorname{Frac}R}$ and the induced map $a:\mathcal O_{S,x}\to R$ to be flat, to satisfy $a(\mathfrak m_x)R=\mathfrak m_R$, and to make $R/\mathfrak m_R$ finite as an $\mathcal O_{S,x}$-module; require also that $\mathcal O_{S,x}\to R/\mathfrak m_R$ be formally unramified.

There is a semiabelian scheme $G/S$ with a group pullback identification $e:A\to G$ over $j$. For every such chart there is a group pullback map $\pi:G_R\to G$ over $\xi$, compatible with the generic identification: the map to $G$ obtained through $\alpha$ and $e$ equals the restriction of $\pi$ to the generic fibre.
