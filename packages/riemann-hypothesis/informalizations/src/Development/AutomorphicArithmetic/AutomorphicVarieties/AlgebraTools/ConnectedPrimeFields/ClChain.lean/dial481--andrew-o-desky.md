---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AlgebraTools/ConnectedPrimeFields/ClChain.lean",
  "declarations": [
    "UpperTheory.V.AlgebraTools.Conn.clChain"
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

## Chains of components cut out by few equations

[Theorem ALG.0505](https://andrewodesky.com/rh/lean/UpperTheory.V.AlgebraTools.Conn.clChain/)

Let $O$ be a complete discrete valuation ring and $R$ a complete Noetherian local $O$-algebra. Assume $O\to R$ is local, the residue field of $R$ is finite as an $O$-module, and $\operatorname{Spec}R$ is irreducible. Let $\mathfrak a\ne R$ be an ideal whose radical is generated up to radical by at most $h$ elements. Let $k,h\ge0$ and suppose $$\dim R\ge k+h+1.$$ Any two primes $\mathfrak p,\mathfrak q$ minimal over $\mathfrak a$ can be joined by a finite chain of primes minimal over $\mathfrak a$, $$\mathfrak p=\mathfrak p_0,\mathfrak p_1,\ldots,\mathfrak p_t=\mathfrak q,$$ with $\dim R/(\mathfrak p_j+\mathfrak p_{j+1})\ge k$ for every $j<t$.
