---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/PoleLengthBound/BallQuot.lean",
  "declarations": [
    "PI.PoleLengthCount.pole_ballQuot"
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

## Length of a quotient of valuation-defined lattices

[Theorem ALG.0587](https://andrewodesky.com/rh/lean/PI.PoleLengthCount.pole_ballQuot/)

Let $O$ be a discrete valuation domain with fraction field $K$ and uniformizer $\varpi$. Let $A$ be a reduced commutative finite-dimensional $K$-algebra and let $R$ be the integral closure of $O$ in $A$. Assume $R$ is finite over $O$ and $R_{\mathfrak m}$ is a discrete valuation domain for every maximal ideal $\mathfrak m$ of $R$. Put $$f_{\mathfrak m}=[\kappa(\mathfrak m):\kappa(O)].$$ Let $V$ be an $A$-module with compatible $K$- and $O$-module structures, and let $e\in V$ make $A\to V$, $a\mapsto ae$, bijective. For $c:\operatorname{MaxSpec}R\to\mathbb Z$, define $$B(c)=\operatorname{span}_R\{ae:\operatorname{ord}_{\mathfrak m}(a)+c_{\mathfrak m}\ge0\text{ for all }\mathfrak m\}.$$ For every $m:\operatorname{MaxSpec}R\to\mathbb N$, $$\operatorname{length}_O\bigl(B(c+m)/B(c)\bigr)=\sum_{\mathfrak m}m_{\mathfrak m}f_{\mathfrak m}.$$
