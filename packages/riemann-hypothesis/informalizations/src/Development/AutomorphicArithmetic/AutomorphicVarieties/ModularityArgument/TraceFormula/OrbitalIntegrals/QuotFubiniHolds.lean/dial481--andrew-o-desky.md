---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/OrbitalIntegrals/QuotFubiniHolds.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.Orb.orbProper_holds"
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

## Compactness modulo the twisted centralizer

[Theorem REP.0265](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.Orb.orbProper_holds/)

Let $E/k$ be a finite Galois extension of nonarchimedean local fields, with $k$ of characteristic zero and the valuation on $E$ extending that on $k$. Let $\sigma$ generate $\operatorname{Gal}(E/k)$, put $d=[E:k]$, and let $n\ge0$. Suppose $\delta\in\operatorname{GL}_n(E)$ has twisted norm $$\mathcal N_\sigma(\delta)=\delta\,\sigma(\delta)\cdots\sigma^{d-1}(\delta)$$ with separable characteristic polynomial. Define $$Z_{\sigma,\delta}=\{t\in\operatorname{GL}_n(E):t^{-1}\delta\sigma(t)=\delta\}.$$ For every compact $C\subseteq\operatorname{GL}_n(E)$ there is a compact $D\subseteq\operatorname{GL}_n(E)$ such that $$x^{-1}\delta\sigma(x)\in C\ \Longrightarrow\ x=tu\text{ for some }t\in Z_{\sigma,\delta},\ u\in D.$$
