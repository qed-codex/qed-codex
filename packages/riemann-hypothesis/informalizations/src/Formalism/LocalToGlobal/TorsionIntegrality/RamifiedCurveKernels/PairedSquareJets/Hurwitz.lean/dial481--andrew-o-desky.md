---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/RamifiedCurveKernels/PairedSquareJets/Hurwitz.lean",
  "declarations": [
    "Formalism.L2.Th1.G.jetsIn_mvExp"
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

## Exponential preserves integral factorial-weighted coefficients

[Theorem ALG.0684](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.G.jetsIn_mvExp/)

Let $K$ be a field of characteristic zero, $R\subset K$ a subring, and $I$ any set. For a finitely supported multiindex $\alpha:I\to\mathbb N$, put $\alpha!=\prod_i\alpha_i!$. If $a\in K[[X_i:i\in I]]$ has zero constant term and $$\alpha!\,[X^\alpha]a\in R\qquad\text{for every }\alpha,$$ then $$\alpha!\,[X^\alpha]\exp(a)\in R\qquad\text{for every }\alpha,$$ where $\exp(a)=\sum_{m\ge0}a^m/m!$ is formal substitution into the exponential series.
