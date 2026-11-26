---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/AutomorphicRepresentations/FlipHalf.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.flip_pf"
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

## A diagonal integral determined by a reflected family

[Theorem ALG.0594](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.flip_pf/)

Let $(X,\nu)$ and $(Z,\mu)$ be measure spaces whose measures are countable sums of finite measures. Let $l:X\to\mathbb R$ and $l':Z\to\mathbb R$ be measurable, $F:\mathbb R\times X\to\mathbb C$ jointly measurable and continuous in its first variable for each $x$, and $m:Z\to\mathbb C$ and $d:X\to\mathbb R$ integrable. Suppose $$|F(s,x)|\le d(x)\qquad(|s-l(x)|\le1).$$ Assume that, for every real $s$ and every continuous compactly supported $u:\mathbb R\to\mathbb C$, $$\int_X F(s,x)u(l(x))\,d\nu(x)=\int_Z m(z)u(-s-l'(z))\,d\mu(z).$$ Then $x\mapsto F(l(x),x)$ is integrable and $$\int_X F(l(x),x)\,d\nu(x)=\frac12\int_Z m(z)\,d\mu(z).$$
