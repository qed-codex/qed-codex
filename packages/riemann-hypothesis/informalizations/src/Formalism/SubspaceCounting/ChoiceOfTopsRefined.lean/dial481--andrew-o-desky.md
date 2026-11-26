---
{
  "module": "src/Formalism/SubspaceCounting/ChoiceOfTopsRefined.lean",
  "declarations": [
    "Formalism.G0.Top.subspaceCount"
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

## Counting subspaces of a finite vector space

[Theorem ALG.0377](https://andrewodesky.com/rh/lean/Formalism.G0.Top.subspaceCount/)

Let $F$ be a finite field with $q$ elements, and let $W$ be a finite $F$-vector space of dimension $n$. For every $k\ge0$, $$\#\{U\subseteq W:U\text{ is an }F\text{-subspace},\ \dim_FU=k\}={n\brack k}_q.$$
