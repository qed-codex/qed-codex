---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PairingTwistedDeterminantSubquotientStatement.lean",
  "declarations": [
    "GlobalTheory.T.pairing_twisted_determinant_subquotient"
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

## A determinant-equivariant pairing detects a dual subquotient

[Theorem REP.1520](https://andrewodesky.com/rh/lean/GlobalTheory.T.pairing_twisted_determinant_subquotient/)

Let $k$ be a nonarchimedean local field, $n,s\ge0$, $S$ a smooth irreducible complex representation of $G=\mathrm{GL}_n(k)$, and $A$ a smooth complex representation of $G$ on a vector space $V$. Suppose a nonzero complex-bilinear pairing $B:S\times V\to\mathbb C$ satisfies $$B(S(g)w,A(g)v)=|\det g|_k^s B(w,v)\qquad(g\in G).$$ Then $A$ has a smooth irreducible subquotient isomorphic to $S^\vee\otimes|\det|_k^s$, where $S^\vee$ is the smooth contragredient.
