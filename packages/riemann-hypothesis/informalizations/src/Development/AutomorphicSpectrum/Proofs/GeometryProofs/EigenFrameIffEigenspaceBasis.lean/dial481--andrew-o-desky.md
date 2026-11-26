---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/EigenFrameIffEigenspaceBasis.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Flat.LieEigFrame.isEigFrame_pt_iff"
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

## A tangent eigenframe is an eigenspace basis

[Theorem AV.0650](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Flat.LieEigFrame.isEigFrame_pt_iff/)

Let $S$ be a scheme, $G\to S$ a commutative group scheme, $R$ a commutative ring, and $x:\operatorname{Spec}R\to S$. Let $M$ be an $R$-linear model of the tangent vectors of $G$ at the identity over $x$, with tangent-vector identification $v\mapsto\operatorname{pt}(v)$. Let a commutative ring $A$ act on $G$, let $\rho:A\to\operatorname{End}_R(M)$ be the corresponding action under this identification, and let $\tau:A\to R$ be a ring homomorphism.

For $b_1,\ldots,b_n\in M$, the tangent vectors $\operatorname{pt}(b_i)$ form a frame of the $\tau$-eigenvectors if and only if $b_1,\ldots,b_n$ are an $R$-basis of $$M_\tau=\{v\in M:\rho(a)v=\tau(a)v\text{ for every }a\in A\}.$$
