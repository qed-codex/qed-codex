---
{
  "module": "src/Formalism/CharacterColumnKernels/IdempotentNormalForms/SplitFibre.lean",
  "declarations": [
    "Formalism.NG.splitAlg"
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

## A universal splitting algebra of factorial rank

[Theorem ALG.0904](https://andrewodesky.com/rh/lean/Formalism.NG.splitAlg/)

Let $T$ be a commutative ring and $P\in T[X]$ monic of degree $n$. There are a commutative $T$-algebra $T'$ and elements $r_0,\ldots,r_{n-1}\in T'$ such that $T'$ is free and finite of rank $n!$ over $T$, $$P(X)=\prod_{i=0}^{n-1}(X-r_i)\quad\text{in }T'[X],\qquad T[r_0,\ldots,r_{n-1}]=T'.$$ For every commutative $T$-algebra $B$ and every ordered family $a_0,\ldots,a_{n-1}\in B$ satisfying $P(X)=\prod_i(X-a_i)$ in $B[X]$, there is a unique $T$-algebra homomorphism $T'\to B$ sending each $r_i$ to $a_i$.
