---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitFundamentalLemmaFirstHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.unit_fundamental_lemma_first_holds"
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

## Equality of unit orbital integrals under unramified base change

[Theorem REP.1196](https://andrewodesky.com/rh/lean/GlobalTheory.T.unit_fundamental_lemma_first_holds/)

Assume the source's unramified descent and orbital-measure input package described below. Let $E/k$ be a finite unramified cyclic Galois extension of nonarchimedean local fields with compatible valuations and generator $\sigma$. Let $n\ge0$, put $G_E=\operatorname{GL}_n(E)$, $G_k=\operatorname{GL}_n(k)$, and choose Haar measures giving $K_E=\operatorname{GL}_n(\mathcal O_E)$ and $K_k=\operatorname{GL}_n(\mathcal O_k)$ volume one. Write $\iota:G_k\hookrightarrow G_E$ and let $\sigma$ act entrywise on $G_E$.

Let $\delta\in G_E$ be twisted regular semisimple, and suppose its ordered norm $$N_\sigma(\delta)=\delta\sigma(\delta)\cdots\sigma^{[E:k]-1}(\delta)$$ equals $h\iota(\gamma)h^{-1}$ for some $\gamma\in G_k$, $h\in G_E$. Put $$C_{\delta,\sigma}=\{x\in G_E:x^{-1}\delta\sigma(x)=\delta\},\qquad C_\gamma=Z_{G_k}(\gamma).$$ Choose Haar measures on these centralizers whose images in $G_E$ under $x\mapsto h^{-1}xh$ and $t\mapsto\iota(t)$ agree. With the resulting quotient measures, $$\int_{C_{\delta,\sigma}\backslash G_E}\mathbf1_{K_E}(x^{-1}\delta\sigma(x))\,d\overline x =\int_{C_\gamma\backslash G_k}\mathbf1_{K_k}(y^{-1}\gamma y)\,d\overline y.$$
