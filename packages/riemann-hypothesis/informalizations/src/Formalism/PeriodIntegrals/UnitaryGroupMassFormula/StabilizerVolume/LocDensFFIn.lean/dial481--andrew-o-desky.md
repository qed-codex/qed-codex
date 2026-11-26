---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/LocDensFFIn.lean",
  "declarations": [
    "PI.VolStabS.FFHS.fFInert_holds"
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

## Counting nondegenerate Hermitian frames over a finite field

[Theorem ALG.0919](https://andrewodesky.com/rh/lean/PI.VolStabS.FFHS.fFInert_holds/)

Let $k$ be a finite field of odd characteristic, $K/k$ a quadratic field extension, and $\sigma$ its nontrivial involutive $k$-automorphism. Put $q=|k|$. Let $0\le a\le M$, and let $J\in M_M(K)$ and $T\in M_a(K)$ be invertible $\sigma$-Hermitian matrices. For vectors $X_0,\ldots,X_{a-1}\in K^M$, put $\operatorname{Gram}_J(X)_{ij}=\sigma(X_i)^tJX_j$. Then $$\#\{X\in(K^M)^a:\operatorname{Gram}_J(X)=T\}=\prod_{j=0}^{a-1}\left(q^{2(M-j)-1}-(-1)^{M-j}q^{M-j-1}\right).$$ The product is $1$ when $a=0$.
