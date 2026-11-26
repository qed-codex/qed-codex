---
{
  "module": "src/Formalism/GaloisIrreducibility/GaloisIrreducibilityProofs/RestrictRoots.lean",
  "declarations": [
    "Formalism.GaloisIrreducibility.restrict_roots_to_subfield"
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

## Power invariance of characteristic roots on an invariant subspace

[Theorem ALG.0257](https://andrewodesky.com/rh/lean/Formalism.GaloisIrreducibility.restrict_roots_to_subfield/)

Let $K$ be an algebraically closed field, $V$ a finite-dimensional $K$-vector space, $T\in\operatorname{End}_K(V)$, $F\in\operatorname{GL}_K(V)$, and $q\ge0$ an integer. Suppose $FT=T^qF$. If $W\subseteq V$ is stable under both $T$ and $F$, then the multiset of roots of the characteristic polynomial of $T|_W$ is a submultiset of that for $T$, and it is unchanged by the map $x\mapsto x^q$.
