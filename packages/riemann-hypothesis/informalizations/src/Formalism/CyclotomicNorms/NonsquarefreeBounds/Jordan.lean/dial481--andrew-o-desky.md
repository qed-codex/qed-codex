---
{
  "module": "src/Formalism/CyclotomicNorms/NonsquarefreeBounds/Jordan.lean",
  "declarations": [
    "Formalism.CyclotomicNorms.jordan_transitivity"
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

## A transitive permutation group containing a large prime cycle

[Theorem ALG.0567](https://andrewodesky.com/rh/lean/Formalism.CyclotomicNorms.jordan_transitivity/)

Let $G$ act transitively on a finite set $\Omega$. Let $p$ be prime and suppose $$p+3\le|\Omega|<2p.$$ If some $g\in G$ acts as a single cycle with support of size $p$, then the image of $G$ in $\operatorname{Sym}(\Omega)$ contains $\operatorname{Alt}(\Omega)$, and $G$ is not solvable.
