---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/DpstRightExact.lean",
  "declarations": [
    "UpperTheory.dpst_right_exact"
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

## Surjectivity on potentially semistable periods

[Theorem PHT.0772](https://andrewodesky.com/rh/lean/UpperTheory.dpst_right_exact/)

Let $\ell$ be prime and let $K,L\subset\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$. Let $$0\longrightarrow V'\xrightarrow{f}V\xrightarrow{p}V''\longrightarrow0$$ be an exact sequence of $L$-linear representations of $G_K$, with compatible underlying $\mathbb Q_\ell$-vector spaces and $V$ finite-dimensional over $L$. If $V$ is potentially semistable, then $V'$ and $V''$ are potentially semistable and $$D_{\mathrm{pst}}(V)\longrightarrow D_{\mathrm{pst}}(V'')$$ is surjective.
