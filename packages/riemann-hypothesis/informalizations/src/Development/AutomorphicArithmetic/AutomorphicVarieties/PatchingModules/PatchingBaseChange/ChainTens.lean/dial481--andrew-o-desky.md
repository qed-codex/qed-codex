---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/PatchingBaseChange/ChainTens.lean",
  "declarations": [
    "UpperTheory.V.Pa.BC.chain_tens"
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

## Lifting linked prime ideals through a finite free base extension

[Theorem ALG.0555](https://andrewodesky.com/rh/lean/UpperTheory.V.Pa.BC.chain_tens/)

Let $O$ be a commutative local ring, let $O'$ be a nonzero commutative $O$-algebra finite and free as an $O$-module, and let $B$ be a commutative $O$-algebra. Put $B'=O'\otimes_O B$, and let $j:B\to B'$ be the natural map. For $h\ge0$, suppose $\mathfrak p_0,\ldots,\mathfrak p_h$ and $\mathfrak e_0,\ldots,\mathfrak e_{h-1}$ are prime ideals of $B$ with $$\mathfrak e_i\subseteq\mathfrak p_i\cap\mathfrak p_{i+1}.$$ There are prime ideals $\mathfrak P_i,\mathfrak E_i$ of $B'$ with contractions $\mathfrak p_i,\mathfrak e_i$ and $$\mathfrak E_i\subseteq\mathfrak P_i\cap\mathfrak P_{i+1}.$$ Moreover, if $\mathfrak P$ is prime in $B'$ and $\mathfrak q$ is prime in $B$ with $\mathfrak q\subseteq j^{-1}(\mathfrak P)$, some prime $\mathfrak Q\subseteq\mathfrak P$ has $j^{-1}(\mathfrak Q)=\mathfrak q$.
