---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalAlgebraisationSchemesStatement.lean",
  "declarations": [
    "GlobalTheory.T.formal_algebraisation_schemes"
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

## Algebraisation of polarized formal schemes

[Theorem AG.1681](https://andrewodesky.com/rh/lean/GlobalTheory.T.formal_algebraisation_schemes/)

Assume the projective formal-effectivity principle: over any complete Noetherian adic ring, a compatible system of closed subschemes of the reductions of a fixed projective space comes from a closed subscheme of that projective space. Let $R$ be a Noetherian commutative ring complete for an ideal $I$, and put $R_e=R/I^{e+1}$. Suppose proper $R_e$-schemes $Y_e$ and maps $\beta_e:Y_e\to Y_{e+1}$ identify $Y_e$ with $Y_{e+1}\times_{R_{e+1}}R_e$. Let $N_e$ be line bundles with $N_e\simeq\beta_e^*N_{e+1}$, and assume $N_0$ is relatively ample.

There are a proper $R$-scheme $X$, a relatively ample line bundle $M$ on $X$, and maps $b_e:Y_e\to X$ such that $$Y_e\simeq X\times_R R_e,\qquad b_{e+1}\beta_e=b_e,\qquad N_e\simeq b_e^*M.$$ The first isomorphisms are the ones induced by $b_e$.
