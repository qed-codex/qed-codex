---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/OrbitalCosetFiniteness/OrbFub.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Th.orbFub"
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

## Interchanging weighted sums over group orbits

[Theorem ALG.0395](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Th.orbFub/)

Let a group $G$ act on sets $X,Y$, and let $C\triangleleft G$ contain the stabilizer of every point of $X$ and $Y$. Let $F:X\times Y\to\mathbb C$ satisfy $F(gx,gy)=F(x,y)$. Assume each row and each column of $F$ has finite support, and only finitely many $G$-orbits in $X$ contain a point $x$ with $F(x,y)\ne0$ for some $y$. Choose representatives $x_{\mathcal O},y_{\mathcal P}$ for the orbits. Then $$\sum_{\mathcal O\in G\backslash X}[C:G_{x_{\mathcal O}}]\sum_{y\in Y}F(x_{\mathcal O},y) =\sum_{\mathcal P\in G\backslash Y}[C:G_{y_{\mathcal P}}]\sum_{x\in X}F(x,y_{\mathcal P}).$$
