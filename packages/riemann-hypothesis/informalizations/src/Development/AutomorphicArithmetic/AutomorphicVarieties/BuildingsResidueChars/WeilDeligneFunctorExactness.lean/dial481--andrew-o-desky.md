---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/WeilDeligneFunctorExactness.lean",
  "declarations": [
    "UpperTheory.weil_deligne_functor_exactness"
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

## Exactness of the Weil-Deligne construction

[Theorem PHT.0363](https://andrewodesky.com/rh/lean/UpperTheory.weil_deligne_functor_exactness/)

Let $\ell$ be prime, $K,L$ finite extensions of $\mathbb Q_\ell$ in a fixed algebraic closure, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Let $$0\longrightarrow V'\xrightarrow{f}V\xrightarrow{p}V''\longrightarrow0$$ be an exact sequence of $L$-linear representations of $G_K$, with $f,p$ equivariant and $V$ finite-dimensional over $L$. If $V$ is potentially semistable for the source's fixed local period datum, then so are $V'$ and $V''$, and the induced sequence of complex vector spaces underlying the Weil–Deligne parameters is exact: $$0\longrightarrow\mathrm{WD}_\iota(V')\xrightarrow{\mathrm{WD}_\iota(f)}\mathrm{WD}_\iota(V)\xrightarrow{\mathrm{WD}_\iota(p)}\mathrm{WD}_\iota(V'')\longrightarrow0.$$ The $\mathbb Q_\ell$-module structures on the three spaces are the restrictions of their $L$-module structures.
