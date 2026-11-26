---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/TraceAsymptotics/DcosSep.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Asm.dcosSep"
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

## Separated Iwahori double cosets have separable characteristic polynomials

[Theorem REP.0212](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Asm.dcosSep/)

Let $E$ be a CM number field, $w$ a finite place, $n\ge0$, and $\varpi\in E_w$ have normalized valuation one. Let $x_1>\cdots>x_n$ be integers and put $t=\operatorname{diag}(\varpi^{x_1},\ldots,\varpi^{x_n})$. Let $I\subseteq\operatorname{GL}_n(E_w)$ be the standard Iwahori subgroup. Every matrix in $ItI$ has separable characteristic polynomial.

Moreover, the characteristic function $\mathbf1_{ItI}$ is a Hecke function for some open subgroup $K'\subseteq\operatorname{GL}_n(\mathcal O_w)$: it is bi-$K'$-invariant and supported on finitely many $K'$-double cosets.
