---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsDeRhamOfIsCrystallineSpanStatement.lean",
  "declarations": [
    "GlobalTheory.T.isDeRham_of_isCrystalline_span"
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

## Crystalline periods span the de Rham periods

[Theorem PHT.0910](https://andrewodesky.com/rh/lean/GlobalTheory.T.isDeRham_of_isCrystalline_span/)

Let $\ell$ be prime, $K,L\subseteq\overline{\mathbb Q}_\ell$ finite extensions of $\mathbb Q_\ell$, and $V$ a finite-dimensional $L$-space with an $L$-linear action of $G_K$. Use crystalline, de Rham, and integral period data compatibly identified with Fontaine's period rings. If $V$ is crystalline for these data, then it is de Rham, and every $y\in D_{\mathrm{dR}}(V)$ has an expression $$y=\sum_{i=1}^m c_i\,\iota(d_i),\qquad c_i\in K,\quad d_i\in D_{\mathrm{cris}}(V),\quad m\ge0,$$ where $\iota$ is induced by $B_{\mathrm{cris}}\to B_{\mathrm{dR}}$ and $c_i$ acts on the period-ring factor.
