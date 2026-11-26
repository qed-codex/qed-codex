---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/NormalRiemannExtensionLocal.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Branch.normalRiemannExtensionLocal"
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

## Local extension of bounded holomorphic functions on a normal variety

[Theorem AG.1691](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Branch.normalRiemannExtensionLocal/)

Assume the following three local principles: bounded holomorphic functions off a polynomial hypersurface admit a nonzero polynomial denominator locally on an irreducible affine variety; bounded quotients of ambient holomorphic functions extend locally on a normal affine variety when their denominator is not identically zero near the point; and a polynomial vanishing near a point on an irreducible affine variety belongs to its prime ideal.

Let $I\subset\mathbb C[x_1,\ldots,x_n]$ be prime with integrally closed quotient, $X=Z(I)$, $h\notin I$, $w\in X$, and $U$ a neighborhood of $w$ in $\mathbb C^n$. Let $f$ be complex-valued, holomorphic on $$S=(X\cap U)\setminus\{h=0\},$$ in the sense of admitting a local ambient holomorphic extension at every point of $S$, and assume $f(S)$ is bounded. There is an open neighborhood $V$ of $w$, with $V\subset U$, and a holomorphic function $F:V\to\mathbb C$ such that $$F=f\quad\text{on }(X\cap V)\setminus\{h=0\}.$$
