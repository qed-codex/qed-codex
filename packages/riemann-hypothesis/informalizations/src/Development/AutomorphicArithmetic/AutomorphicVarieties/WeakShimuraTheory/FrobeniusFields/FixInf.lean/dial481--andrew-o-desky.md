---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/FrobeniusFields/FixInf.lean",
  "declarations": [
    "UpperTheory.V.Ws.fixInf"
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

## Total reality and quadratic CM fields from complex conjugations

[Theorem ANT.0546](https://andrewodesky.com/rh/lean/UpperTheory.V.Ws.fixInf/)

Let $\Omega$ be an algebraic closure of $\mathbb Q$ and let $F\subseteq\Omega$ be a number field. Call $c\in\operatorname{Gal}(\Omega/\mathbb Q)$ a complex conjugation if some embedding $j:\Omega\hookrightarrow\mathbb C$ satisfies $j(c(x))=\overline{j(x)}$ for every $x\in\Omega$. If every complex conjugation fixes $F$ pointwise, then $F$ is totally real. If no complex conjugation fixes $F$ pointwise and $[F:\mathbb Q]=2$, then $F$ is a CM field.
