---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsCompOfIsTraceClass.lean",
  "declarations": [
    "GlobalTheory.TraceDiagonal.traceIsDiagonal_Rop"
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

## The trace of quotient convolution is the integral of its diagonal kernel

[Theorem REP.0548](https://andrewodesky.com/rh/lean/GlobalTheory.TraceDiagonal.traceIsDiagonal_Rop/)

Let $G$ be a second-countable locally compact Hausdorff topological group with its Borel measurable structure, let $\mu$ be a left Haar measure also invariant under right translation, and let $\Gamma\subseteq G$ be a discrete subgroup. Assume the induced quotient measure $\bar\mu$ on $\Gamma\backslash G$ is finite. Let $f:G\to\mathbb C$ be continuous and compactly supported. Define right convolution on $L^2(\Gamma\backslash G)$ by $$R(f)\varphi(x)=\int_G f(g)\varphi(xg)\,d\mu(g).$$ If $R(f)$ is trace class, then its diagonal kernel is integrable and $$\operatorname{tr}R(f)=\int_{\Gamma\backslash G}\sum_{\gamma\in\Gamma}f(x^{-1}\gamma x)\,d\bar\mu(x).$$
