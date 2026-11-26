---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/PCountOut.lean",
  "declarations": [
    "UpperTheory.Gal.crystallineComparison.countOut_of"
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

## Counting subspaces above a quotient by a line

[Theorem ALG.0259](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.countOut_of/)

Let $k$ be a finite field, $H$ a finite-dimensional $k$-vector space, $C\subset H$ a one-dimensional subspace, and $\pi:H\to H/C$ the quotient map. For every subspace $E\subseteq H/C$, $$\#\{D\subseteq H:D\text{ is a linear subspace},\ C\nsubseteq D,\ \pi(D)=E\}=|k|^{\dim_k E}.$$
